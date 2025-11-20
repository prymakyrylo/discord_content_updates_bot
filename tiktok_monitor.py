import requests
import json
import time
from datetime import datetime
import os

# Configuration
TIKTOK_USERNAME = "investingwithjeremy"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1440919493298618538/9nHrnR807FuiCdzbDkKbDz9qzZNRAW6wW78x9pE9FB71-5H9keHUJWdzNZWYYniUJI-k"
CHECK_INTERVAL = 300  # Check every 5 minutes (in seconds)
LAST_POST_FILE = "last_post_id.txt"

def get_latest_tiktok_post(username):
    """
    Fetch the latest TikTok post from the user
    Using TikTok's public API endpoint
    """
    try:
        # TikTok API endpoint (you may need to adjust based on available APIs)
        # This is a simplified version - you might need to use a third-party API
        url = f"https://www.tiktok.com/@{username}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        # Note: This is a basic implementation
        # For production, you'd want to use TikTok's official API or a scraping service
        # This example shows the structure - you'll need to implement actual parsing
        
        return {
            'success': True,
            'post_id': None,  # Would extract from response
            'url': url,
            'timestamp': datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"Error fetching TikTok data: {e}")
        return {'success': False, 'error': str(e)}

def send_discord_notification(post_data):
    """
    Send notification to Discord webhook
    """
    try:
        embed = {
            "title": f"🎵 New TikTok from @{TIKTOK_USERNAME}!",
            "description": f"[@{TIKTOK_USERNAME}](https://www.tiktok.com/@{TIKTOK_USERNAME}) just posted!",
            "color": 0x00f2ea,  # TikTok's brand color
            "url": f"https://www.tiktok.com/@{TIKTOK_USERNAME}",
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {
                "text": "TikTok Monitor"
            },
            "thumbnail": {
                "url": "https://sf-tb-sg.ibytedtos.com/obj/eden-sg/uhtyvueh7nulogqoxo/tiktok-icon2.png"
            }
        }
        
        payload = {
            "embeds": [embed],
            "username": "TikTok Monitor",
        }
        
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 204:
            print(f"✅ Discord notification sent successfully!")
            return True
        else:
            print(f"❌ Failed to send Discord notification: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error sending Discord notification: {e}")
        return False

def load_last_post_id():
    """
    Load the last known post ID from file
    """
    if os.path.exists(LAST_POST_FILE):
        with open(LAST_POST_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_last_post_id(post_id):
    """
    Save the current post ID to file
    """
    with open(LAST_POST_FILE, 'w') as f:
        f.write(str(post_id))

def monitor_tiktok():
    """
    Main monitoring loop
    """
    print(f"🚀 Starting TikTok monitor for @{TIKTOK_USERNAME}")
    print(f"⏰ Checking every {CHECK_INTERVAL} seconds")
    print(f"📡 Discord webhook configured")
    print("-" * 50)
    
    last_post_id = load_last_post_id()
    
    while True:
        try:
            print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking for new posts...")
            
            # Get latest post
            post_data = get_latest_tiktok_post(TIKTOK_USERNAME)
            
            if post_data['success']:
                current_post_id = post_data.get('post_id')
                
                # Check if this is a new post
                if current_post_id and current_post_id != last_post_id:
                    print(f"🎉 New post detected! ID: {current_post_id}")
                    
                    # Send Discord notification
                    if send_discord_notification(post_data):
                        save_last_post_id(current_post_id)
                        last_post_id = current_post_id
                else:
                    print("✓ No new posts")
            else:
                print(f"⚠️ Error checking TikTok: {post_data.get('error')}")
            
            # Wait before next check
            print(f"⏳ Waiting {CHECK_INTERVAL} seconds until next check...")
            time.sleep(CHECK_INTERVAL)
            
        except KeyboardInterrupt:
            print("\n\n👋 Stopping TikTok monitor...")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print(f"⏳ Waiting {CHECK_INTERVAL} seconds before retry...")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_tiktok()