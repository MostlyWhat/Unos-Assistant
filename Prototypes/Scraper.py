# Scrapes the first 2 sentences from the first link found on google based on the input

import json
import requests
from bs4 import BeautifulSoup

class Scraper:
    """
    Scraper class
    """
    def __init__(self):
        self.contexts = ["scrape", "search", "google", "brave"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        for words in self.contexts:
            question = query.replace(f"{words} ", "")

        return self.request_result(question)

    @staticmethod
    def request_result(query):
        """
        It takes a query, searches it on Brave, and returns the first result
        
        :param query: The query to search for
        :return: A string
        """
        question = query.replace(" ", "%20")

        headers = {
            'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }

        params = {
            'q': question,
            'source': 'web'
        }
        
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
                # Cut the snippet to 2 sentence
                snippet = snippet.split('.')[0] + '.'
                
                data.append({
                    'snippet': snippet,
                })
                
        returned = json.dumps(data)
        processing = json.loads(returned)
        first_result = processing[1]['snippet']
        
        if first_result is not None:
            return first_result

        else:
            return None