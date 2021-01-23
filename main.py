import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import requests

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
            id: map_view
            lat: 40.423538
            lon: -86.9217
            zoom: 18
            on_touch_down: print("nice")
            MapMarkerPopup:
                lat: 40.423538
                lon: -86.9217
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
    GridLayout:
        cols:1
        spacing:200
        size: root.width-300, root.height-300
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
            Button:
                text: "Add Event"
                on_press: root.manager.current = 'map'
            Button:
                text: "Cancel"
                on_press: root.manager.current = 'map'                
""")


# Declare screens
class MenuScreen(Screen):
    pass


class MapScreen(Screen):
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print(touch)
        print(type(touch.pos))
        print(touch.pos[1])
        print(self.ids.map_view.lon)
        url = 'http://ipinfo.io/json'
        locData = requests.get(url).json()
        userlat, userlon = locData['loc'].split(",")
        print(userlat, userlon)
        self.ids.map_view.add_marker(
            MapMarker(lon=float(userlon), lat=float(userlat)))


class EventScreen(Screen):
    pass


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