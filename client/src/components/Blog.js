import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Blog() {

    const [posts, setPosts] = useState([]);
    const [users, setUsers] = useState([]);

// Fetches all the posts in the db
    useEffect(() => {
        fetch("/posts")
          .then((r) => r.json())
          .then(setPosts);

        fetch("/users")
          .then((r) => r.json())
          .then(setUsers);
      }, []);
    
    const findUser = (userId) => {
      const user = users.find((user) => user.id === userId);
      return user?user.name : "Unknown User";
    };
    
    // Deletes a post using the id
    function handleDelete(id) {
      fetch(`/posts/${id}`, {
        method: "DELETE",
      }).then((res) =>{
        if (res.ok){
          setPosts((posts) =>
          posts.filter((post) => post.id !== id));
        }
      });
    }


      return (
        <section className="container">
          
          {posts.map((post) => (
            <div key={post.id} className="card">
              <h2>
                <Link to={`/posts/${post.id}`}>{post.title}</Link>
              </h2>
              <img src={post.image} alt="random pictures" width="400px" height="300px" />
              <p>{post.body}</p>
              {post.tags.map((tag) =>(
                <div>
                  <li key={tag.id}>
                    Category: {tag.category} | average of {tag.mins_to_read} minutes to read | post by: {findUser(tag.user_id)} | on {tag.created_at}
                  </li>
                  
                </div>

            ))}
            <button className="delete_btn" onClick={() => handleDelete(post.id)}>Delete</button>
            </div>
            
          ))}
          
        </section>
      );
    }
    

export default Blog