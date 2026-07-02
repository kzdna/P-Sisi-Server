from .mongo import activity_collection
import datetime


class MongoActivityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print("🔥 MONGO MIDDLEWARE JALAN")

        response = self.get_response(request)

        try:

            activity_collection.insert_one({

                "path": request.path,
                "method": request.method,
                "user": str(request.user)
                if request.user.is_authenticated
                else "anonymous",

                "timestamp": datetime.datetime.utcnow(),

            })

            print("✅ INSERT BERHASIL")

        except Exception as e:

            print("❌ Mongo Error:", e)

        return response