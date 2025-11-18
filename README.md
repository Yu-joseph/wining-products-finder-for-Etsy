# Etsy Winning Products Finder

A Python-based web scraping tool to find potentially winning products on Etsy by analyzing product listings and identifying stores with high rankings but relatively low feedback counts.

## Strategy

This tool helps you discover product opportunities on Etsy by finding:

- **High-ranking products** with less competition
- **Stores with low feedback counts** that rank well (indicating new/trending products)
- Products that are currently performing well in search results

The key insight: If a product/store ranks high on Etsy search results but has relatively few reviews, it may indicate:
1. A new trending product with growing demand
2. Less saturated market with opportunity for new sellers
3. Products that are converting well despite being from newer stores

## How It Works

1. **Search**: Enters your keyword into Etsy's search bar
2. **Scrape**: Collects data from search result listings including:
   - Product title
   - Product link
   - Store name
   - Store link
   - Feedback count (number of reviews)
3. **Analyze**: Stores with fewer feedbacks appearing high in search results are potential opportunities
4. **Export**: Saves all data to a CSV file for further analysis

## Prerequisites

- Python 3.x
- Firefox browser installed
- GeckoDriver for Firefox (Selenium)

## Installation

1. Clone or download this repository

2. Install required packages:
```bash
pip install selenium pandas
```

3. Install GeckoDriver:
   - Download from: https://github.com/mozilla/geckodriver/releases
   - Add to your system PATH or place in project directory

## Usage

1. Run the script:
```bash
python script.py
```

2. Enter your search keyword when prompted:
```
Enter a keyword to search: custom mugs
```

3. The script will:
   - Open Firefox browser
   - Search Etsy for your keyword
   - Scrape product data
   - Save results to `etsy_results.csv`
   - Display the first few results in terminal

4. Analyze the CSV file to find:
   - Products ranking high with low feedback counts
   - Potential product opportunities
   - Store patterns and trends

## Output

The script generates `etsy_results.csv` with the following columns:

- **Title**: Product name
- **Product Link**: Direct link to the product listing
- **Store Name**: Seller's store name
- **Store Link**: Link to the seller's store
- **Feedback Count**: Number of reviews/feedback

## Tips for Finding Winning Products

1. Look for products with **high search ranking** but **< 100 feedbacks**
2. Check if multiple stores sell similar products (validates demand)
3. Analyze pricing across similar listings
4. Consider stores with 10-50 feedbacks ranking on first page (sweet spot)
5. Look for seasonal trends and emerging niches

## Limitations

- Only scrapes the first page of results
- Depends on Etsy's HTML structure (may break if Etsy updates their site)
- Rate limiting: Use responsibly to avoid IP blocks

## Disclaimer

This tool is for educational and research purposes only. Please respect Etsy's Terms of Service and use web scraping responsibly. Always verify opportunities manually before making business decisions.

## License

Feel free to modify and use for your needs.
- add more pages
- add filter for shops
- add sells etc ..