
# Python SQLite CRUD Example

This repository demonstrates how to create a basic Python project that interacts with an SQLite database. The project includes methods for performing CRUD (Create, Read, Update, Delete) operations, showcasing how to work with SQLite databases using Python's built-in `sqlite3` module.

## Table of Contents
1. [Getting Started](#getting-started)
2. [CRUD Operations](#crud-operations)
3. [Diagrams](#diagrams)

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- VS Code or any code editor of your choice.
- Basic understanding of Python.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/python-sqlite-crud-example.git
   cd python-sqlite-crud-example
   ```

2. **Create a Virtual Environment**
   Create a virtual environment to manage dependencies and isolate the project environment.
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   Since `sqlite3` is included with Python, no additional packages need to be installed. If you plan to use other dependencies in the future, you can install them using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database**
   Run the `database_setup.py` script to create the SQLite database and table:
   ```bash
   python3 database_setup.py
   ```

6. **Run the CRUD Operations**
   Test the CRUD operations by running the `main.py` script:
   ```bash
   python3 main.py
   ```

## CRUD Operations

This project demonstrates basic CRUD operations on an SQLite database using Python's `sqlite3` module. Below is an explanation of each operation:

### 1. **Create (Insert a Row)**
   - **Function**: `insert_row`
   - **Purpose**: Adds a new record to the `my_table`.
   - **How it works**:
     - Connects to the SQLite database.
     - Executes an `INSERT INTO` SQL statement to add a new row with the provided values.
     - Commits the transaction and closes the connection.

### 2. **Read (Retrieve Rows)**
   - **Function**: `read_rows`
   - **Purpose**: Fetches all rows from the `my_table`.
   - **How it works**:
     - Connects to the SQLite database.
     - Executes a `SELECT *` SQL statement to retrieve all rows.
     - Fetches all rows and returns them.

### 3. **Update (Modify a Row)**
   - **Function**: `update_row`
   - **Purpose**: Updates specific columns of a row in the `my_table`.
   - **How it works**:
     - Connects to the SQLite database.
     - Dynamically builds an `UPDATE` SQL statement based on the provided parameters.
     - Executes the `UPDATE` statement, modifying the specified row by `id`.
     - Commits the transaction and closes the connection.

### 4. **Delete (Remove a Row)**
   - **Function**: `delete_row`
   - **Purpose**: Removes a specific row from the `my_table`.
   - **How it works**:
     - Connects to the SQLite database.
     - Executes a `DELETE FROM` SQL statement to remove the row by `id`.
     - Commits the transaction and closes the connection.

## Diagrams

### CRUD Operations Flow

```mermaid
graph TD;
    A[Start] --> B[Create Database Connection];
    B --> C{Choose Operation};
    C -->|Create| D[Insert a New Row];
    C -->|Read| E[Select and Fetch Rows];
    C -->|Update| F[Build and Execute Update Query];
    C -->|Delete| G[Execute Delete Query];
    D --> H[Commit Changes];
    E --> H;
    F --> H;
    G --> H;
    H --> I[Close Database Connection];
    I --> J[End];
```

### Database Schema

```mermaid
erDiagram
    MY_TABLE {
        INTEGER id PK
        TEXT name
        INTEGER age
        TEXT email
        REAL salary
        INTEGER active
        TEXT created_at
        TEXT updated_at
        TEXT phone_number
        BLOB notes
    }
```

The diagram above outlines the basic flow of CRUD operations and shows the structure of the SQLite database table used in this project.
