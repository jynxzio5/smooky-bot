# Smoker Q8 YouTube Notifier

بوت يقوم بإرسال إشعارات إلى Discord عندما تقوم قناة Smoker Q8 بنشر فيديو جديد أو بدء بث مباشر.

## المميزات
- 🔔 إشعارات فورية للفيديوهات الجديدة
- 🔴 إشعارات للبث المباشر
- 💎 تصميم جميل للإشعارات في Discord
- ⚡ سهل الإعداد والاستخدام
- 🚂 يدعم النشر على Railway

## المتطلبات
- Python 3.8+
- Discord Webhook URL

## التثبيت المحلي

1. قم بنسخ المستودع:
```bash
git clone https://github.com/yourusername/smooky-bot.git
cd smooky-bot
```

2. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

3. قم بإنشاء ملف `.env` وأضف Webhook URL الخاص بك:
```
DISCORD_WEBHOOK_URL=your_webhook_url_here
```

## النشر على Railway

1. قم بربط حسابك على Railway بحساب GitHub
2. قم بإنشاء مشروع جديد واختر هذا المستودع
3. أضف متغير البيئة التالي:
   - `DISCORD_WEBHOOK_URL`: رابط الwebhook الخاص بقناة Discord

البوت سيبدأ العمل تلقائياً على Railway!

## الإعداد في Discord

1. اذهب إلى إعدادات القناة في Discord
2. اختر Integrations -> Webhooks
3. أنشئ webhook جديد
4. انسخ الرابط وأضفه كمتغير بيئة

## المراقبة والصيانة

- يمكنك مراقبة حالة البوت من خلال النقطة النهائية `/health`
- البوت سيعيد تشغيل نفسه تلقائياً في حالة حدوث أي خطأ
- يتم فحص القناة كل 5 دقائق للتحقق من وجود محتوى جديد

## المساهمة
نرحب بمساهماتكم! يرجى إنشاء fork للمشروع وإرسال pull request.