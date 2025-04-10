import os
from typing import Dict


class PeopleRegisterView:
  def registry_person_view(self) -> Dict:
    os.system('cls||clear')
    
    print('Cadastrar Pessoa \n\n')
    name = input('Nome: ')
    age = input('Idade: ')
    height = input('Altura: ')

    new_person_informations = {
      'name': name,
      'age': age,
      'height': height
    }

    return new_person_informations