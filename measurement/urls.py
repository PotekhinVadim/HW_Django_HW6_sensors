from django.urls import path

from measurement.views import SensorListView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view())
]
