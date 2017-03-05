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
def FtoC(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("f",""))
    except:
        return
    val = convert(val_in * q.degF, to = q.degC) 
    val += C_to_F_fix * q.degC
    message.reply("{}°F corresponds to {:.2f}°C!".format(val_in, float(val.magnitude)))

@respond_to('(.*)C', re.IGNORECASE)
def CtoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val_in += C_to_F_fix
    val = convert(val_in * q.degC, to = q.degF) 
    message.reply("{}°C corresponds to {:.2f}°F!".format(val_in, float(val.magnitude)))


" Distance "


@respond_to('(.*)m', re.IGNORECASE)
def MtoInch(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.m, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(val_in, float(val.magnitude)))

@respond_to('(.*)cm', re.IGNORECASE)
def InchtoM(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.cm, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(val_in, float(val.magnitude)))

@respond_to('(.*)"', re.IGNORECASE)
def CMtoInch(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.inch, to = q.m) 
    message.reply("{} \" corresponds to {:.2f} m!".format(val_in, float(val.magnitude)))

@respond_to('(.*)mile', re.IGNORECASE)
def MiletoKM(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.mile, to = q.km) 
    message.reply("{} mile corresponds to {:.2f} km!".format(val_in, float(val.magnitude)))

@respond_to('(.*)km', re.IGNORECASE)
def KMtoMile(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.km, to = q.mile) 
    message.reply("{} km corresponds to {:.2f} mile!".format(val_in, float(val.magnitude)))
