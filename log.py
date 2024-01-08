import logging

from django.http import JsonResponse

log = logging.getLogger()
log_error_email = logging.getLogger("error_email")


def error_send_email(func):
    def check(request, *args, **kwargs):
        response = {
            "code": 500,
            "message": "服务器出现异常",
            "data": {}
        }
        try:
            return func(request, **kwargs)
        except Exception as e:
            # 此处捕捉日志 exception是等级error接口
            log_error_email.exception(f"调用接口{func.__name__}，参数 args:{args} kwargs:{kwargs}  失败：{e}")
            return JsonResponse(response)
    return check
