import time as t
import os

print("Loading screen....")
t.sleep(2)
string_fr1 = "Made by: Noah, [Elemental Production]"
print(string_fr1)
string_fr = "[Elemental Production Members]: Noah, Manraj, Saif and Matvej"
print(string_fr)
t.sleep(2)
print(os.getcwd() + ":File_Directory_Revealed")
t.sleep(2)

while True:
  decide_input_options = input("What calculation would you like to do? [B,D,BA]\n")
  if "B" in decide_input_options:
    t.sleep(1)
    print("Loading Binary converter...")
    t.sleep(1)
    binary_input = input("Enter a number\n")
    while True:
      try:
       int(binary_input)
      except:
       if binary_input != int:
         print("Error 1: Expect an integar\n")
         binary_input = input("Enter a binary number\n")
      else:
        break
    binary = bin(int(binary_input))
    if "b" in binary:
     print(str(binary.replace('0b','')))
  elif "D" in decide_input_options:
      t.sleep(1)
      print("Loading Denary Converter...")
      t.sleep(1)
      denary_input = input("Enter binary number\n")
      while True:
       try:
         int(denary_input)
         break
       except ValueError:
            print("Error 1: Expect an integar\n")
            denary_input = input("Enter a binary number\n")
      lol = int('0b' + denary_input, base=0)
      print(lol)
