import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from database import uploadToDB
import geocoder

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'Goto map'
            size_hint: (.3, .2)
            on_press: root.manager.current = 'map'
            pos: (75,200)
        Button:
            text: 'Quit'
            size_hint: (.3, .2)
            pos: (400, 200)
<MapScreen>:
    FloatLayout:
        MapView:
            lat: 40.423538
            lon: -86.9217
            zoom: 15
            on_touch_down: print("nice")
        Button:
            text: 'Add an event'
            on_press: root.manager.current = 'event'
            size_hint: (.3, .2)
            pos: (600, 100)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            size_hint: (.3, .2)
            pos: (600, 0)
<EventScreen>:
    FloatLayout:
        Button:
            text: '←'
            on_press: root.manager.current = 'map'
            size_hint: (.3, .2)
            pos: (50, 0)
        Button:
            text: 'Upload'
            on_press: root.upload(42, 42, name_box, descrip_box)
            size_hint: (.3, .2)
            pos: (300, 0)
    GridLayout:
        cols:1
        spacing:200
        size: root.width-300, root.height-300
        GridLayout:
            cols: 2
        GridLayout:
            spacing:20

            cols:2
            Label:
                text: "Event Name:"
            TextInput:
                id: name_box
                multiline:False
            Label:
                text: "Description:"
            TextInput:
                id: descrip_box
        GridLayout:
            cols:2
               
""")


# Declare screens
class MenuScreen(Screen):
    pass


class MapScreen(Screen):
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print(touch)
        print("hello")


class EventScreen(Screen):
    def upload(self, lat, long, title, descrip):
        #do database things
        g = geocoder.ip('me')
        uploadToDB(title.text, descrip.text, g.lat, g.lng)
        print('Latitude = {0}, Longitude = {1}, Title = {2}, Description = {3}'.format(lat, long, title, descrip))



class Touch(Widget):
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print(touch)
        print("hello")


class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(EventScreen(name='event'))

        return sm


if __name__ == '__main__':
    MyApp().run()
# MyApp().run()