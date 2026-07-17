// Script.js
const fs = require('fs');
const https = require('https');

const apiKey = process.env.CONGRESS_API_KEY;
const baseUrl = 'https://api.congress.gov/v3';

async function fetchLegislation() {
  try {
    // Example: Fetch bills related to your search term
    const url = `${baseUrl}/bill?limit=250&api_key=${apiKey}`;
    
    // Make your API request and process the data
    const data = await makeRequest(url);
    
    // Format and write to CSV
    const csvData = convertToCSV(data);
    fs.writeFileSync('lake_james_federal_legislation.csv', csvData);
    
    console.log('Successfully updated lake_james_federal_legislation.csv');
  } catch (error) {
    console.error('Error fetching legislation:', error);
    process.exit(1);
  }
}

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

function convertToCSV(data) {
  // Implement your CSV formatting logic here
  return '';
}

fetchLegislation();
