from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
from quantities import markup
import re

#allows nice output from quantities
markup.config.use_unicode = True

approved_channels = ['unit_test']

F_to_C_fix = -32.0*5.0/9.0
C_to_F_fix = +32.0

def convert(val, to):
    input_units = val.units.copy()
    val.units = to
    if(input_units == q.degC and to == q.degF):
        val += C_to_F_fix * q.degF
    if(input_units == q.degF and to == q.degC):
        val += F_to_C_fix * q.degC
    return val

def is_channel(message):
    return ('is_channel' in message.channel._body.keys() and
            message.channel._body['is_channel'] == True)

def is_approved(message):
    return message.channel._body['name'] in approved_channels

def dispatch(message, output):
    #see if this came from a channel (listen_to)
    if is_channel(message):
        #make sure the channel is in approved list for posting
        if is_approved(message): message.send(output)
    else:
        message.reply(output)

def generate_ouput(value, input_units, output_units):
    quantity_in = value * input_units
    quantity_out = convert(quantity_in.copy(), to = output_units)
    quantity_out = round(quantity_out,2) * output_units
    output = "{:} corresponds to {:}!".format(quantity_in, quantity_out)
    return output

def parse_value(message_content, replace_string):
    replace_string = replace_string.lower()
    val_in = message_content.split()[-1].lower()
    val_in = val_in.replace(replace_string,"")
    return float(val_in)
    
" Temperature conversion "

F_match = '(.*)F'
@respond_to(F_match, re.IGNORECASE)
@listen_to(F_match, re.IGNORECASE)
def FtoC(message,incoming_message):
    try:
        val_in = parse_value(incoming_message, "F")
        out_str = generate_ouput(val_in, q.degF, q.degC)
    except:
        return
    dispatch(message, out_str)

C_match = '(.*)C'
@respond_to(C_match, re.IGNORECASE)
@listen_to(C_match, re.IGNORECASE)
def CtoF(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "C")
        out_str = generate_ouput(val_in, q.degC, q.degF)
    except:
        return
    dispatch(message, out_str)

" Distance "
m_match = '(.*)m'
@respond_to(m_match, re.IGNORECASE)
@listen_to(m_match, re.IGNORECASE)
def MtoInch(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "m")
        out_str = generate_ouput(val_in, q.m, q.inch)
    except:
        return
    dispatch(message, out_str)

cm_match = '(.*)cm'
@respond_to(cm_match, re.IGNORECASE)
@listen_to(cm_match, re.IGNORECASE)
def CMtoInch(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "cm")
        out_str = generate_ouput(val_in, q.cm, q.inch)
    except:
        return
    dispatch(message, out_str)

inch_match = '(.*)"'
inch_match1 = '(.*)in'
@respond_to(inch_match, re.IGNORECASE)
@listen_to(inch_match, re.IGNORECASE)
@respond_to(inch_match1, re.IGNORECASE)
@listen_to(inch_match1, re.IGNORECASE)
def CMtoInch(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "in")
        out_str = generate_ouput(val_in, q.inch, q.cm)
    except:
        pass
    try:
        val_in = parse_value(incoming_message, "\"")
        out_str = generate_ouput(val_in, q.inch, q.cm)
    except:
        return
    dispatch(message, out_str)

mile_match = '(.*)mile'
@respond_to(mile_match, re.IGNORECASE)
@listen_to(mile_match, re.IGNORECASE)
def MiletoKM(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "mile")
        out_str = generate_ouput(val_in, q.mile, q.km)
    except:
        return
    dispatch(message, out_str)

km_match = '(.*)km'
@respond_to(km_match, re.IGNORECASE)
@listen_to(km_match, re.IGNORECASE)
def KMtoMile(message, incoming_message):
    try:
        val_in = parse_value(incoming_message, "mile")
        out_str = generate_ouput(val_in, q.km, q.mile)
    except:
        return
    dispatch(message, out_str)
