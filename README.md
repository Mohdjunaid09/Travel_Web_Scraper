# 📚 Travel Book Scraper

## Project Overview

Travel Book Scraper is a simple Python web scraping project that extracts book information from the **Travel** category of the **Books to Scrape** website and stores the data in a CSV file.

This project demonstrates the basics of web scraping using Python, HTML parsing, and data storage in CSV format.

---

## Features

- Scrapes all books from the Travel category.
- Extracts:
  - Book Title
  - Price
  - Availability
  - Rating
  - Product URL
- Stores the scraped data in a CSV file.
- Easy to understand and beginner-friendly.

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas

---

## Project Structure

```
Travel_Web_Scraper/
│
├── travel_scraper.py
├── travel_books.csv
└── README.md
```

---

## Installation

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 pandas
```

---

## How to Run

Open the project folder in VS Code and run:

```bash
python travel_scraper.py
```

or

```bash
py travel_scraper.py
```

---

## Output

The program creates a file named:

```
travel_books.csv
```

The CSV file contains:

- Title
- Price
- Availability
- Rating
- Product URL

---

## Website Used

**Books to Scrape**

https://books.toscrape.com/

Category:

Travel

---

## Sample Output

| Title | Price | Availability | Rating |
|-------|-------|--------------|--------|
| It's Only the Himalayas | £45.17 | In Stock | Two |
| Full Moon over Noah's Ark | £49.43 | In Stock | Four |

---

## Future Enhancements

- Scrape multiple categories.
- Export data to Excel.
- Store data in a database.
- Add command-line options for category selection.
- Visualize scraped data using charts.

---

## Author

**Mohammed Abdul Junaid**

B.Tech CSE

ACE Engineering College
