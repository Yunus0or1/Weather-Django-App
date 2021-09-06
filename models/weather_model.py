class WeatherModel:
    def __init__(self, clouds, humidity, pressure, temperature):
        # These variables will act as Json Name entities
        self.clouds = clouds
        self.humidity = humidity
        self.pressure = pressure
        self.temperature = temperature

    @staticmethod
    def toJsonMap(clouds,humidity, pressure, temparature):
        clouds =  clouds
        humidity =  humidity+ '%'
        pressure = pressure+ ' hPa'
        temperature =  temparature+ "C"
        return WeatherModel(clouds, humidity, pressure, temperature).__dict__
