from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache

from .models import Course, Enrollment, Progress, Lesson
from .serializers import (
    CourseSerializer, UserSerializer, 
    EnrollmentSerializer, ProgressSerializer
)

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'instructor'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'instructor']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser] 
        else:
            permission_classes = [IsInstructorOrReadOnly] 
        return [permission() for permission in permission_classes]

    # =========================
    # 🔥 CACHE: COURSE LIST
    # =========================
    def list(self, request, *args, **kwargs):
        cache_key = "course_list"

        data = cache.get(cache_key)
        if data:
            return Response(data)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        cache.set(cache_key, serializer.data, timeout=60*5)

        return Response(serializer.data)

    # =========================
    # 🔥 CACHE: COURSE DETAIL
    # =========================
    def retrieve(self, request, *args, **kwargs):
        course_id = kwargs.get("pk")
        cache_key = f"course_{course_id}"

        data = cache.get(cache_key)
        if data:
            return Response(data)

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        cache.set(cache_key, serializer.data, timeout=60*5)

        return Response(serializer.data)

    # =========================
    # 🔥 CACHE INVALIDATION
    # =========================
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)
        cache.delete("course_list")

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete("course_list")
        cache.delete(f"course_{instance.id}")

    def perform_destroy(self, instance):
        cache.delete("course_list")
        cache.delete(f"course_{instance.id}")
        instance.delete()


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def progress(self, request, pk=None):
        enrollment = self.get_object()
        lesson_id = request.data.get('lesson_id')
        
        try:
            lesson = Lesson.objects.get(id=lesson_id, course=enrollment.course)
            progress, created = Progress.objects.get_or_create(
                enrollment=enrollment, 
                lesson=lesson
            )
            progress.is_completed = True
            progress.save()
            return Response({'status': 'progress updated'}, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response({'error': 'Lesson not found in this course'}, status=status.HTTP_404_NOT_FOUND)