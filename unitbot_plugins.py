from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
from quantities import markup
import re

#allows nice output from quantities
markup.config.use_unicode = True

approved_channels = ['unit_test']

# Fix conversion when using relative unit (as Celcius)
F_to_C_fix = -32.0*5.0/9.0
C_to_F_fix = +32.0

# Convert the quantity in the output unit
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

# Form the output message
def generate_ouput(value, input_units, output_units):
    quantity_in = value * input_units
    quantity_out = convert(quantity_in.copy(), to = output_units)
    quantity_out = round(quantity_out,2)
    output = "{:} corresponds to {:}!".format(quantity_in, quantity_out)
    return output

# Not sure this is anymore necessary (with the new regular expression)
def parse_value(message_content, replace_string):
    replace_string = replace_string.lower()
    val_in = message_content.split()[-1].lower()
    val_in = val_in.replace(replace_string,"")
    return float(val_in)

# unit dictionnary, this is what we know hoe to convert...
unit_dict = {
    'F' : {q.degF, q.degC},
    'C' : {q.degC, q.degF},
    'm' : {q.m, q.inch},
    'cm': {q.cm, q.inch},
    'in': {q.inch, q.m},
    '"': {q.inch, q.m},
    'km': {q.km, q.mile},
    'mile': {q.mile, q.km}
    }

# triggered if a msg contain '"number""something"' or '"number"" ""something"'
F_match = '(\d{1,}) (.*)'
F_match1 = '(\d{1,})(.*)'
@respond_to(F_match, re.IGNORECASE)
@listen_to(F_match, re.IGNORECASE)
@respond_to(F_match1, re.IGNORECASE)
@listen_to(F_match1, re.IGNORECASE)
def find_match(message, value, unit):
    try:
        val_in = float(value)
        # if unit is known grab the in/out unit and do the conversion...
        if unit in unit_dict:
            in_unit, out_unit = unit_dict[unit]
            out_str = generate_ouput(val_in, in_unit, out_unit)
        else:
            return
    except:
        return
    dispatch(message, out_str)
            

