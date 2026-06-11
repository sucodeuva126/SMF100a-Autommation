import pyvisa
smfTCPIP = "192.168.0.2"
rm = pyvisa.ResourceManager()
rm.list_resources()
smf = rm.open_resource('TCPIP::'+smfTCPIP+'::inst0::INSTR')
print(smf.query('*IDN?'))
smf.close()


class Pulse_Mod_Gen():
    def set_Pulse_output(value):
        smf.write('[:SOURce<hw>]:PGENerator:OUTPut[:STATe] ' + str(value))
class Modulation():
    pass
class RF_Frequency():
    def set_frequency(value): 
        smf.write('SOURce:FREQuency:CW ' + str(value))
    def set_phase(value):
        smf.write('SOURce:PHASe ' + str(value))
    def set_RFoutput(value):
        smf.write(':OUTPut<hw>[:STATe] ' + str(value))
    pass
class Level_Control():
    pass
