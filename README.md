# Django GPT Client
This is a Django application that connects to the GPT core and acts as a client for it.

## Features
- User registration and login
- Chat with GPT
- Retrieve previous user chats
- Swagger API documentation
- Django Admin Panel for managing users and chats

## Installation and Setup

### Prerequisites
- Python 3.11.4

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <project-directory>
   ```

2. Ensure you have Python 3.11.4 installed.


3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

5. Configure the database and apply migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```

Now you can access the application at `http://127.0.0.1:8000/`.

## API Documentation
Swagger documentation is available at:
```
http://127.0.0.1:8000/swagger/
```

## Admin Panel
You can access the Django Admin Panel at:
```
http://127.0.0.1:8000/admin/
```
To log in, create a superuser:
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

## Api Key
You can set your gpt api key in .env file

## License
This project is licensed under the [MIT](LICENSE) license.
