from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail,
         name='product_detail'),
    path('<product_id>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<product_id>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
