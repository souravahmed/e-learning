# Getting started with e-learning project

## Installation

Requirments.txt file has all the dependency.
To install all the dependency run below command after activating your virtualenv also need to run migrations. follow below command

```sh
pip install -r /path/to/requirements.txt
python manage.py makemigrations
python manage.py migrate
```

| Role     | value |
| -------- | ----- |
| Educator | 2     |
| Learner  | 3     |

| Endpoint                                        | Method | Body                                                                                                                                              |
| ----------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| http://localhost:8000/api/users/register        | POST   | ` { "email": "sourav@gmail.com","password": "sourav123","confirm_password": "sourav123","role": "2","first_name": "sourav","last_name": "ahmed"}` |
| http://localhost:8000/api/courses/create        | POST   | ` {"name": "Django","description": "Learn core concept of django","is_active": "true"}`                                                           |
| http://localhost:8000/api/users/login           | POST   | ` {"email": "sourav@gmail.com","password": "sourav123"}`                                                                                          |
| http://localhost:8000/api/courses/update/id     | PUT    | `{"name": "Django","description": "Learn core concept of django","is_active": "true"} `                                                           |
| http://localhost:8000/api/courses/enroll_course | POST   | ` {"user": "3","course": "1"}`                                                                                                                    |

## Features

- User can sign up using two different roles, educator and learner
- JWT authentication
- Only educator can create and update course
- Only learner can enroll into many courses
