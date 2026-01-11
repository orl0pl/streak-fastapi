# streak-api
Failed attempt at making an API for getting streak from Duolingo written with fastapi and deploed on Cloudflare Workers.
Couldn't deploy it so I rewrote it in typescript

This is my first API written in python.

You can find working API repo here:
https://github.com/orl0pl/streak-api

## How to Run

First ensure that `uv` is installed:
https://docs.astral.sh/uv/getting-started/installation/#standalone-installer

Now, if you run `uv run pywrangler dev` within this directory, it should use the config
in `wrangler.jsonc` to run the example.

You can also run `uv run pywrangler deploy` to deploy the example.
