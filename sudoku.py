import numpy as np
line = np.zeros((9, 9), dtype=np.int )
linesus = np.zeros((9, 9, 9), dtype=np.int)   
print("please input unsolved sudoku.")
for i in range(9):
    line[i] = input().split(" ")
    
def solveit():
    print("again")
    for x in range(9):
        for y in range(9):
            if line[x][y] == 0:
                if x<=2 and y<=2:
                    nowbig=22
                elif x<=5 and y<=2:
                    nowbig=52
                elif x<=8 and y<=2:
                    nowbig=82
                elif x<=2 and y<=5:
                    nowbig=25
                elif x<=5 and y<=5:
                    nowbig=55
                elif x<=8 and y<=5:
                    nowbig=85
                elif x<=2 and y<=8:
                    nowbig=28
                elif x<=5 and y<=8:
                    nowbig=58
                else :
                    nowbig=88
                xran=[nowbig//10-2,nowbig//10-1,nowbig//10]
                yran=[nowbig%10-2,nowbig%10-1,nowbig%10]
                for a in xran:
                    for b in yran:
                        if line[a][b]!=0:
                            linesus[x][y][line[a][b]-1]=line[a][b]
                for c in range(9):
                    if line[x][c]!=0:
                        linesus[x][y][line[x][c]-1]=line[x][c]
                for d in range(9):
                    if line[d][y]!=0:
                        linesus[x][y][line[d][y]-1]=line[d][y]
                count=0
                wow=0
                for e in range(9):
                    if linesus[x][y][e]==0:
                        count+=1
                        wow=e
                if count==1:
                    line[x][y]=wow+1
                    print(x,y,wow+1)
                    print("by 1")
                    return
    flag= False
    for f in range(9):
        if flag == True:
            break
        for g in [0,3,6]:
            if flag ==True:
                break
            for h in [0,3,6]:
                if flag ==True:
                    break
                bar=0
                for i in [g,g+1,g+2]:
                    for j in [h,h+1,h+2]:
                        if line[i][j]==0:
                            if linesus[i][j][f]==0:
                                bar+=1
                                yeex=i
                                yeey=j
                if bar==1:
                    line[yeex][yeey]=f+1
                    print(yeex,yeey,f+1)
                    print("by 2")
                    
                    flag = True
        for k in range(9):
            if flag ==True:
                break
            jet=0
            for l in range(9):
                if line[k][l]==0:
                    if linesus[k][l][f]==0:
                        jet+=1
                        yoox=k
                        yooy=l
            if jet==1:
                line[yoox][yooy]=f+1
                print(yoox,yooy,f+1)
                print("by 3")
                
                flag = True
        for m in range(9):
            if flag == True:
                break
            jar=0
            for n in range(9):
                if line[n][m]==0:
                    if linesus[n][m][f]==0:
                        jar+=1
                        yaax=n
                        yaay=m
            if jar ==1:
                line[yaax][yaay]=f+1
                print(yaax,yaay,f+1)
                print("by 4")
                
                flag = True
        for o in [0,3,6]:
            if flag ==True:
                break
            for p in [0,3,6]:
                sflag= False
                for q in [o,o+1,o+2]:
                    if sflag ==True:
                        break
                    for r in [p,p+1,p+2]:
                        if sflag== True:
                            break
                        if line[q][r]==0:
                            if linesus[q][r][f]==0:
                                recx=q
                                recy=r
                                sflag=True
                if sflag==True:
                    aflag= False
                    for s in [o,o+1,o+2]:
                        if aflag==True:
                            break
                        for t in [p,p+1,p+2]:
                            if aflag ==True:
                                break
                            if line[s][t]==0:
                                if linesus[s][t][f]==0:
                                    if s==recx:
                                        continue
                                    else:
                                        aflag=True
                    if aflag==False:
                        this = list(set([0,3,6]).difference(set([p])))
                        for u in this:
                            for v in [u,u+1,u+2]:
                                if line[recx][v]==0:
                                    if linesus[recx][v][f]==0:
                                        linesus[recx][v][f]=f+1
                                        print(recx,v,f)
                                        
                if sflag==True:
                    bflag= False
                    for w in [o,o+1,o+2]:
                        if bflag==True:
                            break
                        for z in [p,p+1,p+2]:
                            if bflag ==True:
                                break
                            if line[w][z]==0:
                                if linesus[w][z][f]==0:
                                    if z==recy:
                                        continue
                                    else:
                                        bflag=True
                    if bflag==False:
                        this = list(set([0,3,6]).difference(set([o])))
                        for aa in this:
                            for bb in [aa,aa+1,aa+2]:
                                if line[bb][recy]==0:
                                    if linesus[bb][recy][f]==0:
                                        linesus[bb][recy][f]=f+1
                                        print(bb,recy,f)
                                        
        superbreak2=False
        for ab in range(9):
            if superbreak2==True:
                break
            cflag =False
            thflag=False
            lol=0
            where=0
            for acc in [0,1,2]:
                if thflag==True:
                    break
                if line[ab][acc]==0:
                    if linesus[ab][acc][f]==0:
                        lol+=1
                        if lol>1:
                            thflag=True
                            where+=1
            lol=0
            if thflag==False:
                for acc in [3,4,5]:
                    if thflag==True:
                        break
                    if line[ab][acc]==0:
                        if linesus[ab][acc][f]==0:
                            lol+=1
                            if lol>1:
                                thflag=True
                                where+=1
            lol=0
            if thflag==False:
                for acc in [6,7,8]:
                    if thflag==True:
                        break
                    if line[ab][acc]==0:
                        if linesus[ab][acc][f]==0:
                            lol+=1
                            if lol>1:
                                thflag=True
                                where+=1
            if where==1:
                if acc<=2:
                    nowy=0
                elif acc<=5:
                    nowy=3
                else :
                    nowy=6
                if ab<=2:
                    nowx=0
                elif ab<=5:
                    nowx=3
                else :
                    nowx=6
                this = list(set([0,3,6]).difference(set([nowy])))
                for ad in this:
                    if cflag== True:
                        break
                    for ae in [ad,ad+1,ad+2]:
                        if cflag==True:
                            break
                        if line[ab][ae]==0:
                            if linesus[ab][ae][f]==0:
                                cflag=True
                if cflag==False:
                    this = list(set([nowx,nowx+1,nowx+2]).difference(set([ab])))
                    for ag in this:
                        for af in [nowy,nowy+1,nowy+2]:
                            if line[ag][af]==0:
                                if linesus[ag][af][f]==0:
                                    linesus[ag][af][f]=f+1
                                    print(ag,af,f+1)
                                    
                superbreak2=True
        superbreak=False
        for ah in range(9):
            if superbreak2==True:
                break
            if superbreak==True:
                break
            tyflag=False
            dflag =False
            rot=0
            there=0
            for aii in [0,1,2]:
                if tyflag ==True:
                    break
                if line[aii][ah]==0:
                    if linesus[aii][ah][f]==0:
                        rot+=1
                        if rot>1:
                            tyflag=True
                            there+=1
            rot=0
            if tyflag==False:
                for aii in [3,4,5]:
                    if tyflag ==True:
                        break
                    if line[aii][ah]==0:
                        if linesus[aii][ah][f]==0:
                            rot+=1
                            if rot>1:
                                tyflag=True
                                there+=1
            rot=0
            if tyflag==False:
                for aii in [6,7,8]:
                    if tyflag ==True:
                        break
                    if line[aii][ah]==0:
                        if linesus[aii][ah][f]==0:
                            rot+=1
                            if rot>1:
                                tyflag=True
                                there+=1
            if there==1:
                if aii<=2:
                    nowx=0
                elif aii<=5:
                    nowx=3
                else :
                    nowx=6
                if ah<=2:
                    nowy=0
                elif ah<=5:
                    nowy=3
                else :
                    nowy=6
                this = list(set([0,3,6]).difference(set([nowx])))
                for aj in this:
                    if dflag== True:
                        break
                    for ak in [aj,aj+1,aj+2]:
                        if dflag==True:
                            break
                        if line[ak][ah]==0:
                            if linesus[ak][ah][f]==0:
                                dflag=True
                if dflag==False:
                    this = list(set([nowy,nowy+1,nowy+2]).difference(set([ah])))
                    for al in this:
                        for am in [nowx,nowx+1,nowx+2]:
                            if line[am][al]==0:
                                if linesus[am][al][f]==0:
                                    linesus[am][al][f]=f+1
                                    print(am,al,f)
                superbreak=True
solveit()
count=0
while not line.all():
    solveit()
    count+=1
    if count==100:
        break
print(line)
