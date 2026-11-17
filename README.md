# RAG Web Browser: Google Scraper API for Python & Node.js (2026)

Web browser for AI agents and RAG pipelines: search Google, fetch the top result pages, and return clean Markdown or text ready for LLMs. Also accepts a single URL.

**[▶ Try the RAG Web Browser free on Scrapely](https://scrape.ly/store/querystone/rag-web-browser)** · [Compare Scrapely vs other scraping tools](https://scrape.ly/compare)

This repository shows how to scrape Google data with the [RAG Web Browser](https://scrape.ly/store/querystone/rag-web-browser) using the official
**Scrapely SDKs for JavaScript and Python**. You pass the input, Scrapely runs the google scraper in the cloud
(proxies, retries, browser and scaling included) and returns clean, structured data as JSON, CSV or Excel.
No scraper code to maintain and no blocked requests to debug.

## Why use this Google scraper

- **No-code or API:** run it from the [Scrapely Store](https://scrape.ly/store/querystone/rag-web-browser) or from your code with the SDK.
- **Structured google data:** ready-to-use fields instead of raw HTML.
- **Pay per result:** $5.18 per 1,000 serp page results, no monthly subscription required.
- **Maintained and monitored:** scrapers are tested around the clock and fixed fast when Google changes.
- **Integrations:** n8n, Make, Zapier, LangChain, LlamaIndex, MCP (Claude, Cursor) and webhooks.

## What Google data can you extract?

Web browser for AI agents and RAG pipelines: search Google, fetch the top result pages, and return clean Markdown or text ready for LLMs. Also accepts a single URL.

| Output field |
|---|
| `metadata.url` |
| `metadata.title` |
| `searchResult.resultType` |
| `markdown` |

## Quick start

1. [Sign up for Scrapely](https://scrape.ly) (free plan available) and copy your API token from
   **Settings → API & Integrations**.
2. Clone this repo and set your token:

```bash
export SCRAPELY_TOKEN=your_token
```

### Node.js (JavaScript SDK)

```bash
npm install
node example.js
```

```js
const { ScrapelyClient } = require('scrapely-client');
const client = new ScrapelyClient({ token: process.env.SCRAPELY_TOKEN });

const run = await client.actor('querystone/rag-web-browser').call({"query": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation", "maxResults": 5, "removeElementsCssSelector": "nav, footer, script, style, noscript, svg, img[src^='data:'],\n[role=\"alert\"],\n[role=\"banner\"],\n[role=\"dialog\"],\n[role=\"alertdialog\"],\n[role=\"region\"][aria-label*=\"skip\" i],\n[aria-modal=\"true\"]", "proxyConfiguration": {"useScrapelyProxy": true}, "htmlTransformer": "none"});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
```

### Python (Python SDK)

```bash
pip install -r requirements.txt
python example.py
```

```python
from scrapely_client import ScrapelyClient
client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

run = client.actor('querystone/rag-web-browser').call(run_input={ "query": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation", "maxResults": 5, "removeElementsCssSelector": "nav, footer, script, style, noscript, svg, img[src^='data:'],\n[role=\"alert\"],\n[role=\"banner\"],\n[role=\"dialog\"],\n[role=\"alertdialog\"],\n[role=\"region\"][aria-label*=\"skip\" i],\n[aria-modal=\"true\"]", "proxyConfiguration": { "useScrapelyProxy": True }, "htmlTransformer": "none" })
items = list(client.dataset(run.default_dataset_id).iterate_items())
```

### REST API / cURL

```bash
curl -X POST "https://api.scrape.ly/v2/acts/querystone~rag-web-browser/run-sync-get-dataset-items?token=$SCRAPELY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @input.json
```

## Example input

```json
{
  "query": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
  "maxResults": 5,
  "removeElementsCssSelector": "nav, footer, script, style, noscript, svg, img[src^='data:'],\n[role=\"alert\"],\n[role=\"banner\"],\n[role=\"dialog\"],\n[role=\"alertdialog\"],\n[role=\"region\"][aria-label*=\"skip\" i],\n[aria-modal=\"true\"]",
  "proxyConfiguration": {
    "useScrapelyProxy": true
  },
  "htmlTransformer": "none"
}
```

See every input option on the [RAG Web Browser page](https://scrape.ly/store/querystone/rag-web-browser).

## Pricing

**$5.18 per 1,000 serp page results.** Free plan available, no credit card needed to start. Check current pricing on the
[Store page](https://scrape.ly/store/querystone/rag-web-browser) and see how Scrapely compares with other tools on [scrape.ly/compare](https://scrape.ly/compare).

## FAQ

**How do I scrape Google with Python?** Install `scrapely-client-python`, set `SCRAPELY_TOKEN` and run
`example.py`. The scraper runs on Scrapely and you read the results from the dataset.

**How do I scrape Google with Node.js?** Install `scrapely-client`, set `SCRAPELY_TOKEN` and run `example.js`.

**Is there a google scraper API?** Yes. Call `POST https://api.scrape.ly/v2/acts/querystone~rag-web-browser/runs`
or use `run-sync-get-dataset-items` to get results in one request.

**Do I need proxies?** No. Proxies, retries and browsers are handled by Scrapely.

**Is scraping Google legal?** This scraper collects publicly available data. Check Google's terms and the
laws that apply to you, especially for personal data (GDPR, CCPA).

**Can I schedule it or get results by webhook?** Yes. Use Scrapely schedules and webhooks, or n8n, Make and Zapier.

## Related Google scrapers

- [Google Maps Scraper](https://github.com/alexrosuleks/google-maps-scraper): Scrape Google Maps places for any search term, location or Google Maps URL: names, addresses, ratings, review counts,…
- [Google Search Scraper](https://github.com/alexrosuleks/google-search-scraper): Scrape Google Search results by query and country in fast search mode: organic results, People Also Ask, and related…
- [Google Maps Reviews Scraper](https://github.com/alexrosuleks/google-maps-reviews-scraper): Scrape Google Maps reviews for any place: text, stars, dates, likes, owner replies, photos and place details. No login…
- [Google Trends Scraper](https://github.com/alexrosuleks/google-trends-scraper): Scrape Google Trends interest over time, interest by region, related queries and topics for any keyword, country and…
- [Google Images Scraper](https://github.com/alexrosuleks/google-images-scraper): Scrape Google Images: full-size image URLs, dimensions, thumbnails, source pages, site names and titles for any query.…
- [Google Jobs Scraper](https://github.com/alexrosuleks/google-jobs-scraper): Scrape Google for Jobs results by query and location: title, company, salary, job type, posted date and apply links. No…

## Looking for an alternative?

Scrapely is an alternative to Apify, Bright Data, ScraperAPI, Firecrawl, Octoparse, PhantomBuster, SerpApi,
Zyte and others. See the side-by-side pricing on [scrape.ly/compare](https://scrape.ly/compare).

---

**Keywords:** rag web browser, google scraper, google scraper api, google scraper python, google scraper node.js,
scrape google, google data extraction, google crawler, google api, export google data to csv, rag-web-browser

License: MIT. Example code only; the scraper runs on [Scrapely](https://scrape.ly/store/querystone/rag-web-browser).
