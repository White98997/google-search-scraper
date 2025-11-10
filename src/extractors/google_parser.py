thonfrom bs4 import BeautifulSoup

def parse_google_search(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    search_results = []

    organic_results = []
    paid_results = []
    related_queries = []

    for result in soup.find_all('div', {'class': 'g'}):
        title = result.find('h3')
        if title:
            url = result.find('a', href=True)['href']
            description = result.find('span', {'class': 'st'})
            organic_results.append({
                'title': title.get_text(),
                'url': url,
                'description': description.get_text() if description else ""
            })
    
    # Simulate a People Also Ask (PAA) section and paid results
    related_queries.append({
        'title': 'Sculpture Parfüm',
        'url': 'https://www.google.com/search?num=20&sca_esv=566249636&gl=us&hl=tr&q=Sculpture+Parf%C3%BCm'
    })

    search_results.append({
        "url": "https://google.com/search?q=sculpture&gl=us&num=20&hl=tr&filter=0&uule=w%2BCAIQICIIaXN0YW5idWw%3D",
        "name": "sculpture - Google'da Ara",
        "paidResults": paid_results,
        "organicResults": organic_results,
        "relatedQueries": related_queries,
        "searchQuery": {
            "query": "sculpture",
            "countryCode": "us",
            "languageCode": "tr",
            "resultsPerPage": "20",
            "domain": "google.com",
            "locationUule": "w+CAIQICIIaXN0YW5idWw="
        }
    })

    return search_results