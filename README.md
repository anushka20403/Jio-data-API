# Jio Recharges API

This project includes an Exploratory Data Analysis (EDA) of Jio recharges dataset and a FastAPI-based API to interact with the analyzed data. 

### Project Structure

- **`graphs.ipynb`**: Contains visualizations such as bar graphs and other plots that represent insights from the Jio recharges dataset.
- **`functions.py`**: Contains functions for performing Exploratory Data Analysis (EDA) on the Jio recharges dataset, which are imported and used by the FastAPI application to generate various data insights.
- **`app.py`**: Main FastAPI application file. Run the app in the terminal using command: $ uvicorn app:app --reload --port 9898

### Features

- **EDA**: Analyze the Jio recharges dataset to understand key metrics and trends.
- **Data Visualization**: Visualizations such as bar graphs and other plots that give insights into the data.
- **FastAPI API**: Provides endpoints to access various statistics and insights derived from the data.

### Endpoints

The FastAPI application exposes the following endpoints:

- **`GET /jiodata/stats`**: Retrieve various statistics from the dataset. You can specify query parameters to get different types of insights:
  - `value`: (1 to 7) An integer parameter to choose the type of statistic to retrieve.
  - `pg_name`: An optional string parameter to filter results by payment gateway name.

### Example:

#### value=6 gives data about recharges made from which payment gateways, number of successes, failures, not confirmed payments per PG and their percentages.

![Screenshot 2024-07-29 171923](https://github.com/user-attachments/assets/baba0e67-edc0-4cd9-97e6-361c3878ade8)
