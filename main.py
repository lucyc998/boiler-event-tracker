import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

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
        TextInput:
            id: my_text
            size_hint:(.3, .2)
""")

# Declare screens
class MenuScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class EventScreen(Screen):
    pass

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
#MyApp().run()


