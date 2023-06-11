
## About
This code repository contains the source code for a robust blogging platform API built using Django, a powerful Python web framework, and PostgreSQL, a reliable open-source relational database management system. The repository offers a comprehensive set of features for creating, managing, and interacting with blog content through RESTful endpoints. Additionally, the repository includes a suite of tests to ensure the stability and reliability of the API.

Key Features:

1.  RESTfull API: The platform provides a RESTful architecture, allowing clients to interact with the blogging platform through well-defined endpoints. Users can perform CRUD (Create, Read, Update, Delete) operations on blogs, comments, categories, and tags.
    
2.  User Management: The API supports user authentication and authorization, enabling users to register, log in, and manage their profiles. Role-based access control can be implemented to restrict certain actions or endpoints based on user roles.
    
3.  Blog Operations: Authors can create, retrieve, update, and delete blog posts using the API endpoints. The platform supports features such as rich text content, categorization, and tagging. Pagination and sorting options are available to efficiently handle large volumes of blog posts.
    
4.  Commenting System: Users can interact with blog posts by adding comments. The API provides endpoints to create, retrieve, update, and delete comments. Optional features like comment moderation and nested comments can be implemented based on specific requirements.
    
5.  Testing: The repository includes a comprehensive suite of tests to verify the functionality and performance of the API. These tests cover various scenarios and can be run to ensure the stability and reliability of the blogging platform.
    

By utilizing this code repository, developers can easily set up and customize a Django-PostgreSQL-based blogging platform with a RESTful API, empowering them to create engaging and interactive blog experiences for their users.

## Install:

### Using Docker:

```bash
# clone repository
git clone git@github.com:chato1337/drf-blog.git

# copy and set your env variables
cd drf-blog
cp .env.example .env

# create docker imgae
docker-compose build

# rucn docker image
docker-compose up
```

### Manually Install
before make sure you have installed on your system: python 3.9, pipenv and create a database in postgresql

```bash
# clone repository
git clone git@github.com:chato1337/drf-blog.git

# copy and set your env variables
cd drf-blog
cp .env.example .env

# init virtual env
pipenv shell

# install dependencies
pipenv install

# run migrations
python manage.py migrate

# run server
python manage.py runserver

# (optional) run tests
python manage.py test
```

## Dependencies

- https://django-rest-framework-simplejwt.readthedocs.io/en/stable/getting_started.html
- https://drf-yasg.readthedocs.io/en/stable/index.html
- https://pypi.org/project/django-cors-headers/
- https://django-filter.readthedocs.io/en/stable/index.html