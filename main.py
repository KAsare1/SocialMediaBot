# Example usage
import json
from src.data_fetcher import fetch_data


if __name__ == "__main__":
    industry = "Artificial Intelligence"
    top_headlines = fetch_data(industry)

    if "error" in top_headlines:
        print(f"Error: {top_headlines['error']}")
    else:
        print(json.dumps(top_headlines, indent=4))