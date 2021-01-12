from django.urls import path,include
from . import views



urlpatterns=[
  path('getshifts/', views.get_shifts),
  path('addshifts/', views.add_shift),
  path('updateshift/<int:shift_id>', views.update_shift),
  path('deleteshift/<int:shift_id>', views.delete_shift),
]