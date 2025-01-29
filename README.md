# YouTube Discord Notifier

بوت يقوم بإرسال إشعارات إلى Discord عندما تقوم قناة Smoker Q8 بنشر فيديو جديد أو بدء بث مباشر.

## المميزات
- 🔔 إشعارات فورية للفيديوهات الجديدة
- 🔴 إشعارات للبث المباشر
- 💎 تصميم جميل للإشعارات في Discord
- ⚡ سهل الإعداد والاستخدام

## المتطلبات
- Python 3.8+
- Discord Webhook URL

## التثبيت

1. قم بنسخ المستودع:
```bash
git clone https://github.com/yourusername/youtube-discord-notifier.git
cd youtube-discord-notifier
```

2. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

3. قم بإنشاء ملف `.env` وأضف Webhook URL الخاص بك:
```
DISCORD_WEBHOOK_URL=your_webhook_url_here
```

## التشغيل
```bash
python youtube_notifier.py
```

## الإعداد في Discord

1. اذهب إلى إعدادات القناة في Discord
2. اختر Integrations -> Webhooks
3. أنشئ webhook جديد
4. انسخ الرابط وضعه في ملف `.env`

## المساهمة
نرحب بمساهماتكم! يرجى إنشاء fork للمشروع وإرسال pull request.
#   s m o o k y - b o t  
 