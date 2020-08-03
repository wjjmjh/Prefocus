# credits: Stephen Ka-Wah Ma
from prefocus.lib import MySQLManager, now, wrap

mysql = MySQLManager()

_focusing_fields = ["date", "prefocus", "id"]
_focused_fields = ["date", "prefocus", "id"]


def append_a_prefocus(prefocus, id):
    date = now()
    mysql.insert_into_default_focusing_table([[date, str(prefocus), str(id)]])


def focusing_to_focused(id):
    # fetched is one dimensional query result.
    fetched = mysql.fetch("SELECT * FROM focusing WHERE id = {id}".format(id=wrap(id)))[
        0
    ]
    mysql.do("DELETE FROM focusing WHERE id = {id}".format(id=wrap(id)))
    mysql.insert_into_default_focused_table([fetched])


def focused_to_focusing(id):
    # fetched is one dimensional query result.
    fetched = mysql.fetch("SELECT * FROM focused WHERE id = {id}".format(id=wrap(id)))[
        0
    ]
    mysql.do("DELETE FROM focused WHERE id = {id}".format(id=wrap(id)))
    mysql.insert_into_default_focusing_table([fetched])


def abandon_a_record(id):
    mysql.do("DELETE FROM focusing WHERE id = {id}".format(id=wrap(id)))
    mysql.do("DELETE FROM focused WHERE id = {id}".format(id=wrap(id)))


def purge_database():
    mysql.purge_database()


def all_today_prefocus():
    today = now()
    print(today)
    got = mysql.fetch(
        "SELECT * FROM focusing WHERE date = {date}".format(date=wrap(today))
    )
    return {
        "allTodayFocus": [
            {
                "id": it[_focusing_fields.index("id")],
                "text": it[_focusing_fields.index("prefocus")],
                "done": False,
            }
            for it in got
        ]
    }
