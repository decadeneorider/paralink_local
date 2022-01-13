
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os




class Email:
    def send_email(self,receivers,message1,email_title):
        results = []
        print(receivers)
        print(receivers)
        for receiver in receivers:
            sender = 'service@paralink.com.cn'
            print(message1)
            # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
            message = MIMEText(message1, 'plain', 'utf-8')
            message["From"] = "service@paralink.com.cn"
            message['To'] = receiver  # 接收者

            subject = email_title
            message['Subject'] = Header(subject, 'utf-8')

            mail_host = "smtp.paralink.com.cn"
            mail_sender = "service@paralink.com.cn"
            mail_license = "1_B5kCU22jk4"
            # stp = smtplib.SMTP()
            # stp.connect(mail_host, 25)
            # stp.login(mail_sender, mail_license)
            # stp.login(mail_sender, mail_license)
            # stp.sendmail(sender, receiver, message.as_string())
            try:
                # 创建SMTP对象
                stp = smtplib.SMTP()
                # 设置发件人邮箱的域名和端口，端口地址为25
                stp.connect(mail_host, 25)
                stp.login(mail_sender, mail_license)
                stp.sendmail(sender, receiver, message.as_string())
            except smtplib.SMTPException:
                print("发送失败")
                results.append(receiver)
        return results


    def send_file_email(self,receivers,title,message1,file_pathes,file_name):
        results = []
        for receiver in receivers:
            sender = 'maintenance@paralink.com.cn'
            # 创建一个带附件的实例
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            subject = title
            message['Subject'] = Header(subject, 'utf-8')
            # 邮件正文内容
            message.attach(MIMEText(message1, 'plain', 'utf-8'))
            # 构造附件1，传送当前目录下的 te
            # st.txt 文件
            for file_path in file_pathes:
                att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
                att1["Content-Type"] = 'application/octet-stream'
                # 这里的filename可以任意写，写什么名字，邮件中显示什么名字\
                print(os.path.basename(file_path))
                print(type(file_name))
                att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', file_name))
                message.attach(att1)
            mail_host = "smtp.paralink.com.cn"
            mail_sender = "maintenance@paralink.com.cn"
            mail_license = "JQU2L0M__p"

            try:
                # 创建SMTP对象
                stp = smtplib.SMTP()
                # 设置发件人邮箱的域名和端口，端口地址为25
                stp.connect(mail_host, 25)
                stp.login(mail_sender, mail_license)
                stp.sendmail(sender, receiver, message.as_string())
            except smtplib.SMTPException:
                results.append(receiver)
        return results


if __name__ == '__main__':
     basepath  = os.path.abspath('..')
     upload_path = os.path.join(basepath, "email_file", "邮箱.txt")
     result = Email().send_file_email(["1808863016@qq.com"],"测试","侧卧时达hi东海岛hi啊",[upload_path],"test1.txt")
     print(["1808863016@qq.com"],"测试","侧卧时达hi东海岛hi啊",["test.txt"],"test1.txt")
     print(result)