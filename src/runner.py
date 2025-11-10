thonimport json
import requests
from extractors.google_parser import parse_google_search
from outputs.exporters import export_data

def main():
    query = "sculpture"
    country_code = "us"
    language_code = "tr"
    location_uule = "w+CAIQICIIaXN0YW5idWw="
    max_results = 20

    url = f"https://www.google.com/search?q={query}&gl={country_code}&num={max_results}&hl={language_code}&uule={location_uule}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve data (Status Code: {response.status_code})")
        return

    search_results = parse_google_search(response.text)
    export_data(search_results)

if __name__ == "__main__":
    main()