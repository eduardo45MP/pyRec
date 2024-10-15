import os
from pytsk3 import Img_Info

# Caminho do HD (pode ser /dev/sda para Linux)
DISK_PATH = '/dev/sda3'
SECTOR_SIZE = 512  # Tamanho padrão de setor (512 bytes)

class DiskImage(Img_Info):
    def __init__(self, disk_path):
        self.disk_path = disk_path
        super(DiskImage, self).__init__(disk_path)

    def read_sectors(self, start_sector, num_sectors):
        offset = start_sector * SECTOR_SIZE
        size = num_sectors * SECTOR_SIZE
        with open(self.disk_path, 'rb') as f:
            f.seek(offset)
            return f.read(size)

# Função para processar um bloco de setores
def process_sectors(disk_image, start_sector, num_sectors):
    data = disk_image.read_sectors(start_sector, num_sectors)
    return data

if __name__ == '__main__':
    disk_image = DiskImage(DISK_PATH)
    start_sector = 0
    num_sectors = 100  # Quantidade de setores para ler em cada batch

    # Lendo os primeiros 100 setores
    data = process_sectors(disk_image, start_sector, num_sectors)
    print(f"Leitura dos primeiros {num_sectors} setores concluída.")