import subprocess
import sys
import os
# from webapp.models import status
activity_score = ''
potency = ''
efficacy = ''


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
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
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
    attachment = open(os.getcwd() + '/media/' + dirname + '/results.txt', "rb")

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


dirname = sys.argv[1]
email = sys.argv[2]
command = 'Rscript'
path2script = '5.R'

# Variable number of args in a list
args = [dirname]

# Build subprocess command
cmd = [command, path2script] + args

# check_output will run the command and store to result
x = subprocess.check_output(cmd, universal_newlines=True)
print(x)
file = open(os.getcwd() + '/media/' + dirname + '/results.txt', 'w')
if x == 'Active':
    os.system('Rscript ' + os.getcwd() + '/models/activity_test.R ' + dirname)
    activity_score = runforactivity_score(dirname)
    os.system('Rscript ' + os.getcwd() + '/models/efficacy_test.R ' + dirname)
    efficacy = runforefficacy(dirname)
    os.system('Rscript ' + os.getcwd() + '/models/potency_test.R ' + dirname)
    potency = runforpotency(dirname)
    print(activity_score, potency, efficacy)
    msg = 'Activity score is ' + str(activity_score) + '\n' + 'Potency is ' + str(potency) + '\n' + 'Efficacy is ' + str(
        efficacy)
    msg = "The Molecule you submitted for evaluation is found to be active. If you are satisfied with the results " \
          "do support us or contact us if not for a feedback.\n" + msg + "\n\n\n\n"
    footer = "Contact details:\n Rohan Piplani \n piplani.rohan@gmail.com\n +919592983965\n"
    msg += footer
    file.write(msg)
    file.close()
    sendmail(email, msg)
    sendmailwithattachments(email, dirname)

else:
    print('Molecule is inactive')
    msg = 'The Molecule you submitted for evaluation is found to be inactive. If you are satisfied with the ' \
          'results do support us or contact us if not for a feedback.\n\n\n\n'
    footer = "Contact details:\n Rohan Piplani \n piplani.rohan@gmail.com\n +919592983965\n"
    msg += footer
    sendmail(email, msg)


# saving results into models

# arr = status.objects.filter(status_id=int(dirname))
# print(arr[0].status)
# arr[0].status = True
# arr[0].save()