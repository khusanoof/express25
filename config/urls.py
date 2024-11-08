
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from accaunt.views import LogoutView,LoginView,RegisterView



schema_view = get_schema_view(
    openapi.Info(
        title="Express 25",
        default_version='v1',
        description="Restaurants and Stores delivery service",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="express25@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/store/',include('store.urls'),name='store-api' ),

    path('api/v1/delivery/',include('delivery.urls')),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/auth/', include('dj_rest_auth.urls')),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
