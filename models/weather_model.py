class WeatherModel:
    def __init__(self, clouds, humidity, pressure, temperature):
        # These variables will act as Json Name entities
        self.clouds = clouds
        self.humidity = humidity
        self.pressure = pressure
        self.temperature = temperature

    @staticmethod
    def toJsonMap(data):
        clouds = data['weather'][0]['main']
        humidity = str(data['main']['humidity']) + '%'
        pressure = str(data['main']['pressure']) + ' hPa'
        temperature = str(data['main']['temp_max']) + "C"
        return WeatherModel(clouds, humidity, pressure, temperature).__dict__
