# User Management System with Login and CRUD Operations

This project is a web application that implements a user authentication system (Login) and user management (CRUD) functionality, following the MVC (Model-View-Controller) design pattern. The frontend is built using **Vue.js** and the backend is developed with **Python**. The application uses **MongoDB** for data storage and is containerized with **Docker**.

## Features

- **Login System**: Authenticates users with hardcoded credentials for now (admin@gmail.com, admin123).
- **User CRUD Operations**: Allows admins to create, read, update, and delete users.
- **Authentication Protection**: Users cannot access the CRUD section without logging in. If an unauthenticated user attempts to access the `/users` route, they will be redirected to the login page.
- **Session Management**: Uses `localStorage` to store authentication state.
- **Logout Functionality**: Users can log out, which clears the session and redirects them to the login page.

## Technologies

### Frontend
- **Vue.js**: The frontend is implemented with Vue.js to create a dynamic, interactive user interface.
- **SweetAlert2**: Used for showing alerts for login success/failure, CRUD operations, and logout confirmation.

### Backend
- **Python**: Backend server is implemented in Python.
- **FastAPI**: Used for managing the API and user data.
- **MongoDB**: The user data is stored in MongoDB for persistence.
- **Docker**: The entire application is containerized using Docker for easy deployment and environment consistency.

### Styling
- **Custom CSS**: For a modern and dark theme UI.

## Project Structure

The project follows the MVC architecture pattern:

1. **Model**: Represents the user data stored in MongoDB, managed by the backend.
2. **View**: Handled by Vue.js components to render the login and user management interface.
3. **Controller**: Contains the logic for routing between login and CRUD functionalities, and handles the session state.

## Setup Instructions

### Frontend

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm run dev
    ```

### Backend

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Install the required Python dependencies (ensure you have Python installed):
    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server using Docker:
    ```bash
    docker-compose up
    ```

    This will start the backend along with MongoDB in a Docker container.

## Usage

1. Open the frontend at `http://localhost:5173` and login using the hardcoded credentials:
   - Email: `admin@gmail.com`
   - Password: `admin123`
   
2. Upon successful login, you'll be redirected to the **User Management** interface where you can manage users (add, edit, or delete).

3. Click "Logout" to end the session, which will redirect you back to the login page.

## Routes

- **/login**: Displays the login form.
- **/users**: Shows the user management interface (CRUD operations). This route is protected and can only be accessed after successful authentication.

## Future Enhancements

- **Full Database Integration**: Replace hardcoded credentials with real users stored in MongoDB.
- **API Authentication**: Implement JWT for secure authentication and session management.
- **Role-Based Access**: Introduce roles (e.g., admin, user) for managing permissions.
