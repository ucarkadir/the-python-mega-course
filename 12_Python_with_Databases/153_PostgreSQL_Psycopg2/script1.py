'''
1. connet to a databese
2. create a cursor object 
3. write an sql query
4. commit changes
5. close database connection
'''

'''
PostgreSQL

user: postgres
password: postgres123
port: 5432

https://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg

psycopg2‑2.7.6.1‑cp37‑cp37m‑win_amd64.whl
    cp37 => py 3.7 
pip install psycopg2

'''

import psycopg2

def create_table():
    conn= psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn= psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows




# run functions
create_table()

insert("water glass", 10, 5)
insert("coffee cup", 12, 7.75)

delete("coffee cup")
update(15,9.75,"water glass")

print(view())
