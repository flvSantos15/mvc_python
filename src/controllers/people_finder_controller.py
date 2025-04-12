from typing import Dict


class PeopleFinderController:
  def find_by_name(self, person_finder_informations: Dict) -> Dict:
    try:
      self.__validate_fields(person_finder_informations)

      # person = Buscar do banco de dados

      message = self.__format_response(person_finder_informations)

      return {'success': True, 'message': message}
    except Exception as exception:
      return {'success': False, 'error': str(exception)}
    
  def __validate_fields(self, person_finder_informations: Dict) -> None:
    if not isinstance(person_finder_informations['name'], str):
      raise Exception('Name must be a string')
    
  def __format_response(self, person_finder_informations: Dict) -> Dict:
    return {
      'count': 1,
      'type': 'Person',
      'attributes': person_finder_informations
    }