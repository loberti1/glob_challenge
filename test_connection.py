from sqlalchemy import create_engine,text

#generate connection
server = 'E-01520'
database = 'glob_dw'
username = 'sqlserverluciano'
password = 'crisiscore789'
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)

#sql query
try:
    with engine.connect() as my_connection:
        sql = text("SELECT 1")
        result = my_connection.execute(sql)
        print("connection working OK")
except Exception as e:
    print(f"error present: {e}")