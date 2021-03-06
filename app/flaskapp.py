from flask import Flask
from flask_mysqldb import MySQL
import os

HOST = 'db'

app = Flask(__name__)

app.config['MYSQL_HOST'] = HOST
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'

mysql = MySQL(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM nflteams.team_colors''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
