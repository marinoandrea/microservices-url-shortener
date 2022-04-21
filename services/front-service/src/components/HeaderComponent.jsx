import React from "react";

const HeaderComponent = () => (
  <header>
    <nav className="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid">
      <div>
        <a href="/home" className="navbar-brand">
          Url Shortener Management
        </a>
      </div>

     <button class="btn btn-outline-success d-flex" onClick={ (e) => {
        e.preventDefault();
        window.localStorage.token=""
        window.location.reload(false);
    }}> Logout</button>
</div>
    </nav>
  </header>
);

export default HeaderComponent;
