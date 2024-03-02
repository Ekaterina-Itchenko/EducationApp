from rest_framework import serializers


class ProductInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    start_date = serializers.DateTimeField()
    author = serializers.CharField()
    amount_of_lessons = serializers.IntegerField()
