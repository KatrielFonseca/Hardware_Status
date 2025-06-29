import cpuinfo
import psutil
import GPUtil
import os
import re
import time


class SystemInfos(self):
	"""atributos do objeto"""
	def __init__(self):
		self.info_processador = self.get_info_processador()
		self.info_memoria = self.get_info_memoria()
		self.info_gpu = self.get_info_gpu()
		self.info_motherboard = self.get_info_motherboard()

		"""Método que recolhe informações do processador"""
	def get_info_processador (self):
		info = cpuinfo.get_cpu_info()
		nome = info['brand_raw']

		return {"nome": nome,
		 "temperatura": self.get_temperatura_cpu()}


		 """Método que recolhe informações da memória"""
	def get_info_memoria(self):
		memoria = psutil.virtual_memory()
		total = memoria.total / (1024**3)

		return {
			"nome": "Memória RAM", 
			"Capacidade": f"{total:.2f} GB"
		}

		"""Método que recolhe informações da placa de video"""
	def get_info_gpu(self):
		gpus = GPUtil.getGPUs()
		gpu_infos = []

		for gpu in gpus:
			gpu_infos.append({
				"nome": gpu.name,
				"capacidade": f"{gpu.memoryTotal} MB",
				"temperatura": f"{gpu.temperature} °C"
				})
			return gpu_infos


			"""Método que recolhe informações da placa mãe"""
	def get_info_motherboard(self):
		sistema_operacional = platform.system()

		if sistema_operacional == "Windows":
			try:
				import wmi
				c = wmi.WMI()
				for board in c.win32_baseboard():
					return{
					"Nome": board.ManuFacturer + " " + board.Product,

					}
			except ImportError:
				return{"Nome": "Não foi possivel obter informações da placa-mãe (wmi não instalado)"}		

		else: 
			return {"Nome": "Informações da placa-mãe não suportadas neste sistema operacional"}		



	"""Método que busca temperatura da cpu"""

def get_temperatura_cpu(self):
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        try:
            import wmi
            c = wmi.WMI(namespace="root\WMI")
            temperature_info = c.MSAcpi_ThermalZoneTemperature()[0]
            temperature_kelvin = float(temperature_info.CurrentTemperature)
            temperature_celsius = (temperature_kelvin - 2731.5) / 10.0
            return f"{temperature_celsius:.2f} °C"
        except Exception as e:
            return "Não foi possível obter a temperatura da CPU (Windows)"
    elif sistema_operacional == "Linux":
        try:
            output = os.popen("sensors").read()
            # Tenta encontrar a temperatura em diferentes formatos
            temperatures = re.findall(r"(\+?\d+\.\d+)\s?°C", output)
            if not temperatures:
                temperatures = re.findall(r"temp1:\s+(\+?\d+\.\d+)\s?°C", output)
            if temperatures:
                return f"{temperatures[0]} °C"
            else:
                return "Não foi possível obter a temperatura da CPU (Linux)"
        except Exception as e:
            return f"Não foi possível obter a temperatura da CPU (Linux): {e}"
    else:
        return "Temperatura da CPU não suportada neste sistema operacional"




	"""Função que mostra relatório das buscas"""			

	def mostrar_relatorio(self):
	    print("===== RELATÓRIO DE SISTEMA =====")
	    print("Atualizado em: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # Adiciona timestamp
	    print("\n--- PROCESSADOR ---")
	    for chave, valor in self.info_processador.items():
	        print(f"  {chave}: {valor}")

	    print("\n--- MEMÓRIA ---")
	    for chave, valor in self.info_memoria.items():
	        print(f"  {chave}: {valor}")

	    print("\n--- GPU ---")
	    for gpu in self.info_gpu:
	        print("\n  --- Placa de Vídeo ---")
	        for chave, valor in gpu.items():
	            print(f"    {chave}: {valor}")

	    print("\n--- PLACA MÃE ---")
	    for chave, valor in self.info_motherboard.items():
	        print(f"  {chave}: {valor}")



"""Cria uma instância da classe SistemaInfos"""
def main():
    sistema = SistemaInfos()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        sistema.mostrar_relatorio()
        time.sleep(1)  # Aguarda 1 segundo
