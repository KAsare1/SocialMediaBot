import json
import os
import requests
from newsapi import NewsApiClient
import logging
from .config import NEWS_API_KEY

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_data(industry):
    try:
        # Initializing the NewsApiClient with the API key
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        
        # Fetching available sources from the NewsAPI
        api_sources = newsapi.get_sources()
        
        if api_sources and 'sources' in api_sources:
            try:
                # Fetching top headlines for the given industry from the available sources
                top_headlines = newsapi.get_everything(q=industry,
                                                       sources=','.join([s['id'] for s in api_sources['sources']]),
                                                       language='en',
                                                       sort_by='publishedAt',
                                                       page_size=5)
                
                # Ensure the 'data' directory exists
                os.makedirs('data', exist_ok=True)
                
                # Save the fetched data to a JSON file in the 'data' directory
                file_path = os.path.join('data', f'{industry}_headlines.json')
                with open(file_path, 'w') as outfile:
                    json.dump(top_headlines, outfile, indent=4)
                
                logger.info(f"Data saved to {file_path}")
                return top_headlines
            
            except Exception as e:
                logger.error(f"Error fetching headlines: {e}")
                return {"error": "Error fetching headlines"}
        
        else:
            logger.error("No sources available from NewsAPI")
            return {"error": "No sources available from NewsAPI"}
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")
        return {"error": "Network error"}
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}
