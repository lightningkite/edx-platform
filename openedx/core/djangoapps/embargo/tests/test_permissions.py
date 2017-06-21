from django.test import TestCase, RequestFactory

from openedx.core.djangoapps.embargo.permissions import CanCallCheckCourseAccessAPI
from student.tests.factories import ContentTypeFactory, PermissionFactory, UserFactory


class CanCallCheckCourseAccessAPITest(TestCase):
    """ Tests for user permissions to call the check course access API. """
    def setUp(self):
        super(CanCallCheckCourseAccessAPITest, self).setUp()
        self.request = RequestFactory().get('/test/url')

    def test_user_permission_granted(self):
        permission = PermissionFactory(
            codename='can_call_check_course_access_api',
            content_type=ContentTypeFactory(app_label='embargo',)
        )
        user = UserFactory()
        user.user_permissions.add(permission)
        self.request.user = user

        result = CanCallCheckCourseAccessAPI().has_permission(self.request, None)
        self.assertTrue(result)

    def test_user_permission_not_granted(self):
        self.request.user = UserFactory()
        result = CanCallCheckCourseAccessAPI().has_permission(self.request, None)
        self.assertFalse(result)
