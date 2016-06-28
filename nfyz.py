file=open('lola.txt','r', encoding ='utf-8')
d={}
string=file.read()
string=string.lower()
words = string.split( )
for word in words:
        word=word.strip("!@$%^&*()_+=-[].,№;:")
        if word in d:       
            d[word]+=1
        else:
            d[word]=1
for word in sorted(d, key =d.get, reverse= True):
        if d[word] >= 300:
            print (word + ' '+ str(d[word]))
file.close()


            
        
