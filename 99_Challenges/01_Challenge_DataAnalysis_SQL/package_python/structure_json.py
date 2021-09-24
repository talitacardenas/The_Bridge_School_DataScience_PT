queries = {
    "header": {
            "nombre_del_fichero": "task01",
    "format": "sql",
    "date": "2021.09.22T19:15:12"
    "version": 1.0
    "author": mrusso
    },
    "content": {
        [
            
              "set_index": "merchant_id",
              "outputfilename": "task01"  
            }
        ]
    }


}



open(f"sql_queries/{nombre_del_fichero}", "r") as f:
    f.read
