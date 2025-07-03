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

todos_os_hardwares = []
capacidade_total = 0
porcentegem_uso = 0


def main():
    try:


        w = wmi.WMI()

        # Informações do Processador
        for cpu in w.Win32_Processor():
            todos_os_hardwares.append(HardwareStatus("Processador", cpu.Manufacturer,cpu.Name,cpu.CurrentClockSpeed,cpu.NumberOfCores,""))
        #-----------------------------------------------------------------------------------------------------------------------

        # Informações da Placa Mãe
        for b in w.Win32_BaseBoard():
            todos_os_hardwares.append(HardwareStatus("Placa mãe", b.Manufacturer, b.product, "", "", ""))



        # Informações da Placa de Vídeo
        for gpu in w.Win32_VideoController():
            todos_os_hardwares.append(HardwareStatus("GPU", gpu.Name,"","","",gpu.AdapterRAM / (-1024 ** 3)))

        # -----------------------------------------------------------------------------------------------------------------------



        # Informações da Memória RAM
        for mem in w.Win32_PhysicalMemory():
            todos_os_hardwares.append(HardwareStatus("RAM", mem.Manufacturer.strip(), "", "", "", int(mem.Capacity) / (1024 ** 3)))

        capacidade_total = 0
        for aux in todos_os_hardwares:
            if aux.hardware == "RAM":
                capacidade_total += aux.capacidade
        porcentegem_uso = (((capacidade_total - float(w.Win32_OperatingSystem()[0].FreePhysicalMemory) / 1024 ** 2) / capacidade_total) * 100)

        # -----------------------------------------------------------------------------------------------------------------------

        '''for i in todos_os_hardwares:
            HardwareStatus.Imprimir_Hardware(i)
            print("\n")
        print("Capacidade total RAMs: " + str(capacidade_total) + " GB")
        print("Porcentegem uso RAM: {:.2f} %".format(porcentegem_uso))'''




    except Exception as e:
        print(f"Ocorreu um erro ao coletar informações do sistema: {e}")





if __name__ == '__main__':
    main()
