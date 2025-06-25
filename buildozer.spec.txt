[app]

# نام برنامه
title = PHDownloader

# نام فایل main
source.main = main.py

# نام بسته
package.name = phdownloader

# نام کامل بسته (reverse domain)
package.domain = org.example

# آیکن برنامه (اختیاری – اگر نداری همین خط را تغییر نده)
# icon.filename = %(source.dir)s/icon.png

# فهرست فایل‌هایی که در APK گنجانده شوند
source.include_exts = py,png,jpg,kv,atlas

# مجوزهای مورد نیاز
android.permissions = INTERNET

# کتابخانه‌هایی که برنامه نیاز دارد
requirements = python3,kivy,yt_dlp

# پلتفرم‌های مورد نظر برای ساخت
osx.python_version = 3
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a

# پشتیبانی از orientation عمودی
orientation = portrait

# به‌صورت تمام‌صفحه اجرا شود؟
fullscreen = 1

# نمایش نام برنامه
android.entrypoint = org.kivy.android.PythonActivity

# خاموش کردن log در نسخه release
log_level = 2

# برای جلوگیری از اجرا نشدن در اندرویدهای جدید
android.allow_backup = 1

# فعال‌سازی پشتیبانی از ABI‌ها
android.ndk_api = 21

# پشتیبانی از ورودی لمسی
input.keyboard_mode = systemanddock

# کاهش حجم فایل APK
android.strip = true

# فایل خروجی APK در کجا ساخته شود
# bin/PHDownloader-0.1-debug.apk

# نسخه برنامه
version = 0.1

# تنظیمات اضافی اختیاری:
# android.debug = 0
# android.logcat_filters = *:S python:D

# پشتیبانی از پروژه‌های pure-python
p4a.bootstrap = sdl2

# اگر از فایل‌های صوتی یا تصویری استفاده می‌کنی این خط را فعال کن:
# android.add_assets = assets/

# اگر خواستی نسخه release بسازی این خط را تغییر بده:
# buildozer android release

# تنظیماتی برای اجرای سریع‌تر روی شبیه‌ساز:
# android.force_build = 1
