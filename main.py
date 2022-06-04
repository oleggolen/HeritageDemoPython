class Employee:
    def __init__(self, first_name, last_name, patronymic, department, experience):
        self.__firstName = first_name
        self.__lastName = last_name
        self.__patronymic = patronymic
        self.__department = department
        self.__experience = experience

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def get_patronymic(self):
        return self.__patronymic

    def get_department(self):
        return self.__department

    def get_experience(self):
        return self.__experience


class Manager:
    def __init__(self, first_name, last_name, patronymic, department, experience, level, team):
        self.__firstName = first_name
        self.__lastName = last_name
        self.__patronymic = patronymic
        self.__department = department
        self.__experience = experience
        self.__level = level
        self.__team = team

    def get_first_name(self):
        return self.__firstName

    def get_last_name(self):
        return self.__lastName

    def get_patronymic(self):
        return self.__patronymic

    def get_department(self):
        return self.__department

    def get_experience(self):
        return self.__experience

    def get_level(self):
        return self.__level

    def get_team(self):
        return self.__team

