import os
import shutil
listOfItemWithLocation={}
def getMP3(folderLocation):
    os.chdir(folderLocation)
    listOfItems=os.listdir(folderLocation)
    for item in listOfItems:
        listOfItemWithLocation['{}'.format(item)]=os.path.realpath(item)
    listOfSongs=[]
    while(len(listOfItems)!=0):
        currentItem=listOfItems.pop()
        if(os.path.isdir(listOfItemWithLocation[currentItem+""])):
            os.chdir(listOfItemWithLocation['{}'.format(currentItem)])
            newList=os.listdir(os.getcwd())
            listOfItems+=newList
            for item in newList:
                listOfItemWithLocation['{}'.format(item)]=os.path.realpath(item)
            #print(currentItem)
        else:
            f=os.path.splitext(currentItem)
            if f[1]=='.mp3':
                listOfSongs.append(currentItem)
    return listOfSongs

def move(newLocation):
    list=getMP3('G:\English')
    #print list
    for it in list:
        shutil.move(listOfItemWithLocation['{}'.format(it)],newLocation)
        print listOfItemWithLocation['{}'.format(it)]
    #print newLocation

def main():
    location='G:\\try'
    #print location
    move(location)
if(__name__=="__main__"):
    main()
            
            
            