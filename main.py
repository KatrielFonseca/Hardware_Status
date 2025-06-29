import platform

# Verifica se o sistema operacional é Windows
if platform.system() != "Windows":
    print("Este script foi desenvolvido para Windows utilizando WMI. Execute-o em um sistema Windows.")
    exit()

try:
    import wmi
except ImportError:
    print("O módulo WMI não está instalado. Por favor, instale-o usando 'pip install wmi'.")
    exit()


def obter_temperatura_cpu(w):
    """
    Tenta obter a temperatura da CPU usando a classe MSAcpi_ThermalZoneTemperature.
    Nem todos os sistemas retornam esses dados via WMI.
    """
    try:
        zonas = w.MSAcpi_ThermalZoneTemperature()
        for zona in zonas:
            # A temperatura é retornada em décimos de Kelvin.
            temp_celsius = (int(zona.CurrentTemperature) / 10) - 273.15
            return temp_celsius
    except Exception:
        pass
    return None


def main():
    w = wmi.WMI()

    # Informações do Processador
    print("=== Processador ===")
    for cpu in w.Win32_Processor():
        print("Fabricante:", cpu.Manufacturer)
        print("Frequência: {} MHz".format(cpu.CurrentClockSpeed))
        temp_cpu = obter_temperatura_cpu(w)
        if temp_cpu is not None:
            print("Temperatura: {:.2f} °C".format(temp_cpu))
        else:
            print("Temperatura: Não disponível")
        # Considera somente o primeiro processador caso haja mais de um
        break

    # Informações da Memória RAM
    print("\n=== Memória RAM ===")
    fabricantes_ram = set()
    capacidade_total_bytes = 0
    for mem in w.Win32_PhysicalMemory():
        if mem.Manufacturer:
            fabricantes_ram.add(mem.Manufacturer.strip())
        if mem.Capacity:
            capacidade_total_bytes += int(mem.Capacity)
    print("Fabricante(s):", ", ".join(fabricantes_ram) if fabricantes_ram else "Não disponível")

    # Obter informações de uso de memória via Win32_OperatingSystem
    os_info = w.Win32_OperatingSystem()[0]
    total_mem_kb = int(os_info.TotalVisibleMemorySize)  # em KB
    free_mem_kb = int(os_info.FreePhysicalMemory)  # em KB
    used_mem_kb = total_mem_kb - free_mem_kb
    print("Capacidade Máxima: {:.2f} GB".format(capacidade_total_bytes / (1024 ** 3)))
    # Converte KB para GB (1 GB = 1024*1024 KB)
    print("Capacidade Usada: {:.2f} GB".format(used_mem_kb / (1024 ** 2)))

    # Informações da Placa de Vídeo
    print("\n=== Placa de Vídeo ===")
    for gpu in w.Win32_VideoController():
        print("Fabricante:", gpu.AdapterCompatibility)
        if gpu.AdapterRAM:
            print("Capacidade: {:.2f} GB".format(int(gpu.AdapterRAM) / (1024 ** 3)))
        else:
            print("Capacidade: Não disponível")
        # A maioria dos sistemas não fornece a temperatura da GPU via WMI
        if hasattr(gpu, "CurrentTemperature") and gpu.CurrentTemperature is not None:
            try:
                temp_gpu = (int(gpu.CurrentTemperature) / 10) - 273.15
                print("Temperatura: {:.2f} °C".format(temp_gpu))
            except Exception:
                print("Temperatura: Não disponível")
        else:
            print("Temperatura: Não disponível")
        # Considera somente a primeira placa de vídeo encontrada
        break

    # Informações da Placa Mãe
    print("\n=== Placa Mãe ===")
    for base in w.Win32_BaseBoard():
        print("Fabricante:", base.Manufacturer)
        # Considera somente a primeira placa mãe encontrada
        break


if __name__ == '__main__':
    main()
