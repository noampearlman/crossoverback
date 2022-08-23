from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
 
from .serializers import NoteSerializer,KidSerializer,PropertySerializer,ConnectionSerializer,DirectionSerializer,TypeSerializer
from base.models import Note,Kid,Property,Connection,Direction,Type
 
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)
 
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    print("innnn")
    user = request.user
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    print(request.data)
    user = request.user
    Note.objects.create(body=request.data["notebody"],user=user)
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getKids(request):
    user = request.user
    kids = user.kid_set.all()
    serializer = KidSerializer(kids, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addKid(request):
    print(request.data)
    user = request.user
    Kid.objects.create( name=request.data["name"],
                        age=request.data["age"],
                        user=user)
    kids = user.kid_set.all()
    serializer = KidSerializer(kids, many=True)
    return Response(serializer.data) 



# -----Connections-----
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCons(request):
    cons = Connection.objects.all()
    serializer = ConnectionSerializer(cons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCon(request):
    print(request.data["secondProperty"])
    print(Property.objects.filter(id = request.data["firstProperty"]).first())
    Connection.objects.create(      firstProperty=Property.objects.filter(id = request.data["firstProperty"]).first(),
                                    secondProperty=Property.objects.filter(id = request.data["secondProperty"]).first(),
                                    direction=Direction.objects.filter(id = request.data["direction"]).first(),
                                    type=Type.objects.filter(id = request.data["type"]).first(),
                                    desc=request.data["desc"])
    cons = Connection.objects.all()
    serializer = ConnectionSerializer(cons, many=True)
    return Response(serializer.data)

# -----Props-----
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProps(request):
    props = Property.objects.all()
    serializer = PropertySerializer(props, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProp(request):
    Property.objects.create(    name=request.data["name"],
                                page_Content=request.data["page_Content"])
    props = Property.objects.all()
    serializer = PropertySerializer(props, many=True)
    return Response(serializer.data)

# -----Types-----
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTypes(request):
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addType(request):
    Type.objects.create(   name=request.data["name"],
                                desc=request.data["desc"])
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data)

# -----Directions-----
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDirs(request):
    directions = Direction.objects.all()
    serializer = DirectionSerializer(directions, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addDir(request):
    Direction.objects.create(   name=request.data["name"],
                                desc=request.data["desc"])
    directions = Direction.objects.all()
    serializer = DirectionSerializer(directions, many=True)
    return Response(serializer.data)


# register
@api_view(['POST'])
def addUser(request):
    User.objects.create_user(   username=request.data["username"],
                                email=request.data["email"],
                                password=request.data["password"])
    return JsonResponse({"added":request.data["username"]} )
 


    
 
