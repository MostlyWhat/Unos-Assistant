import json

import requests
from bs4 import BeautifulSoup

query = str(input("Query: "))

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    'q': query,
    'source': 'desktop'
}

# Collect all the results from the search engine
def get_organic_results():
    html = requests.get('https://search.brave.com/search', headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    data = []

    for result, sitelinks in zip(soup.select('.snippet.fdb'), soup.select('.deep-results-buttons .deep-link')):
        try:
            # removes "X time ago" -> split by \n -> removes all whitespaces to the LEFT of the string
            snippet = result.select_one('.snippet-content .snippet-description').text.strip().split('\n')[1].lstrip()
        except:
            snippet = None

        if snippet is not None:
            # Cut the snippet to 1 sentence
            snippet = snippet.split('.')[0] + '.'
            
            data.append({
                'snippet': snippet,
            })
      
    return_data = json.dumps(data, indent=2)  
    
    # # load return_data into a json object
    # return_data = json.loads(return_data)
    
    # # collect the first snippet from return_data
    # first_snippet = return_data[0]['snippet']
    
    # print(first_snippet)
    print(return_data)

get_organic_results()
