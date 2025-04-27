from django.urls import path
from .views import predict_risk

urlpatterns = [
    path("predict/", predict_risk, name="predict"),
    path("test/", lambda request: JsonResponse({"ok": True})), 
]
