import re
from collections import Counter




def read_template(path):
 with open(path) as file:
  file=file.read()
 return file

def parse_template(sentence):
    x=re.sub("{.*?}","{}",sentence)
    y=re.findall(r"(?<=\{).+?(?=\})", sentence)
    return (str(x),tuple(y))

def merge(sentence,collection):
  formated=sentence.format(*collection)
  return formated



def play_game(path):
  print("""
  Welcome to the Madlib game!

  to start:
  """)
  file=read_template(path)
  x,y=parse_template(file)
  inputs=()
  for i in y:
    z=input('Enter any>>>>')
    inputs+=(z,)
  print(merge(x,inputs))
  with open('/home/anas-abusaif/401-projects/madlib-cli/assets/game_result.txt', 'w') as result_file:
   result_file.write(merge(x,inputs))

if __name__=="__main__":
 play_game('/home/anas-abusaif/401-projects/madlib-cli/assets/madlib.txt')
