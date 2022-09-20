#API Assignment 1
#Q6 Find any external API besides that given in the assignment. Retrieve the data from that api with the GET operation,
#   clean the data and load it in your local as "example.json" file. Finally, perform all crud operations in that data.

#external api:  https://api.publicapis.org/entries

from re import search
from flask import Flask, jsonify, request
import urllib.request, json

app = Flask(__name__)


# Retrieve data of public api entries from https://api.publicapis.org/entries
# and load it into the system as example.json file

@app.route('/get-entries', methods=['GET'])
def get_entries():
    results = []
    url = f"https://api.publicapis.org/entries"
    response = urllib.request.urlopen(url)
    data = json.load(response)
    results = data["entries"]

    # loading the results data into example.json file
    with open('example.json', mode='w') as local_file:
        local_file.write(json.dumps(results, indent=4))

    return jsonify({
        'status': 200,
        'message': 'Public API entries successfully loaded',
        'data': {
            'number_of_results': len(results),
            'results': results,
        },
    })


#Perform CRUD operations in the data

#GET operation
# List the API name, Description, and Link of all entries based on provided category

@app.route('/apis/<Category>', methods=['GET'])
def get_apis(Category):
    try:
        with open('example.json', 'r') as file:
            data = json.load(file)
        api_data = []
        for entry in data:
            if entry['Category'] == Category:
                api_data.append(
                    {"Category": entry["Category"], "API": entry['API'], "Description": entry["Description"],
                     "Link": entry["Link"]})
        if not api_data:
            return jsonify({
                'status': 404,
                'Category': Category,
                'message': 'No api of the Category found',
            })
        return jsonify({"example": api_data})


    except Exception as e:
        return jsonify({'message': e})


#POST operation
#Insert a new entry

@app.route('/apis/insert', methods = ['POST'])
def insert_entry():
    body = request.get_json()
    try:
        with open('example.json', mode='r') as file:
            entries = json.load(file)
            for entry in entries:
                if entry['API'] == body['API']:
                    raise Exception
            entries.append(body)

        with open('example.json', mode='w') as w_file:
            w_file.write(json.dumps(entries, indent=4))
        return jsonify({
            'status': 200,
            'message': 'New entry successfully inserted',
            'data': body,
        })

    except Exception as e:
        return jsonify({
            'status': 400,
            'message': 'Entry not inserted! API already exists.',
            'data': {},
        })
#post is done in postman


#PUT operation
#Update the HTTPS status to False
#Update the category names to uppercase
@app.route('/update-https/<API>', methods=['PUT'])
def update_https(API):
    try:
        with open('example.json', mode='r') as file:
            api_data = json.load(file)
            api_entry = dict()
            for entry in api_data:
                if entry['API'] == API:
                    entry['HTTPS'] = False
                    api_entry = entry
                    break

            file.close()
            if len(api_entry) == 0:
                raise Exception

            else:
                with open('example.json', mode='w') as w_file:
                    w_file.write(json.dumps(api_data, indent=4))

                return jsonify({
                    'status':200,
                    'message': 'HTTPS status of the given API was successfully updated.',
                    'data': api_entry
                })

    except Exception:
        return jsonify({
            'error': 404,
            'message': 'API not found',
            'data': {},
        })



#DELETE operation
# Delete all entries of the given api (eg: Chainlink, Axolotl)
@app.route('/delete/<API>', methods=['DELETE'])
def delete_api(API):
    try:
        with open('example.json', mode='r') as file:
            api_data = json.load(file)
            new_entry = []
            api_entry = dict()
            api_found = False
            for entry in api_data:
                if entry['API'] == API:
                    api_found = True
                    api_entry = entry
                    continue
                new_entry.append(entry)
            file.close()

            if not api_found:
                raise Exception
            else:
                with open('example.json', mode='w') as w_file:
                    w_file.write(json.dumps(new_entry, indent=4))

                return jsonify({
                    'status': 200,
                    'message': 'Data of API {} has been successfully deleted'.format(API),
                    'data': api_entry,
                })

    except Exception:
        return jsonify({
            'error': 404,
            'message': 'The API doesn\'t exist',
        })


if __name__ == "__main__":
    app.run(debug=True)