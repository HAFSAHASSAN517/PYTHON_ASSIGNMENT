import urllib.request
import json
import os

def fetchnsave_news():
    # Public JSON endpoint (simulating news API output)
    url = "https://jsonplaceholder.typicode.com/posts?_limit=10"
    
    print("Fetching news from API...")
    
    try:
        # Create request with standard headers
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        # Open URL and read response
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        output_file = "news.json"
        
        # Save parsed data to JSON file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        if os.path.exists(output_file):
            print(f"Top 10 news saved to {output_file}")

    except Exception as e:
        print(f"Error occurred while processing news: {e}")

if __name__ == "__main__":
    fetchnsave_news()