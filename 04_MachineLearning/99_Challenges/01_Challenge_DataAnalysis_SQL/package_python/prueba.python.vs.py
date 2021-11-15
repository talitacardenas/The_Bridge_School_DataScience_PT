import pandas as pd
import numpy as n

## db libraries
from sqlalchemy import create_engine

## Warnings and other tools
import itertools
import warnings
warnings.filterwarnings("ignore")

# definición de la creación del engine
def createSQLdb():
    '''
    aquí va la descripción de la función
    Description:dsdsd

    Subject:

    Argumentos:

    Return:

    Example:
    
    '''
    global dbConnection
    try:
        db_engine = create_engine("postgresql://postgres:password@data-challenge.co4whz3w2rtn.us-east-1.rds.amazonaws.com:5432/dbneoland", pool_recycle=3600)
        dbConnection = db_engine.connect();
        print("------- SQL Start ------")
    except Exception as e:
        print(f"Existe un error en la función {createSQLdb.__name__} que es {e}")
    finally:
        return queryInput(dbConnection)
  
  
  # definición de la finalización del motor SQL

def stopSQL(dbConnection):
    dbConnection.close()
    print("------ Completed, SQL DB closed! -----")


# Definición de las recogida de queries
def getQueries(queries):
    open("ruta_donde_están_las_queries.txt", "r") as f:
        '''
        COMPLETAR
        '''
    return excelDF(varQuery,dbConnection )


# Definición de las queries
def queryInput(dbConnection):
    q_task1 = '''
            select
                O.merchant_uuid as merchant_id,
                count(O.uuid) as num_creditos,
                round(sum(O.booking)::numeric, 2) as Sales
            from public.orders as O
            inner join public.merchants as M
            on O.merchant_uuid = M.uuid
            where O.number_instalments > 0 and O.annual_percentage_rate > 0
            group by merchant_id
            order by  num_creditos desc
            '''
    return excelDF(q_task1,dbConnection )

merchant_id = "resultado_desde_otra_función_que_lee_un_json"
nombre_fichero = "resultado_desde_otra_función_que_lee_un_json"
outputfilename = "resultado_desde_otra_función_que_lee_un_json"


def excelDF(varQuery,dbConnection):
    try:
        df = pd.read_sql_query(sql=varQuery, con=dbConnection)
        df.set_index(df[merchant_id], inplace=True)
        df.drop([merchant_id], axis=1, inplace=True)
        df.to_excel('task_{index}.xlsx', index=True, sheet_name="task_{sheet_name}")
        print("------ Complete, Excel file generated! -----")
    except Exception as e:
        print(e)
    finally:
        stopSQL(dbConnection)
        
def queryInput(dbConnection):
    q_task2 = '''
            select
                industry_code,
                count(O.uuid) as num_creditos,
                round(sum(O.booking)::numeric, 2) as Sales
            from public.orders as O
            inner join public.merchants as M
            on O.merchant_uuid = M.uuid
            where O.number_instalments > 0 and O.annual_percentage_rate > 0
            group by industry_code
            order by  num_creditos desc
            '''    return excelDF(q_task2,dbConnection
            
#def excelDF(q_task2,dbConnection):
    try:
        df = pd.read_sql_query(sql=q_task2, con=dbConnection)
        df.set_index(df['industry_code'], inplace=True)
        df.drop(['industry_code'], axis=1, inplace=True)
        df.to_excel('task2.xlsx', index=True, sheet_name="task2.2")
        print("------ Complete, Excel file generated! -----")
    except Exception as e:
        print(e)
    finally:
        stopSQL(dbConnection)

def queryInput(dbConnection):
    q_task3 = '''
                SELECT created,
                EXTRACT(MONTH FROM created) AS created_month,
                round(sum(booking)::numeric, 2) as sum_booking,
                industry_code
                FROM orders
                JOIN merchants
                ON orders.merchant_uuid = merchants.uuid
                group by created, merchants.industry_code,booking
                order by created, booking asc
            '''
    return excelDF(q_task3,dbConnection)
    

def excelDF(q_task3,dbConnection):
    try:
        df = pd.read_sql_query(sql=q_task3, con=dbConnection)
        df.assign(created=lambda x: pd.DatetimeIndex(x.created).month)
        df.set_index(df['created_month'], inplace=True)
        df.drop(['created','created_month'], axis=1, inplace=True)
        df.to_excel('task3.xlsx', index=True, sheet_name="task2.3")
        print("------ Complete, Excel file generated! -----")
    except Exception as e:
        print(e)
    finally:
        stopSQL(dbConnection)
        
        

if __name__ == '__main__':
    createSQLdb()