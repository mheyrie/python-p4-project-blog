import { Link } from "react-router-dom";
import React from 'react'

function Navbar() {
  return (
    <header className="nav-header">
        <div className="navbar-heading">
            <h1>Welcome to Mary's Blog</h1>
        </div>
        <nav className="nav_details">
            <Link to="signup" className="nav_signup">SignUp</Link>
            <Link to="login" className="nav_login">Login</Link>
            <Link to="blog" className="nav_blog">Blog</Link>
            <Link to="create_blog" className="nav_create_blog">Create Blog</Link>
            
        </nav>    
    </header>
  );
}

export default Navbar