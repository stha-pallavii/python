# Python Projects Repository

## Overview

This repository is a collection of various Python projects and exercises, each organized into its own branch. The projects cover a range of topics, including API development, Object-Relational Mapping (ORM), data analysis with Pandas, and coding challenges from Codewars.

## Repository Structure

The repository is organized into the following branches:

1.  ### Main Branch
   - **Description**: Serves as the primary branch containing general information and links to other project-specific branches.

2. ### API Branch
This branch contains a **Flask-based REST API** that performs CRUD operations on JSON data. It includes:

a. **`app.py`** - Implements API endpoints to retrieve, insert, update, and delete posts stored in `posts.json`.
b. **`q6.py`** - Interacts with an **external API** (`https://api.publicapis.org/entries`), saves data locally in `example.json`, and allows CRUD operations.
c. **`API.ipynb`** - A Jupyter Notebook for interactive API testing and exploration.

#### Key Features:
- **Retrieve & filter data:** Fetch posts by user ID and interact with public API entries.
- **Modify data:** Convert text fields to uppercase and update HTTPS status.
- **CRUD operations:** Insert, update, and delete records in local JSON files.
- **Testing:** A **Postman collection** (`API_assignment_I.postman_collection`) is provided for easy API testing.

#### Setup:
bash
git checkout api
pip install flask
python app.py  # or python q6.py


3. ### Codewars Branch
This branch contains a collection of solutions to coding challenges from [Codewars](https://www.codewars.com/), focusing on enhancing problem-solving skills and mastering Python programming concepts.

#### Key Components:
- **`codewars.ipynb`**:
  - A Jupyter Notebook documenting Python solutions to various Codewars challenges.
  - Includes explanations and code implementations for challenges ranging from beginner to advanced levels.

#### Features:
- Covers topics such as:
  - String manipulation
  - Data structure operations
  - Algorithmic problem-solving
  - Mathematical computations


4. ### ORM Branch
This branch implements **Object-Relational Mapping (ORM) using SQLAlchemy** to manage university-related data such as programs, semesters, courses, sections, students, and instructors.

#### Key Components:
a. **`db.py`** – Defines the **database schema** and initializes the MySQL database with required tables.
b. **`api.py`** – Implements **Flask-based API endpoints** for database CRUD operations.
c. **`ORM_Assignment.postman_collection.json`** – A **Postman collection** for testing API requests.
d. **`ORM_datacamp_practice.ipynb`** – A **Jupyter Notebook** demonstrating ORM queries and database interactions.
e. **`orm_database_mysql.sql`** – Contains the **SQL script** for setting up the database.
f. **`ORM_LMS_ERD.qsee`** – Entity-Relationship Diagram (ERD) for database structure visualization.
g. **`questions.txt`** – Lists key database operations such as inserting programs, retrieving students, and counting instructors.

#### Features:
- **Program & Course Management** – Insert programs, semesters, departments, and courses.
- **Student & Instructor Management** – Add students and instructors, retrieve their details.
- **Database Queries** – Fetch students by section, courses by semester, and instructors by program.
- **Flask API** – Exposes RESTful endpoints for database operations.

#### Setup:
bash
git checkout orm
pip install flask sqlalchemy mysql-connector-python
python db.py  # Initializes the database
python api.py  # Starts the Flask API


5.### Pandas Branch
This branch focuses on **data analysis and manipulation** using the **Pandas library**. It contains multiple assignments and practice notebooks that explore various Pandas functionalities, such as data cleaning, grouping, visualization, and time series analysis.

#### Key Components:
1. **`pandas_assignment_I`**:
   - Contains notebooks covering:
     - Getting and knowing your data
     - Filtering, grouping, and merging data
     - Time series analysis and data visualization

2. **`pandas_assignment_II`**:
   - Focuses on intermediate data manipulation techniques using Pandas.

3. **`pandas_assignment_III`**:
   - Includes a comprehensive assignment analyzing real-world data (e.g., COVID-19 and country data).
   - Key files:
     - `assignment_3_pandas.ipynb` – Main notebook.
     - `countries.csv` & `covid-countries-data.csv` – Datasets for analysis.

4. **`pandas_datacamp_practice`**:
   - A practice notebook (`pandas_datacamp_practice.ipynb`) summarizing exercises from DataCamp.

5. **`pandas_demo_practice`**:
   - Contains a notebook and dataset for practicing Pandas operations using IMDb's most popular films and series data.
  

6. **Final Project Branch**
   - **Description**: The culmination of the projects, integrating API development, ORM, and data analysis with Pandas.
   - **Contents**: Comprehensive Python application showcasing accumulated knowledge.
   - **Access**: [API_ORM_Pandas_Project Repository](https://github.com/stha-pallavii/API_ORM_Pandas_Project)

## Getting Started

To explore any of the projects:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/stha-pallavii/python.git
   cd python
