"""
Tests for course welcome messages.
"""
from django.core.urlresolvers import reverse

from student.models import CourseEnrollment
from student.tests.factories import UserFactory
from xmodule.modulestore import ModuleStoreEnum
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.tests.factories import CourseFactory, ItemFactory

from .test_course_updates import create_course_update, remove_course_updates

TEST_PASSWORD = 'test'
TEST_WELCOME_MESSAGE = '<h2>Welcome!</h2>'


def welcome_message_url(course):
    """
    Returns the URL for the welcome message view.
    """
    return reverse(
        'openedx.course_experience.welcome_message_fragment_view',
        kwargs={
            'course_id': unicode(course.id),
        }
    )


class TestWelcomeMessageView(ModuleStoreTestCase):
    """
    Tests for the course welcome message fragment view.
    """
    def setUp(self):
        """Set up the simplest course possible, then set up and enroll our fake user in the course."""
        super(TestWelcomeMessageView, self).setUp()
        with self.store.default_store(ModuleStoreEnum.Type.split):
            self.course = CourseFactory.create()
            with self.store.bulk_operations(self.course.id):
                # Create a basic course structure
                chapter = ItemFactory.create(category='chapter', parent_location=self.course.location)
                section = ItemFactory.create(category='sequential', parent_location=chapter.location)
                ItemFactory.create(category='vertical', parent_location=section.location)

        self.user = UserFactory(password=TEST_PASSWORD)
        CourseEnrollment.enroll(self.user, self.course.id)

        self.client.login(username=self.user.username, password=TEST_PASSWORD)

    def tearDown(self):
        remove_course_updates(self.course)
        super(TestWelcomeMessageView, self).tearDown()

    def test_welcome_message(self):
        create_course_update(self.course, self.user, 'First Update', date='January 1, 2000')
        create_course_update(self.course, self.user, 'Second Update', date='January 1, 2017')
        create_course_update(self.course, self.user, 'Retroactive Update', date='January 1, 2010')
        response = self.client.get(welcome_message_url(self.course))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Second Update')

    def test_replace_urls(self):
        img_url = 'img.png'
        create_course_update(self.course, self.user, "<img src='/static/{url}'>".format(url=img_url))
        response = self.client.get(welcome_message_url(self.course))
        self.assertContains(response, "/asset-v1:{org}+{course}+{run}+type@asset+block/img.png".format(
            org=self.course.id.org,
            course=self.course.id.course,
            run=self.course.id.run
        ))

    def test_empty_welcome_message(self):
        response = self.client.get(welcome_message_url(self.course))
        self.assertEqual(response.status_code, 204)
