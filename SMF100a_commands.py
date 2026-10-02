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

    def config_RF_Frequency(self, **kwargs):
        if self.connected:
            if "freq" in kwargs: self.smf.write('SOURce:FREQuency:CW ' + str(kwargs["freq"]))
            if "freq_offset" in kwargs: self.smf.write('SOURce:FREQuency:OFFSet' + str(kwargs["freq_offset"]))
            if "reset_phase_ref" in kwargs: self.smf.write('SOURce:PHASe;:REFerence ' + str(kwargs["reset_phase_ref"]))
            if "phase" in kwargs: self.smf.write('SOURce:PHASe ' + str(kwargs["phase"]))
            if "output_state" in kwargs: self.smf.write(':OUTPut<hw>[:STATe] ' + str(kwargs["output_state"]))
        return None
    def config_Level_Control(self):
        return None
