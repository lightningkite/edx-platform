"""
Permissions classes for Course Access API endpoint.
"""
from __future__ import unicode_literals

from rest_framework import permissions


class CanCallCheckCourseAccessAPI(permissions.BasePermission):
    """
    Grants access to CheckCourseAccessView if the requesting user has the
    explicit permission to access the API view.
    """
    def has_permission(self, request, view):
        return request.user.has_perm('student.can_call_check_course_access_api')
