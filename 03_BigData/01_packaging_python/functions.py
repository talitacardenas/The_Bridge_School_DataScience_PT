from argparse import ArgumentParser
import os
import logging
from datetime import datetime

# Definición de la recogida de los argumentos
def setArguments():
  global options
  parser = ArgumentParser(description='Ejemplo recogida de parámetros')
  parser.add_argument('-op','--opType',choices=['night','day'],
                      default='night', type=str,
                      help="ejemplo de recogida parámetro entre varias opciones, \
                      ' día o noche'")
  parser.add_argument('-e','--env',choices=['BAK','INT','DEV','PRE','PRO'],
                      default='PRE', type=str,
                      help="parámetro obligatorio, seleccionar entre PRE y el resto")
  options = parser.parse_args()
  return options

# Definimos la función principal
def concatena_args(*args):
  '''
  description

  return

  args

  example

  '''
  try:
    print("*"*10, "\/"*15, "*"*10)
    print(f"Estos son los parámetros que has seleccionado: el primero es {args[0].upper()} y el segundo es {args[1].upper()}. \n")
  except Exception as e:
    print(e)



# Creamos la carpeta para guardar los ficheros logs

def create_logdir(log_directory):
  global file_handler
  filepath = os.path.join(log_directory, f"output.log")
  try:
    if not os.path.exists(log_directory):
      os.makedirs(os.path.dirname(log_directory), exist_ok=True)
  except:
    pass


# Definición del logfile

def create_logfile():
    global logger
    try:
        log_directory = "logs/"
        if not os.path.exists(log_directory):
            create_logdir(log_directory)
                # Gets or creates a logger
            logger = logging.getLogger(__name__) 
            logger.setLevel(logging.WARNING)
            logger.setLevel(logging.DEBUG)
            # define file handler and set formatter
            new_date = datetime.now()
            file_handler = logging.FileHandler(f"{log_directory}/outputlog_"+str(new_date)+".log", mode="w", encoding=None, delay=False)
            #file_handler = logging.FileHandler(f"logfile_{str(new_date)}.log", mode="w", encoding=None, delay=False)
            #formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
            formatter = logging.Formatter('%(asctime)s : %(levelno)s : %(levelname)s : %(name)s : %(message)s')
            file_handler.setFormatter(formatter)
            # add file handler to logger
            logger.addHandler(file_handler)
            
    except:
        pass