import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button 
from radarAPIcalls import getAddresses
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout 
from database import uploadToDB
from database import fetchFromDB

Window.size = (350, 625)

Builder.load_string("""
<MapScreen>:
    FloatLayout:
        MapView:
            id: map_view
            lat: 40.423538
            lon: -86.9217
            zoom: 15
        Button:
            text: 'Add Event'
            on_press: root.manager.current = 'event'
            size_hint: (.3, .12)
            pos: (125, 20)
        Label:
            text: 'Boiler Event Tracker'
            pos: (0, 297)
            font_size: 20
            color: (0, 0, 0, 1)

<EventScreen>:
    FloatLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'map'
            size_hint: (.43, .12)
            pos: (17, 20)
        Button:
            text: 'Upload'
            on_press: root.upload(name_box.text, descrip_box.text, location_box.text)
            size_hint: (.43, .12)
            pos: (183, 20)
        TextInput
            text: 'Event Name: '
            id: name_box
            font_size: 25
            size_hint: (.90, .24)
            pos: (17, 455)
            background_color: (255, 255, 255, 1)
            color: (255, 255, 255, 1)
            multiline: True 
        TextInput
            text: 'Location: '
            id: location_box 
            font_size: 25
            size_hint: (.90, .24)
            pos: (17, 285)
            background_color: (255, 255, 255, 1)
            color: (255, 255, 255, 1)
            multiline: True
        TextInput
            text: 'Description: '
            id: descrip_box 
            font_size: 25
            size_hint: (.90, .24)
            pos: (17, 115)
            background_color: (255, 255, 255, 1)
            color: (255, 255, 255, 1)
            multiline: True 
""")


# Declare screens

class MapScreen(Screen):

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        posts = fetchFromDB()
        for event in posts:
            lat = event['lat']
            lon = event['lon']
            marker = MapMarkerPopup(lon=lon,lat=lat, source="small_marker.png")
            self.ids.map_view.add_marker(marker)
            btn = Button(
                text ='Event: ' + event['Event'] + '\n\n\n' + 'Description:' + event['Description'],
                size_hint = (3, 2),
                font_size = 20)
            btn.bind(on_release= callback)
            marker.add_widget(btn)

        
def callback(instance):
    instance.opacity=0
    instance.disabled=True
 

class EventScreen(Screen):
    def upload(self, title, descrip, location):
        #do database things
        result = getAddresses(location.replace('Location:', "").strip())[0]
        if result == 0:
            return 0
        uploadToDB(title.replace("Event Name:", ""), result['placeLabel'], descrip.replace("Description:", ""), result['latitude'], result['longitude'])
        #print('Latitude = {0}, Longitude = {1}, Title = {2}, Description = {3}'.format(lat, long, title, descrip, location))



class Touch(Widget):
    def on_touch_down(self, touch):
        super().on_touch_down(touch)


class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(EventScreen(name='event'))

        return sm

if __name__ == '__main__':
    MyApp().run()
# MyApp().run()

''' m1 = MapMarkerPopup(lon=-86.9217, lat=40.423538, source="small_marker.png")
        self.ids.map_view.add_marker(m1)
        btn1 = Button(text="Get event info")
        btn1.bind(on_press=callback)
        m1.add_widget(btn1)'''
       
''' def add_markers():
        posts = fetchFromDB()
        for event in posts:
            print(event)
            lat = event['lat']
            lon = event['lon']
            marker = MapMarkerPopup(lon=lon,lat=lat, source="small_marker.png")
            self.ids.map_view.add_marker(marker)  '''