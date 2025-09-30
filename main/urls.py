from django.urls import path
from main.views import show_main, addEmployee, showEmployees, show_json, show_xml, show_json_by_id, show_xml_by_id, add_product, show_detail
from main.views import register, login_user,logout_user, add_car, edit_product, delete_product, wishlist_page, toggle_wishlist

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', addEmployee, name='add_employee'),  # New URL pattern for adding an employee
    path('show/', showEmployees, name='show_employees'),  # New URL pattern for showing employees
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products<int:id>/edit', edit_product, name='edit_product'),
    path('products/<int:id>/delete', delete_product, name='delete_product'),
    path("wishlist/", wishlist_page, name="wishlist"),
    path("wishlist/toggle/<int:id>/", toggle_wishlist, name="toggle_wishlist"),
]