import React from "react";
import "../styles/focus-item.scss";
import axios from "axios";

class FocusItem extends React.Component {
  constructor(props) {
    super(props);
    this.markCompleted = this.markCompleted.bind(this);
    this.deleteItem = this.deleteItem.bind(this);
    this.stashItem = this.stashItem.bind(this);
  }
  markCompleted(event) {
    this.props.onItemCompleted(this.props.id);
  }

  async deleteItem(event) {
    this.props.onDeleteItem(this.props.id);
    await axios.post("http://127.0.0.1:1114/abandon_a_record", null, {
      params: { recordId: this.props.id },
    });
  }

  stashItem(event) {
    this.props.onStashItem(this.props.id);
  }

  // Highlight newly added item for several seconds.
  componentDidMount() {
    if (this._listItem) {
      // 1. Add highlight class.
      this._listItem.classList.add("highlight");

      // 2. Set timeout.
      setTimeout(
        (listItem) => {
          // 3. Remove highlight class.
          listItem.classList.remove("highlight");
        },
        500,
        this._listItem
      );
    }
  }
  render() {
    const itemClass =
      "form-check todoitem " + (this.props.completed ? "done" : "undone");
    return (
      <li className={itemClass} ref={(li) => (this._listItem = li)}>
        <label className="form-check-label">
          <input
            type="checkbox"
            className="form-check-input"
            onChange={this.markCompleted}
          />{" "}
          {this.props.text}
        </label>
        <button
          type="button"
          id={"stashItem"}
          className=""
          onClick={this.stashItem}
        >
          Stash
        </button>
        <button
          type="button"
          id={"deleteItem"}
          className=""
          onClick={this.deleteItem}
        >
          Remove
        </button>
      </li>
    );
  }
}

export default FocusItem;
