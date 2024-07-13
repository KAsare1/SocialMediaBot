# Social Media Post Idea Generation Bot

This project is designed to generate social media post ideas by fetching data from various sources, analyzing emerging trends in a chosen industry, and applying those trends to identify emerging problems within the industry.

## Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Virtual Environment**: It is recommended to create and activate a virtual environment to manage dependencies.

## Setup

1. **Clone the Repository**:

2. **Create and Activate a Virtual Environment**
    ```sh
    python -m venv virtualenv
    source virtualenv/bin/activate 
    ```
3. **Install all requirements**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Industry**: You can change the industry of choice by modifying the industry variable in the main.py file.
    ``` sh
    industry = "Artificial Intelligence"  # Change this to your desired industry
    ```
5. **Run the application**
    ``` sh
    python main.py
    ```
    Make sure you're in the root directory of the folder it 

6. The fetched data can be found in the <industry_name>_headlines.json file in the data folder