import requests
from bs4 import BeautifulSoup
import re

# Some funding keywords I thought of
funding_keywords = ['grant', 'funding', 'allocation', 'investment', 'loan', 'aid', 'donation']

# URL - this is one of the article I used
url = 'https://www.uncdf.org/article/7949/pacific-islands-fintech-innovation-challenge-2022-wrap-up'

# Get article text
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text(separator=' ')

# Clean extra whitespace
text = re.sub(r'\s+', ' ', text)

# Tokenize text into words
words = text.split()

# Function to find numbers near a keyword I just arbitrarily chose 7 words before or after the keywords
def find_numbers_near_keyword(words, keyword, window=7):
    matches = []
    for i, word in enumerate(words):
        if keyword.lower() in word.lower(): #Makes everything lowercase to perfrom a case-insensitive comparison
            # Get words within window before and after
            start = max(0, i - window)
            end = min(len(words), i + window + 1) #Slicing is inclusive of the start index but exclusive of the end index
            nearby_words = words[start:end]
            # Look for numbers (can include $ and commas, e.g. $50,000)
            number_pattern = r'\$?\d{1,3}(?:,\d{3})*(?:\.\d+)?'
            found_numbers = re.findall(number_pattern, ' '.join(nearby_words))
            if found_numbers:
                matches.append({'keyword': keyword, 'context': ' '.join(nearby_words), 'numbers': found_numbers}) 
                # Returns the number and context for verification as well
    return matches

# Run the function for each keyword
results = []
for keyword in funding_keywords:
    results.extend(find_numbers_near_keyword(words, keyword, window=7))

# Print matches
for match in results:
    print(f"\nKeyword: {match['keyword']}\nContext: {match['context']}\nNumbers found: {match['numbers']}")
