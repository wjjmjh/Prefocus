import React from "react";
import FocusItem from "./FocusItem";
import "../styles/focus-list.scss";

class FocusList extends React.Component {
  render() {
    return (
        <div>
          {this.props.items.map((item) => (
              <FocusItem
                  key={item.id}
                  id={item.id}
                  text={item.text}
                  completed={item.done}
                  onItemCompleted={this.props.onItemCompleted}
                  onItemEdited={this.props.onItemEdited}
                  onDeleteItem={this.props.onDeleteItem}
                  onStashItem={this.props.onStashItem}
              />
          ))}
        </div>
    );
  }
}

export default FocusList;
