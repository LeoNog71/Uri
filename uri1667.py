string = input()

string = string.replace("<br>","\n")
string = string.replace("\n<hr>","--------------------------------------------------------------------------------\n")
string = string.replace("<hr>","\n--------------------------------------------------------------------------------")

print(string)
