# Django Discourse

Django Discourse is a web application built with the Django framework for Python, designed to provide users with a platform to create, join, and engage in discussions on various topics. Drawing inspiration from popular communication platforms like Discord, Django Discourse aims to provide a user-friendly and dynamic environment for meaningful conversations.

## Features

- **User Authentication:** Secure user authentication system to ensure only registered users can create and participate in discussions.
- **Room Creation:** Users can create discussion rooms based on their favorite topics or interests.
- **Room Joining:** Seamless room joining functionality, allowing users to easily become part of the discussions that interest them.
- **Chat:** Dynamic chat functionality enables users to engage in conversations within the created rooms.
- **Responsive Design:** The application is built with a responsive design, ensuring a consistent user experience across various devices.
- **RESTful API:** Comprehensive API endpoints for seamless integration with external applications and services.

## Getting Started

Follow these steps to set up Django Discourse on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-discourse.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-discourse
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your web browser to access Django Discourse.

## Usage

1. Log in with your superuser account or create a new account.
2. Explore existing discussion rooms or create your own.
3. Join rooms to participate in discussions.
4. Engage in real-time chat with other users in the selected room.

## Contributing

We welcome contributions to Django Discourse. Feel free to submit bug reports, feature requests, or even pull requests. Please refer to our [contribution guidelines](CONTRIBUTING.md) for more information.

## License

Django Discourse is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

---

Happy discussing! 🗨️✨