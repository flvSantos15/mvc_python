class PersonRepository:
  def __init__(self) -> None:
    self.__persons = []

  def registry_person(self, person: object) -> None:
    self.__persons.append(person)

  def find_by_name(self, name: str) -> object:
    for person in self.__persons:
      if person.name == name:
        return person
      
    return None
  
  def find_all(self) -> list:
    return self.__persons
  
  def clear_all(self) -> None:
    self.__persons = []

    return
  
  def delete(self, name: str) -> None:
    for index, p in enumerate(self.__persons):
      if p.name == name:
        del self.__persons[index]

    return

  def update(self, person: object) -> None:
    for index, p in enumerate(self.__persons):
      if p.name == person.name:
        self.__persons[index] = person

    return
  
person_repository = PersonRepository()