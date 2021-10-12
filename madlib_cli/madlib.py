import re
from collections import Counter

print("""
Welcome to the Madlib game!

to start:
""")

if __name__=='__main__':
 char=input('Please enter you character name>>>')
 adj1=input(f'Enter a cool adjective that fits {char}>>>')
 adj2=input('Enter another cool adjetive>>>')
 past_verb=input('Enter a verb in past tense>>>')
 name1=input("Enter some Name>>>")
 adj3=input('Enter an adjective>>>')
 adj4=input('Enter another adjective>>>')
 item1=input('Enter a random item in plural>>>')
 lrg_an=input("Enter a large animal>>>")
 sml_an=input('Enter small animal>>>')
 girl=input("Enter a girl's name>>>")
 adj5=input('Enter an adjective>>>')
 item2=input('Enter a random item plural>>>')
 adj6=input('Enter an adjective>>>')
 item3=input('Enter a random item plural>>>')
 num1=input('Enter a number between 1 and 50>>>')
 name2=input("Enter some Name>>>")
 num2=input('Enter a number between 1 and 50>>>')
 item4=input('Enter a random item plural>>>')
 num3=input('Enter a number between 1 and 50>>>')
 item5=input('Enter a random item plural>>>')
 inputs=(adj1,adj2,char,past_verb,name1,adj3,adj4,item1,lrg_an,sml_an,girl,adj5,item2,adj6,item3,num1,name1,num2,item4,num3,item5)


def read_template(path):
 file=open(path)
 file=file.read()
 return file

def parse_template(sentence):
    x=re.sub("{.*?}","{}",sentence)
    y=re.findall(r"(?<=\{).+?(?=\})", sentence)
    return (str(x),tuple(y))

def merge(sentence,collection):
  formated=sentence.format(*collection)
  return formated

with open('/home/anas-abusaif/401-projects/madlib-cli/assets/madlib.txt') as file:
  madlib_game=file.read()
  x,y=parse_template(madlib_game)
  print(merge(x,inputs))
with open('/home/anas-abusaif/401-projects/madlib-cli/assets/game_result.txt', 'w') as result_file:
  result_file.write(merge(x,inputs))

