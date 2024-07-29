# Jio Recharges API

This project includes an Exploratory Data Analysis (EDA) of Jio recharges dataset and a FastAPI-based API to interact with the analyzed data. 

### Project Structure

- **`graphs.ipynb`**: Contains visualizations such as bar graphs and other plots that represent insights from the Jio recharges dataset.
- **`functions.py`**: Contains functions for performing Exploratory Data Analysis (EDA) on the Jio recharges dataset, which are imported and used by the FastAPI application to generate various data insights.
- **`app.py`**: Main FastAPI application file.

### Features

- **EDA**: Analyze the Jio recharges dataset to understand key metrics and trends.
- **Data Visualization**: Visualizations such as bar graphs and other plots that give insights into the data.
- **FastAPI API**: Provides endpoints to access various statistics and insights derived from the data.

### Endpoints

The FastAPI application exposes the following endpoints:

- **`GET /jiodata/stats`**: Retrieve various statistics from the dataset. You can specify query parameters to get different types of insights:
  - `value`: (1 to 7) An integer parameter to choose the type of statistic to retrieve.
  - `pg_name`: An optional string parameter to filter results by payment gateway name.


![Screenshot 2024-07-29 171941](https://github.com/user-attachments/assets/7d71d2b9-82e5-47d2-b2bd-2751e25ce8dd)
