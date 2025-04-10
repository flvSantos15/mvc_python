from src.views.people_finder_view import PeopleFinderView


def people_finder_constructor():
  people_finder_view = PeopleFinderView()
  # controller

  person_finder_informations = people_finder_view.find_person_view()
  # enviar para o controller
