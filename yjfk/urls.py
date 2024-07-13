from django.urls import path
from . import views, user, web

urlpatterns = [
    path("getinfo/", user.getinfo, name="getinfo"),
    path("userlist/", user.userlist, name="userlist"),
    path("userone/", user.userone, name="userone"),
    path("useradd/", user.useradd, name="useradd"),
    path("userupdate/", user.userupdate, name="userupdate"),

    path("getsign/", web.getsign, name="getsign"),
    path("getuserinfo/", web.getuserinfo, name="getuserinfo"),
    path("webuserlist/", web.webuserlist, name="webuserlist"),
    path("webuseradd/", web.webuseradd, name="webuseradd"),
    path("webuserone/", web.userone, name="userone"),
    path("webuserupdate/", web.userupdate, name="userupdate"),
]
