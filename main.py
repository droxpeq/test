from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psycopg2

app = FastAPI()

def get_db_connection():
    con = psycopg2.connect(
        host="localhost",
        database="task2db",
        user="postgres",
        password="123456"
    )
    return con

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <h1>Главная страница</h1>
    <button onclick="window.location.href='/people'">Люди</button>
    <button onclick="window.location.href='/animals'">Животные</button>
    """

@app.get("/people", response_class=HTMLResponse)
async def read_people():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM person;")
    rows = cur.fetchall()
    cur.close()
    con.close()

    people_html = "<h1>Таблица людей</h1><table border='1'><tr><th>ID</th><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Пол</th><th>Дата рождения</th><th>Номер дома</th></tr>"
    for row in rows:
        people_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3] if row[3] else ''}</td><td>{'Ж' if row[4] else 'М'}</td><td>{row[5].strftime('%d.%m.%Y')}</td><td>{row[6]}</td></tr>"
    people_html += "</table><br><button onclick=\"window.location.href='/'\">На главную</button>"
    
    return people_html

@app.get("/animals", response_class=HTMLResponse)
async def read_animals():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM animal;")
    rows = cur.fetchall()
    cur.close()
    con.close()

    animals_html = "<h1>Таблица животных</h1><table border='1'><tr><th>ID</th><th>Владелец</th><th>Кличка</th><th>Вид</th><th>Пол</th><th>Дата рождения</th><th>Дата и время регистрации</th><th>Описание</th></tr>"
    for row in rows:
        
        animals_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{'Ж' if row[4] else 'М'}</td><td>{row[5].strftime('%d.%m.%Y')}</td><td>{row[6].strftime('%d.%m.%Y %H:%M:%S')}</td><td>{row[7]}</td></tr>"
    animals_html += "</table><br><button onclick=\"window.location.href='/'\">На главную</button>"
    
    return animals_html

