from django.test import TestCase
from .utils import add
from django.urls import reverse

class AddTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 7)

class NotesTestcase(TestCase):
    def test_notes_can_be_added(self):
        res=self.client.post(reverse('notes:add'),{
            "title":"Hello",
            "description":"Notes from test"
        })

        self.assertEqual(res.status_code,302)

        reshome=self.client.get(res.url)

        self.assertContains(reshome,"Hello")

