import requests
import json
from config import AIRTABLE_API_KEY, BASE_ID, SOURCES_TABLE_NAME, PROJECTS_TABLE_NAME, TASKS_TABLE_NAME

class AirtableIntegration:
    def __init__(self):
        self.base_url = f"https://api.airtable.com/v0/{BASE_ID}"
        self.headers = {
            "Authorization": f"Bearer {AIRTABLE_API_KEY}",
            "Content-Type": "application/json"
        }

    def get_sources(self):
        url = f"{self.base_url}/{SOURCES_TABLE_NAME}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('records', [])
        else:
            print(f"Error fetching sources: {response.status_code}")
            return []

    def get_projects(self):
        url = f"{self.base_url}/{PROJECTS_TABLE_NAME}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('records', [])
        else:
            print(f"Error fetching projects: {response.status_code}")
            return []

    