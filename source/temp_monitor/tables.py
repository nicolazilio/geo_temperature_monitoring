import django_tables2 as tables
from .models import Temperature

class TemperatureTable(tables.Table):
    class Meta:
        model = Temperature
        template_name = "django_tables2/bootstrap.html"
        fields = ("temp", "temp_taken_date_time")
        # attrs = {
        #     "th" : {
        #         "_ordering": {
        #             "temp": "sortable",
        #             "temp_taken_date_time": "sortable", 
        #         }
        #     }
        # }