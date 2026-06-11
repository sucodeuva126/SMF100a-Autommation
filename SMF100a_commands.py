import pyvisa
smfIP = "10.10.10.10"
rm = pyvisa.ResourceManager()
rm.list_resources()
smf = rm.open_resource('TCPIP::'+smfIP+'::inst0::INSTR')
print(smf.query('*IDN?'))
smf.close()