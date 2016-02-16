#To Do - Add unix date converter
#integrate crimes and suburb information
#scale up for each crime
#export to excel

import googlemaps, requests, bs4, json
gmaps = googlemaps.Client(key='AIzaSyAOaR4VaOIs2iNmDziwwqe8Fn5ff86sfEA')


address = "44 johnston st, carina"

#Start and end date of when to test for crime data (in Unix timestamp format)
start_date = '946684800' #1/1/2010
end_data = '1453420800' #22/1/16

#Convert Address to Geocode
def replace_spaces(word):
    new_word = str(word.replace(" ","+"))
    return(new_word)

def geocode_address(address_string):
    replace_spaces(address_string)
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address_string)
    response.raise_for_status()
    resp_json_payload = response.json()
    return(resp_json_payload)

address_table = geocode_address(address)

#Convert Geocoded address to suburb, post code etc
#Answer from StackOverflow User Saleem Latif - http://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
#Post Code = https://developers.google.com/maps/documentation/geocoding/intro

post_code = (address_table)['results'][0]['address_components'][5]['long_name']
suburb = (address_table)['results'][0]['address_components'][2]['long_name']
state = (address_table)['results'][0]['address_components'][3]['long_name']
latitude = (address_table)['results'][0]['geometry']['location']['lat']
longitude = (address_table)['results'][0]['geometry']['location']['lng']
replace_spaces(suburb)

#Get Crime details
police_data = requests.get('https://data.police.qld.gov.au/api/boundary?name='+ suburb +'&returngeometry=true&maxresults=1&offences=54')
police_data = police_data.json()
print(police_data)
