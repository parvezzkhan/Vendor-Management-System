# Vendor Management System

Brief description of your project.

## API Documentation

Explore the API endpoints using [Postman API Documentation](https://documenter.getpostman.com/view/31599184/2s9YeLZA9F). If you're a developer looking to integrate with our API, follow the documentation for detailed information.

## Table of Contents

- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Install Requirements](#install-requirements)
  - [Apply Migrations](#apply-migrations)
  - [Create Superuser](#create-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these steps to set up the project locally on your machine.

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

#!/bin/bash

# Clone the repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

# Install requirements using Pipenv
pipenv install --dev

# Apply migrations to create the database
pipenv run python manage.py migrate

# Create superuser
pipenv run python manage.py createsuperuser

# Run the development server
pipenv run python manage.py runserver &

# Open API documentation in default browser
sleep 5 # Wait for the server to start (adjust as needed)
xdg-open https://documenter.getpostman.com/view/31599184/2s9YeLZA9F

# Optionally, you can add a message to notify the user
echo "Setup completed. The development server is running, and API documentation is opened in your default browser."

