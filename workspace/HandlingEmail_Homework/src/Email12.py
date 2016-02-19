import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email import encoders

##  v:/workspace/HandlingEmail_Homework/python-logo.png

def sendemail(address, body, attachments=[]):
    msg = MIMEMultipart()
    msg['From'] = 'paul.refalo@gmail.com'
    msg['To'] = address
    msg['Subject'] = "Python email system testing"
    msg['Body'] = body
    msg.attach(MIMEText(body))
    
    for path in attachments:
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            fp = open(path)
            # Note: we should handle calculating the charset
            att = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(path, 'rb')
            att = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(path, 'rb')
            att = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(path, 'rb')
            att = MIMEBase(maintype, subtype)
            att.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(msg)
        # Set the filename parameter
        msg.add_header('Content-Disposition', 'attachment', filename=path)
        msg.attach(att)
  
    return msg
    
    
if __name__ == '__main__':
    #print(sendemail('paul.refalo@gmail.com', 'Body of the email', ['walt.txt']))
    
    print(sendemail('paul.refalo@gmail.com', 'Body of the email', ['walt.txt', 'logo.png']))
    
    #print(sendemail('paul.refalo@gmail.com', 'Body of the email', 'python-logo.png'))
    