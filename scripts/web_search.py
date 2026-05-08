#!/usr/bin/env python3
"""
Product Tower Kit - Web Scraping Integration

Unified web scraping across multiple providers:
- Valyu: Real-time web search + proprietary content
- Firecrawl: Scrape any site -> markdown
- Brave Search: Free web search, no tracking
- Tavily: AI-optimized search, free tier
- crawl4ai: AI extraction, Python, free

Usage:
    python web_search.py <provider> <query> [options]
    python web_search.py valyu "Vietnam SaaS" --mode web
    python web_search.py firecrawl "https://example.com"
    python web_search.py brave "startup tools" --num-results 10
    python web_search.py tavily "market research" --search-depth advanced
    python web_search.py crawl4ai "https://example.com" --extract-ai
"""

import sys
import os
import json
import argparse
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PROVIDERS = {
    'valyu': {
        'name': 'Valyu',
        'description': 'Real-time web + proprietary content (papers, filings, patents)',
        'requires_key': True,
        'key_env': 'VALYU_API_KEY',
        'key_url': 'https://valyu.ai',
        'modes': ['web', 'deep', 'academic'],
        'free': False,
    },
    'firecrawl': {
        'name': 'Firecrawl',
        'description': 'Scrape any website -> markdown',
        'requires_key': True,
        'key_env': 'FIRECRAWL_API_KEY',
        'key_url': 'https://firecrawl.dev',
        'modes': ['scrape', 'crawl'],
        'free': False,
    },
    'brave': {
        'name': 'Brave Search',
        'description': 'Free web search, no tracking',
        'requires_key': True,
        'key_env': 'BRAVE_API_KEY',
        'key_url': 'https://brave.com/search/api',
        'modes': ['web', 'news'],
        'free': True,
    },
    'tavily': {
        'name': 'Tavily',
        'description': 'AI-optimized search, free tier available',
        'requires_key': True,
        'key_env': 'TAVILY_API_KEY',
        'key_url': 'https://tavily.com',
        'modes': ['search', 'deep'],
        'free': True,
    },
    'crawl4ai': {
        'name': 'crawl4ai',
        'description': 'AI-powered web extraction, Python, free',
        'requires_key': False,
        'key_env': None,
        'key_url': 'https://github.com/uncle-lyozha/crawl4ai',
        'modes': ['scrape', 'crawl'],
        'free': True,
    },
}


def check_provider(provider):
    """Check if provider is available and API key is set."""
    info = PROVIDERS[provider]
    
    if info['requires_key']:
        key_name = info['key_env']
        api_key = os.environ.get(key_name)
        if not api_key:
            print(f"API key not set: {key_name}")
            print(f"  Get your key at: {info['key_url']}")
            print(f"  Then: export {key_name}=your_key")
            sys.exit(1)
        return api_key
    return None


def search_valyu(query, mode='web', max_results=10, api_key=None):
    """Valyu search."""
    try:
        import valyu
    except ImportError:
        print("valyu not installed. Run: pip install valyu")
        sys.exit(1)
    
    client = valyu.Valyu(api_key=api_key)
    print(f"Searching Valyu ({mode}): {query}")
    
    search_type_map = {'web': 'web', 'deep': 'all', 'academic': 'proprietary'}
    stype = search_type_map.get(mode, 'all')
    results = client.search(query, max_num_results=max_results, search_type=stype)
    
    return {
        "provider": "valyu",
        "mode": mode,
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }


def search_firecrawl(url, mode='scrape', api_key=None):
    """Firecrawl scrape."""
    try:
        from firecrawl import FirecrawlApp
    except ImportError:
        print("firecrawl-py not installed. Run: pip install firecrawl-py")
        sys.exit(1)
    
    app = FirecrawlApp(api_key=api_key)
    print(f"Scraping Firecrawl ({mode}): {url}")
    
    if mode == 'scrape':
        result = app.scrape(url)
    else:
        result = app.crawl(url)
    
    return {
        "provider": "firecrawl",
        "mode": mode,
        "url": url,
        "results": result,
        "timestamp": datetime.now().isoformat()
    }


def search_brave(query, num_results=10, api_key=None):
    """Brave Search using requests directly."""
    import requests
    
    print(f"Searching Brave: {query}")
    response = requests.get(
        'https://api.search.brave.com/res/v1/web/search',
        headers={'X-Subscription-Token': api_key},
        params={'q': query, 'count': num_results}
    )
    
    if response.status_code != 200:
        print(f"Brave API error: {response.status_code} {response.text}")
        sys.exit(1)
    
    data = response.json()
    results = data.get('web', {}).get('results', [])
    
    return {
        "provider": "brave",
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }


def search_tavily(query, search_depth='basic', max_results=10, api_key=None):
    """Tavily Search."""
    try:
        from tavily import TavilyClient
    except ImportError:
        print("tavily not installed. Run: pip install tavily-python")
        sys.exit(1)
    
    client = TavilyClient(api_key=api_key)
    print(f"Searching Tavily ({search_depth}): {query}")
    results = client.search(query, depth=search_depth, max_results=max_results)
    
    return {
        "provider": "tavily",
        "query": query,
        "depth": search_depth,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }


