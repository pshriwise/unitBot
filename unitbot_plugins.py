from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
import re


F_to_C_fix = -32.0*5.0/9.0
C_to_F_fix = +32.0*5.0/9.0

def convert(val, to):
    input_units = val.units
    if(input_units == q.degC and to == q.degF):
        val += F_to_C_fix * q.degF
    val.units = to
    if(input_units == q.degF and to == q.degC):
        val += C_to_F_fix * q.degC
    return val

" Temperature conversion "

F_match = '(.*)F'
@respond_to(F_match, re.IGNORECASE)
@listen_to(F_match, re.IGNORECASE)
def FtoC(message,incoming_message):
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("f",""))
    except:
        return
    val = convert(val_in * q.degF, to = q.degC)
    message.reply("{}F corresponds to {:.2f}C!".format(val_in, float(val.magnitude)))

C_match = '(.*)C'
@respond_to(C_match, re.IGNORECASE)
@listen_to(C_match, re.IGNORECASE)
def CtoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.degF, to = q.degC) 
    message.reply("{}C corresponds to {:.2f}F!".format(val_in, float(val.magnitude)))

" Distance "
m_match = '(.*)m'
@respond_to(m_match, re.IGNORECASE)
@listen_to(m_match, re.IGNORECASE)
def MtoInch(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.m, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(val_in, float(val.magnitude)))

cm_match = '(.*)cm'
@respond_to(cm_match, re.IGNORECASE)
@listen_to(cm_match, re.IGNORECASE)
def InchtoM(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.cm, to = q.inch) 
    message.reply("{} m corresponds to {:.2f} \"!".format(val_in, float(val.magnitude)))

inch_match = '(.*)"'
inch_match1 = '(.*)in'
@respond_to(inch_match, re.IGNORECASE)
@listen_to(inch_match, re.IGNORECASE)
@respond_to(inch_match1, re.IGNORECASE)
@listen_to(inch_match1, re.IGNORECASE)
def CMtoInch(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.inch, to = q.m) 
    message.reply("{} \" corresponds to {:.2f} m!".format(val_in, float(val.magnitude)))

mile_match = '(.*)mile'
@respond_to(mile_match, re.IGNORECASE)
@listen_to(mile_match, re.IGNORECASE)
def MiletoKM(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.mile, to = q.km) 
    message.reply("{} mile corresponds to {:.2f} km!".format(val_in, float(val.magnitude)))

km_match = '(.*)km'
@respond_to(km_match, re.IGNORECASE)
@listen_to(km_match, re.IGNORECASE)
def KMtoMile(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        val_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    val = convert(val_in * q.km, to = q.mile) 
    message.reply("{} km corresponds to {:.2f} mile!".format(val_in, float(val.magnitude)))
