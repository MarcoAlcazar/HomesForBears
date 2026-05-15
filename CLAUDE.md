# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HomesForBears is a Django 4.2 web application that lets UC Berkeley students browse, search, and submit off-campus housing listings and landlord reviews. Registration is restricted to `@berkeley.edu` email addresses; accounts require email activation before login.

## Common Commands

```bash
# Activate the virtualenv (always do this first)
source virt/bin/activate

# Run the dev server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create and apply new migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Run tests for a single app
python manage.py test myapp
python manage.py test members

# Open the Django shell
python manage.py shell

# Collect static files (for production / Heroku)
python manage.py collectstatic
```

The Procfile runs `gunicorn myproj.wsgi` for production (Heroku).

## Architecture

### Django apps

| App | Purpose |
|-----|---------|
| `myapp` | Core housing & landlord data: models, views, forms, URLs |
| `members` | Authentication: register, login, logout, email activation, profile edit, password reset |

Project config lives in `myproj/` (`settings.py`, root `urls.py`).

### URL routing

`myproj/urls.py` wires three prefixes:
- `''` → `myapp.urls` (main housing/landlord routes)
- `members/` → `members.urls` (auth routes)
- `members/` → `django.contrib.auth.urls` (built-in password-reset views)

### Data models (`myapp/models.py`)

- **`Landlord`** — `FullName`, `Rating` (1–5), `Description`
- **`Housing`** — `address`, `Bedrooms`, `Bathrooms`, `Description`, `Rating`, `Price`, `LandLord` (FK to Landlord), up to 5 image fields (`housing_image` … `housing_image5`)

`Housing.save()` resizes uploaded images via Pillow and mirrors both housing and landlord data as JSON blobs to S3 (`homesforbears` bucket, `housing/` and `landlord/` prefixes).

### Authentication flow (`members/`)

1. User registers via `RegisterUserForm` (validates `@berkeley.edu` email).
2. Account is saved with `is_active=False`; `activateEmail()` sends a tokenised activation link via Gmail SMTP.
3. Clicking the link calls `activate()`, which verifies the token and sets `is_active=True`.
4. Token generation is in `members/tokens.py` (`AccountActivationTokenGenerator`).

### Storage

In production `DEFAULT_FILE_STORAGE` is `S3Boto3Storage` (media files go to the `homesforbears` S3 bucket). Static files are served via **WhiteNoise** (`CompressedManifestStaticFilesStorage`). Locally, `MEDIA_ROOT` is the `media/` directory at the project root.

### Templates

Templates live inside each app under `<app>/templates/<app>/`. Authentication templates are in `members/templates/authenticate/`. The shared nav partial is `myapp/templates/myapp/nav.html`.

## Known Issues / Gotchas

- AWS credentials are hard-coded in `myapp/models.py` and `members/views.py` (and also in `myproj/settings.py`). These should be moved to environment variables / `.env`.
- `myproj/` contains a duplicate nested copy of the app tree (its own `manage.py`, `settings.py`, templates, etc.). The active project root is the top-level directory, not `myproj/`.
- `Housing` model fields use inconsistent casing (`Address` vs `address`, `LandLord` vs `landLord`) between the model definition and the form — be careful when adding fields.
- `DEBUG = True` and `ALLOWED_HOSTS = []` are the current settings; change both before any public deployment.
