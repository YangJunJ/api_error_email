from django.urls import path

from views import *

urlpatterns = [
    path('test_common_require_api', test_common_require_api),
    path('test_common_error_require_api', test_common_error_require_api),
    path('test_protect_error_require_api', test_protect_error_require_api),
    path('test_api_protect_error_require_api', test_api_protect_error_require_api),
]