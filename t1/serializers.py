from rest_framework import serializers
from models import Tuple

class TupleSerializer(serializers.ModelSerializer):
      class Meta:
          model=Tuple
          field=('id','string_field','numeric_value')


