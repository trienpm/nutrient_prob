Rough code for querying the SRDatabase.

"""
# FILENAME "FoodPairs.xlsx" 
Detail: Excel table containing food pairs.
# FILENAME "rawListWet"
Function: Contains list of FDC_IDs for querying, the index of each item is matched accordingly with "cookedListWet"
# FILENAME "cookedListWet"
Detail: Contains list of FDC_IDs for querying, the index of each item is matched accordingly with "rawListWet"
# FILENAME "rawListDry"
Detail: Contains list of FDC_IDs for querying, the index of each item is matched accordingly with "cookedListDry"
# FILENAME "cookedListDry"
Detail: Contains list of FDC_IDs for querying, the index of each item is matched accordingly with "rawListDry"
"""
# FILENAME "food_details.txt"
Detail: an example respone for a call.
# FILENAME "query_SRDatabase.py"
Detail: Contains a function for querying USDA's SR-Legacy database. Accepts a single string of FDC_ID as argument. Currently returns a dictionary that holds 3 entries:
    - fdcid: the food's fdcid
    - nameSequence: the name sequence of the desired 27 nutritions
    - rawData: the amount of each nutrition, in float data type
*you can also extract a number of other datas. In which case please look into "food_details.txt" and change the code as you need.
Mechanism: Utilizing the FDC's API, due to the restriction of 25 nutrition data per call in order to achieve what we need, 2 calls are required. The current DEMO_API key is limited to 50 calls/hour. This can be mitigated by requesting an API key at "https://fdc.nal.usda.gov/api-key-signup.html", which will supposedly email you your key. However, they never seem to send me my key. Please look into this.
# FILENAME "food_details_out.txt"
Detail: example output of the python script



