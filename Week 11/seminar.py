fout = open('output.txt', 'w')

line1 = "This here's some text\n"
fout.write(line1)

x = 52
fout.write(str(x) + "\n")

camels = 42
horses = 17

fout.write('I have spotted %d camels.' % camels + "\n")
fout.write('I have spotted %d camels and %d horses.' % (camels, horses) + "\n")

fout.close()


import os
cwd = os.getcwd()

print(cwd)
print(os.listdir(cwd))