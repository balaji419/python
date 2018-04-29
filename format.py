class myclass:
    def __init__(self,listl=[],element):
        start=0
        self.list=listl
        self.element=element
        found=False
        counter=0
        while (start< len(listl) and found==False ):
            if( list(start)==element):
                print ("Element founnd")
                found=True
                counter+=1
                print ("You have counter %d no of times" %counter)
            start+=1

print("Enter the element to be searched")
ele=int(input())
obj1=myclass([2,3,5,6,'nyyt','k',655], ele)
