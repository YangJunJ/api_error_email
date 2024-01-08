import logging
import traceback
from logging.handlers import HTTPHandler

from ApiErrorEmail.settings import LOG_FORMAT
from email_tool import send_text_email, ERROR_ACCEPT_USER_LIST


class LogHTTPHandler(HTTPHandler):
    def __init__(self, host, url, method="GET", secure=False, credentials=None,
                 context=None, *args, **kwargs):
        super(LogHTTPHandler, self).__init__(host, url, method, secure, credentials, context)

    def emit(self, record):
        """
        微信公众号：PyGo学习笔记

        详情可以查阅文档地址：https://docs.python.org/zh-cn/3/library/logging.handlers.html#httphandler

        重写该方法，这个方法是将日志通过url发送到别的服务器进行处理
        此处只需要将将日志处理并调用之前的发送邮件接口即可
        """
        data = self.mapLogRecord(record)  # 返回日志所有信息
        # 增加判断，只有等级大于ERROR的日志才做发送处理
        # 日志等级可以查阅该文档：https://docs.python.org/zh-cn/3/library/logging.html#logging-levels
        if data["levelno"] >= logging.ERROR:
            # 当有调用堆栈时，stack_info是整个代码调用堆栈，方便报错时快速定位到报错日志
            # 可以查阅文档：https://docs.python.org/zh-cn/3/library/logging.html?highlight=stack_info
            stack_info = data.get('stack_info', None)
            exc_text = None
            if not stack_info:
                exc_text = data.get('exc_text', None)

            data = LOG_FORMAT % data
            data += "\n"

            if stack_info:
                data += stack_info

            if exc_text:
                data += exc_text

            # 将日志发送到每一个开发人员的邮箱中
            send_text_email(ERROR_ACCEPT_USER_LIST, data)






