"""
  Playlist_de_filmes_e_series

  Curso de Python 3: Avançando na orientação a objetos

  Professor: Luan Marques

  Aluno: Breno

  Plataforma de aprendizado: Alura (https://cursos.alura.com.br/)

"""


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} Minutos - Likes: {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


#------------------------------------------------------------------------------------------------------------------#

# Filme e Séries
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em Pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

# Dando Like
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

# playlist/Lista
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

# Verificando se possui o filme 'demolidor' na playlista
print(f'Cadastrado na playlist: {demolidor in playlist_fim_de_semana}')

# Retornando o primeiro item da playlist
print(f'Primeiro filme da Playlist{playlist_fim_de_semana[0]}')

# Percorre os (programas = Filmes e Séries) dentro da playlist
for programa in playlist_fim_de_semana:
    print(programa)
