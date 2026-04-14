from bs4 import BeautifulSoup
import requests
import datetime
import csv

url = "https://www.bbc.com/news"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

headlines = soup.find_all("h2")

clean_headlines = []

for h in headlines:
    text = h.text.strip()
    if text and len(text) > 20:
        clean_headlines.append(text)

# Remove duplicates
clean_headlines = list(set(clean_headlines))

# Safe input
try:
    n = int(input("How many headlines you want? "))
except:
    print("Invalid input! Using default = 5")
    n = 5

clean_headlines = clean_headlines[:n]

# Add timestamp
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\nTop Headlines:\n")
for i, h in enumerate(clean_headlines, 1):
    print(f"{i}. {h}")

# Ask format
choice = input("Save as (1 = txt, 2 = csv): ")

if choice == "1":
    with open("headlines.txt", "w") as f:
        for h in clean_headlines:
            f.write(f"{time_now} | {h}\n")

elif choice == "2":
    with open("headlines.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Headline"])
        for h in clean_headlines:
            writer.writerow([time_now, h])

else:
    print("Invalid choice! Not saved.")

print("\nSaved successfully!")
