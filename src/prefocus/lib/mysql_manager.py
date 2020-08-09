import math

import mysql.connector

focused_table = "focused"
focusing_table = "focusing"


def wrap(val):
    if isinstance(val, str):
        return '"{}"'.format(val)
    return "{}".format(val)


class SelectSQL:
    template1 = "SELECT {columns} FROM {table};"
    template2 = "SELECT DISTINCT {columns} FROM {table};"

    def select_query(self, table, columns="*", distinct=False):

        if distinct:
            return self.template2.format(columns=columns, table=table)
        return self.template1.format(columns=columns, table=table)


class InsertSQL:
    template1 = "INSERT INTO {table} ({columns}) VALUES ({values});"
    template2 = "INSERT INTO {table} VALUES ({values});"
    template3 = "INSERT INTO {table} ({columns}) VALUES {value_tuples};"
    template4 = "INSERT INTO {table} VALUES {value_tuples};"
    template5 = "INSERT INTO {tableB} SELECT * FROM {tableA};"

    def append_query(self, tableA, tableB):
        return self.template5.format(tableA=tableA, tableB=tableB)

    def _with_columns(self, table, columns, values, single_query=True):
        if single_query:
            return self.template1.format(table=table, columns=columns, values=values)
        return self.template3.format(table=table, columns=columns, value_tuples=values)

    def _without_columns(self, table, values, single_query=True):
        if single_query:
            return self.template2.format(table=table, values=values)
        return self.template4.format(table=table, value_tuples=values)

    def insert_query(self, if_specify_columns=True, **kwargs):
        """
        :param if_specify_columns: if inserting into specified fields or not
        :param kwargs: table, columns(optional), values
        :return: a constructed inserting sql query
        """
        if if_specify_columns:
            return self._with_columns(
                kwargs["table"], kwargs["columns"], kwargs["values"]
            )
        else:
            return self._without_columns(kwargs["table"], kwargs["values"])

    def insert_multipe_query(self, if_specify_columns=True, **kwargs):
        """
        kwargs["rows"] would be a two dimensional array
        """
        rows = kwargs["rows"]
        values = ", ".join(
            ["({})".format(", ".join([wrap(ele) for ele in row])) for row in rows]
        )
        if if_specify_columns:
            return self._with_columns(
                kwargs["table"], kwargs["columns"], values, single_query=False
            )
        else:
            return self._without_columns(kwargs["table"], values, single_query=False)


class UpdateSQL:
    # TODO: this class needs to be further developed and enhanced.
    template1 = "UPDATE {table} SET {target_column}={target_value} WHERE {base_column}={base_value};"
    template2 = "UPDATE {table} SET {kwargs} WHERE {condition};"

    def update_multiple_query(self, table, src):
        """
        src is a list of tuples: [(target_column, target_value), (base_column, base_value)]
        its length has to be 2: the former one for target, and the latter one for base
        """
        target = src[0]
        base = src[-1]
        got = self.template1.format(
            table=table,
            target_column=str(target[0]),
            target_value=wrap(target[1]),
            base_column=str(base[0]),
            base_value=wrap(base[1]),
        )
        return got


class MySQLManager:
    def __init__(self, walk_to_network_vector_database=True):
        self.mydb = mysql.connector.connect(
            host="database.dev", user="root", password="mysql_password"
        )
        if self.mydb.is_connected():
            print("MySQL Database has been successfully connected!")
            self.cursor = self.mydb.cursor()
        if walk_to_network_vector_database:
            self.do("USE prefocus;")
        self.capacity = 1000000

    def tear_down(self):
        self.mydb.close()

    def fetch(self, select_query):
        try:
            self.cursor.execute(select_query)
            got = self.cursor.fetchall()
            got = [list(tu) for tu in got]
            return got
        except Exception as e:
            return []

    def do(self, cmd, test=False):
        try:
            if test:
                pass
            else:
                self.cursor.execute(cmd)
                self.mydb.commit()
        except Exception as e:
            print(
                "MySQLManager failed executing the command:\n{cmd}\nError:{error}".format(
                    cmd=str(cmd), error=str(e)
                )
            )

    def get_default_focused_table(self):
        return self.fetch(SelectSQL().select_query(focused_table))

    def get_default_focusing_table(self):
        return self.fetch(SelectSQL().select_query(focusing_table))

    def _insert_into_default_table_with_multiple_queries(self, table, rows):

        chunks = [
            rows[i : i + self.capacity] for i in range(0, len(rows), self.capacity)
        ]
        for chunk in chunks:
            insert_sql = InsertSQL().insert_multipe_query(
                if_specify_columns=False, rows=chunk, table=table
            )
            self.do(insert_sql)

    def insert_into_default_focused_table(self, rows):
        self._insert_into_default_table_with_multiple_queries("focused", rows)

    def insert_into_default_focusing_table(self, rows):
        self._insert_into_default_table_with_multiple_queries("focusing", rows)

    def clean_default_focused(self):
        self.do("DELETE FROM focused;")

    def clean_default_focusing(self):
        self.do("DELETE FROM focusing;")

    def purge_database(self):
        self.clean_default_focused()
        self.clean_default_focusing()
