# Vendor Management System

Vendor Management System is a Django project designed to Simplifying vendor, purchase order, and performance metric management in a single system.
## Getting Started

Explore the API endpoints using [Postman API Documentation](https://documenter.getpostman.com/view/31599184/2s9YeLZA9F).


Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python (3.7 or higher)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/parvezzkhan/Vendor-Management-System.git
    cd vendor_management_system
    ```

2. Install requirements using Pipenv:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations to create the database:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be accessible at http://127.0.0.1:8000/.




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
