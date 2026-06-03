import easyocr
inputPath = input("paste path here")
inputPath = inputPath.strip().strip('""/')
language = easyocr.Reader(['en'])
text = language.readtext(inputPath, detail=0, paragraph=True)
with open("text.txt","w",encoding="utf-8") as file:
    for line in text:
        textVar = line
        file.write(f"{textVar} \n")
print("we are  done")