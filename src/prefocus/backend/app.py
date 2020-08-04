from flask import Flask, request
from flask_cors import CORS

from prefocus.backend import (abandon_a_record, all_today_prefocus,
                              append_a_prefocus, bytes_to_dict,
                              focused_to_focusing, focusing_to_focused,
                              merge_uncomplete_prefocus_from_a_selected_date,
                              purge_database)

app = Flask(__name__)
cors = CORS(app)

GOOD = "g"
GOOD_STATUS = {"status": GOOD}


@app.route("/")
def hello_prefocus():
    return "Hello Prefocus!"


@app.route("/abandon_a_record", methods=["POST"])
def app_abandon_a_record():
    record_id = request.args.get("recordId")
    abandon_a_record(record_id)
    return GOOD_STATUS


@app.route("/append_a_prefocus", methods=["POST"])
def app_append_a_prefocus():
    got = bytes_to_dict(request.data)
    prefocus_desc = got["prefocusDesc"]
    prefocus_id = got["prefocusId"]
    append_a_prefocus(prefocus_desc, prefocus_id)
    return GOOD_STATUS


@app.route("/focused_to_focusing", methods=["POST"])
def app_focused_to_focusing():
    record_id = request.args.get("recordId")
    focused_to_focusing(record_id)
    return GOOD_STATUS


@app.route("/focusing_to_focused", methods=["POST"])
def app_focusing_to_focused():
    record_id = request.args.get("recordId")
    focusing_to_focused(record_id)
    return GOOD_STATUS


@app.route("/purge_database", methods=["POST"])
def app_purge_database():
    purge_database()
    return GOOD_STATUS


@app.route("/all_today_prefocus", methods=["GET"])
def app_all_today_prefocus():
    return all_today_prefocus()


@app.route("/merge_uncomplete_prefocus_from_a_selected_date", methods=["GET"])
def app_merge_uncomplete_prefocus_from_a_selected_date():
    selected = request.args.get("selected")
    return merge_uncomplete_prefocus_from_a_selected_date(selected)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1112")
