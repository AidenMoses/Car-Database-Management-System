# Car Database Management System

This is a simple Python-based Car Database Management System (DBMS) that allows you to perform various operations on a database of cars. It uses SQLite for data storage and management, as well as Pandas for data manipulation.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Operations](#operations)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new cars to the database.
- Delete cars from the database.
- Update existing car records.
- View all cars in the database.
- Search for cars based on specific criteria.
- Reset the database to its initial state.
- Quit the program.

## Getting Started

### Prerequisites

To run this code, you will need:

- Python 3.x installed on your computer.
- The following Python libraries: `sqlite3`, `pandas`.

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/car-database-management.git
   ```

2. Change into the project directory:

   ```
   cd car-database-management
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required libraries:

   ```
   pip install sqlite3 pandas
   ```

## Usage

1. Make sure you've followed the installation steps above.

2. Run the program:

   ```
   python car_dbms.py
   ```

3. Follow the on-screen menu to perform various operations on the car database.

## Operations

- **Add a new car to the database**: You can add a new car by providing its brand, model, year, VIN, odometer reading, and price.

- **Delete a Car from the database**: You can delete a car from the database by specifying its model.

- **Update an existing database record**: You can update an existing record by specifying the model to be updated and providing new information.

- **View all cars in the database**: This option displays all cars in the database.

- **Search for a car or set of cars that meet certain criteria**: You can search for cars based on specific criteria such as brand, model, year, etc.

- **Delete all data from the database**: This option resets the database to its initial state by dropping and recreating the `Cars` table.

- **Quit the Program**: This option exits the program.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
