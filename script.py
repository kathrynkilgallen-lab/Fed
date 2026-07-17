import os
import requests
import csv
import json
from datetime import datetime

API_KEY = os.environ.get('CONGRESS_API_KEY')
BASE_URL = 'https://api.congress.gov/v3'

def fetch_legislation():
    try:
        # Example: Fetch bills related to your search term
        url = f'{BASE_URL}/bill?limit=250&api_key={API_KEY}'
        
        # Make your API request and process the data
        data = make_request(url)
        
        # Format and write to CSV
        convert_to_csv(data)
        
        print('Successfully updated lake_james_federal_legislation.csv')
    except Exception as error:
        print(f'Error fetching legislation: {error}')
        exit(1)

def make_request(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

def convert_to_csv(data):
    if not data.get('results') or len(data['results']) == 0:
        return  # Return if no results
    
    bills = data['results']
    
    # Define CSV headers
    headers = ['Bill Number', 'Title', 'Introduced Date', 'Latest Action', 'Latest Action Date']
    
    # Write to CSV file
    with open('lake_james_federal_legislation.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        # Write data rows
        for bill in bills:
            writer.writerow([
                bill.get('number', ''),
                bill.get('title', ''),
                bill.get('introducedDate', ''),
                bill.get('latestAction', {}).get('text', ''),
                bill.get('latestAction', {}).get('actionDate', '')
            ])

if __name__ == '__main__':
    fetch_legislation()
