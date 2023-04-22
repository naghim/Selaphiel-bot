# Selaphiel-bot

The Messenger Archangel

# How to run:

First, install dependencies:

```bash
python -m pip install -r requirements.txt
```

Then, create a `settings.json` configuration file:

```json
{
    "twitter": {
        "api_key": "",
        "api_secret": "",
        "access_token": "",
        "access_secret": ""
    },
    "discord": {
        "token": "",
        "channel_ids": [111111111111111111]
    }
}
```

Finally, start the application:

```bash
python -m selaphiel.main
```
