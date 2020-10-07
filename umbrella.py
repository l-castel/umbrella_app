import json
import requests

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