def search_crawl4ai(url, mode='scrape', extract_ai=True, api_key=None):
    """crawl4ai extraction."""
    try:
        from crawl4ai import WebCrawler
    except ImportError:
        print("crawl4ai not installed. Run: pip install crawl4ai")
        sys.exit(1)
    
    crawler = WebCrawler()
    print(f"Scraping crawl4ai ({mode}): {url}")
    
    if mode == 'scrape':
        result = crawler.run(url=url, extract_ai=extract_ai)
    else:
        result = crawler.crawl(urls=[url], extract_ai=extract_ai)
    
    return {
        "provider": "crawl4ai",
        "mode": mode,
        "url": url,
        "results": result,
        "timestamp": datetime.now().isoformat()
    }


def format_results(data):
    """Format results for markdown output."""
    output = []
    output.append(f"# Search Results: {data.get('query', data.get('url', 'N/A'))}")
    output.append(f"\n**Provider:** {data['provider'].upper()}")
    output.append(f"**Mode:** {data.get('mode', 'N/A')}")
    output.append(f"**Timestamp:** {data['timestamp']}")
    
    raw = data.get('results')
    
    if hasattr(raw, 'markdown'):
        markdown_content = raw.markdown[:2000] if len(raw.markdown) > 2000 else raw.markdown
        output.append(f"\n## Content (markdown, {len(raw.markdown)} chars)")
        output.append(f"\n{markdown_content}\n")
        if raw.metadata:
            output.append("\n### Metadata")
            meta_dict = raw.metadata.model_dump()
            for k, v in list(meta_dict.items())[:10]:
                if v:
                    output.append(f"- **{k}:** {v}")
        return "\n".join(output)
    
    if hasattr(raw, 'results'):
        results = raw.results
        output.append(f"**Results:** {len(results)}")
    elif isinstance(raw, list):
        results = raw
        output.append(f"**Results:** {len(results)}")
    elif isinstance(raw, dict):
        results = [raw]
        output.append(f"**Results:** 1")
    else:
        results = []
        output.append(f"**Results:** 0")
    
    output.append("\n---\n")
    
    for i, result in enumerate(results, 1):
        if hasattr(result, 'title'):
            title = result.title or 'No title'
            url = result.url or 'N/A'
            snippet = getattr(result, 'content', getattr(result, 'snippet', ''))
            score = getattr(result, 'relevance_score', 'N/A')
        elif isinstance(result, dict):
            title = result.get('title', result.get('name', 'No title'))
            url = result.get('url', result.get('link', 'N/A'))
            snippet = result.get('snippet', result.get('content', result.get('description', '')))
            score = result.get('score', result.get('relevance', 'N/A'))
        else:
            title = str(result)
            url = 'N/A'
            snippet = ''
            score = 'N/A'
        
        output.append(f"## {i}. {title}")
        output.append(f"- **URL:** {url}")
        if score != 'N/A':
            output.append(f"- **Relevance:** {score}")
        if snippet:
            snippet_text = snippet[:500] if len(snippet) > 500 else snippet
            output.append(f"\n> {snippet_text}")
        output.append("")
    
    return "\n".join(output)


def save_results(data, output_dir="data"):
    """Save results to data directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/search_{data['provider']}_{timestamp}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(format_results(data))
    
    print(f"Saved to: {filename}")
    return filename


def main():
    parser = argparse.ArgumentParser(description='Product Tower Kit - Web Search')
    parser.add_argument('provider', choices=list(PROVIDERS.keys()), help='Search provider')
    parser.add_argument('query', help='Search query or URL')
    parser.add_argument('--mode', choices=['web', 'deep', 'academic', 'scrape', 'crawl', 'news', 'search'], default='web')
    parser.add_argument('--max-results', type=int, default=10)
    parser.add_argument('--num-results', type=int, default=10)
    parser.add_argument('--search-depth', choices=['basic', 'advanced'], default='basic')
    parser.add_argument('--extract-ai', action='store_true', default=True)
    parser.add_argument('--output', '-o', help='Output file (default: auto)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    provider = args.provider
    api_key = check_provider(provider)
    
    if provider == 'valyu':
        data = search_valyu(args.query, args.mode, args.max_results, api_key)
    elif provider == 'firecrawl':
        data = search_firecrawl(args.query, args.mode, api_key)
    elif provider == 'brave':
        data = search_brave(args.query, args.num_results, api_key)
    elif provider == 'tavily':
        data = search_tavily(args.query, args.search_depth, args.max_results, api_key)
    elif provider == 'crawl4ai':
        data = search_crawl4ai(args.query, args.mode, args.extract_ai, api_key)
    
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(format_results(data))
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            if args.json:
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(format_results(data))
        print(f"Saved to: {args.output}")
    else:
        save_results(data)


if __name__ == "__main__":
    main()
