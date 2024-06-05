import requests
import math
import json 

# Define your custom headers here
headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # Add more headers as needed
}

# Function to fetch data from the API
def fetch_data_from_tiki(product_id, limit=20):
    
    base_url = f"https://tiki.vn/api/v2/reviews?page=1&limit={limit}&product_id={product_id}"
    

    # Fetch the first page
    response = requests.get(base_url, headers=headers)
    
    # print(f"https://tiki.vn/api/v2/reviews?page=1&limit={limit}&product_id={product_id}",response.json())

    # Convert json into dictionary 
    response_dict = response.json() 
    total = response_dict['paging']['total']
    per_page = response_dict['paging']['per_page']

    all_page = math.floor(total / per_page)
    if(total % per_page):
        all_page = all_page + 1

    print(total, per_page, all_page)

    all_data = response_dict['data']

    for x in range(2, all_page+1):
        # print(x) 
        base_url = f"https://tiki.vn/api/v2/reviews?page={x}&limit={limit}&product_id={product_id}"
        # Fetch the first page
        response = requests.get(base_url, headers=headers)

        response_data_dict = response.json()

        # print(*response_data_dict['data'])
        dataJson = response_data_dict['data']
        all_data = [*all_data, *dataJson]
        # print(all_data)

    list_data_format = []

    for x in all_data:
        if( len(x['content']) > 0 
        # and len(x['content']) < 62
        ):
            print(len(x['content']))
            data_format = {
                "name":x['created_by']['name'],
                "content":x['content'],
                "purchased":x['created_by']['purchased'],
                "predict": '',

            }
            list_data_format.append(data_format)

    # print(len(all_data))
    # print(list_data_format)

    # Pretty Printing JSON string back 
    # print(json.dumps(all_data, indent=4, sort_keys=True))
    

    return list_data_format

# Fetch and print the data
# print(all_data)