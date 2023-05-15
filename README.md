# Kanban

P.O.C.

## Setting up the repository

- Choose a new repository name

- Use it to rename the current cloned repository

- Delete the current `.git` folder (the folder might be hidden)

- Update `README.md`

- Run the following command in the terminal of the repository :
  
  ```git
  git init
  git add .
  git commit -m "<commit message>"
  ```

*You are now ready to install the project. :)*

## Installation

- Install a virtual environment
  
  ```powershell
  <Python command> -m venv .env
  ```

- Activate the virtual environment
  
  - Windows
    
    ```powershell
    .env\Scripts\activate
    ```
  
  - Linux
    
    ```powershell
    source .env/bin/activate
    ```

- Install packages
  
  ```powershell
  pip install -r requirements.txt
  ```

- Hide the key to the castle
  
  - Create the safe
    
    Inside `project` folder, create a file called `.env`.
  
  - Generate the key
    
    We gonna generate the key through the Django shell interface.
    
    To launch the shell interface, run the following command in the terminal of your Django project :
    
    ```powershell
    <Python command> manage.py shell
    ```
    
    - Import the key generator function
      
      Run the following command and hit `Enter` :
      
      ```python
      from django.core.management.utils import get_random_secret_key
      ```
    
    - Generate a random key
      
      On the next line we can now use the function to generate the secret key.
      
      ```python
      print(get_random_secret_key())
      ```
    
    - Hide the key
      
      Copy the generated key and exit the shell interface using the following command :
      
      ```python
      exit()
      ```
      
      In the `.env` file, declare a `SECRET_KEY` variable as follows :
      
      ```python
      SECRET_KEY=<generated key>
      ```
      
      *The castle is well-protected now. :)*

- Setting up the database
  
  - Install the PostgreSQL database connection package
    
    - Windows
      
      ```powershell
      pip install psycopg2
      ```
    
    - Linux
      
      ```powershell
      pip install psycopg2-binary
      ```
  
  - Create the database through pgAdmin
  
  - Update `project/settings.py`
    
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
    ```
  
  - Update `project/.env`
    
    ```python
    DB_NAME=<database name>
    DB_USER=<database user>
    DB_PASSWORD=<database password>
    ```

- Make the first migrations
  
  ```powershell
  <Python command> manage.py makemigrations
  <Python command> manage.py migrate
  ```

- Populate database
  
  ```powershell
  <Python command> manage.py init_local_dev
  ```
  
  When populating the database, a superuser is created.
  
  Superuser credentials :
  
  - Username : admin
  
  - Password : admin

- Update `base_user.py`
  
  ```python
  # Windows : .env/Lib/site-packages/django/contrib/auth/base_user.py
  # Linux : .env/lib/python<Python version>/site-packages/django/contrib/auth/base_user.py
  
  from django.db import transaction
  
  class AbstractBaseUser(models.Model):
    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    #...
    @transaction.atomic
    def deactivate(self):
        if self.is_active is True:
            self.is_active = False
            self.save()
  
    @transaction.atomic
    def activate(self):
        if self.is_active is False:
            self.is_active = True
            self.save()
  ```

## API REST

| URI                                | Authorization | Method | Data                       | Description                  |
| ---------------------------------- | ------------- | ------ | -------------------------- | ---------------------------- |
| /api/users/                        | No Auth       | GET    | None                       | List of users                |
| /api/users/\<id_user\>/            | No Auth       | GET    | None                       | User instance                |
| /api/users/\<id_user\>/            | Basic Auth    | PATCH  | {"email": "\<new email\>"} | Update user's instance email |
| /api/users/\<id_user\>/activate/   | Basic Auth    | PATCH  | None                       | Activate user instance       |
| /api/users/\<id_user\>/deactivate/ | Basic Auth    | PATCH  | None                       | Deactivate user instance     |
| /api/predict/                      | No Auth       | GET    | None                       | Dummy price prediction       |
