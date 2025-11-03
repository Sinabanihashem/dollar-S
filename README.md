# 💸 SinaDollar – Python Client

یک اسکریپت پایتون ساده و زیبا برای دریافت **قیمت لحظه‌ای دلار آزاد** از وب‌سرویس [SinaDollar API](https://dollar.api-sina-free.workers.dev/dollar) 🇮🇷

---

## 🚀 ویژگی‌ها

- واکشی سریع قیمت دلار از **tgju.org**  
- نمایش خروجی با استایل رنگی (کتابخانه [`rich`](https://pypi.org/project/rich/))  
- مدیریت خطاهای اتصال و پاسخ سرور  
- مناسب برای پروژه‌های مالی، ربات‌ها و اپ‌های اطلاع‌رسانی  

---

## ⚙️ نصب

ابتدا پیش‌نیازها را نصب کنید:

```bash```
```pip install requests rich```


---

## 🧠 استفاده

فایل را اجرا کنید:

```python sina_dollar.py```

نمونه خروجی:

┌──────────────────────────────┐
│      💸 قیمت لحظه‌ای دلار آزاد      │
├──────────────┬──────────────────────┤
│ 💰 قیمت به تومان │ 107,640 تومان 🇮🇷      │
│ 💵 قیمت به ریال │ 1,076,400 ریال         │
│ ⏰ آخرین بروزرسانی │ 2025-11-03 10:29:37     │
│ 🌐 منبع         │ tgju.org                 │
│ 👤 توسعه‌دهنده   │ @Sinabani_api            │
└──────────────────────────────┘


---

## API Info

Endpoint:

https://dollar.api-sina-free.workers.dev/dollar

Method: GET
Response Type: JSON
Source: tgju.org


---

## 👨‍💻 Developer

Created by (Rubika): @Sinabani_api
Hosted on: Cloudflare Workers
Python Script Author: [You 😉]
