intro=str(input("introduce yourself"))
print(intro)
wordcount=1
charactercount=0

for character in intro:
        charactercount=charactercount+1
        if  (character==" "):
         wordcount=wordcount+1

       
       
print(charactercount)
print(wordcount)
