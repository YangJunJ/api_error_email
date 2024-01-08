

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from threading import Thread

SENDER_EMAIL = 'xxxx@qq.com'  # 服务器专门用来发邮件的邮箱账号
SENDER_NAME = "发件人名字"                 # 服务器专门用来发邮件的发件人名字
SENDER_AUTHORIZATION_CODE = "xxxxx"  # 上一步骤拿到的授权码


ERROR_ACCEPT_USER_LIST = [
    ("收件人名字", "xxxxx@qq.com"),
]


def async_execute(func):
    def auth(*args, **kwargs):
        th = Thread(target=func, args=args, kwargs=kwargs)
        th.start()
    return auth


@async_execute  # 不确定发邮件的效率，此处增加线程装饰器，异步发送邮件
def send_text_email(accept_email_list, msg):
    """
    发送文本邮箱
    :param accept_email_list:
    :param msg:
    :return:
    """
    msg = MIMEText(msg, 'plain', 'utf-8')  # 填写邮件内容
    msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
    server.login(SENDER_EMAIL, SENDER_AUTHORIZATION_CODE)
    for accept_email in accept_email_list:
        msg['To'] = formataddr(accept_email)
        server.sendmail(SENDER_EMAIL, [accept_email[1]], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()


if __name__ == "__main__":
    send_text_email(ERROR_ACCEPT_USER_LIST, "测试邮件")





