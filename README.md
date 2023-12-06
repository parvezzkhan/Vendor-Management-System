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

```bash
# Clone the Repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

# Install Requirements
pipenv install --dev

# Apply Migrations
pipenv run python manage.py migrate

# Create Superuser
pipenv run python manage.py createsuperuser

# Run the Development Server
pipenv run python manage.py runserver
