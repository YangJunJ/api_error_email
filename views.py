from django.http import JsonResponse

from log import log, error_send_email


def test_common_require_api(request, *args, **kwargs):
    """
    微信公众号: PyGo学习笔记
    测试普通接口
    正常返回数据，输出一条info日志
    """
    response = {
        "code": 200,
        "message": "",
        "data": {
            "msg": "已经输出一条info日志"
        }
    }
    log.info("正常输出一条info日志")
    return JsonResponse(response)


def test_common_error_require_api(request, *args, **kwargs):
    """
    微信公众号: PyGo学习笔记
    测试下接口里面遇到报错，查看是否能收到邮件、以及错误日志的情况
    """
    response = {
        "code": 200,
        "message": "",
        "data": {
            "msg": ""
        }
    }

    # 此处加一行会报错的代码
    a = 1 / 0
    return JsonResponse(response)


@error_send_email
def test_protect_error_require_api(request, *args, **kwargs):
    """
    微信公众号: PyGo学习笔记

    测试增加错误装饰器保护的接口，日志输出情况、以及邮件发送情况
    """
    response = {
        "code": 200,
        "message": "",
        "data": {
            "msg": ""
        }
    }
    # 此处加一行会报错的代码
    a = 1 / 0
    return JsonResponse(response)


def test_api_protect_error_require_api(request, *args, **kwargs):
    """
    微信公众号: PyGo学习笔记

    接口内增加保护，并触发异常输出到日志中
    """
    response = {
        "code": 200,
        "message": "",
        "data": {
            "msg": ""
        }
    }
    # 此处加一行会报错的代码
    try:
        a = 1 / 0
    except Exception as e:
        log.exception(f"test_api_protect_error_require_api 触发的异常：{e}")
    return JsonResponse(response)

