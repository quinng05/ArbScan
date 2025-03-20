from scraper import scrape_fliff_odds

fliff_odds = scrape_fliff_odds()
for line in fliff_odds:
    print(line)