from django.urls import path
from . import views

urlpatterns = [
    # Display the list of all sticky notes
    path('', views.note_list, name='note_list'),

    # Create a new sticky note
    path('create/', views.note_create, name='note_create'),

    # Edit an existing sticky note identified by primary key (pk)
    path('edit/<int:pk>/', views.note_update, name='note_update'),

    # Delete an existing sticky note identified by primary key (pk)
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),

    # Toggle the 'pinned' status of a note identified by primary key (pk)
    path('toggle-pin/<int:pk>/', views.note_toggle_pin, name='note_toggle_pin'),
]
