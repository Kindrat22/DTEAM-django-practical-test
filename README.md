
## 📦 Loading Sample Data (Fixtures)

To load the sample CV data into your database, run the following command from your project root:

```
python manage.py loaddata main/fixtures/sample_cv.json
```

This will create at least one sample CV instance in your database for testing and development.

## 🧪 Running Tests

To run the tests for the CV list and detail views, use:

```
python manage.py test main
```

This will execute the basic tests for your views and ensure everything is working as expected.

## ✅ Final Notes

- Complete **each task thoroughly**
- Follow the **branch-and-merge** workflow
- Ensure `README.md` includes instructions on how to:
  - Install the project
  - Run the project
  - Run tests

We look forward to reviewing your submission.  
**Thank you!**

---

## 🚀 Deployment

To deploy this Django project:

1. Set up your production environment (VPS, DigitalOcean, etc.)
2. Clone your repository and install Python dependencies:
   ```sh
   poetry install
   ```
3. Set up your environment variables and database (see Docker/PostgreSQL instructions if needed).
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Collect static files:
   ```sh
   python manage.py collectstatic
   ```
6. Create a superuser (optional):
   ```sh
   python manage.py createsuperuser
   ```
7. Start the Django server (or configure with Gunicorn, uWSGI, etc.):
   ```sh
   python manage.py runserver 0.0.0.0:8000
   ```

---

## ⚠️ WeasyPrint on Windows

If you see an error like:

> This error means WeasyPrint (and its dependency Cairo) cannot find the required GTK or GObject libraries on your Windows system. This is a common issue when using WeasyPrint on Windows.

**Solution:**
- Download and install the GTK3 runtime for Windows from:
  https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
- Add the GTK3 `bin` directory (e.g., `C:\Program Files\GTK3-Runtime Win64\bin`) to your system `PATH`.
- Restart your terminal and try again.

If you want a pure-Python solution, consider using `xhtml2pdf` or `Pyppeteer` instead.
