import psycopg2
import json




class InserDb():

    def Conectdb():

 

        local_conexion = psycopg2.connect(
            host='localhost',
            port=5432,
            user="postgres",
            password="admin",
            database="arq_datos"
        )

        cursorl = local_conexion.cursor()
        return local_conexion

    con = Conectdb()

    def etl_data(*args):
        # print(args)
        cursorl = InserDb.con.cursor()
        
        placeholders = ', '.join(['%s'] * len(args))
      
      
        query = "INSERT INTO etl_datos (estu_tipodocumento, cole_area_ubicacion, cole_bilingue, cole_depto_ubicacion, cole_jornada, estu_depto_reside, estu_genero, estu_mcpio_presentacion, estu_mcpio_reside, fami_estratovivienda, desemp_ingles, punt_ingles, punt_matematicas, punt_sociales_ciudadanas, punt_c_naturales, punt_lectura_critica, punt_global) VALUES (" + placeholders + ")"
       
        cursorl.execute(query, args)
        InserDb.con.commit()
        cursorl.close()
    # def etl_data(*args):
    #     print(args)
    #     cursorl = InserDb.con.cursor()
    #     cursorl.execute(
    #         "INSERT INTO etl_datos (estu_tipodocumento,cole_area_ubicacion,cole_bilingue,cole_depto_ubicacion,cole_jornada,estu_depto_reside,estu_genero,estu_mcpio_presentacion,estu_mcpio_reside,fami_estratovivienda,desemp_ingles,punt_ingles,punt_matematicas,punt_sociales_ciudadanas,punt_c_naturales,punt_lectura_critica,punt_global) VALUES (%s)", (args))
    #     InserDb.con.commit()
    #     cursorl.close()
