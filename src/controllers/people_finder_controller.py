from typing import Dict

from src.models.entity.person import Person
from src.models.repository.person_repository import person_repository


class PeopleFinderController:
  def find_by_name(self, person_finder_informations: Dict) -> Person:
    try:
      self.__validate_fields(person_finder_informations)

      person = self.__find_person(person_finder_informations)

      message = self.__format_response(person)

      return {'success': True, 'message': message}
    except Exception as exception:
      return {'success': False, 'error': str(exception)}
    
  def find_all(self) -> Person:
    try:
      # person = Buscar do banco de dados
      person = self.__find_all()

      message = self.__format_response(person)

      return {'success': True, 'message': message}
    except Exception as exception:
      return {'success': False, 'error': str(exception)}
  
  def __find_all(self) -> Person:
    person = person_repository.find_all()

    if not person:
      raise Exception('Person not found')

    return person
  
  def __find_person(seld, person_finder_informations: Dict) -> Person:
    name = person_finder_informations['name']

    person = person_repository.find_by_name(name)

    if not person:
      raise Exception('Person not found')
    return person
    
  def __validate_fields(self, person_finder_informations: Dict) -> None:
    if not isinstance(person_finder_informations['name'], str):
      raise Exception('Name must be a string')
    
  def __format_response(self, person: Person) -> Dict:
    return {
      'count': 1,
      'type': 'Person',
      'infos': {
        'name': person.name,
        'age': person.age,
        'height': person.height
      }
    }