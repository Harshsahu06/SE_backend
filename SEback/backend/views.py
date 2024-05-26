from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
import json
from backend.models import User,hospital
from .serializer import hospitaldataserializer,userDataSerializer
from rest_framework import status


# hospital data API working with post and get request 
@api_view(['POST',"GET"])
def hospitaldata(request):
    if request.method=="GET":
        data=hospital.objects.get(id=4)
        serializer1=hospitaldataserializer(data)
        data1=serializer1.data
        # data1=json.loads(data)
        print(data1)
        return Response({"status":200,"message":" api hospital data is working","data":data1})
    elif request.method=="POST":
        serializer = hospitaldataserializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
         serializer.save()
         print("reached")
         return Response({"status":200,"message":"Post api of hospital","data":"harsh","data":serializer.data})
        else:
            print("Validation failed:", serializer.errors)
            return Response({
                "status": "error",
                "message": "Validation failed",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST) 
    # return Response(status=status.HTTP_401_UNAUTHORIZED) 
    return Response({"status":"nothing done"})  
    
# user profile data API working with get ,post ,patch
@api_view(["GET","POST","PATCH"])
def userdata(request,pk):
    instance=User.objects.get(pk=pk)
    serializer1=userDataSerializer(instance,data=request.data,partial=True)
    if request.method=="GET":
     data=User.objects.all()
     Userdata=userDataSerializer(data,many=True)
     Userdata=Userdata.data
     return JsonResponse({"status":status.HTTP_201_CREATED,"message":" GET api is working userdata !!","data":Userdata})
    elif request.method=="POST":
       serializer=userDataSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save() 
           return Response(status=status.HTTP_201_CREATED)
       return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        if serializer1.is_valid():
            serializer1.save()
            print("done")
        return Response(status=status.HTTP_200_OK)
        

# login details get from user by post method API pending(error hand-ling)
@api_view(["GET","POST"])  
def login(request):
    if request.method=="GET":
        return JsonResponse({"status":200,"message":"api login is working"})
    elif request.method=="POST":
        # data=json.loads(request.body)
        data=userDataSerializer(data=request.data)
        # name=data.get("name")
        # print(data,name,"done")
        if data.is_valid():
            data.save()
        return JsonResponse({"status":200,"message":"data received !!"})
    
# sign up data retrive from frontend by POST  method
@api_view(["GET","POST"])     
def signup(request):
    if request.method=="GET":
        return JsonResponse({"status":200,"message":"signup api is working"}) 
    elif request.method=="POST":
        data=json.loads(request.body)
        return JsonResponse({"status":200,"message":"post method of signup is working","data":data})
    else:
       return ({"status":404,"message":"methiod not allowed"})  
   
# @api_view(["POST","GET"])   
# def medicaldata(request):
#     if request.method=="POST":
#         data=json.loads(request.body)
#         print(data)
#         return JsonResponse({"status":200,"message":"working","data":data})
#     elif request.method=="GET":
#         return JsonResponse({"status":200,"message":"get reuqest of medical"})
  
  
#  For refrence
#   try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
         
