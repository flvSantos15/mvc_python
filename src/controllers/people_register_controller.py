from typing import Dict

from src.models.entity.person import Person
from src.models.repository.person_repository import person_repository


class PeopleRegisterController:
  def register(self, new_person_informations) -> Dict:
    try:
      self.__validate_fields(new_person_informations)
      # enviar para models para cadastro de dados
      person_created = self.__create_person_entity_and_store(new_person_informations)
      response = self.__format_response(person_created)
      
      return {'success': True, 'message': response}
    except Exception as exception:
      return {'success': False, 'error': str(exception)}
    
  def __create_person_entity_and_store(self, new_person_informations) -> Person:
    name = new_person_informations['name']
    age = new_person_informations['age']
    height = new_person_informations['height']

    new_person = Person(name, age, height)
    person_repository.registry_person(new_person)

    return new_person

  def __validate_fields(self, new_person_informations) -> None:
    if not isinstance(new_person_informations['name'], str):
      raise Exception('Name must be a string')
    
    try: int(new_person_informations['age'])
    except: raise Exception('Age must be a number')

    try: float(new_person_informations['height'])
    except: raise Exception('Height must be a number')

  def __format_response(self, new_person_informations) -> Dict:
    return {
      'count': 1,
      'type': 'Person',
      'attributes': new_person_informations,
    }
