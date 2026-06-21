from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_URI)

db = client[settings.MONGO_DB_NAME]

# 🔥 WAJIB ADA INI
activity_collection = db["activity_logs"]
analytics_collection = db["learning_analytics"]