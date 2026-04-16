import os
import django
import time
from django.db import connection, reset_queries

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course

def run_demo():
    print("--- 1. Tanpa Optimasi (N+1 Problem) ---")
    reset_queries()
    courses = Course.objects.all() # Belum di-optimasi
    for c in courses:
        print(f"Course: {c.title} | Instructor: {c.instructor.username}")
    print(f"Total Query: {len(connection.queries)}")

    print("\n--- 2. Dengan Optimasi (select_related) ---")
    reset_queries()
    courses_optimized = Course.objects.for_listing() 
    for c in courses_optimized:
        print(f"Course: {c.title} | Instructor: {c.instructor.username}")
    print(f"Total Query: {len(connection.queries)}")

if __name__ == "__main__":
    run_demo()