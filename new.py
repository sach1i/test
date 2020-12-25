from kivy.app import App
from kivy.uix.button import Button
from plyer import gps

class MainApp(App):
    def my_func(self):
        gps.configure(on_location=self.on_gps)
        gps.start()
        gps.stop()

    def on_gps(self, **kwargs):
        lat = 'lat: {lat}'.format(**kwargs)
        lon = 'lon: {lon}'.format(**kwargs)
        return (lat,lon)

    def build(self):
        self.my_func()
        result = self.on_gps()
        return Button(text=result)

MainApp().run()
