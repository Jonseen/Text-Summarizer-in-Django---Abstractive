import requests
import json
from .searcher import Search
class UrlLoader:

    def getResults(query, pageOffset=1, timeout=10):
        ''' Given a query searches a Google Programmable search engine for results.
        Query Parameters:
            query:          This is the query to search.
            pageOffset:     Use this to get other page results, for example 1 means result page 1, while 10 is result page 10. Max of 50
        '''
        MAX_PAGE = 50
        MIN_PAGE = 1
        if pageOffset < MIN_PAGE: pageOffset = MIN_PAGE
        elif pageOffset > MAX_PAGE: pageOffset = MAX_PAGE

        searcher = Search()
        NUM_RESULT_PER_PAGE = 1
        FIRST_PAGE_OFFSET = 1
        start = NUM_RESULT_PER_PAGE * (pageOffset - 1) + FIRST_PAGE_OFFSET
        url = "https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyD_C8sT1q4fJnRaC0lvUvJWFt-7pNq3ga4&cx=943ee1f0248af9858&q={}&start={}&alt=json".format(query, start)

        response = requests.get(url, timeout)

        result = {'maxPage': MAX_PAGE}
        try:
            if response.status_code == 200:
                search = json.loads(response.content)
                result['query'] = search['queries']['request'][0]['searchTerms']
                result['totalResults'] = search['searchInformation']['totalResults']

                items = search['items']
                result['items'] = [{'title': x['title'], 'link': x['link'], 'summary': searcher.result(x['link'])} for x in items]
                return result
            else: raise Exception('Request failed, Invalid server response.')
        except Exception as error:
            print('An error occurred! failed to complete request:', error)

  
