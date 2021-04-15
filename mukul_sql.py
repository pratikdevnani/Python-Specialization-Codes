import sqlite3

conn = sqlite3.connect('muks.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')

cur.execute('''SELECT name FROM Artist''')
res = cur.fetchall()
l = []
for x in res:
    l.append(x)
