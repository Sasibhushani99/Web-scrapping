import requests
from bs4 import BeautifulSoup
import csv
url="https://www.bikewale.com/royalenfield-bikes/"

# Function to scrape quotes from the website
def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = []

        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

            quotes.append({
                'Text': text,
                'Author': author,
                'Tags': ', '.join(tags)
            })

        return quotes
    else:
        print(f"Failed to fetch the web page (HTTP status code {response.status_code})")
        return []

# Function to save scraped data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['Text', 'Author', 'Tags']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for quote in data:
            writer.writerow(quote)

if __name__ == '__main__':
    url = 'http://quotes.toscrape.com'
    quotes = scrape_quotes(url)

    if quotes:
        csv_filename = 'scraped_quotes.csv'
        save_to_csv(quotes, csv_filename)
        print(f'Data has been scraped and saved to {csv_filename}')
    else:
        print('No data to save.')
