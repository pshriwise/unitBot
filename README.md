*******
UnitBot
*******


`unitBot` is a slack bot that converts imperial units into european units, and vice
versa.

To run one needs a `pivate.py` file which contains (see example below):
- api token,
- a user name or channel name to send the error messages.

```
API_TOKEN= 'my_slack_group_token'
ERRORS_TO= 'where_to_send_erorr'
```
**Note**: The API token can also provided the API token in a
`SLACKBOT_API_TOKEN` environment variable.

`unitBot` depends on the `quantities` python library as well as slackbot.

The `unibot_plugins.py` contains the parameters of the `unitbot`.

To add new unit conversion, add lines in the ` unit_dict`, using the following
syntax: `'X': [q.X, q.Y],`, where `X` represents the unit symbol that `uniBot`
should recognize, `q.X` the corresponding `quantities` unit, and `q.Y` the
`quantities` output unit.


**Note**: if using a non absolute value (such as `Celcius`), the conversion might need some
offset adjustment (see Celcius to Fahraneit conversion).
