Bookstore Web Scraper & Data Pipeline

A python-based web scraping tool designed to automatically crawl a mock bookstore website, extract real-time inventory data, and format it into a clean, business-ready spreadsheet.

Features:
* Data Extraction: Automatically parses HTML to grab Book Title, Price, URL, and Stock Availability.
* Ethical Scraping: Implements a rate-limiting ('time.sleep()') to respect server hosting and mimic human-like browsing behaviour.
* Data Cleaning: Scrubs currency symbols and handles string parsing to prepare raw text for mathematical analysis.

Technologies used:

*Python 3

*BeautifulSoup4 (for HTML parsing)

*Requests (as HTTP client)

*CSV module(Data structuring)

Output:

The final script generates an interactive spreadsheet containing clean columns for business intelligence or pricing analysis. e.g. 'Book Title' | 'Price' | 'Link' | 'Status'.

What I learned:

Through this project, I mastered navigating nested HTML trees, handling file encoding mismatches(getting rid of rogue characters), managing file 'write' operations, and writing defensive, courteous scraping scripts.
