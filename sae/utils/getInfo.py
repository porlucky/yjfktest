import requests
from django.http import JsonResponse


def get_info(code: str):
    app_key = "ding7vu6vbk1gjwqrsyp",
    app_secret = "w3W7RdBjYGUl2RFlbesI_VYsna1uQo-No4Loru0u9uvYhsONvhzJdx_lVQzqXkx5"
    url = f'http://dingtalknba.thdfh.cn:876/ddapi/get_access_token/'
    data = {
        'app_key': app_key,
        'app_secret': app_secret
    }
    response = requests.post(url, data=data)
    res = response.json()
    if res['errcode'] > 0:
        return JsonResponse({"error": res['errcode'], 'errmsg': res['errmsg']})
    access_token1 = res['access_token']

    # 用户信息
    url1 = f'https://oapi.dingtalk.com/topapi/v2/user/getuserinfo?access_token={access_token1}'
    data1 = {
        'code': code
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url1, json=data1, headers=headers)
    res1 = response.json()
    if res1['errcode'] > 0:
        return JsonResponse({"error": res1['errcode'], 'errmsg': res1['errmsg']})

    # 用户信息详细
    url2 = f"https://oapi.dingtalk.com/topapi/v2/user/get?access_token={access_token1}"
    data2 = {
        'userid': res1['result']['userid']
    }
    response = requests.post(url2, json=data2, headers=headers)
    res2 = response.json()
    if res2['errcode'] > 0:
        return JsonResponse({"error": res2['errcode'], 'errmsg': res2['errmsg']})

    # 用户部门
    url3 = f"https://oapi.dingtalk.com/topapi/v2/department/get?access_token={access_token1}"
    data3 = {
        'dept_id': res2['result']['dept_order_list'][0]['dept_id']
    }
    response = requests.post(url3, json=data3, headers=headers)
    res3 = response.json()
    if res3['errcode'] > 0:
        return JsonResponse({"error": res3['errcode'], 'errmsg': res3['errmsg']})
    return {'user_id': res1['result']['userid'], 'user_name': res1['result']['name'],
            'dept_name': res3['result']['name'], 'user_avatar': res2['result']['avatar']}
