from rest_framework import serializers

# class ExtractionSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField()
#     title = serializers.CharField(max_length=200)
#     sku = serializers.CharField(max_length=200)
#     price = serializers.CharField(max_length=200)



class PKSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    