from django.http import JsonResponse

from yjfk.models import YJFKUser
from yjfk.utils.webgetinfo import get_sign, get_info
from yjfk import models
import datetime


def getsign(request):
    url = request.GET.get('url')
    res = get_sign(url)
    res['agentId'] = '3151931470'
    res['corpId'] = 'ding695cc080d2b37f8a24f2f5cc6abecb85'
    return JsonResponse(res)


def getuserinfo(request):
    code = request.GET.get('code')
    ret = get_info(code)
    return JsonResponse(ret)


def webuserlist(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        YJFKUser_list = YJFKUser.objects.filter(user_id=user_id).values().all().order_by("-add_datetime")
        for item in YJFKUser_list:
            item['add_datetime'] = item['add_datetime'].strftime("%Y-%m-%d %H:%M:%S")
        return JsonResponse({'ret': list(YJFKUser_list)})


def webuseradd(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        item = request.POST.get('item')
        description = request.POST.get('description')
        user_name = request.POST.get('user_name')
        dept_name = request.POST.get('dept_name')
        address = request.POST.get('address')
        add_datetime = datetime.datetime.now()
        ret = models.YJFKUser()
        ret.user_id = user_id
        ret.item = item
        ret.description = description
        ret.user_name = user_name
        ret.dept_name = dept_name
        ret.address = address
        ret.add_datetime = add_datetime.strftime("%Y-%m-%d %H:%M:%S")
        ret.save()
        return JsonResponse({'error': 0}, status=200)


def userone(request):
    if request.method == "GET":
        uid = request.GET.get('id')
        try:
            YJFKUser_info = list(YJFKUser.objects.filter(id=uid).values())
            for item in YJFKUser_info:
                item['add_datetime'] = item['add_datetime'].strftime("%Y-%m-%d %H:%M:%S")
            return JsonResponse({'ret': YJFKUser_info[0]})
        except YJFKUser.DoesNotExist:
            return JsonResponse({'ret': 'User not found'}, status=404)


def userupdate(request):
    if request.method == "POST":
        uid = request.POST.get('id')
        item = request.POST.get('item')
        description = request.POST.get('description')
        user_name = request.POST.get('user_name')
        dept_name = request.POST.get('dept_name')
        address = request.POST.get('address')
        add_datetime = datetime.datetime.now()
        models.YJFKUser.objects.filter(id=uid).update(item=item, description=description, user_name=user_name,
                                                      dept_name=dept_name, address=address, add_datetime=add_datetime)
        return JsonResponse({'error': 0}, status=200)
