import pandas as pd
import numpy as np

## db libraries
from sqlalchemy import create_engine

## Warnings and other tools
import itertools
import warnings
warnings.filterwarnings("ignore")



# definición de la creación del engine
def createSQLdb():
  global dbConnection
  db_engine = create_engine("postgresql://postgres:password@data-challenge.co4whz3w2rtn.us-east-1.rds.amazonaws.com:5432/dbneoland", pool_recycle=3600)
  dbConnection = db_engine.connect();
  print("------- SQL Start ------")
  return queryInput(dbConnection)


# definición de la finalización del motor SQL
def stopSQL(dbConnection):
    dbConnection.close()
    print("------ Completed, SQL DB closed! -----")


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

def excelDF(q_task1,dbConnection):
    try:
        df = pd.read_sql_query(sql=q_task1, con=dbConnection)
        df.set_index(df['merchant_id'], inplace=True)
        df.drop(['merchant_id'], axis=1, inplace=True)
        df.to_excel('task1.xlsx', index=True, sheet_name="task2.1")
        print("------ Complete, Excel file generated! -----")
    except Exception as e:
        print(e)
    finally:
      stopSQL(dbConnection)


if __name__ == '__main__':
    createSQLdb()
    