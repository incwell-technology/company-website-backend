from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  FormParser, MultiPartParser
from company_manager import models as company_manager_models
from team import models as team_models
from Portfolio import models as Portfolio_models
from careers import models as careers_models
from company_manager import serializers as company_serializers


def company_details(request):
    try:
        company = company_manager_models.Company.objects.get(id=1)
        data = []
        data.append({
            'company_name':company.company_name,
            'phone':company.phone,
            'location':company.location,
            'email':company.email,
            'id':company.id,
            'video':company.video
        })
        return JsonResponse({"status":True, "data":data}, status=200)
    except (company_manager_models.Company.DoesNotExist) as e:
        print(e)
        return JsonResponse({"status":False, "data":[]}, status=500)


def careers(request):
    try:
        career = careers_models.Career.objects.all()
        data = []
        for career_data in career:
            data.append({
                'title':career_data.title,
                'short_description':career_data.short_description,
                'job_description':career_data.job_description,
                'skills':career_data.skills,
                'id':career_data.id
            })
        return JsonResponse({"status":True, "data":data}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"status":False, "data":data}, status=500)
        

def portfolio(request):
    try:
        portfolio_data = Portfolio_models.Portfolio.objects.all()
        data = []
        full_path = request.build_absolute_uri()
        
        path = full_path.split('/api/')[0]
        
        for p_data in portfolio_data:
            data.append({
                "image": path + "/static/"+p_data.image.url.split('/static/')[1],
                "link":p_data.link,
                "id":p_data.id
            })

        return JsonResponse({"status":True, "data":data}, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({"status":False, "data":data}, status=500)
        

def team(request):
    try:
        team_data = team_models.Team_Members.objects.all()
        data = []
        full_path = request.build_absolute_uri()
        
        path = full_path.split('/api/')[0]

        for t_data in team_data:
            data.append({
                'id':t_data.id,
                'full_name':t_data.full_name,
                'designation':t_data.designation,
                'image': path + "/static/" + t_data.image.url.split('/static/')[1]
            })
        
        return JsonResponse({"status":True, "data":data}, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({"status":False, "data":data}, status = 500)



@csrf_exempt
@api_view(["POST"])
@parser_classes((MultiPartParser, FormParser,))
def apply_career(request):
    if request.method == "POST":
        holiday = {}
        print(request.data)
        serializer = company_serializers.CareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse({"status":True, "payload":"Saved successfully"}, status=201)
        else:
            return JsonResponse({"status":False, "message":"Failed to store."},status = 400)
    