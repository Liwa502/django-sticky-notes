from django.test import TestCase
from .models import StickyNote
from datetime import date


class StickyNotesTest(TestCase):
    def setUp(self):
        """
        Runs before every test.
        Creates a sample sticky note in the database to use for testing.
        """
        self.note = StickyNote.objects.create(
            title="Test Note",
            content="This is a test note."
        )

    def test_note_creation(self):
        """
         Test creation of a StickyNote.
        Checks if the note has the correct values and default fields.
        """
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")
        self.assertFalse(self.note.pinned)  # Default should be False
        self.assertIsNone(self.note.due_date)  # Default should be None

    def test_note_read(self):
        """
         Test retrieving a StickyNote from the database.
        Ensures stored content matches expected values.
        """
        note = StickyNote.objects.get(title="Test Note")
        self.assertEqual(note.content, "This is a test note.")

    def test_note_update(self):
        """
         Test updating a StickyNote's fields (title, pinned, due_date).
        """
        # Update note fields
        self.note.title = "Updated Title"
        self.note.pinned = True
        self.note.due_date = date(2025, 12, 31)
        self.note.save()

        # Retrieve and verify updates
        updated_note = StickyNote.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, "Updated Title")
        self.assertTrue(updated_note.pinned)
        self.assertEqual(updated_note.due_date, date(2025, 12, 31))

    def test_note_delete(self):
        """
         Test deleting a StickyNote from the database.
        """
        note_id = self.note.id
        self.note.delete()
        # Ensure note no longer exists
        self.assertFalse(StickyNote.objects.filter(id=note_id).exists())

    def test_toggle_pin(self):
        """
         Test toggling the 'pinned' field:
        False → True → False.
        """
        # Toggle pinned to True
        self.note.pinned = not self.note.pinned
        self.note.save()
        self.assertTrue(StickyNote.objects.get(id=self.note.id).pinned)

        # Toggle pinned back to False
        self.note.pinned = not self.note.pinned
        self.note.save()
        self.assertFalse(StickyNote.objects.get(id=self.note.id).pinned)
