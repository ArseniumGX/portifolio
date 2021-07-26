class Contato:
    def __init__(self) -> None:
        self.__name = str()
        self.__email = str()
        self.__phone = str()
        self.__message = str()
    
    def __str__(self):
        return f'''Name: {self.name}\nEmail: {self.email}\nTelephone: {self.phone}\nMessage: {self.message}'''

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, value):
        self.__message = value

# contato = Contato()
# 
# contato.name = 'Teste dos Testes'
# contato.email = 'test@test.com'
# contato.phone = '0800010101010'
# contato.message = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi aut rerum cupiditate vel dolore ipsa, doloremque error modi? In, facere provident maxime modi quia dignissimos iusto voluptatem. Iusto consequuntur at ea quaerat voluptates odio culpa a laboriosam dolores accusamus, ipsa quos sed vitae quam fugit autem, dolorum quod eius quo?'
# 
# print(contato)