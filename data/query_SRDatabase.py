import requests
import json
# API endpoint for SR-legacy database
url = " https://api.nal.usda.gov/fdc/v1/food/"

# API key for accessing the database
api_key = "DEMO_KEY"

def fetch_food_details(fdcic):
    # Send the API request
    response1 = requests.get(url + str(fdcic) +"?format=full&nutrients=203,204,205,255,301,303,304,305,306,307,309,312,315,317,320,401,404,405,406,410,415,417,418,601&api_key=" + api_key)
    response2 = requests.get(url + str(fdcic) +"?format=full&nutrients=606,645,646&api_key=" + api_key)
    # Check if the request was successful
    if response1.status_code == 200:
        # Parse the JSON response
        rawAmount = ""
        nameSequence = ""
        data1 = response1.json()
        data2 = response2.json()
        nutrients1 = data1['foodNutrients']
        nutrients2 = data2['foodNutrients']
        for nutrient in nutrients1:
            rawAmount = rawAmount + str(nutrient['amount']) + " "
            nameSequence = nameSequence + nutrient['nutrient']['name'] + " "
        for nutrient in nutrients2:
            rawAmount = rawAmount + str(nutrient['amount']) + " "
            nameSequence = nameSequence + nutrient['nutrient']['name'] + " "
        out = {"fdcId":fdcic, "nameSequence":nameSequence, "rawAmount":rawAmount}
        return out
    else:
        # If the request was not successful, raise an exception
        response1.raise_for_status()
# write to file
# print(json.dumps(out, indent=4, sort_keys=True), file=open("food_details.txt", "a"))

with open('food_details_out.txt', 'w', encoding="utf-8") as f:
    out = fetch_food_details("169961")
    f.writelines(out["fdcId"] + "\n" + out["nameSequence"] + "\n" + out["rawAmount"] + "\n")
