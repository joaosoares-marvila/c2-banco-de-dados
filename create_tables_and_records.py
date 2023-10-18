import sys

import os
from pathlib import Path

from src.conexion.oracle_queries import OracleQueries

diretorio_atual = Path(__file__).resolve().parent
diretorio_sql = os.path.join(diretorio_atual, 'sql')

diretorio_create_tables = os.path.join(diretorio_sql, 'create_tables.sql')
diretorio_insert_sample_records = os.path.join(diretorio_sql, 'inserting_samples_records.sql')

print(diretorio_sql)

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:   
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def run():

    with open(diretorio_create_tables) as f:
        query_create = f.read()

    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

    with open(diretorio_insert_sample_records) as f:
        query_generate_records = f.read()

    print("Gerenating records")
    generate_records(query=query_generate_records)
    print("Records successfully generated!")


if __name__ == '__main__':
    run()
    