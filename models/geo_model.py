class GeoModel:
    def __init__(self, lat, lng):
        # These variables will act as Json Name entities
        self.lat = lat
        self.lng = lng

    @staticmethod
    def toJsonMap(data):
        lat = data[0]['lat']
        lng = data[0]['lon']
        return GeoModel(lat , lng,).__dict__
