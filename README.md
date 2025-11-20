# discord_content_updates_bot# TikTok Monitor Bot for Discord

Monitors @investingwithjeremy on TikTok and sends notifications to Discord when new posts are detected.

## Features

- 🎵 Monitors TikTok account for new posts
- 📢 Sends Discord notifications via webhook
- ⏰ Runs automatically every 5 minutes
- 🔄 Tracks last seen post to avoid duplicates

## Setup

### Option 1: Run Locally

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the monitor:**
   ```bash
   python tiktok_monitor.py
   ```

   The bot will check every 5 minutes for new posts.

### Option 2: GitHub Actions (Automated)

1. **Create a new GitHub repository**

2. **Upload these files to your repo:**
   - `tiktok_monitor.py`
   - `requirements.txt`
   - `monitor.yml` (place in `.github/workflows/` directory)

3. **Add your Discord webhook as a secret:**
   - Go to your repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `DISCORD_WEBHOOK_URL`
   - Value: `https://discord.com/api/webhooks/1440919493298618538/9nHrnR807FuiCdzbDkKbDz9qzZNRAW6wW78x9pE9FB71-5H9keHUJWdzNZWYYniUJI-k`

4. **Enable GitHub Actions:**
   - Go to the Actions tab
   - Enable workflows if prompted

The bot will now run automatically every 5 minutes!

## Configuration

Edit `tiktok_monitor.py` to customize:

- `TIKTOK_USERNAME`: The TikTok account to monitor
- `CHECK_INTERVAL`: How often to check (in seconds)
- `DISCORD_WEBHOOK_URL`: Your Discord webhook URL

## Important Notes

### TikTok API Limitation

⚠️ **This is a basic implementation.** TikTok doesn't have an official public API for fetching user posts easily. For a production-ready bot, you have a few options:

1. **Use a third-party TikTok API service:**
   - [RapidAPI TikTok APIs](https://rapidapi.com/hub?search=tiktok)
   - [Apify TikTok Scraper](https://apify.com/clockworks/tiktok-scraper)

2. **Use TikTok's Official Business API:**
   - Requires approval from TikTok
   - Best for legitimate commercial use

3. **Web scraping approach:**
   - More complex but free
   - May need to handle anti-scraping measures

### Recommended: Using RapidAPI

Here's how to integrate a TikTok API from RapidAPI:

```python
# Install rapidapi-connect
# pip install requests

def get_latest_tiktok_post(username):
    url = "https://tiktok-api.p.rapidapi.com/user/posts"
    
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "tiktok-api.p.rapidapi.com"
    }
    
    querystring = {"username": username}
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    # Extract latest post
    if data['posts']:
        latest = data['posts'][0]
        return {
            'success': True,
            'post_id': latest['id'],
            'url': f"https://www.tiktok.com/@{username}/video/{latest['id']}",
            'description': latest.get('desc', ''),
            'timestamp': datetime.now().isoformat()
        }
```

## Testing

To test the Discord webhook:

```bash
curl -X POST "https://discord.com/api/webhooks/1440919493298618538/9nHrnR807FuiCdzbDkKbDz9qzZNRAW6wW78x9pE9FB71-5H9keHUJWdzNZWYYniUJI-k" \
  -H "Content-Type: application/json" \
  -d '{"content": "Test notification from TikTok Monitor!"}'
```

## File Structure

```
.
├── .github/
│   └── workflows/
│       └── monitor.yml          # GitHub Actions workflow
├── tiktok_monitor.py            # Main monitoring script
├── requirements.txt              # Python dependencies
├── last_post_id.txt             # Tracks last seen post (auto-generated)
└── README.md                    # This file
```

## Troubleshooting

### Bot not sending notifications

1. Check your Discord webhook URL is correct
2. Verify the webhook hasn't been deleted in Discord
3. Check GitHub Actions logs for errors

### How to get your Discord Webhook URL

1. Open Discord and go to your server
2. Right-click the channel → Edit Channel → Integrations
3. Click "Create Webhook" or edit an existing one
4. Copy the Webhook URL

## License

MIT License - Feel free to modify and use as needed!