# Templates for Extracting UN Funding Data
This repository contains two Python-based tools designed for extracting funding-related information from international development project web pages and articles. These tools use a combination of web scraping, text mining, and regular expressions to automate data extraction workflows often used in economic research contexts.

## Programs

### scraperTemplates
This is the template I use for doing simple web scraping in general, tweaked to fit the UNCDF Inclusive Innovation Challenges page, although I have used this same template to scrape other UN sites for fundraiser names. 

**How it works:**  
- Sends an HTTP request to the target UNCDF webpage.
- Parses the page's HTML content using BeautifulSoup.
- Finds all `<div>` elements with the class `description`.
- Extracts the text inside each `<h2>` tag within those `div` elements.
- Outputs the list of challenge titles to a CSV file.

### fundingAmount
This program reads an article and finds the funding-related keywords I gave it (e.g. 'grant', 'funding', 'aid') in that article, then scans the surrounding words to find numbers and return them, intended to give the user a funding amount listed on a page simply by inputting a url into the program.

**How it works:**  
- Scrapes the text of an article page using BeautifulSoup.
- Tokenizes the article text into individual words.
- For each keyword occurrence, scans a configurable number of words before and after (default: 7) to find nearby numbers.
- Uses a regular expression to detect numbers with or without dollar signs, commas, and decimal points.
- Outputs the keyword context and matched numbers for review.

## Lessons Learned 

While building these tools, I learned a lot about the nuances of scraping real-world websites — especially development organization pages that don’t always follow clean or predictable HTML structures. I also got better at writing regular expressions that can handle messy number formats with commas, dollar signs, and decimals, which come up often in financial reporting.

One thing I realized is that proximity-based text mining (like scanning 7 words around a keyword) is a quick and useful approach for extracting contextually relevant data, but it isn’t foolproof. Numbers can show up in unexpected places, and deciding which one actually matters sometimes needs human review. For example, in the sample article I use in the fundingAmount program, there are actually two funding amounts that show up - 50,000 and 100,000, which is why I decided to keep the context around the numbers to double check that the program pulled the correct value. 

Lastly, working on these made me appreciate how even small automation scripts can meaningfully speed up econ/development research workflows — especially when scraping funding data from scattered press releases or project pages.
