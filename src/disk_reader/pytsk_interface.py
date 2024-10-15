import pytsk3
import os

def read_disk(disk_path):
    """
    Lê setores de um disco rígido usando a biblioteca pytsk.

    :param disk_path: Caminho para o dispositivo do disco (ex: /dev/sda).
    :return: Lista de setores lidos.
    """
    if not os.path.exists(disk_path):
        raise FileNotFoundError(f"O caminho {disk_path} não existe.")

    try:
        img = pytsk3.Img_Info(disk_path)
        fs = pytsk3.FS_Info(img)

        sectors = []
        for sector in fs.open_dir("/"):
            sectors.append(sector)

        return sectors

    except Exception as e:
        print(f"Erro ao ler o disco: {e}")
        return []

if __name__ == "__main__":
    # Exemplo de uso
    disk_path = "/dev/sda3"  # Altere conforme necessário
    sectors = read_disk(disk_path)
    print(f"Setores lidos: {sectors}")
