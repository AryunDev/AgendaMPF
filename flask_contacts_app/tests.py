# from mysql.connector import connect, Error
# from flask import Flask, request, render_template

# class DataBase:

#     def __init__(self):
#         try:
#             aux = connect(
#                 host ='localhost',
#                 user ='root',
#                 password =  'abc.123', # getpass("Antes de continuar, debe que ingresar la clave de administrador de este sistema: \n-------->"),
#                 database ='contacts'
#             )
#             self.connection = aux
#             print("conectados")
            
#         except Error as e:
#             print("Error" + e)
    
#     def insert(self,sql):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(sql)
#             self.connection.commit()
#             self.close()
#         except Error as e:
#             print(e)