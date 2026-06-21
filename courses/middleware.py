from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("🔥 RATE LIMIT MIDDLEWARE JALAN")

        ip = self.get_client_ip(request)
        key = f"rate_limit:{ip}"

        requests = cache.get(key)

        print(f"IP: {ip}")
        print(f"REQUEST COUNT: {requests}")

        if requests is None:
            print("➡️ REQUEST PERTAMA (SET = 1)")
            cache.set(key, 1, timeout=60)
        else:
            if requests >= 60:  
                print("⛔ LIMIT KENA")
                return JsonResponse(
                    {"error": "Too many requests (limit 60/minute)"},
                    status=429
                )
            print("➕ TAMBAH COUNTER")
            cache.incr(key)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')