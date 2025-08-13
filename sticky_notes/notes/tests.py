from django.test import TestCase
from django.urls import reverse
from .models import StickyNote
from datetime import date

# ----- MODEL TESTS -----
class StickyNotesTest(TestCase):
    def setUp(self):
        self.note = StickyNote.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")
        self.assertFalse(self.note.pinned)
        self.assertIsNone(self.note.due_date)

    def test_note_read(self):
        note = StickyNote.objects.get(title="Test Note")
        self.assertEqual(note.content, "This is a test note.")

    def test_note_update(self):
        self.note.title = "Updated Title"
        self.note.pinned = True
        self.note.due_date = date(2025, 12, 31)
        self.note.save()
        updated_note = StickyNote.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, "Updated Title")
        self.assertTrue(updated_note.pinned)
        self.assertEqual(updated_note.due_date, date(2025, 12, 31))

    def test_note_delete(self):
        note_id = self.note.id
        self.note.delete()
        self.assertFalse(StickyNote.objects.filter(id=note_id).exists())

    def test_toggle_pin(self):
        self.note.pinned = not self.note.pinned
        self.note.save()
        self.assertTrue(StickyNote.objects.get(id=self.note.id).pinned)
        self.note.pinned = not self.note.pinned
        self.note.save()
        self.assertFalse(StickyNote.objects.get(id=self.note.id).pinned)


# ----- VIEW TESTS -----
class StickyNoteViewTests(TestCase):
    def setUp(self):
        self.note = StickyNote.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_list_view(self):
        url = reverse('note_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_create_view(self):
        url = reverse('note_create')
        data = {'title': 'New Note', 'content': 'New note content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(StickyNote.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        url = reverse('note_update', args=[self.note.id])
        data = {'title': 'Updated Title', 'content': 'Updated content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')

    def test_note_delete_view(self):
        url = reverse('note_delete', args=[self.note.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(StickyNote.objects.filter(id=self.note.id).exists())

    def test_toggle_pin_view(self):
        url = reverse('note_toggle_pin', args=[self.note.id])
        response = self.client.post(url)
        self.note.refresh_from_db()
        self.assertTrue(self.note.pinned)
