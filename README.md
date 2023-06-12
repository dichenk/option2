Aim: Develop an application in which users can write posts and comment on them. 
Create models and appropriate API points to interact with them.

Specifications:
- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

Task 1:
MODELS 
**User**
- username
- password
- number
- date of birth
- creation date
- edit date
**Post**
- headline
- text
- image (if any)
- author
- comments
- creation date
- edit date
**Comment**
- author
- text
- creation date
- edit date

Task 2
Implement CRUD for each model.
ENDPOINTS
**User**
- create: all users (register)
- read: administrator/authorised users
- update: admin/user can only edit themselves
- delete: admin
**Post**
- create: authorised users
- read: all users
- update: admin/user can only edit themselves
- delete: administrator/user can delete their own posts
**Comment**
- create: authorised users
- read: all users
- update: admin/user can only edit themselves
- delete: administrator/user can delete their comments

Task 3
VALIDATORS
**User model**.
- Implement a validator for the password (must be at least 8 characters, must include digits)
- Implement a validator for mail (domains allowed: mail.ru, yandex.ru)
**Model post**.
- Implement a check that the author of a post is at least 18 years old
- Implement a check that the author has not put illegal words in the title: nonsense, nonsense, nonsense

Task 4
ADMIN'S PANEL
- Add a link to the author in the post object.
- Add a filter based on the date the post was created.