import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr


def send_email(
        sender_email,
        sender_password,
        recipient_email,
        subject,
        body,
        smtp_server="smtp.example.com",  # 默认SMTP服务器地址
        smtp_port=587,  # 默认SMTP端口号
        attachment_path=None,  # 可选附件路径
        use_tls=True  # 是否使用TLS加密
):
    """
    发送邮件的封装方法

    参数:
        sender_email (str): 发件人邮箱地址
        sender_password (str): 发件人邮箱密码（注意：某些邮箱需要使用授权码）
        recipient_email (str): 收件人邮箱地址
        subject (str): 邮件主题
        body (str): 邮件正文内容
        smtp_server (str, optional): SMTP服务器地址，默认为 "smtp.example.com"
        smtp_port (int, optional): SMTP服务器端口号，默认为 587
        attachment_path (str, optional): 附件路径，如果不需要附件，可以设置为 None
        use_tls (bool, optional): 是否使用TLS加密，默认为 True

    返回:
        dict: 包含发送结果的字典，格式为：
              {
                  "code": 200 或 00,
                  "message": "发送成功" 或 "发送失败的原因"
              }
    """
    try:
        # 创建邮件对象
        msg = MIMEMultipart()
        msg['From'] = formataddr(('Sender', sender_email))
        msg['To'] = formataddr(('Recipient', recipient_email))
        msg['Subject'] = subject

        # 添加邮件正文
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 如果有附件，添加附件
        if attachment_path:
            try:
                with open(attachment_path, 'rb') as attachment_file:
                    part = MIMEApplication(attachment_file.read(), Name=attachment_path.split('/')[-1])
                    part['Content-Disposition'] = f'attachment; filename="{attachment_path.split("/")[-1]}"'
                    msg.attach(part)
            except FileNotFoundError:
                return {
                    "code": 00,
                    "message": f"附件文件未找到：{attachment_path}"
                }
            except Exception as e:
                return {
                    "code": 00,
                    "message": f"添加附件失败，原因：{str(e)}"
                }

        # 连接到SMTP服务器并发送邮件
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if use_tls:
                server.starttls()  # 启用TLS加密
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        # 发送成功
        return {
            "code": 200,
            "message": "邮件发送成功"
        }

    except smtplib.SMTPAuthenticationError:
        return {
            "code": 00,
            "message": "SMTP认证失败，请检查邮箱地址和密码/授权码是否正确"
        }
    except smtplib.SMTPException as e:
        return {
            "code": 00,
            "message": f"SMTP错误：{str(e)}"
        }
    except Exception as e:
        return {
            "code": 00,
            "message": f"邮件发送失败，原因：{str(e)}"
        }
