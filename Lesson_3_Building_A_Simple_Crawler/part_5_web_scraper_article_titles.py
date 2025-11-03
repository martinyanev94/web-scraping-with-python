import csv

# Data to save
data = []

# Assuming we have crawled and collected titles already
base_url = 'https://example.com/article/'

for i in range(1, 6):
    url = f"{base_url}{i}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for title in soup.find_all('h1'):
            data.append([f"Article {i}", title.get_text(strip=True)])

# Writing to a CSV file
with open('article_titles.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Article Number', 'Title'])  # Writing header
    writer.writerows(data)  # Writing data
