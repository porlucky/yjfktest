from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models


def create_client() -> dingtalkoauth2_1_0Client:
    """
    使用 AppKey 和 AppSecret 初始化账号Client
    @return: Client
    @throws Exception
    """
    config = open_api_models.Config()
    config.protocol = 'https'
    config.region_id = 'central'  # 根据实际情况设置 region_id
    return dingtalkoauth2_1_0Client(config)


def get_access_token_from_dingtalk() -> str:
    """
    从 DingTalk 获取 access_token
    @return: access_token
    @throws Exception
    """
    client = create_client()
    get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
        app_key="dinghughq49iep57v3kq",
        app_secret="ythpLXPx3uFuEzYFU53ByDuUBGCE-dQFC10txDgifYD8Kgog3f0orPDIZKlbtGlW"
    )
    try:
        response = client.get_access_token(get_access_token_request)
        return response.body.access_token
    except Exception as err:
        if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
            # err 中含有 code 和 message 属性，可帮助开发定位问题
            raise Exception(f"获取 access_token 失败: {err.code}, {err.message}")
        else:
            raise Exception("获取 access_token 失败")


def jsapiTicket() -> str:
    client = create_client()
    create_jsapi_ticket_headers = dingtalkoauth_2__1__0_models.CreateJsapiTicketHeaders()
    create_jsapi_ticket_headers.x_acs_dingtalk_access_token = get_access_token_from_dingtalk()
    try:
        response = client.create_jsapi_ticket_with_options(create_jsapi_ticket_headers, util_models.RuntimeOptions())
        return response.body.jsapi_ticket
    except Exception as err:
        if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
            print(err.code)
            print(err.message)
            # err 中含有 code 和 message 属性，可帮助开发定位问题
            pass
