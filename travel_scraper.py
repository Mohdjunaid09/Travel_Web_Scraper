import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").get_text(strip=True)
    rating = book.find("p", class_="star-rating")["class"][1]
    product_url = urljoin(url, book.h3.a["href"])

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating,
        "Product URL": product_url
    })

df = pd.DataFrame(books)
df.to_csv("travel_books.csv", index=False, encoding="utf-8-sig")

print("CSV file created successfully!")
print(df)