import googlemaps, requests, bs4, json, urllib

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text_file = open('/Users/Joshua/Desktop/Python/suburb_id.txt', 'w')
for n in range(len(alphabet)):
    data = requests.get('https://data.police.qld.gov.au/api/boundary?name='+alphabet[n]+'&returngeometry=false&maxresults=')
    data = data.json()

    for k in range(len(data['Result'])):
        if 'QldSuburbId' in data['Result'][k]:
            print(data['Result'][k]['QldSuburbId'])
            text_file.write(str(data['Result'][k]['QldSuburbId']))
            text_file.write("\n")
text_file.close()
