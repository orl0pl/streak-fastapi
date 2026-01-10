# streak-api
API for getting streak from Duolingo written with fastapi and deploed on Cloudflare Workers.

This is my first API written in python.

## Development
- Have Python 3.14 installed
- Create venv by running `uv venv`
- Install depedencies by running `uv pip install requests fastapi pydantic`
- Run `uvicorn main:app --reload --host 0.0.0.0 --port 8000` to start development server
