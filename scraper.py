from dc_base_scrapers.arcgis_scraper import ArcGisScraper


districts_url = "https://services.arcgis.com/wDcUiJYKtMulHM03/arcgis/rest/services/Electoral_boundaries/FeatureServer/1/query?f=pjson&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=27700&resultOffset=0&resultRecordCount=4000&resultType=tile"
council_id = 'E07000077'


districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID_12')
districts_scraper.scrape()
