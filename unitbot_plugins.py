from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
import re


F_to_C_fix = -32.0*5.0/9.0
C_to_F_fix = +32.0*5.0/9.0

def convert(val, to):
    val.units = to
    return val


" Temperature conversion "

@respond_to('(.*)F', re.IGNORECASE)
def temptoC(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("f",""))
    except:
        return
    temp = convert(temp_in * q.degF, to = q.degC) 
    temp += C_to_F_fix * q.degC
    message.reply("{}°F corresponds to {:.2f}°C!".format(temp_in, float(temp.magnitude)))

@respond_to('(.*)C', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp_in += C_to_F_fix
    temp = convert(temp_in * q.degC, to = q.degF) 
    message.reply("{}°C corresponds to {:.2f}°F!".format(temp_in, float(temp.magnitude)))


" Distance "


@respond_to('(.*)m', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = convert(temp_in * q.m, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(temp_in, float(temp.magnitude)))

@respond_to('(.*)cm', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = convert(temp_in * q.cm, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(temp_in, float(temp.magnitude)))

@respond_to('(.*)"', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = convert(temp_in * q.inch, to = q.m) 
    message.reply("{} \" corresponds to {:.2f} m!".format(temp_in, float(temp.magnitude)))

@respond_to('(.*)mile', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = convert(temp_in * q.mile, to = q.km) 
    message.reply("{} mile corresponds to {:.2f} km!".format(temp_in, float(temp.magnitude)))

@respond_to('(.*)km', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = convert(temp_in * q.km, to = q.mile) 
    message.reply("{} km corresponds to {:.2f} mile!".format(temp_in, float(temp.magnitude)))
