import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL - This was one of the web pages I checked 
url = 'https://www.uncdf.org/inclusiveinnovation/challenges'

# Send HTTP request
response = requests.get(url)

# Extract all of the html on the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with the correct class 
descriptions = soup.find_all('div', class_='description')

# Here the challenges are stored within the h2 block within each div of class "description"
challenges = []
for desc in descriptions:
    h2_tag = desc.find('h2')
    if h2_tag:
        challenges.append(h2_tag.text.strip())

# Convert to DataFrame
df = pd.DataFrame(challenges, columns=['Challenge Title'])

# Save to CSV
df.to_csv('UNCDF_challenges.csv', index=False)

# Print preview
print(df.head())
