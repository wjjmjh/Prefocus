import React from "react";
import FocusItem from "./FocusItem";
import "../styles/focus-list.scss";

class FocusList extends React.Component {
  render() {
    return (
      <ul className="todolist">
        {this.props.items.map((item) => (
          <FocusItem
            key={item.id}
            id={item.id}
            text={item.text}
            completed={item.done}
            onItemCompleted={this.props.onItemCompleted}
            onDeleteItem={this.props.onDeleteItem}
          />
        ))}
      </ul>
    );
  }
}

export default FocusList;
