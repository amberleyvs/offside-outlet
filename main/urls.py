from django.urls import path
from main.views import (
    proxy_image, show_main, addEmployee, showEmployees,
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    add_product, show_detail,
    register, login_user, logout_user,
    edit_product, delete_product,
    wishlist_page, toggle_wishlist,
    add_product_entry_ajax,
    update_product_entry_ajax,
    delete_product_ajax,
    create_product_flutter,
)
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', addEmployee, name='add_employee'), 
    path('show/', showEmployees, name='show_employees'),  
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path('add_product/', add_product, name='add_product'),
    path('detail/<int:id>/', show_detail, name='show_detail'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<int:id>/edit', edit_product, name='edit_product'),
    path('products/<int:id>/delete', delete_product, name='delete_product'),
    path("wishlist/", wishlist_page, name="wishlist"),
    path("wishlist/toggle/<int:id>/", toggle_wishlist, name="toggle_wishlist"),
    path("products/<int:id>/update-ajax/", update_product_entry_ajax, name="update_product_entry_ajax"),
    path("products/<int:id>/delete-ajax/", delete_product_ajax, name="delete_product_ajax"),
    path("products/add-ajax/", add_product_entry_ajax, name="add_product_entry_ajax"),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]