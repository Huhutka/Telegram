[app]
# Имя приложения
title = Telegram Local Proxy

# Уникальный идентификатор
package.name = telegramproxy
package.domain = org.example

# Исходный файл
source.dir = .
source.include_exts = py,png,jpg,kv,atxt

# Версия
version = 1.0

# Требования
requirements = python3,kivy,openssl

# Ориентация
orientation = portrait

# Разрешения
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# Настройки
android.arch = arm64-v8a
android.allow_backup = True

# Режим отладки
android.debug = True

[buildozer]
log_level = 2
warn_on_root = 1