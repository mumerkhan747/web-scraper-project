# import csv
# import json
# import requests
# from bs4 import BeautifulSoup


# # Base URL (Aap yahan apni target website ka URL dein ge jahan pagination ho)
# # Misal ke tor par hum ek sample e-commerce site ya quotes site use kar sakte hain
# BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# all_records = []

# print("Scraping the data is being started...")


# # Pagination loop (Misal ke tor par pehle 5 pages scrape karte hain taake 100+ records mil saken)
# for page in range(1, 6):
#     url = BASE_URL.format(page)
#     print(f"Scraping the page: {page} --> {url}")

#     headers = {
#         "User-Agent" : (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
#             " like Gecko) Chrome/120.0.0.0 Safari/537.36"
#           )
#     }

#     try:
#         response = requests.get(url, headers=headers)

#         if response.status_code != 200:
#             print(f"Error on the page {page}. \nStatus code: {response.status_code}")
#             break


#         soup = BeautifulSoup(response.text, "html.parser")

#         # Yahan hum items ko dhoondtay hain (Target website ke HTML structure ke mutabiq)
#         # Yeh example 'Books to Scrape' website ke liye hai
#         items = soup.find_all("aritcle", class_="product_pod")

#         for item in items:
            
#             title = item.find("h3").find("a")["title"]  #... Title nikalna
            
#             price = item.find("p", class_="price_color").text   #... Price nikalna
            
#             rating_tag = item.find("p", class_="star-rating")  #... rating nikalna
#             rating = rating_tag["class"][1] if rating_tag else "Unknown"

#             all_records.append({
#                "title": title,
#                "price": price,
#                "metadata":f"Rating: {rating}",
#             })
            
#             # Record ko dictionary ki shakal mein store karna
#             # record = {"title": title, "price": price, "metadata": f"Rating: {rating}"}

#             # all_records.append(record)

#     except Exception as e:
#         print(f"An error occured: {e}")


# print(f"Records found: {len(all_records)}")

# # Data ko JSON file mein save karna
# with open("extracted_data.json", "w", encoding="utf-8") as f:
#     json.dump(all_records, f, indent=4, ensure_ascii=False)


# # Data ko CSV file mein save karna
# with open("extracted_data.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames = ["title", "price", "metadata"] )
#     writer.writeheader()
#     writer.writerows(all_records)



# print("Data successfully saved in CSV and JSON files!")




import csv
import json
import requests
from bs4 import BeautifulSoup

all_records = []

print("Scraping shuru ho rahi hai...")

for page in range(1, 6):
  # Yahan hum check kar rahe hain ke agar page 1 hai toh index.html use ho
  if page == 1:
    url = "http://books.toscrape.com/index.html"
  else:
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

  print(f"Scraping page: {page} -> {url}")

  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      )
  }

  try:
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
      print(f"Page {page} error: {response.status_code}")
      continue

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("article", class_="product_pod")

    for item in items:
      title = item.find("h3").find("a")["title"]
      price = item.find("p", class_="price_color").text

      rating_tag = item.find("p", class_="star-rating")
      rating = rating_tag["class"][1] if rating_tag else "Unknown"

      all_records.append({
          "title": title,
          "price": price,
          "metadata": f"Rating: {rating}",
      })

  except Exception as e:
    print(f"Error on page {page}: {e}")

print(f"\nTotal records found: {len(all_records)}")

# Export to JSON
with open("extracted_data.json", "w", encoding="utf-8") as f:
  json.dump(all_records, f, indent=4, ensure_ascii=False)

# Export to CSV
with open("extracted_data.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.DictWriter(f, fieldnames=["title", "price", "metadata"])
  writer.writeheader()
  writer.writerows(all_records)

print("Data successfully saved in CSV and JSON files!")