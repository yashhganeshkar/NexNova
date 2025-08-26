# FirstBit Institute – Trainer & Subject Management System

## What This Is
A web-based solution built with Django for managing trainers and subjects at your institute. It shows lists on a dashboard where you can easily view details, add new entries, or remove old ones. It includes a secure admin interface and is designed to be extended later—think linking trainers to subjects or generating reports.

## Why It Matters
This makes managing your institute’s trainers and subjects smooth and organized. No manual work or spreadsheets needed—everything is secure and accessible online.

## How to Use It

1. Clone the repository.
2. Set up Python environment:
    bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    
3. Prepare the database:
    bash
    python manage.py migrate
    python manage.py createsuperuser
    
4. Start the server:
    bash
    python manage.py runserver
    
5. Open your browser at http://127.0.0.1:8000.
6. Use the dashboard or Django’s admin interface to manage trainers and subjects.

## What’s Included

- Clean lists of trainers and subjects with buttons to *Add, **View Details, and **Remove*
- Django-powered admin area for backend control
- Simple design that looks good on any device
- Ready for future improvements like report generation or trainer–subject linking

## How to Run Tests
Run all tests using:
```bash
python manage.py test
