from flask import Flask, request
from flask_cors import CORS

from prefocus.backend import (abandon_a_record, all_today_prefocus,
                              append_a_prefocus, focused_to_focusing,
                              focusing_to_focused, purge_database)

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def hello_prefocus():
    return "Hello Prefocus!"


@app.route("/abandon_a_record", methods=["POST"])
def app_abandon_a_record():
    record_id = request.args.get("recordId")
    abandon_a_record(record_id)


@app.route("/append_a_prefocus", methods=["POST"])
def app_append_a_prefocus():
    prefocus_desc = request.args.get("prefocusDesc")
    prefocus_id = request.args.get("prefocusId")
    append_a_prefocus(prefocus_desc, prefocus_id)


@app.route("/focused_to_focusing", methods=["POST"])
def app_focused_to_focusing():
    record_id = request.args.get("recordId")
    focused_to_focusing(record_id)


@app.route("/focusing_to_focused", methods=["POST"])
def app_focusing_to_focused():
    record_id = request.args.get("recordId")
    focusing_to_focused(record_id)


@app.route("/purge_database", methods=["POST"])
def app_purge_database():
    purge_database()


@app.route("/all_today_prefocus", methods=["GET"])
def app_all_today_prefocus():
    return all_today_prefocus()


if __name__ == "__main__":
    app.run()
