from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def extract_data():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    # Extracting the required data from the API response
    name = data['results'][0]['name']['first'] + ' ' + data['results'][0]['name']['last']
    email = data['results'][0]['email']
    phone = data['results'][0]['phone']
    userName = data["results"][0]["login"]["username"]
    passWord = data["results"][0]["login"]["password"]
    # Creating a dictionary to return as JSON response
    result = [{
        'name': name,
        'email': email,
        'phone': phone
        },
    {
        'userName': userName,
        'passWord': passWord
    }]
    return jsonify(result)

@app.route('/address/')
def address():
    response = requests.get("https://randomuser.me/api/")
    add_data = response.json()

    HouseNO = add_data["results"][0]["location"]["street"]["number"] 
    name = add_data["results"][0]["location"]["street"]["name"]
    city = add_data["results"][0]["location"]["city"]
    state = add_data["results"][0]["location"]["state"]
    country = add_data["results"][0]["location"]["country"]
    postcode = add_data["results"][0]["location"]["postcode"]

    result = [{
        'HouseNO': HouseNO,
        'city': city,
        'state': state,
        'country': country,
        'postcode': postcode
        }]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
