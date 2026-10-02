import pyvisa

class Instrument:
    def __init__(self):
        pass
    def connect(self, ip):
        try:
            ip = "192.168.0.2"
            rm = pyvisa.ResourceManager()
            rm.list_resources()
            self.smf = rm.open_resource('TCPIP::'+ip+'::inst0::INSTR')
            self.smf.timeuout = 5000
            answer = self.smf.query('*IDN?')
            print(answer)
            self.connected = "Rohde&Schwarz" in answer
        except:
            self.connected = False

            
    def config_Pulse_Mod_Gen(self, value):
        if self.connected:
            self.smf.write('[:SOURce<hw>]:PGENerator:OUTPut[:STATe] ' + str(value))
        else:
            return None

    def config_Modulation(self):
        return None

    def config_RF_Frequency(self, freq, phase, output_state):
        if self.connected:
            self.smf.write('SOURce:FREQuency:CW ' + str(freq))
            self.smf.write('SOURce:PHASe ' + str(phase))
            self.smf.write(':OUTPut<hw>[:STATe] ' + str(output_state))
        return None
    def config_Level_Control(self):
        return None
