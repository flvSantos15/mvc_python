from typing import Dict


class PeopleRegisterController:
  def register(self, new_person_informations) -> Dict:
    try:
      self.__validate_fields(new_person_informations)
      # enviar para models para cadastro de dados
      response = self.__format_response(new_person_informations)
      
      return {'success': True, 'message': response}
    except Exception as exception:
      return {'success': False, 'error': str(exception)}

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
