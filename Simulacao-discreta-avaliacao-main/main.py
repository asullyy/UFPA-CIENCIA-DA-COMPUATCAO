import simpy

class Caixa:
  def __init__ (self, env, n_caixas):
    self.env = env
    self.n_caixas = n_caixas

  def Atendimento(self, cliente, tmp_chegada, tmp_atendimento):
    yield self.env.timeout(tmp_chegada)
    print("cliente {} chegou no tempo {}".format(cliente, self.env.now))
    with self.n_caixas.request() as caixa:
      yield caixa
      print("cliente {} iniciou o atendimento em {}".format(cliente, self.env.now))
      yield self.env.timeout(tmp_atendimento)
      print("cliente {} saiu no tempo {}".format(cliente, self.env.now))

import simpy
env = simpy.Environment()

caixas = simpy.Resource(env, capacity=1)
c = Caixa(env, caixas)

#A lista data é composta pelo tempo de atendimento de 150 pessoas, bem como a lista chegada é o tempo em que cada uma chegou. Ex.: P01 levou 5 tempo para ser atendida. 

#A contagem dos dados foi feita de forma manual e pode ser consultada através do link https://docs.google.com/spreadsheets/d/1AnHe4UKhZu3HmhHZ7G0Lg0vq92wSnXDQ9JukVCWsKo8/edit?usp=sharing

data = [5, 6, 3, 1, 1, 1, 2, 3, 5, 2, 3, 1, 2, 4, 6, 6, 1, 2, 1, 6, 3, 3, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 2, 4, 2, 1, 2, 4, 2, 1, 6, 1, 2, 2, 3, 3, 1, 2, 4, 1, 2, 2, 2, 2, 4, 2, 5, 1, 3, 2, 2, 2, 5, 2, 1, 1, 1, 1, 3, 3, 2, 2, 3, 4, 3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 4, 3, 2, 3, 3, 3, 2, 2, 2, 2, 3, 3, 2, 1, 3, 2, 3, 3, 3, 2, 1, 3, 3, 3, 3, 2, 3, 3, 2, 2, 4, 1, 3, 2, 3, 3, 4, 2, 2, 2, 3, 4, 4, 2, 3, 1, 2, 2, 1, 3, 3, 3, 2, 3, 4, 3, 2, 3]

chegada = [0, 0, 0, 3, 4, 5, 5, 6, 6, 7, 9, 9, 10, 11, 12, 12, 15, 16, 18, 18, 18, 19, 21, 22, 23, 24, 24, 24, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 31, 31, 32, 33, 34, 35, 36, 37, 37, 37, 38, 39, 40, 42, 43, 43, 44, 45, 45, 47, 47, 47, 49, 49, 51, 51, 53, 54, 54, 55, 56, 56, 57, 58, 58, 59, 59, 60, 62, 62, 62, 64, 65, 66, 67, 67, 67, 69, 70, 70, 72, 74, 76, 76, 77, 78, 79, 80, 81, 82, 82, 83, 84, 84, 86, 86, 87, 87, 89, 89, 90, 92, 92, 92, 93, 95, 96, 96, 98, 98, 99, 100, 101, 101, 102, 104, 104, 104, 107, 107, 108, 109, 109, 110, 114, 113, 114, 116, 116, 115, 118, 118, 118, 121, 121, 121, 123, 124, 125]

for i in range (0, len(data)):
  env.process(c.Atendimento(i, chegada[i], data[i]))

env.run()
  
    

