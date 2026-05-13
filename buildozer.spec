[app]
title = H2O Pro
package.name = h2opro
package.domain = org.seunome
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.1.1,pyjnius,android

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION
android.api = 33
android.minapi = 21
android.build_tools = 33.0.0
android.accept_sdk_license = True

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
