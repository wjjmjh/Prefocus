import ReactDOM from "react-dom";
import React from "react";
import Prefocus from "./components/Prefocus";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div>
      <Prefocus />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
