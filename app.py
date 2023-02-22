from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def extract_data():
    
#     visit this link 'https://randomuser.me/api' to get the api. example api, {"results":[{"gender":"male","name":{"title":"Monsieur","first":"Valentin","last":"Francois"},"location":{"street":{"number":6331,"name":"Rue de L'Abbé-Migne"},"city":"Stein am Rhein","state":"Solothurn","country":"Switzerland","postcode":3778,"coordinates":{"latitude":"-60.6328","longitude":"-3.5683"},"timezone":{"offset":"-5:00","description":"Eastern Time (US & Canada), Bogota, Lima"}},"email":"valentin.francois@example.com","login":{"uuid":"f54a9da4-cc02-4fd8-ad25-34e6459a9163","username":"blackfrog292","password":"spongebo","salt":"XYbj93F3","md5":"d0f147edaf386ec86d51398cbd7bb6b3","sha1":"aabac5881c507052182649d1a25e6c61ca9a682f","sha256":"a1f6a08b0036b915307e670e76e0a35e558edea90b61c6632f1ee12ffe715bbb"},"dob":{"date":"1962-02-24T12:07:22.207Z","age":60},"registered":{"date":"2020-02-09T08:34:22.233Z","age":3},"phone":"076 666 04 29","cell":"075 015 79 50","id":{"name":"AVS","value":"756.6675.8882.37"},"picture":{"large":"https://randomuser.me/api/portraits/men/42.jpg","medium":"https://randomuser.me/api/portraits/med/men/42.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/42.jpg"},"nat":"CH"}],"info":{"seed":"568efa3fdb7607ca","results":1,"page":1,"version":"1.4"}}
    
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

# address route which is used to get address of the user.
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
