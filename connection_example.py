
"""
Find the instruments in your environment with the defined VISA implementation
"""

import RsInstrument

# In the optional parameter visa_select you can use e.g.: 'rs' or 'ni'
# Rs Visa also finds any NRP-Zxx USB sensors
instr_list = RsInstrument.list_resources('?*', 'rs')
print(instr_list)

"""
Basic example on how to use the RsInstrument module for remote-controlling your VISA instrument
Preconditions:
    - Installed RsInstrument Python module Version 1.50.0 or newer from pypi.org
    - Installed VISA e.g. R&S Visa 5.12 or newer
"""



# A good practice is to assure that you have a certain minimum version installed
RsInstrument.assert_minimum_version('1.50.0')
resource_string_HISLIP = 'TCPIP::169.254.1.20::hislip0'
resource_string_VXI11 = 'TCPIP::169.254.1.20::INSTR'

# Initializing the session
instr = RsInstrument(resource_string_HISLIP)
# instr = RsInstrument(resource_string_VXI11)

idn = instr.query_str('*IDN?')
print(f"\nHello, I am: '{idn}'")
print(f'RsInstrument driver version: {instr.driver_version}')
print(f'Visa manufacturer: {instr.visa_manufacturer}')
print(f'Instrument full name: {instr.full_instrument_model_name}')
print(f'Instrument installed options: {",".join(instr.instrument_options)}')

# Close the session
instr.close()

"""
Basic string write_str / query_str
"""



# A good practice is to assure that you have a certain minimum version installed
RsInstrument.assert_minimum_version('1.50.0')
resource_string_HISLIP = 'TCPIP::169.254.1.20::hislip0'
resource_string_VXI11 = 'TCPIP::169.254.1.20::INSTR'

instr = RsInstrument(resource_string_HISLIP, True, True)
instr.write_str('*RST')
response = instr.query_str('*IDN?')
print(response)

# Close the session
instr.close()

"""
Basic string write_str / query_str
"""



# A good practice is to assure that you have a certain minimum version installed
RsInstrument.assert_minimum_version('1.50.0')
resource_string_HISLIP = 'TCPIP::169.254.1.20::hislip0'
resource_string_VXI11 = 'TCPIP::169.254.1.20::INSTR'

instr = RsInstrument(resource_string_HISLIP, True, True)
# Timeout in milliseconds
instr.visa_timeout = 3000

instr.reset()
print(instr.idn_string)

# Close the session
instr.close()

"""
Basic string write_xxx / query_xxx
"""



# A good practice is to assure that you have a certain minimum version installed
RsInstrument.assert_minimum_version('1.50.0')
resource_string_HISLIP = 'TCPIP::169.254.1.20::hislip0'
resource_string_VXI11 = 'TCPIP::169.254.1.20::INSTR'

instr = RsInstrument(resource_string_HISLIP, True, True)
instr.visa_timeout = 5000
instr.instrument_status_checking = True
# Default value after init is False
instr.opc_query_after_write = True

instr.reset()
print(instr.idn_string)
instr.write('FREQ 5GHz')

# instr.write_int('SWEEP:COUNT ', 10)  # sending 'SWEEP:COUNT 10'
# instr.write_bool('SOURCE:RF:OUTPUT:STATE ', True)  # sending 'SOURCE:RF:OUTPUT:STATE ON'
# instr.write_float('SOURCE:RF:FREQUENCY ', 1E9)  # sending 'SOURCE:RF:FREQUENCY 1000000000'

# sc = instr.query_int('SWEEP:COUNT?')  # returning integer number sc=10
# out = instr.query_bool('SOURCE:RF:OUTPUT:STATE?')  # returning boolean out=True
# freq = instr.query_float('SOURCE:RF:FREQUENCY?')  # returning float number freq=1E9

# Close the session
instr.close() 