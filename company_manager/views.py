from django.shortcuts import render
from django.http import JsonResponse
from company_manager import models as company_manager_models
from team import models as team_models
from Portfolio import models as Portfolio_models
from careers import models as careers_models


def company_details(request):
    try:
        company = company_manager_models.Company.objects.get(id=1)
        data = []
        data.append({
            'company_name':company.company_name,
            'phone':company.phone,
            'location':company.location,
            'email':company.email
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
                'skills':career_data.skills
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
                "link":p_data.link
            })

        return JsonResponse({"status":True, "data":data}, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse({"status":False, "data":data}, status=500)
        