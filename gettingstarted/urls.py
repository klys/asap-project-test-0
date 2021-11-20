from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("member_id/", hello.views.member_id, name="member_id"),
    path("member_id/validate/", hello.views.validate_member_id_html, name="validate_member_id"),
    path("member_id/validate/check/", hello.views.validate_member_id, name="validate_member_id_response"),
]
