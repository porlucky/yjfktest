
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_tea_util.client import Client as UtilClient


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
        app_key="dingu6b9qcwcbvafblnj",
        app_secret="87hJBPGTNEjB7Nnc2m3t6U-_aH4G7QeHULtYQ8xNDdNmFyVDjRsn2IFkmAwWswgJ"
    )
    try:
        response = client.get_access_token(get_access_token_request)
        return response.body.access_token
    except Exception as err:
        if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
            # err 中含有 code 和 message 属性，可帮助开发定位问题
            raise Exception(f"获取失败: {err.code}, {err.message}")
        else:
            raise Exception("获取失败")

