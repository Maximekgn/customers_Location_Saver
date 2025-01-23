# Project Title

This project is a Flask web application that allows users to add and view geolocations on a map.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:
- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment (optional but recommended):po
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python app.py
    ```

### Running the Application

1. Start the Flask development server:
    ```bash
    c
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

### Usage

- To add a new geolocation, go to `http://127.0.0.1:5000/add` and fill out the form.
- To view the map with all the added geolocations, go to `http://127.0.0.1:5000/map`.

### Project Structure

- `app.py`: The main Flask application file.
- `models.py`: Contains the database model for the geolocations.
- `templates/`: Contains the HTML templates for the application.
  - `form.html`: The form for adding new geolocations.
  - `map.html`: The map displaying all the geolocations.

### Contributing

If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

