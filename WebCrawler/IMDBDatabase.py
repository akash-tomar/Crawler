import requests
import bs4
import re

match=[]
mapForVisitedLink={}
mapForMovieRelease={}
mapForMovieDirector={}
mapForMovieRating={}
movieList=[]
def getAllLinksFromPage(url):
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.text,'html.parser')
    list=soup.find_all(name='a')
    soup.find
    pattern='/title/tt.*\"'
    for li in list:
        t=(re.search(pattern, str(li) ))
        if(t):
            sr='\"http://www.imdb.com'+str(t.group())
            #print sr[1:-1]
            if mapForVisitedLink.has_key(r'{}'.format(sr[1:-1]))==False:
            #if mapForVisitedLink[]==False:
                match.append(r'{}'.format(sr[1:-1])+'')
                mapForVisitedLink[r'{}'.format(sr[1:-1])]=True
    #print "hello"          
    
            
def visitingAllLinks():
    while(len(match)!=0):
        file=open('abc.txt','a+')
        currentLink=match[0]
        del match[0]
        r=requests.get(currentLink)
        #print currentLink
        #if re.search('.*TV series.*', r.text)==True:
        #    continue
        
        # -----------movie name-----------------
        soup=bs4.BeautifulSoup(r.text,'html.parser')
        movieNameTag=soup.find_all('h1','header')
        if len(movieNameTag)==0:
            continue
        movieNameGroup=re.search('\"name\"\>.*\</',str(movieNameTag[0]))
        if movieNameGroup==None:
            continue
        movieName=movieNameGroup.group()
        
        movieName=((str(movieName)+'')[7:-2])
        if mapForMovieDirector.has_key(movieName+''):
            continue
        movieList.append(movieName)
        print movieName
        

        #-----------Year of release----------
        movieYearTag=soup.find_all('span',"nobr")
        movieYear=str(movieYearTag[0])
        movieYear=movieYear[-16:-12]
        mapForMovieRelease[movieName+'']=movieYear
        print movieYear
        
        #-----------Movie Rating-------------
        movieRatingGroup=re.search('star-box-giga-star\"\>.*\<\/', str(soup))
        if(movieRatingGroup):
            movieRating=movieRatingGroup.group()
            movieRating=movieRating[21:25]
        else:
            movieRating=-1
        print movieRating
        mapForMovieRating[movieName+'']=movieRating
        
        
        #----------Director name--------------
        drNameTag=soup.find_all('div','txt-block','director')
        if len(drNameTag)==0:
            continue
        drNameGroup=re.search('itemprop=\"name\"\>.*\<\/',str(drNameTag[0]))
        drName= drNameGroup.group()
        drName=drName[16:-9]
        print drName
        print "\n"
        mapForMovieDirector[movieName+'']=drName
        
        
        #----------append movies from this page-----------
        getAllLinksFromPage(currentLink+'')
        
        
        
    

getAllLinksFromPage('http://www.imdb.com')
visitingAllLinks()
