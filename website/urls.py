from django.urls import path
from django.conf.urls.static import static
from website.views import *


urlpatterns = [
    path('', index_view),

]
