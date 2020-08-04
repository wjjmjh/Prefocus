import React from "react";
import moment from "moment";
import DayNames from "./Daynames";
import Week from "./Week";
import "../../styles/calendar/calendar.scss";
import axios from "axios";

class Calendar extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      month: moment(),
      selected: moment().startOf("day"),
    };

    this.previous = this.previous.bind(this);
    this.next = this.next.bind(this);
  }

  previous() {
    const { month } = this.state;

    this.setState({
      month: month.subtract(1, "month"),
    });
  }

  next() {
    const { month } = this.state;

    this.setState({
      month: month.add(1, "month"),
    });
  }

  async select(day) {
    this.setState({
      selected: day.date,
      month: day.date.clone(),
    });

    const selected = day.date.format("DDMMYYYY");
    await axios
      .get(
        `http://127.0.0.1:1112/merge_uncomplete_prefocus_from_a_selected_date`,
        { params: { selected: selected } }
      )
      .then((response) => {
        const got = response.data["uncompleted"];
        this.props.mergeUncompleted(got);
      });
  }

  renderWeeks() {
    let weeks = [];
    let done = false;
    let date = this.state.month
      .clone()
      .startOf("month")
      .add("w" - 1)
      .day("Sunday");
    let count = 0;
    let monthIndex = date.month();

    const { selected, month } = this.state;

    while (!done) {
      weeks.push(
        <Week
          key={date}
          date={date.clone()}
          month={month}
          select={(day) => this.select(day)}
          selected={selected}
        />
      );

      date.add(1, "w");

      done = count++ > 2 && monthIndex !== date.month();
      monthIndex = date.month();
    }

    return weeks;
  }

  renderMonthLabel() {
    const { month } = this.state;

    return <span className="month-label">{month.format("MMMM YYYY")}</span>;
  }

  render() {
    return (
      <section className="calendar">
        <header className="header">
          <div className="month-display row">
            <i className="arrow left" onClick={this.previous} />
            {this.renderMonthLabel()}
            <i className="arrow right" onClick={this.next} />
          </div>
          <DayNames />
        </header>
        {this.renderWeeks()}
      </section>
    );
  }
}

export default Calendar;
