# The Minions — Django Band Site

## Run (venv)
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Run (Docker)
docker build -t minions .
docker run -p 8000:8000 minions

### Notes
- Don’t commit secrets. Keep them in a local `.env` (ignored by `.gitignore`).
- `requirements.txt` is generated from the venv.
- User docs are in `./docs` (open `docs/index.html`).
