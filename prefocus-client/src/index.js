import ReactDOM from "react-dom";
import React from "react";
import Prefocus from "./components/Prefocus";
import Calendar from "./components/calendar/Calendar";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div>
      <Prefocus />
      <Calendar />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
