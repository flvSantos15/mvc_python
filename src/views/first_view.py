def introduction_page():
  message = '''
  Sistema Cadastral

  * Cadastrar Pessoa 1 *
  * Burcar Pessoa Por Nome 2 *
  * Sair 3 *
  '''
  
  print(message)

  command = input('Digite a opção desejada: ')

  return command