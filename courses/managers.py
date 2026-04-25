from django.db import models

class CourseQuerySet(models.QuerySet):
    def public(self):
        # Bisa ditambah filter (misal: is_published=True) di masa depan
        return self.all()

class EnrollmentQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)