![Build Status](https://github.com/Codewithnavy/dummy-branch-app/actions/workflows/pipeline.yml/badge.svg)

# Branch Loan API

curl http://localhost:8000/api/loans
```

## Configuration

See `.env.example` for env vars. By default:
- `DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/microloans`
- API listens on `localhost:8000`.

## API

- GET `/health` → `{ "status": "ok" }`
- GET `/api/loans` → list all loans
- GET `/api/loans/:id` → get loan by id
- POST `/api/loans` → create loan (status defaults to `pending`)

Example create:
```bash
curl -X POST http://localhost:8000/api/loans \
  -H 'Content-Type: application/json' \
  -d '{
    "borrower_id": "usr_india_999",
    "amount": 12000.50,
    "currency": "INR",
    "term_months": 6,
    "interest_rate_apr": 24.0
  }'
```

- GET `/api/stats` → aggregate stats: totals, avg, grouped by status/currency.

## Development

- App entrypoint: `wsgi.py` (`wsgi:app`)
- Flask app factory: `app/__init__.py`
- Models: `app/models.py`
- Migrations: `alembic/`

## DevOps Setup

### Local Development
1. **Prerequisites**: Docker and Docker Compose installed.
2. **Start the application**:
   ```bash
   docker-compose up --build
   ```
   The API will be available at `http://localhost:8000`.
   The source code is mounted into the container, so changes will trigger a reload.

### Running Tests
To run tests locally (requires Python environment):
```bash
pip install -r requirements.txt
pytest
flake8
```

### CI/CD Pipeline
The GitHub Actions pipeline (`.github/workflows/pipeline.yml`) performs the following:
1. **Test**: Runs `pytest` and `flake8`.
2. **Build**: Builds the Docker image, scans for vulnerabilities using Trivy, and pushes to Docker Hub (on push to main).

## Notes

- Amounts are validated server-side (0 < amount ≤ 50000).
- No authentication for this prototype.