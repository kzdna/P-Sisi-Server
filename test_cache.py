import time
from weather_api import get_weather

# First call (slow)
start = time.time()
result1 = get_weather("Jakarta")
time1 = time.time() - start
print(f"First call: {time1:.2f}s")

# Second call (fast)
start = time.time()
result2 = get_weather("Jakarta")
time2 = time.time() - start
print(f"Second call (cached): {time2:.2f}s")