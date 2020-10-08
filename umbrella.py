import json
import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



def get_precip():
    postal_code = input("postal code:")
    country_code = input("Country code(i.e ES, DE, FR)")

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
    return "Chance of rain is " + str(precip)  +" : " + msg
get_precip()

class MyGrid(Widget):
    
    post_cod = ObjectProperty(None)
    country_cod = ObjectProperty(None)

    def btn(self):
        print("Código Postal: ", self.post_cod.text, "Código País:", self.country_cod.text)

    


class Umbrella(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    Umbrella().run()