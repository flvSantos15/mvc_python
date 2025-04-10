import os
from typing import Dict


class PeopleFinderView:
  def find_person_view(self) -> Dict:
    os.system('cls||clear')

    print('Buscar Pessoa \n\n')
    name = input('Digite o nome da pessoa: ')

    person_finder_informations = {
      'name': name
    }

    return person_finder_informations
