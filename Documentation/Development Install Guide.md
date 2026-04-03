# Development Install Guide

### Setup

1. Create a virtual environment:
```Shell
python -m venv .venv
```

2. Activate `venv`:
```Shell
.\.venv\Scripts\activate
```

3. Install dependencies:
```Shell
pip install -r "dev-requirements.txt"
```

---

### Running Tests

To run tests use the following command:
```Shell
pytest -v
```