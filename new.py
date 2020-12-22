from kivy.app import App
from plyer import gps

class MainApp(App):
    def my_func(self):
        gps.configure(on_location=self.on_gps)
        gps.start()
        gps.stop()

    def on_gps(self, **kwargs):
        print('lat: {lat}, lon: {lon}'.format(**kwargs))

MainApp().run()
