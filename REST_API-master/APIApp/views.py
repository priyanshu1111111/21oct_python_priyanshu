from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import post_tbl
from .serializers import post_serial

@api_view(['GET'])
def getall(request):
    bdata = post_tbl.objects.all()
    serial = post_serial(bdata, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getid(request, id):
    try:
        bdata = post_tbl.objects.get(id=id)
    except post_tbl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial = post_serial(bdata)
    return Response(serial.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def savedata(request):
    if request.method == 'POST':
        serial = post_serial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def update(request, id):
    try:
        Tank = post_tbl.objects.get(id=id)
    except post_tbl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = post_serial(Tank)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serial = post_serial(data=request.data, instance=Tank)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def deleteid(request, id):
    try:
        Tank = post_tbl.objects.get(id=id)
    except post_tbl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serial = post_serial(Tank)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        Tank.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
