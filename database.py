import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT)")
    conn.commit()


conn = sqlite3.connect('test.db')

# list of files

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop through each object in the tuple to find files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_list (col_files) VALUES (?)", (x,))
            print(x)

conn.close()
