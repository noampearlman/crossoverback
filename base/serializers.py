from rest_framework.serializers import ModelSerializer
from base.models import Connection,Direction,Property,Type
# from base.models import  Note,Kid
 
# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'

# class KidSerializer(ModelSerializer):
#     class Meta:
#         model = Kid
#         fields = '__all__'

class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class ConnectionSerializer(ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


