from kivy.app import App
from kivy.uix.button import Button
from plyer import gps

class MainApp(App):
    def my_func(self):
        gps.configure(on_location=self.on_gps)
        gps.start()

    def on_gps(self, **kwargs):
        gps.stop()
        return Button(text=kwargs)


MainApp().run()
