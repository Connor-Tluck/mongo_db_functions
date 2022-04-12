
'''mongodb database manipulation functions'''
from pymongo import MongoClient
import pandas as pd

class Database:

    def __init__(self, mongo_user,mongo_pass,database_name,collection_name):
        self.mongo_user = mongo_user
        self.mongo_pass = mongo_pass
        self.database_name = database_name
        self.collection_name = collection_name

        #connection functions
        connector_string = f"mongodb+srv://{self.mongo_user}:{self.mongo_pass}@cluster0.ijjjl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        myclient = MongoClient(connector_string)
        self.connected_database = myclient
        self.mydb = myclient[self.database_name]
        self.mycol = self.mydb[self.collection_name]



    "Database Manipulation Functions Below."
    def read_all_data(self):
        df = pd.DataFrame()
        for x in self.mycol.find():
            df = df.append(x, ignore_index=True)
        print(df)

    def write_to_csv(self):
        df = pd.DataFrame()
        for x in self.mycol.find():
            df = df.append(x, ignore_index=True)
        df.to_csv('customer_database_requests.csv', index=False)
        print('database written as customer_database_requests.csv')

    def delete_all(self):
        user_input = input('Are you sure you want to delete all the data in your Database, This cannot be undone! Type "YES" if you wish to Delete all the contents in your Database')
        if user_input == 'YES':
            self.mycol.delete_many({})
            print(x.deleted_count, " documents deleted.")
        else:
            print('Choose to not Delete, passing function, Database intact.')

    def check_connection(self):
        if self.connected_database.server_info().get('ok') == 1.0:
            print('server login OKAY')
        else:
            print('please confirm username and password')

    def visualize(self):
        from folium_preview import Nearmap_Folium_Map
        from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
        import sys

        app = QApplication(sys.argv)
        okno = Nearmap_Folium_Map(self)
        sys.exit(app.exec_())

if __name__ == "__main__":

    mongo_user = 'xxx'
    mongo_pass = 'xxx'
    database_name = 'xxx'
    collection_name = 'xxx'

    myDatabase = Database(mongo_user,mongo_pass,database_name,collection_name)
