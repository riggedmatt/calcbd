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
  if decide_input_options == "B":
    t.sleep(1)
    print("Loading Binary converter...")
    t.sleep(1)
    binary_input = input("Enter a number\n")
    while True:
      try:
       int(binary_input)
       break
      except ValueError:
         print("Error 1: Expect an integer\n")
         binary_input = input("Enter a binary number\n")
    binary = bin(int(binary_input))
    if "b" in binary:
     print(str(binary.replace('0b','')))
  elif decide_input_options == "D":
      t.sleep(1)
      print("Loading Denary Converter...")
      t.sleep(1)
      denary_input = input("Enter binary number\n")
      while True:
       try:
         int(denary_input)
         break
       except ValueError:
            print("Error 1: Expect an integer\n")
            denary_input = input("Enter a binary number\n")
      lol = int('0b' + denary_input, base=0)
      print(lol)
  elif decide_input_options == "BA":
    t.sleep(1)
    print("Loading Binary Addition..")
    t.sleep(1)
    first_input = input("Enter a number\n")
    second_input = input("Enter another number\n")
    while True:
      try:
       int(first_input)
       int(second_input)
       break
      except ValueError:
         print("Error 1: Expect an integer\n")
         first_input = input("Enter a number\n")
    first_number = int(first_input)
    second_number = int(second_input)
    final_out_put = first_number + second_number
    final_lol_really = bin(final_out_put)
    print(str(final_lol_really.replace('0b','')))
