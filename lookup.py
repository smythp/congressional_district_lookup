import csv
import requests
from key import api_key


def generate_request(address, city, county, state, zip):
    url_base = 'https://maps.googleapis.com/maps/api/geocode/json?key='

    components = "components=locality:%s|country:US|administrative_area:%s|postal_code=%s" % (city, state, zip)

    address = address.replace(' ', '+')
    
    address_formatted = 'address=%s' % address

    url = url_base + api_key + '&' + components + '&' + address_formatted

    return url


def geocode(address, city, county, state, zip):
    url = generate_request(address, city, county, state, zip)
    response = requests.get(url)
    json_response = response.json()

    locations = json_response['results'][0]['geometry']['location']

    return (locations['lat'], locations['lng'])

# output = geocode(generate_request(address, city, county, state, zip))


district_list = []

with open('test.csv', 'r') as in_csv:
    csv_dict = csv.DictReader(in_csv)
    for row in csv_dict:
        locations = geocode(row['address'], row['city'],
                            row['county'], row['state'], row['zip'])
        print(locations)

        district_url = 'https://congress.api.sunlightfoundation.com/districts/locate?latitude=%s&longitude=%s' % locations

        district_request = requests.get(district_url)

        district = (district_request.json()['results'][0]['state'],
                    district_request.json()['results'][0]['district'])
        district_list.append(str(district[0] + ' ' + str(district[1])))


with open('test.csv', 'r') as in_rows:
    with open('output.csv', 'w') as out_file:
        reader = csv.reader(in_rows)
        writer = csv.writer(out_file, lineterminator='\n')
        for i, row in enumerate(reader):
            if i != 0:
                row.append(district_list[i - 1])
            writer.writerow(row)
