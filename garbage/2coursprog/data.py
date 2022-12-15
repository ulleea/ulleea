path='F:\python\project\котировки.txt'
class ABC:
    def __init__(self):
        self.min=self.max=0
        self.totalhistory=dict()

    def reading(self,path):
        self.g=dict()
        sprev=0
        first=[]
        last=[]
        with open(path,'r',encoding='utf-8') as file:
            s=file.readline()
            print(s)
            x = []
            y = []
            for i in file:
                s=i.split(';')
                if s[0] not in self.g:
                    first.append([s[0],s[2]])
                    self.g[s[0]]=[]
                    # print(s[0],s[2])
                    if x and y:
                        self.g[prev]=[x,y]
                        last.append([sprev[0],sprev[2]])
                    x=[]
                    y=[]
                    count=0
                if sprev!=0 and s[0]==sprev[0] and abs(self.days_between(sprev,s))>1:
                    sr=(float(s[5])+float(sprev[5]))/2
                    for _ in range(abs(self.days_between(sprev,s))-1):
                        y.append(sr)
                        x.append(count)
                        count+=1
                        prev=s[0]
                y.append(float(s[5]))
                x.append(count)
                count+=1
                prev=s[0]
                sprev=s
            self.g[prev]=[x,y]
            last.append([sprev[0],sprev[2]])
            min=max=sprev[2]
            n=len(first)
            for i in range(n):
                if self.days_between(first[i][1],min)<0:
                    min=first[i][1]
                if self.days_between(first[i][1],max)>0:
                    max=last[i][1]
            self.min=min
            self.max=max
            for i in range(n):
                for j in range(abs(self.days_between(min,first[i][1]))):
                    self.g[first[i][0]][0].append(self.g[first[i][0]][0][-1]+1)
                    self.g[first[i][0]][1].insert(0,self.g[first[i][0]][1][0])
            for i in range(n):
                for j in range(abs(self.days_between(last[i][1],max))):
                    self.g[last[i][0]][0].append(self.g[last[i][0]][0][-1]+1)
                    self.g[last[i][0]][1].append(self.g[last[i][0]][1][-1])
            self.total_days(path)
        print(self.g)

    def total_days(self,path):
        if self.min and self.max:
            self.period= abs(self.days_between(self.min,self.max))
        else:
            self.reading(path)
            self.period= abs(self.days_between(self.min, self.max))


    def dataa(self,s):
        from datetime import date
        if type(s) == list:
            dd = s[2][0:2]
            mm = s[2][2:4]
            yy = s[2][4:6]
            yy = int('20' + yy)
            dd = int(dd)
            mm = int(mm)
            s = date(yy, mm, dd)
            return s
        if type(s)==str:
            dd = s[0:2]
            mm = s[2:4]
            yy = s[4:6]
            yy = int('20' + yy)
            dd = int(dd)
            mm = int(mm)
            s = date(yy, mm, dd)
            return s

    def days_between(self,sprev, s):
        d1 = self.dataa(s)
        d2= self.dataa(sprev)
        return (d2 - d1).days

    def printing(self,name):
        import matplotlib.pyplot as plt
        plt.plot(self.g[name][0],self.g[name][1])
        if name in self.totalhistory:
            for i in self.totalhistory[name]:
                plt.scatter(i[0],self.g[name][1][i[0]])
                print(i[0],self.g[name][1][i[0]])
                if i[1]!=self.max:
                    plt.scatter(i[1],self.g[name][1][i[1]])
                    print(i[1],self.g[name][1][i[1]])
                else:
                    print(self.period)
                    plt.scatter(self.period,self.g[name][1][self.period])
                    print(self.period,self.g[name][1][self.period])
        plt.grid()
        plt.show()

    def training(self,a):
        self.timetrain=round(self.period/3)
        # self.trainstr=input()
        self.trainstr=a
        train=__import__(self.trainstr)
        self.portfolio=[]
        self.array=[]
        for i in self.g.keys():
            self.array.append([i,0])
        for i in range(self.timetrain):
            self.portfolio,self.array=train.trainfun(self.portfolio,self.array,self.g,i)
        print(self.portfolio,self.array)

    def getportfoliomoney(self,i):
        sum=0
        for j in self.portfolio:
            sum+=self.g[j[0]] [1][i]*j[1]
        return sum+self.money

    def history(self,j):
        for i in self.portfolio:
            if i[0] not in self.totalhistory:
                self.totalhistory[i[0]]=[[j,self.max]]
            elif self.totalhistory[i[0]][-1][1]!=self.max:
                self.totalhistory[i[0]].append([j,self.max])
        for i in self.totalhistory.keys():
            t=0
            for _ in self.portfolio:
                if _[0]==i:
                    t=1
            if t==0:
                if self.totalhistory[i][-1][1]==self.max:
                    self.totalhistory[i][-1][1]=j

    def traiding(self,a,money):
        self.timetraid=self.period-self.timetrain
        # self.traidstr=input()
        self.traidstr=a
        traid=__import__(self.traidstr)
        self.portfolio=[]
        count=0
        self.money=money
        self.totalvaluess=[[],[]]
        for i in range(self.timetraid):
            self.portfolio,self.money=traid.traidfun(self.portfolio,self.array,self.g,i,self.money)
            self.history(i)
            totalvalue=self.getportfoliomoney(i)
            self.totalvaluess[0].append(count)
            count+=1
            self.totalvaluess[1].append(totalvalue)
        # print('сейчас история портфолио')
        print('--=====',self.totalhistory)
        # self.portfoliohistory()
        return(self.totalvaluess)

    def portfoliohistory(self):
        import matplotlib.pyplot as plt
        plt.plot(self.totalvaluess[0], self.totalvaluess[1])
        plt.grid()
        plt.show()

# a=ABC()
# a.reading(path)
# # print(a.days_between([11,22,'010321'],[11,22,'250621']))
# a.printing('+МосЭнерго')
# a.training('train')
# a.portfoliohistory()