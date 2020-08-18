import axios from "axios";
import React from "react";

import "../styles/focus-item.scss";
import EditPrefocus from "./dialogs/editPrefocus";

class FocusItem extends React.Component {
  constructor(props) {
    super(props);

    this.label = React.createRef();
    this.markCompleted = this.markCompleted.bind(this);
    this.markEdited = this.markEdited.bind(this);
    this.deleteItem = this.deleteItem.bind(this);
    this.stashItem = this.stashItem.bind(this);
  }
  markCompleted() {
    this.props.onItemCompleted(this.props.id);
  }

  markEdited(id, val) {
    this.props.onItemEdited(id, val);
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
      <div>
        <div>
          <div id={"checkbox_and_prefocus"}>
            <input
                id={"checkbox"}
                type="checkbox"
                onChange={this.markCompleted}
            />
            <label
                id={"prefocus"}
                ref={this.label}
                contentEditable="true"
                onKeyPress={this.markEdited}
            >
              {this.props.text}
            </label>
          </div>
          <div id={"btns"}>
            <button
                className={"btn"}
                type="button"
                onClick={this.stashItem}
            >
              Stash
            </button>
            <button
                className={"btn"}
                type="button"
                onClick={this.deleteItem}
            >
              Remove
            </button>
          </div>
        </div>
        <EditPrefocus editPrefocus={this.markEdited} />
      </div>
    );
  }
}

export default FocusItem;
