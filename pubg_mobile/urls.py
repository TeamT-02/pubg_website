"""
URL configuration for pubg_mobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pubg_mobile import help_admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('super_admin/admin', help_admin_views.super_admin, name='super_admin'),
    # Hod staff panel url
    path('Hod/Staff/Add', help_admin_views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', help_admin_views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', help_admin_views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', help_admin_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', help_admin_views.DELETE_STAFF, name='delete_staff'),
    path('Hod/Staff/feedback', help_admin_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
    path('Hod/Staff/feedback/save', help_admin_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),
    path('Hod/Staff/Send_Notification', help_admin_views.STAFF_SEND_NOTIFICATION,
         name='staff_send_notification'),
    path('Hod/Staff/save_notification', help_admin_views.SAVE_STAFF_NOTIFICATION,
         name='save_staff_notification'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
