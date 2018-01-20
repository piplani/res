import os
import subprocess
import sys
from webapp.models import status, data

arr = status.objects.filter(status=False)
for i in arr:
    dirname = str(i.status_id)
    file = open(os.getcwd()+ '/media/'+ dirname + '/results.txt', 'w')
    activity_score = ''
    potency = ''
    efficacy = ''
    #print(os.getcwd())
    #print(sta.status)

    def sendmail(reciever, mes):
        import smtplib
        message = 'Subject: {}\n\n{}'.format('Result Mail', mes)
        sender = 'akshaykumar.90447@gmail.com'  # place your email id here
        sender_pswd = 'piplani@786'  # place your pswd here
        # reciever = 'piplani.rohan@gmail.com'

        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender, sender_pswd)
        mail.sendmail(sender, reciever, message)
        mail.close()

    def sendmailwithattachments(receiver, dirname):
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        from email.MIMEBase import MIMEBase
        from email import encoders

        fromaddr = "akshaykumar.90447@gmail.com"
        toaddr = receiver

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Result"

        body = "download attachment for Results"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'Results.txt'
        attachment = open(os.getcwd()+ '/media/' + dirname + '/results.txt', "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "piplani@786")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    def runforactivity_score(dirname):
        import subprocess
        command = 'Rscript'
        path2script = os.getcwd() + '/models/activity_predict.R'

        # Variable number of args in a list
        args = [dirname]

        # Build subprocess command
        cmd = [command, path2script] + args

        # check_output will run the command and store to result
        activity_score = subprocess.check_output(cmd, universal_newlines=True)
        return activity_score


    def runforefficacy(dirname):
        import subprocess
        command = 'Rscript'
        path2script = os.getcwd() + '/models/efficacy_predict.R'

        # Variable number of args in a list
        args = [dirname]

        # Build subprocess command
        cmd = [command, path2script] + args

        # check_output will run the command and store to result
        efficacy = subprocess.check_output(cmd, universal_newlines=True)
        return efficacy


    def runforpotency(dirname):
        import subprocess
        command = 'Rscript'
        path2script = os.getcwd() + '/models/potency_predict.R'

        # Variable number of args in a list
        args = [dirname]

        # Build subprocess command
        cmd = [command, path2script] + args

        # check_output will run the command and store to result
        potency = subprocess.check_output(cmd, universal_newlines=True)
        return potency

    os.system('java -jar PaDEL-Descriptor.jar -2d -3d -dir ' + 'media/' + dirname + '/ -file ' + 'media/' + dirname + '/res.csv')
    os.system('python 1.py ' + dirname)
    os.system('Rscript ' + os.getcwd() + '/models/testingNewDataSet.R ' + dirname)
    os.system('python 2.py ' + dirname)
    # os.system('python 3.py ' + dirname)
    command = 'Rscript'
    path2script = '5.R'

    # Variable number of args in a list
    args = [dirname]

    # Build subprocess command
    cmd = [command, path2script] + args

    # check_output will run the command and store to result
    x = subprocess.check_output(cmd, universal_newlines=True)
    print(x)
    st = True
    email = data.objects.filter(id=int(dirname))[0].email
    if x == 'Active':
        os.system('Rscript ' + os.getcwd() + '/models/activity_test.R ' + dirname)
        activity_score = runforactivity_score(dirname)
        os.system('Rscript ' + os.getcwd() + '/models/efficacy_test.R ' + dirname)
        efficacy = runforefficacy(dirname)
        os.system('Rscript ' + os.getcwd() + '/models/potency_test.R ' + dirname)
        potency = runforpotency(dirname)
        print(activity_score, potency, efficacy)
        msg = 'Activity score is ' + str(activity_score) + '\n' + 'Potency is ' + str(potency) + '\n' + 'Efficacy is' + str(efficacy)
        file.write(msg)
        file.close()
        # sendmail(email, msg)
        sendmailwithattachments(email, dirname)
    else:
        sendmail(email, 'Molecule is inactive')
    print(x)
    i.status = True
    i.activity_score = activity_score
    i.efficacy = efficacy
    i.potency = potency
    i.save()
