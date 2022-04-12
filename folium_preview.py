import io
import sys
from pathlib import Path
import folium
from folium.plugins.draw import Draw
from folium import GeoJson, raster_layers
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from folium.plugins import TimestampedWmsTileLayers, Geocoder
root = str(Path(__file__).parents[2]).replace('\\', '/')  # Get root of project

class Nearmap_Folium_Map(QWidget):

    def __init__(self, connected_database, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        vbox = QVBoxLayout(self)
        self.webEngineView = QWebEngineView()
        self.webEngineView.page().profile().downloadRequested.connect(
            self.handle_downloadRequested
        )
        self.loadPage()
        vbox.addWidget(self.webEngineView)
        self.setLayout(vbox)
        self.setGeometry(1000, 150, 1000, 900)
        self.setWindowTitle("Nearmap Folium Download Map")
        self.show()


    def loadPage(self):
        m = folium.Map(location=[42.3549317072117, -71.06890472570417], zoom_start=5)

        folium.TileLayer('cartodbdark_matter').add_to(m)

        Geocoder(
            collapsed=False,
            position='topleft',
            add_marker=True
        ).add_to(m)


        import pandas as pd
        client = connected_database.connected_database
        db = connected_database.mydb
        mycollection = connected_database.mycol

        # Create the pandas DataFrame for printing.
        df = pd.DataFrame()

        for x in mycollection.find():
            df = df.append(x, ignore_index=True)

        for row,column in df.iterrows():
            geojson_data = column['geojson_data']
            style = lambda x: {'fillColor': '#036ffc', 'color': "#000", 'opacity': 0.5, 'weight': 0.5,'fillOpacity': 0.4}

            tooltip_string = f'Client is {column.client_name} \n Requested Area is {column.request_area} \n User who Downloaded is: {column.user}'

            GeoJson(data =geojson_data,
                    name="Customer Data Pull",
                    tooltip=tooltip_string,
                    style_function=style
                    ).add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webEngineView.setHtml(data.getvalue().decode())

    def handle_downloadRequested(self, item):
        path = file_defined_name
        if path:
            item.setPath(path)
            item.accept()


if __name__ == "__main__":
    from main import Database

    mongo_user = 'xxx'
    mongo_pass = 'xxx'
    database_name = 'xxx'
    collection_name = 'xxx'

    connected_database = Database(mongo_user,mongo_pass,database_name,collection_name)

    app = QApplication(sys.argv)
    okno = Nearmap_Folium_Map(connected_database)
    sys.exit(app.exec_())

