from rest_framework import serializers


class Dictionary(object):
    def __init__(self, dictionary):
        self.data = dictionary["data"]
        self.complete_analysis=dictionary["complete_analysis"]

# create a serializer
class DictionarySerializer(serializers.Serializer):
    # initialize fields
    data = serializers.ListField(
        child=serializers.DictField())
    complete_analysis = serializers.CharField()

