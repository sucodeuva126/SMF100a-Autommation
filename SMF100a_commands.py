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

    def config_Modulation(self, **kwargs):
        if self.connected:
            # Estado Global
            if "mod_state" in kwargs:self.smf.write("SOURce:MODulation:STATe " + str(kwargs["mod_state"]))

            # AM
            if "am_state" in kwargs:self.smf.write("SOURce:AM:STATe " + str(kwargs["am_state"]))
            if "am_depth" in kwargs:self.smf.write("SOURce:AM:DEPTh " + str(kwargs["am_depth"]))
            if "am_source" in kwargs:self.smf.write("SOURce:AM:SOURce " + str(kwargs["am_source"]))

            # FM
            if "fm_state" in kwargs:self.smf.write("SOURce:FM:STATe " + str(kwargs["fm_state"]))
            if "fm_dev" in kwargs:self.smf.write("SOURce:FM:DEViation " + str(kwargs["fm_dev"]))
            if "fm_source" in kwargs:self.smf.write("SOURce:FM:SOURce " + str(kwargs["fm_source"]))

            # PM
            if "pm_state" in kwargs:self.smf.write("SOURce:PM:STATe " + str(kwargs["pm_state"]))
            if "pm_dev" in kwargs:self.smf.write("SOURce:PM:DEViation " + str(kwargs["pm_dev"]))
            if "pm_source" in kwargs:self.smf.write("SOURce:PM:SOURce " + str(kwargs["pm_source"]))

            # Modulação por Pulso (PULM)
            if "pulm_state" in kwargs:self.smf.write("SOURce:PULM:STATe " + str(kwargs["pulm_state"]))
            if "pulm_width" in kwargs:self.smf.write("SOURce:PULM:WIDTh " + str(kwargs["pulm_width"]))
            if "pulm_period" in kwargs:self.smf.write("SOURce:PULM:PERiod " + str(kwargs["pulm_period"]))
            if "pulm_source" in kwargs:self.smf.write("SOURce:PULM:SOURce " + str(kwargs["pulm_source"]))
        return None

    def config_RF_Frequency(self, **kwargs):
        if self.connected:
            if "freq" in kwargs: self.smf.write('SOURce:FREQuency:CW ' + str(kwargs["freq"]))
            if "freq_offset" in kwargs: self.smf.write('SOURce:FREQuency:OFFSet' + str(kwargs["freq_offset"]))
            if "reset_phase_ref" in kwargs: self.smf.write('SOURce:PHASe;:REFerence ' + str(kwargs["reset_phase_ref"]))
            if "phase" in kwargs: self.smf.write('SOURce:PHASe ' + str(kwargs["phase"]))
            if "output_state" in kwargs: self.smf.write(':OUTPut<hw>[:STATe] ' + str(kwargs["output_state"]))
        return None
    
    def config_RF_Level(self, **kwargs):
        if self.connected:
            if "level" in kwargs: self.smf.write("SOURce:POWer:AMPLitude " + str(kwargs["level"]))
            if "level_offset" in kwargs:self.smf.write("SOURce:POWer:OFFSet " + str(kwargs["level_offset"]))
            if "level_limit" in kwargs:self.smf.write("SOURce:POWer:LIMit:AMPLitude " + str(kwargs["level_limit"]))
            if "level_mode" in kwargs:self.smf.write("SOURce:POWer:MODE " + str(kwargs["level_mode"]))
            if "alc_state" in kwargs:self.smf.write("SOURce:POWer:ALC:STATe " + str(kwargs["alc_state"]))
            if "alc_sonce" in kwargs:self.smf.write("SOURce:POWer:ALC:SONCe")
            if "attenuator_mode" in kwargs:self.smf.write("OUTPut:AMODe " + str(kwargs["attenuator_mode"]))
            if "output_state" in kwargs:self.smf.write("OUTPut:STATe " + str(kwargs["output_state"]))
        return None
