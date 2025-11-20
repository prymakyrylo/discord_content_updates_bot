import requests
from datetime import datetime
import sys

# Your Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1440919493298618538/9nHrnR807FuiCdzbDkKbDz9qzZNRAW6wW78x9pE9FB71-5H9keHUJWdzNZWYYniUJI-k"

def test_discord_webhook():
    """
    Test the Discord webhook connection
    """
    print("🧪 Testing Discord Webhook Connection...")
    print("-" * 50)
    
    try:
        # Create a test embed
        embed = {
            "title": "✅ TikTok Monitor Test",
            "description": "If you're seeing this, your Discord webhook is working correctly!",
            "color": 0x00f2ea,  # TikTok cyan color
            "fields": [
                {
                    "name": "Monitoring",
                    "value": "@investingwithjeremy",
                    "inline": True
                },
                {
                    "name": "Status",
                    "value": "✅ Connected",
                    "inline": True
                }
            ],
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {
                "text": "TikTok Monitor - Test Message"
            }
        }
        
        payload = {
            "content": "🎉 **Bot Test Notification**",
            "embeds": [embed],
            "username": "TikTok Monitor"
        }
        
        print("📤 Sending test message to Discord...")
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 204:
            print("✅ SUCCESS! Check your Discord channel for the test message.")
            print("\n📱 Your webhook is configured correctly!")
            return True
        else:
            print(f"❌ FAILED! Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_simple_message():
    """
    Send a simple text message to Discord
    """
    print("\n🧪 Testing Simple Message...")
    print("-" * 50)
    
    try:
        payload = {
            "content": "🔔 Simple test message from TikTok Monitor bot!"
        }
        
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 204:
            print("✅ Simple message sent successfully!")
            return True
        else:
            print(f"❌ Failed to send simple message: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_imports():
    """
    Check if all required libraries can be imported
    """
    print("\n🧪 Testing Python Dependencies...")
    print("-" * 50)
    
    libraries = {
        'requests': 'requests',
        'json': 'json (built-in)',
        'time': 'time (built-in)',
        'datetime': 'datetime (built-in)',
        'os': 'os (built-in)'
    }
    
    all_good = True
    for lib, display_name in libraries.items():
        try:
            __import__(lib)
            print(f"✅ {display_name}")
        except ImportError:
            print(f"❌ {display_name} - NOT INSTALLED")
            all_good = False
    
    return all_good

def main():
    print("=" * 50)
    print("  TIKTOK MONITOR - TEST SUITE")
    print("=" * 50)
    
    # Test 1: Check dependencies
    deps_ok = test_imports()
    
    # Test 2: Test Discord webhook with embed
    webhook_ok = test_discord_webhook()
    
    # Test 3: Test simple message
    simple_ok = test_simple_message()
    
    # Summary
    print("\n" + "=" * 50)
    print("  TEST SUMMARY")
    print("=" * 50)
    print(f"Dependencies:     {'✅ PASS' if deps_ok else '❌ FAIL'}")
    print(f"Discord Webhook:  {'✅ PASS' if webhook_ok else '❌ FAIL'}")
    print(f"Simple Message:   {'✅ PASS' if simple_ok else '❌ FAIL'}")
    print("=" * 50)
    
    if all([deps_ok, webhook_ok, simple_ok]):
        print("\n🎉 All tests passed! Your bot is ready to run.")
        print("\nNext steps:")
        print("1. Run: python tiktok_monitor.py")
        print("2. The bot will check @investingwithjeremy every 5 minutes")
        print("3. You'll get Discord notifications for new posts")
        return 0
    else:
        print("\n⚠️ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())