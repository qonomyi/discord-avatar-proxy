# Discord-Avatar-Proxy
Get discord avatar by user id

## Host
Write config.py:
```python
token = "DISCORD_BOT_TOKEN"
port = 8000
host = "0.0.0.0
```

And run it
```bash
$ uv sync # if you not using uv: `pip -r requirements.txt`
$ python main.py
```

## Usage
GET Request to `http://host:port/{user_id}`, redirect to avatar.
If user's avatar is not set, redirect to default avatar.
Also can be used with options: `http://host:port/{user_id}.{ext}?size={size}`

If you lazy to host it: https://dap.donotsolve.me
