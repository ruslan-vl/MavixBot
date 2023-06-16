import sqlite3

import errors



db = sqlite3.connect("database.db")
sql = db.cursor()




def create_teble(name, **kwargs):
	kwargs = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT"} | kwargs
	fields = ", ".join([f"[{field}] {types}" for field, types in kwargs.items()])
	sql.execute(f"create table if not exists '{name}' ({fields})")


create_teble("history", time_at = "BIGINTEGER", action = "INTEGER")



def get(table, fields = "*", order_by = "id asc", limit = None, offset = 0, **where):
	fields_ = (f'{", ".join(fields)}') if fields != "*" else fields
	where_fields = ", ".join([f"[{_fields}] = '{value}'" for _fields, value in where.items()])
	where = "" if not where else f"WHERE {where_fields}"
	order_by = "" if not order_by else f"ORDER BY {order_by}" # ask 1-9, desc 9-1
	limit = "" if not limit else f"LIMIT {limit}"
	offset = "" if not offset else f"OFFSET {offset}"
	result = sql.execute(f"SELECT {fields_} FROM [{table}] {where} {order_by} {limit} {offset}").fetchall()
	if result:
		return result
	else:
		return None



def add(table, *values, **kwargs):# fields: list = None, values: list = None):
	if not values:
		fields = list(kwargs.keys())
		values = list(kwargs.values())
	else:
		fields = None
	if values == None: raise errors.ErrorUnknown()
	fields = f'({", ".join(fields)})' if fields else ""
	num_values = ", ".join(["?" for i in values])
	lastrowid = sql.execute(f"INSERT INTO '{table}' {fields} VALUES ({num_values})", values).lastrowid
	db.commit()
	return lastrowid



def update(table, where, **fields):
	where = ", ".join([f"[{_fields}] = '{value}'" for _fields, value in where.items()])
	math = lambda f, v: f"[{f}] {v}" if str(v)[0] in ("+", "-") else f"'{v}'"
	edits = ", ".join([f"[{_fields}] = {math(_fields, value)}" for _fields, value in fields.items()])
	
	sql.execute(f"UPDATE '{table}' SET {edits} WHERE {where}")
	db.commit()



def delete(table, where):
	sql.execute(f"DELETE FROM '{table}' WHERE {where}")
	db.commit()

