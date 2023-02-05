from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("config/", views.stripe_config, name="payment-config"),
    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create-checkout-session",
    ),
    path("success/", views.SuccessView.as_view(), name="payment-success"),
    path("cancelled/", views.CancelledView.as_view(), name="payment-cancelled"),
    path('webhook/', views.stripe_webhook),
]
