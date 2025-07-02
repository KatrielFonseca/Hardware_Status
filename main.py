import platform

# Verifica se o sistema operativo é Windows
if platform.system() != "Windows":
    print("Este script foi desenvolvido para Windows utilizando WMI. Execute-o em um sistema Windows.")
    exit()

try:
    import wmi
except ImportError:
    print("O módulo WMI não está instalado. Por favor, instale-o usando 'pip install wmi'.")
    exit()


class HardwareStatus:
    def __init__(self, hardware, fabricante, modelo, frequencia, nucleos, capacidade,):
        self.hardware = hardware
        self.fabricante = fabricante
        self.modelo = modelo
        self.frequencia = frequencia
        self.nucleos = nucleos
        self.capacidade = capacidade

    def Imprimir_Hardware(self):
        for chave , valor in self.__dict__.items():
            if valor == "":
                continue
            print(f"{chave} : {valor}")


def main():
    try:
        w = wmi.WMI()

        # Informações do Processador

        for cpu in w.Win32_Processor():
            proc = HardwareStatus("Processador", cpu.Manufacturer,cpu.Name,cpu.CurrentClockSpeed,cpu.NumberOfCores,"")
            HardwareStatus.Imprimir_Hardware(proc)
        #-----------------------------------------------------------------------------------------------------------------------

        print("\n")
        # Informações da Memória RAM
        rams = set()
        for mem in w.Win32_PhysicalMemory():
            rams.add(HardwareStatus("RAM", mem.Manufacturer.strip(),"","","",int(mem.Capacity)/(1024 ** 3)))
        capacidade_total = 0
        for aux in rams:
            HardwareStatus.Imprimir_Hardware(aux)
            capacidade_total += aux.capacidade
        print("Capacidade Máxima: ", capacidade_total, "GB")
        print("Porcentagem de Uso: {:.2f}%".format(((capacidade_total - float(w.Win32_OperatingSystem()[0].FreePhysicalMemory)/1024**2)/capacidade_total)*100))
        # -----------------------------------------------------------------------------------------------------------------------

        print("\n")


        # Informações da Placa de Vídeo
        gpus = set()
        for gpu in w.Win32_VideoController():
            gpus.add(HardwareStatus("GPU", gpu.Name,"","","",gpu.AdapterRAM / (-1024 ** 3)))

        for aux in gpus:
            HardwareStatus.Imprimir_Hardware(aux)
        # -----------------------------------------------------------------------------------------------------------------------

            print("\n")

        # Informações da Placa Mãe
        for b in w.Win32_BaseBoard():
            placa_mae = HardwareStatus("Placa mãe", b.Manufacturer, b.product, "", "", "")
            HardwareStatus.Imprimir_Hardware(placa_mae)




    except Exception as e:
        print(f"Ocorreu um erro ao coletar informações do sistema: {e}")


    todos_os_hardwares = set()


if __name__ == '__main__':
    main()
