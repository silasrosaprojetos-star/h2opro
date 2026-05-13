[app]
title = H2O Pro
package.name = h2opro
package.domain = org.seunome
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0

# Forçamos o Python 3.11 para evitar a versão 3.14 de testes (que causou o erro no compilador C)
requirements = python3,kivy==2.3.0,kivymd==1.1.1

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION
android.api = 33
android.minapi = 21
android.build_tools = 33.0.0
android.accept_sdk_license = True
p4a.branch = stable
android.archs = arm64-v8a, armeabi-v7a

# Definimos as arquiteturas de processador e fixamos o NDK 25b (versões mais novas como a r28c quebram o Cython)
android.archs = arm64-v8a, armeabi-v7a
android.ndk = 25b

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
