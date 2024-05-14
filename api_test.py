import requests

base_url = "https://api.mouser.com/api/v2/"
api_key = "2c18ba1d-7b17-4d2e-9e0f-34e05a5e674c"

    
def search_parts_by_keyword_and_manufacturer(manufacturer_name, keyword, records, page_number, search_options, lang, return_type):
    search_endpoint = "search/keywordandmanufacturer"
    url = base_url + search_endpoint + "?apiKey=" + api_key

    payload = {
        "SearchByKeywordMfrNameRequest": {
            "manufacturerName": manufacturer_name,
            "keyword": keyword,
            "records": records,
            "pageNumber": page_number,
            "searchOptions": search_options,
            "searchWithYourSignUpLanguage": lang
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": ""
    }
    headers["Accept"] = "application/" + return_type
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"Error": response.status_code}
    
def search_parts_by_part_number_and_manufacturer(manufacturer_name, mouser_part_number, part_search_options, return_type):
    search_endpoint = "search/partnumberandmanufacturer"
    url = base_url + search_endpoint + "?apiKey=" + api_key

    payload = {
        "SearchByPartMfrNameRequest": {
            "manufacturerName": manufacturer_name,
            "mouserPartNumber": mouser_part_number,
            "partSearchOptions": part_search_options
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": ""
    }
    headers["Accept"] = "application/" + return_type
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.content
        return data
    else:
        return {"Error": response.status_code}
    
def get_run_user_input():
    function_call = int(input("Enter 1 to search by keyword or 2 to search by part number: "))
    if function_call == 1:
        manufacturer_name = input("Enter the manufacturer name: ")
        keyword = input("Enter the keyword: ")
        records = int(input("Enter the records: "))
        page_number = int(input("Enter the page number: "))
        search_options = input("Enter the search options: ")
        lang = input("Enter the search language: ")
        return_type = input("Enter return data type (xml or json): ")
        return search_parts_by_keyword_and_manufacturer(manufacturer_name, keyword, records, page_number, search_options, lang, return_type)
    elif(function_call == 2):
        manufacturer_name = input("Enter the manufacturer name: ")
        mouser_part_number = input("Enter the Mouser part number: ")
        part_search_options = input("Enter the part search options: ")
        return_type = input("Enter return data type (xml or json): ")
        return search_parts_by_part_number_and_manufacturer(manufacturer_name, mouser_part_number, part_search_options, return_type)
    

def main():
    search_results = get_run_user_input()
    print(search_results)

if __name__ == "__main__":
    main()