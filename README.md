# User-RegLog

## Features

        - User Registration
        - User Login
        - User Logout
        - Password Change
        - JWT (JSON Web Tokens) for authentication

## Endpoints
        List the API endpoints along with a brief description of each.

        /user/register/: User registration endpoint.
        /user/login/: User login endpoint.
        /user/logout/: User logout endpoint.
        /user/password-change/: Password change endpoint.
        /user/token/: TAking access and refresh token every 4 days
## Authentication
        JWT (JSON Web Tokens) are used for authentication and after taking access token from using user/token endpoint,you should put it into bearer token in Auth in Postman.

# Installation

        Clone the repository:

        ```bash
        
            git clone https://github.com/Ravshanbekk07//User-RegLog.git

            cd your-project

            pip install -r req.txt

            python manage.py migrate

            python manage.py runserver



