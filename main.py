text=input("Ievadiet tekstu: ")
def replaceO (text):
  if text.count("o")>0 or text.count("O")<0:
    text = text.replace("o","%")
    text = text.replace("O","%")
    print (text)
  else:
    text = "Nav burtu O vai o."
    print (text)
  return text
replaceO (text)