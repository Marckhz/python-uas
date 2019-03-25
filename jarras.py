import random 





class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

  def size(self):
    return len(self.queue)

  def show(self):

    return self.queue


class game():

  def __init__(self, g1=[], g2=[]):

    self.g1 = g1
    self.g2 = g2


  def fill_g1(self):

    if self.g1 == 0 and self.g2 == 0:
      self.g1 = 4
      self.g1 > self.g2

  def fill_g2(self):

    if self.g2 == 0:
      self.g2 = 3
  
  def empty_g1(self):

    if self.g1 != 0:
      self.g1 < 4

  def empty_g2(self):

    if self.g2 != 0:
      self.g2 < 3

  def g1_into_g2(self):

    if self.g1 != 0 and self.g2 !=0:
      if self.g1 > 1 and  self.g2 < 3:
        self.g2 = self.g1 + self.g2

  def g2_into_g1(self):

    if self.g1 != 0 and self.g2 !=0:
      if self.g2 > 1 and self.g1 < 4:
        self.g1 = self.g1 + self.g2



def graph():
  

  x = []
  y = []


  jar_game = game(x,y)



  space  = 10000

  n = random.randint(0,4)
  x = random.randint(0,4)


  goal_state = [2, n]

  abierto = Queue()
  cerrado = Queue()

  abierto.addtoq([0,0])
  
  while abierto.size() > 1:
    actual_state = abierto.removefromq()

graph()
