import os
import json
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import yt_dlp
from dotenv import load_dotenv
from flask import Flask, jsonify
from threading import Thread

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

class YoutubeNotifier:
    def __init__(self, channel_url):
        self.webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
        self.channel_url = channel_url
        self.last_video_id = None
        self.last_stream_id = None
        
        # Configure yt-dlp
        self.ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True
        }
        
    def get_channel_info(self):
        """Get channel information using yt-dlp"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(self.channel_url, download=False)
                return info
        except Exception as e:
            print(f"Error getting channel info: {str(e)}")
            return None

    def check_new_content(self):
        """Check for new videos and live streams"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # Get channel info
                info = ydl.extract_info(self.channel_url, download=False)
                
                if 'entries' in info:
                    latest_video = info['entries'][0]
                    video_id = latest_video['id']
                    
                    # Check if it's new content
                    if video_id != self.last_video_id:
                        self.last_video_id = video_id
                        
                        # Check if it's a live stream
                        is_live = latest_video.get('is_live', False)
                        
                        # Send notification
                        self.send_discord_notification(latest_video, is_live)
                        
        except Exception as e:
            print(f"Error checking new content: {str(e)}")

    def send_discord_notification(self, video_data, is_live):
        """Send a beautiful Discord notification"""
        try:
            webhook = DiscordWebhook(url=self.webhook_url)
            
            # Create embed
            embed = DiscordEmbed()
            
            # Set title and color based on content type
            if is_live:
                embed.title = "🔴 بث مباشر جديد من Smoker Q8!"
                embed.color = 'ff0000'  # Red for live streams
            else:
                embed.title = "🎥 فيديو جديد من Smoker Q8!"
                embed.color = '00ff00'  # Green for videos
                
            # Add video details
            embed.add_embed_field(name='العنوان', value=video_data['title'])
            if 'description' in video_data:
                desc = video_data['description']
                if len(desc) > 200:
                    desc = desc[:200] + '...'
                embed.add_embed_field(name='الوصف', value=desc)
            
            # Set thumbnail
            if 'thumbnail' in video_data:
                embed.set_thumbnail(url=video_data['thumbnail'])
            
            # Set video URL
            video_url = f"https://www.youtube.com/watch?v={video_data['id']}"
            embed.url = video_url
            
            # Add footer with timestamp
            embed.set_footer(text='تم النشر في')
            embed.set_timestamp()
            
            # Add embed to webhook
            webhook.add_embed(embed)
            
            # Send notification
            webhook.execute()
            
        except Exception as e:
            print(f"Error sending Discord notification: {str(e)}")

    def run(self, check_interval=300):  # Check every 5 minutes by default
        """Run the notifier"""
        print(f"Starting YouTube notifier for channel: {self.channel_url}")
        print("Checking for new content every 5 minutes...")
        
        while True:
            try:
                self.check_new_content()
                time.sleep(check_interval)
            except Exception as e:
                print(f"Error in main loop: {str(e)}")
                time.sleep(check_interval)

# Flask routes
@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "service": "Smoker Q8 YouTube Notifier",
        "time": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "last_check": datetime.now().isoformat()
    }), 200

def run_flask():
    """Run Flask app"""
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    CHANNEL_URL = "https://www.youtube.com/@smoker_q8"
    
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    
    # Start the notifier
    notifier = YoutubeNotifier(CHANNEL_URL)
    notifier.run()
