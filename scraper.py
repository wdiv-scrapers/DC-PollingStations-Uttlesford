from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "http://www.uttlesford.gov.uk/CHttpHandler.ashx?id=6593&p=0"
districts_url = "http://www.uttlesford.gov.uk/CHttpHandler.ashx?id=6594&p=0"
council_id = 'E07000077'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
