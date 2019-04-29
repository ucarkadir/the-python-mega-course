import sqlite3
  
# constructor __init__

class Database:  
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()
        

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()        
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",(title, author, year, isbn))
        rows=self.cur.fetchall()        
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn,id,))
        self.conn.commit()
    
    def __del__(self): # deleting database object
        self.conn.close()

# insert("kitap1", "yazar1", 1, 1111)

# insert("kitap2", "yazar2",2,2222)
#print(search(title="kitap1"))
# insert("kitap3", "yazar3",3,3333)
# delete(3)
# update(id=2, title="kitaps",author="yazars",year=3,isbn=3333)
# insert("kitap4", "yazar4",4,4444)
# print(view())