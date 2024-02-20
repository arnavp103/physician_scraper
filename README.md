# Scrapers for registries of physicians in Canada

The scrapers in this repository are designed to extract data from the websites of the various provincial and territorial colleges of physicians and surgeons in Canada. The data can then be extracted from json through duckdb or other means.

## Usage

Look at the scraper in the `scrapers` directory for the province or territory you are interested in. Make sure you have `scrapy` installed and activated in your environment, and then run the scraper with the following command:

```bash
scrapy crawl <scraper_name> -O <output_file>.json
```

The `-O` flag specifies the output file. The scraper will create a json file with the data it extracts. This overwrites the previous file. Use `-o` to append to the file instead.