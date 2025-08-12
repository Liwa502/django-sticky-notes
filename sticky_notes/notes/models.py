from django.db import models


# The StickyNote model represents a single note in the application.
class StickyNote(models.Model):
    # Title of the note (max 100 characters)
    title = models.CharField(max_length=100)

    # Main content/body of the note (no length limit)
    content = models.TextField()

    # Timestamp: set automatically when note is first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp: updates automatically whenever the note is saved
    updated_at = models.DateTimeField(auto_now=True)

    # Boolean flag to mark note as pinned (important or prioritized)
    pinned = models.BooleanField(default=False)

    # Optional due date for the note (can be left blank or null)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String representation of the note.
        This is what will be shown in the Django admin and shell.
        """
        return self.title
