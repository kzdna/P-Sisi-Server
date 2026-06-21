import requests
import time
import redis
import json

# koneksi ke Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def get_weather(city):
    cache_key = f"weather:{city}"

    # 🔍 CEK CACHE
    cached_data = r.get(cache_key)
    if cached_data:
        print("✅ Ambil dari CACHE")
        return json.loads(cached_data)

    # ❌ kalau tidak ada → call API
    print("❌ Ambil dari API (slow)")
    time.sleep(2)  # simulasi delay API

    # dummy response (karena api.example.com gak real)
    data = {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }

    # 💾 SIMPAN KE REDIS (EXPIRE 5 MENIT)
    r.setex(cache_key, 300, json.dumps(data))

    return data