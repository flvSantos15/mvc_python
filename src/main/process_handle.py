from .constructor.introduction_process import introduction_process


def start() -> None:
  while True:
    command = introduction_process()

    if command == '1':
      print('Cadastrar Pessoa')
    elif command == '2':
      print('Buscar Pessoa Por Nome')
    elif command == '3':
      print('Sair')
      break