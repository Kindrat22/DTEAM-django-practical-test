# DTEAM - Django Developer Practical Test

Welcome!  
This test will help us see how you structure a Django project, work with various tools, and handle common tasks in web development. Follow the instructions step by step. Good luck!

---

## 🧾 Requirements

- Follow PEP 8 and other style guidelines  
- Use clear and concise commit messages and docstrings where needed  
- Structure your project for readability and maintainability  
- Optimize database access using Django’s built-in methods  
- Provide enough details in your `README.md`

---

## 🗂 Version Control System

1. Create a public GitHub repository for this practical test (e.g. `DTEAM-django-practical-test`)
2. Put the **entire text of this test** (all instructions) into `README.md`
3. For each task, create a **separate branch**, e.g.:
   - `tasks/task-1`
   - `tasks/task-2`
   - ...
4. After completing each task:
   - Merge the task branch back into `main`
   - **Do not delete** the original task branch

---

## 🐍 Python Virtual Environment

1. Use **pyenv** to manage the Python version
   - Create a `.python-version` file in the repo to store the exact version
2. Use **Poetry** to manage dependencies
   - This will generate a `pyproject.toml` file
3. Update your `README.md` with clear setup instructions for pyenv and Poetry

---

## ✅ Tasks

### 🧱 Task 1: Django Fundamentals

1. **Create a New Django Project**
   - Name it something like `CVProject`
   - Use the Python version from Task 2
   - Use the latest stable Django release
   - Use **SQLite** for now

2. **Create an App and Model**
   - Create a Django app (e.g. `main`)
   - Define a `CV` model with fields like: `firstname`, `lastname`, `skills`, `projects`, `bio`, `contacts`
   - Organize the data efficiently and logically

3. **Load Initial Data with Fixtures**
   - Create a fixture with at least one sample CV instance
   - Include instructions in `README.md` on how to load it

4. **List Page View and Template**
   - Implement a view for `/` that displays a list of CV entries
   - Use any CSS library for styling
   - Ensure efficient database access

5. **Detail Page View**
   - Implement a view for `/cv/<id>/` to show all data for a single CV
   - Style it nicely and ensure performance

6. **Tests**
   - Add basic tests for list and detail views
   - Include test instructions in `README.md`

---

### 🖨 Task 2: PDF Generation Basics

1. Choose and install an HTML-to-PDF library/tool  
2. Add a **“Download PDF”** button on the CV detail page

---

### 🌐 Task 3: REST API Fundamentals

1. Install **Django REST Framework (DRF)**  
2. Create **CRUD endpoints** for the CV model  
3. Add tests for each endpoint

---

### 🧩 Task 4: Middleware & Request Logging

1. **Create a `RequestLog` model**
   - In existing or new app (e.g. `audit`)
   - Include fields: `timestamp`, `method`, `path`, `query_string`, `remote_ip`, `user` (optional)

2. **Implement Logging Middleware**
   - Create a custom middleware to log each request
   - Save logs to the database

3. **Recent Requests Page**
   - Create a view `/logs/` showing the 10 most recent logs
   - Display `timestamp`, `method`, `path`

4. **Test Logging**
   - Add tests to verify the middleware

---

### 🧠 Task 5: Template Context Processors

1. Create a `settings_context` processor  
   - Inject the Django settings into all templates

2. Create a `/settings/` page  
   - Display `DEBUG` and other values from context

---

### 🐳 Task 6: Docker Basics

1. Use **Docker Compose** to containerize the project  
2. Switch from **SQLite** to **PostgreSQL**  
3. Store all secrets (e.g. DB credentials) in a `.env` file

---

### 🔁 Task 7: Celery Basics

1. Install and configure **Celery**  
   - Use **Redis** or **RabbitMQ** as a broker  
2. Add a Celery worker in Docker Compose  
3. On the CV detail page:
   - Add an email input field
   - Add a **“Send PDF to Email”** button  
   - Trigger a Celery task that emails the CV PDF

---

### 🌍 Task 8: OpenAI Basics

1. On the CV detail page, add a **“Translate”** button and a language selector  
2. Include these languages:

   > Cornish, Manx, Breton, Inuktitut, Kalaallisut, Romani, Occitan, Ladino, Northern Sami,  
   > Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama

3. Connect to OpenAI API or other service to perform translation

---

### 🚀 Task 9: Deployment

Deploy the project to **DigitalOcean** or any VPS.  
If needed, use this referral link to get $200 in credits:  
[https://m.do.co/c/967939ea1e74](https://m.do.co/c/967939ea1e74)

---

## ✅ Final Notes

- Complete **each task thoroughly**
- Follow the **branch-and-merge** workflow
- Ensure `README.md` includes instructions on how to:
  - Install the project
  - Run the project
  - Run tests

We look forward to reviewing your submission.  
**Thank you!**
