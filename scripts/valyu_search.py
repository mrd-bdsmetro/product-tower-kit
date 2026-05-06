#!/usr/bin/env python3
"""
Product Tower Kit — Valyu Search Integration

Enhanced market research using Valyu API.
Provides real-time web search + proprietary content (papers, filings, patents).

Usage:
    python valyu_search.py <query> [--mode web|deep|academic] [--max-results 10]
    python valyu_search.py "Vietnam SaaS market size 2025" --mode deep
    python valyu_search.py "product-market fit framework" --mode academic

Environment:
    VALYU_API_KEY — Required. Get from https://valyu.ai
"""

import sys
import os
import json
import argparse
from datetime import datetime

# Fix Unicode on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def check_valyu():
    """Check if valyu is installed and API key is set."""
    try:
        import valyu
    except ImportError:
        print("❌ valyu not installed. Run: pip install valyu")
        sys.exit(1)
    
    api_key = os.environ.get('VALYU_API_KEY')
    if not api_key:
        print("❌ VALYU_API_KEY not set.")
        print("   Get your key at: https://valyu.ai")
        print("   Then: export VALYU_API_KEY=your_key")
        sys.exit(1)
    
    return valyu, api_key

def search_web(query, max_results=10):
    """Standard web search."""
    valyu, api_key = check_valyu()
    client = valyu.Valyu(api_key=api_key)
    
    print(f"🔍 Searching web: {query}")
    results = client.search(query, max_results=max_results)
    
    return {
        "mode": "web",
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }

def search_deep(query, max_results=10):
    """Deep search with full content extraction."""
    valyu, api_key = check_valyu()
    client = valyu.Valyu(api_key=api_key)
    
    print(f"🔬 Deep searching: {query}")
    results = client.search(
        query, 
        max_results=max_results,
        search_type="deep"
    )
    
    return {
        "mode": "deep",
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }

def search_academic(query, max_results=10):
    """Academic search (papers, filings, patents)."""
    valyu, api_key = check_valyu()
    client = valyu.Valyu(api_key=api_key)
    
    print(f"📚 Academic search: {query}")
    results = client.search(
        query,
        max_results=max_results,
        search_type="academic"
    )
    
    return {
        "mode": "academic",
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    }

def format_results(data):
    """Format results for markdown output."""
    output = []
    output.append(f"# Search Results: {data['query']}")
    output.append(f"\n**Mode:** {data['mode']}")
    output.append(f"**Timestamp:** {data['timestamp']}")
    output.append(f"**Results:** {len(data['results'])}")
    output.append("\n---\n")
    
    for i, result in enumerate(data['results'], 1):
        output.append(f"## {i}. {result.get('title', 'No title')}")
        output.append(f"- **URL:** {result.get('url', 'N/A')}")
        output.append(f"- **Source:** {result.get('source', 'N/A')}")
        output.append(f"- **Relevance:** {result.get('score', 'N/A')}")
        
        snippet = result.get('snippet', result.get('content', ''))
        if snippet:
            output.append(f"\n> {snippet[:500]}...")
        output.append("")
    
    return "\n".join(output)

def save_results(data, output_dir="data"):
    """Save results to data directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/search_{data['mode']}_{timestamp}.md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(format_results(data))
    
    print(f"✅ Saved to: {filename}")
    return filename

def main():
    parser = argparse.ArgumentParser(description='Valyu Search for Product Tower Kit')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--mode', choices=['web', 'deep', 'academic'], 
                       default='web', help='Search mode')
    parser.add_argument('--max-results', type=int, default=10, 
                       help='Maximum results')
    parser.add_argument('--output', '-o', help='Output file (default: auto)')
    parser.add_argument('--json', action='store_true', 
                       help='Output as JSON')
    
    args = parser.parse_args()
    
    # Run search
    if args.mode == 'web':
        data = search_web(args.query, args.max_results)
    elif args.mode == 'deep':
        data = search_deep(args.query, args.max_results)
    elif args.mode == 'academic':
        data = search_academic(args.query, args.max_results)
    
    # Output
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(format_results(data))
    
    # Save
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            if args.json:
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(format_results(data))
        print(f"✅ Saved to: {args.output}")
    else:
        save_results(data)

if __name__ == "__main__":
    main()
