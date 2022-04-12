from pymongo import MongoClient
import datetime
import json
from main import Database


if __name__ == "__main__":

    mongo_user = 'xxx'
    mongo_pass = 'xxx'
    database_name = 'xxx'
    collection_name = 'xxx'

    myDatabase = Database(mongo_user,mongo_pass,database_name,collection_name)

    db = myDatabase.connected_client.usage #We can now create a database object referencing a new database, called “usage”, as follows:

    from random import randint
    #Step 1: Connect to MongoDB - Note: Change connection string as needed
    client = MongoClient(port=27017)

    #throwaway testing data
    project_number = 111234123
    currentDateTime = datetime.datetime.now()
    start_date = 'end date'
    end_date = 'start date'
    selected_content = 'content'
    coords = 'testing coords'
    geo = 'D:/AEC_Downloader/map (6).geojson'

    # Loading or Opening the json file
    with open(geo) as file:
        file_data = json.load(file)

    coords = file_data.get('features')[0].get('geometry').get('coordinates')[0]

    #Create sample data
    geometry_data_request = {'project_number': project_number,
                             'requested_time': currentDateTime,
                             'start_date': start_date,
                             'end_date': end_date,
                             'selected_content': str(selected_content),
                             'coordinate_request': coords,
                             'geojson_data': file_data
                             }



    result = db.requests.insert_one(geometry_data_request)
    print('Created Entry'.format(result.inserted_id))
    print('finished adding geometry to the Mongo DB Database!')
