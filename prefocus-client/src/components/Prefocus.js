import React from "react";
import FocusList from "./FocusList";
import axios from "axios";
import Calendar from "./calendar/Calendar";
import "../styles/prefocus.scss";

class Prefocus extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      items: [],
      text: "",
    };

    this.handleTextChange = this.handleTextChange.bind(this);
    this.handleAddItem = this.handleAddItem.bind(this);
    this.markItemCompleted = this.markItemCompleted.bind(this);
    this.handleDeleteItem = this.handleDeleteItem.bind(this);
  }
  handleTextChange(event) {
    this.setState({
      text: event.target.value,
    });
  }
  async handleAddItem(event) {
    event.preventDefault();

    var newItem = {
      id: Date.now(),
      text: this.state.text,
      done: false,
    };

    this.setState((prevState) => ({
      items: prevState.items.concat(newItem),
      text: "",
    }));

    await axios.post("http://127.0.0.1:5000/append_a_prefocus", {
      prefocusDesc: newItem.text,
      prefocusId: newItem.id,
    });
  }
  async markItemCompleted(itemId) {
    var updatedItems = await this.state.items.map((item) => {
      if (itemId === item.id) {
        if (item.done === false) {
          axios.post("http://127.0.0.1:5000/focusing_to_focused", null, {
            params: { recordId: itemId },
          });
        } else {
          axios.post("http://127.0.0.1:5000/focused_to_focusing", null, {
            params: { recordId: itemId },
          });
        }

        item.done = !item.done;
      }
      return item;
    });

    // State Updates are Merged
    this.setState({
      items: [].concat(updatedItems),
    });
  }

  handleDeleteItem = (itemId) => {
    var updatedItems = this.state.items.filter((item) => {
      return item.id !== itemId;
    });

    this.setState({
      items: [].concat(updatedItems),
    });
  };

  mergeUncompleted = (uncompleted) => {
    this.setState({ items: this.state.items.concat(uncompleted) });
  };

  componentDidMount() {
    const host = "http://127.0.0.1:5000";
    return axios.get(`${host}/all_today_prefocus`).then((response) => {
      const got = response.data["allTodayFocus"];
      this.setState({ items: this.state.items.concat(got) });
    });
  }

  render() {
    return (
      <div>
        <div id={"stack"}>
          <div className="row">
            <div className="col-md-3">
              <FocusList
                items={this.state.items}
                onItemCompleted={this.markItemCompleted}
                onDeleteItem={this.handleDeleteItem}
              />
            </div>
          </div>
          <form className="row">
            <div className="col-md-3">
              <input
                type="text"
                className="form-control"
                onChange={this.handleTextChange}
                value={this.state.text}
              />
            </div>
            <div className="col-md-3">
              <button
                className="btn btn-primary"
                onClick={this.handleAddItem}
                disabled={!this.state.text}
              >
                {"Add > " + (this.state.items.length + 1)}
              </button>
            </div>
          </form>
        </div>
        <Calendar mergeUncompleted={this.mergeUncompleted} />
      </div>
    );
  }
}

export default Prefocus;
