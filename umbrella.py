import json
import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout



def get_precip(postal_code, country_code):
    

    access_key = "e0869c46affe410a85b7bd30345383e5"


    url = f'http://api.weatherbit.io/v2.0/forecast/daily?postal_code={postal_code}&country={country_code}&days=1&key={access_key}'
    r = requests.get(url)
    data = json.loads(r.content)
    data_dict = data['data']
    precip = data_dict[0]['precip']


    if(int(precip) > 55):
        msg = "You should bring an umbrella with you today!"
    else:
        msg = "Doesn't look like you'll need an umbrella today..."

    print(type(data))
    print("Chance of rain is " + str(precip)  +" : " + msg)




class MyFloat(FloatLayout):
    post_cod = ObjectProperty(None)
    country_cod = ObjectProperty(None)
    
    def start(self):
        postal_code = self.post_cod.text
        country_code = self.country_cod.text

        return get_precip(postal_code, country_code)






class Umbrella(App):
    
    def build(self):
        return MyFloat()

if __name__ == "__main__":
    Umbrella().run()