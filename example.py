"""RAG Web Browser with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "query": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation",
        "maxResults": 5,
        "removeElementsCssSelector": "nav, footer, script, style, noscript, svg, img[src^='data:'],\n[role=\"alert\"],\n[role=\"banner\"],\n[role=\"dialog\"],\n[role=\"alertdialog\"],\n[role=\"region\"][aria-label*=\"skip\" i],\n[aria-modal=\"true\"]",
        "proxyConfiguration": {
            "useScrapelyProxy": True
        },
        "htmlTransformer": "none"
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('querystone/rag-web-browser').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
