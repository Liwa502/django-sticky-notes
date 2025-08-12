from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm
from django.views.decorators.http import require_POST


def note_list(request):
    """
    Display the list of all sticky notes.
    Notes are ordered to show pinned notes first,
    then by due date ascending, then by most recently updated.
    """
    notes = StickyNote.objects.order_by('-pinned', 'due_date', '-updated_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_create(request):
    """
    Handle creation of a new sticky note.
    Display form on GET request,
    process form and save note on POST if valid,
    then redirect to note list.
    """
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = StickyNoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Create'})


def note_update(request, pk):
    """
    Handle editing an existing sticky note identified by primary key (pk).
    On GET, display the form pre-filled with note data.
    On POST, validate and save updates, then redirect to note list.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'action': 'Update'})


def note_delete(request, pk):
    """
    Handle deletion of a sticky note identified by primary key (pk).
    On GET, display a confirmation page.
    On POST, delete the note and redirect to note list.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


@require_POST
def note_toggle_pin(request, pk):
    """
    Toggle the 'pinned' status of a note identified by primary key (pk).
    This view only allows POST requests for safety.
    After toggling, redirect back to the note list.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    note.pinned = not note.pinned
    note.save()
    return redirect('note_list')
