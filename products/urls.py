from django.urls import path
from . import views

urlpatterns = [
	path('publish',views.publish,name='publish'),
	path('<int:product_id>',views.detail,name='detail'),
]