# Traffic Data Analysis Pipeline

## Overview
This project is designed to ingest, transform, and visualize traffic data collected from UAVs using a robust ELT pipeline.
The goal is to improve traffic flow in urban areas by analyzing vehicle trajectories and providing actionable insights through visualizations.

## Technology Stack
- **Apache Airflow**: Used for orchestrating the workflow of data loading and transformation.
- **PostgreSQL**: Serves as the data warehouse where data is loaded and transformed.
- **dbt (Data Build Tool)**: Manages data transformation within PostgreSQL.
- **Redash**: Used for visualizing the transformed data and generating reports.
- **Docker**: Containerization platform used to create a consistent development environment.

## Architecture

![Architecture](https://github.com/derejehinsermu/10x_scalable_datawarehouse_week-2/assets/45657872/6c7f97b9-4733-4b23-81f0-ecf8abf92f48)


- Data is extracted from CSV files.
- Data is loaded into PostgreSQL.
- Transformations are performed within PostgreSQL using dbt.
- Redash is used to visualize and report on the transformed data.


## Setup Instructions

### Prerequisites
- Docker: Install Docker- Desktop from this link: https://www.docker.com/products/docker-desktop/
- Docker Compose download template using this:
  ```sh
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.0/docker-compose.yaml'
    
    ```
- Access to a PostgreSQL server
- Run Airflow in Docker using this link : https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html



1. Python 3.x and pip (Usually bundled with Python installation)

2. Git installed on your machine.

3. Virtualenv. You can install it using pip:
    ```sh
    pip install virtualenv

### Steps

1. **Clone the Repository**
    ```sh
     git@https://github.com/derejehinsermu/10x_scalable_datawarehouse_week-2.git
    
    ```
2. **Create and Activate a Virtual Environment**
    Navigate to the root directory of the project and create a virtual environment named 'venv', then activate it:
    ```sh
    cd 10x_scalable_datawarehouse_week
    python -m venv venv  | virtualenv venv
    source venv/bin/activate
    ```
3. **Install Requirements**
    While inside the virtual environment, install the project requirements:
    ```sh
    pip install -r requirements.txt

    docker-compose up
    
    ```


