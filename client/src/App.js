import { Route, Routes } from "react-router";
import Blog from "./components/Blog";
import Navbar from "./components/Navbar";
import SignUp from "./components/SignUp";
import CreateBlog from "./components/CreateBlog";
import Login from "./components/Login";




function App() {
  return (
    <div className="App_page">
      <Navbar />
      <Routes>
        <Route exact path="signup" element={<SignUp/>} />
        <Route exact path="login" element={<Login />} />
        <Route exact path="blog" element={<Blog/>} />
        <Route exact path="create_blog" element={<CreateBlog/>} />
        
         
      </Routes>
    </div>
  );
}

export default App;
