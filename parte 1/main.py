# main.py

import os
import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins = "*")

def connection_to_database():
    try:
        connection = psycopg2.connect (
            user = "postgres",
            password = os.environ["DB_PASSWORD"],
            host = "localhost",
            port = "5432",
            database = "postgres",
            cursor_factory = RealDictCursor
        )

        return connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL - ", error)

def query_get_all_data(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM teste.relatorio_cadop")
        data = cursor.fetchall()
        return data
    
def search_query(connection, searched_word):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                       select 
                       * 
                       from teste.relatorio_cadop
                       where
                       razao_social ilike '%{searched_word}%'
                       """)
        data = cursor.fetchall()
        return data

@app.get("/cadastros")
async def read_relatorio():
    connection_db = connection_to_database()
    relatorio = query_get_all_data(connection_db)
    connection_db.close()
    return {"data" : relatorio}

@app.get("/cadastros/procurar")
async def read_procurar_from_relatorio(palavra: str = ''):
    connection_db = connection_to_database()
    relatorio = search_query(connection_db, palavra)
    connection_db.close()
    return {"resultado" : relatorio}