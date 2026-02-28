# asap-project-test-0

Django web app prototype (Heroku-style structure) for generating and validating member IDs.

## Overview

This project starts from the Heroku Python starter template and adds custom member flows:

- create a member record and generated `member_id`
- validate whether a member ID exists
- basic HTML pages for submit/lookup results

## Stack

- Python + Django
- Gunicorn (deployment)
- `django-heroku` integration
- `django-cors-headers`

## Key App Modules

- `hello/models.py`
  - `Members` model (member_id, first/last name, country, date_of_birth)
  - `Greeting` model from starter template
- `hello/views.py`
  - `member_id` endpoint to create a member and return JSON
  - `validate_member_id` endpoint to check member existence and render result page
  - `validate_member_id_html` simple form page
- `hello/helpers.py`
  - `generate_id(first_name, last_name)` helper

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Main Flows

- Create member (POST fields expected):
  - `first_name`
  - `last_name`
  - `dob`
  - `country`
- Validate member (POST):
  - `member_id`

## Notes / Current Limitations

- CSRF is disabled on key endpoints via `@csrf_exempt`
- `generate_id` is random and can collide (helper check function is not fully wired)
- `helpers.py` references `Member` (singular) in `check_id`, while model is `Members`
- Existing README content was generic Heroku starter text

## Suggested Improvements

- enforce unique member ID generation loop with DB check
- add serializer/schema validation for inputs
- enable CSRF protection for browser form flows
- add API tests for create/validate endpoints
- document URL routes explicitly in README
