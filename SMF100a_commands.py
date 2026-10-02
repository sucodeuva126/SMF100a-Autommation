import pyvisa

class Instrument:
    def __init__(self):
        pass
    def connect(self, ip, timeout):
        try:
            rm = pyvisa.ResourceManager()
            rm.list_resources()
            self.smf = rm.open_resource('TCPIP::'+ip+'::inst0::INSTR')
            self.smf.timeuout = timeout
            answer = self.smf.query('*IDN?')
            print(answer)
            self.connected = "Rohde&Schwarz" in answer
        except:
            print("Connection Failed")
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
            if "output_state" in kwargs: self.smf.write('OUTPut:STATe ' + str(kwargs["output_state"]))
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
    
    def config_Pulse_Train(self, **kwargs):
        if self.connected:

            # Define o diretório padrão de listas
            if "directory" in kwargs:
                self.smf.write(
                    "MMEMory:CDIRectory " + str(kwargs["directory"])
                )

            # --- MÉTODOS DE DEFINIÇÃO DIRETA (Sem arquivo CSV) ---
            if "train_file" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:SELect "
                    + f"'{str(kwargs['train_file'])}'"
                )

            if "on_times" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:ONTime "
                    + str(kwargs["on_times"])
                )

            if "off_times" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:OFFTime "
                    + str(kwargs["off_times"])
                )

            if "repetitions" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:REPetition "
                    + str(kwargs["repetitions"])
                )

            # --- MÉTODOS DE IMPORTAÇÃO DE ARQUIVO ASCII/CSV (DEXChange) ---
            if "import_ascii_file" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:MODE IMPort"
                )

            if "ascii_ext" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:AFILe:EXTension "
                    + str(kwargs["ascii_ext"])
                )

            if "col_separator" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:AFILe:SEParator:COLumn "
                    + str(kwargs["col_separator"])
                )

                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:AFILe:SELect "
                    + f"'{str(kwargs['import_ascii_file'])}'"
                )

            if "target_train_file" in kwargs:
                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:SELect "
                    + f"'{str(kwargs['target_train_file'])}'"
                )

                self.smf.write(
                    "SOURce:PULM:TRAin:DEXChange:EXECute"
                )

            # --- ESTADO E MODO DE MODULAÇÃO ---
            if "pulse_source" in kwargs:
                self.smf.write(
                    "SOURce:PULM:SOURce "
                    + str(kwargs["pulse_source"])
                )  # ex: INTernal ou EXTernal

            if "pulse_mode" in kwargs:
                self.smf.write(
                    "SOURce:PULM:MODE "
                    + str(kwargs["pulse_mode"])
                )  # ex: PTRain, SINGle ou DOUBle

            if "pulm_state" in kwargs:
                self.smf.write(
                    "SOURce:PULM:STATe "
                    + str(kwargs["pulm_state"])
            )

            return None



SMF = Instrument()
SMF.connect("192.168.0.2", 5000)
SMF.config_RF_Frequency(freq = 200000000, output_state = 1)
# Importa o arquivo CSV de pulsos e ativa a modulação no gerador
# 1. Envia o arquivo do PC para o gerador
pc_path = "/home/gustavohenrique/SMF100A_control/pulso_quadrado.csv"                       # Arquivo no seu computador
remote_path = "/var/user/Lists/pulso_quadrado.csv"  # Destino no gerador



