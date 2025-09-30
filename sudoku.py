"""pylint support"""
import numpy as np
line = np.zeros((9, 9), dtype=int )
linesus = np.zeros((9, 9, 9), dtype=int)
print("please input unsolved sudoku.")
for userinput in range(9):
    line[userinput] = input().split(" ")
#function for solve
def solveit():
    """move 1 : Same big block have or same row have, can't put it.And then only one left, put it."""
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
    # now look at each number as f
    for f in range(9):
        if flag:
            break
        """move 2 : Only this left in possibility of big block"""
        for g in [0,3,6]:
            if flag:
                break
            for h in [0,3,6]:
                if flag:
                    break
                onlysus=0
                yeex=0
                yeey=0
                for i in [g,g+1,g+2]:
                    for j in [h,h+1,h+2]:
                        if line[i][j]==0:
                            if linesus[i][j][f]==0:
                                onlysus+=1
                                yeex=i
                                yeey=j
                if onlysus==1:
                    line[yeex][yeey]=f+1
                    print(yeex,yeey,f+1)
                    print("by 2")
                    #flag = True
                    return
        """move 3 : Only this left in possibility of row or column"""
        for k in range(9):
            if flag:
                break
            jet=0
            yoox=0
            yooy=0
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
        """move 4 : Only this left in possibility of row or column."""
        for m in range(9):
            if flag:
                break
            jar=0
            yaax=0
            yaay=0
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
        """Tips 5: If in a big block, a number can only be in one row or one column, then it can't be in that row or column in other big blocks."""
        for o in [0,3,6]:
            if flag:
                break
            for p in [0,3,6]:
                sflag= False
                recx=0
                recy=0
                for q in [o,o+1,o+2]:
                    if sflag:
                        break
                    for r in [p,p+1,p+2]:
                        if sflag:
                            break
                        if line[q][r]==0:
                            if linesus[q][r][f]==0:
                                recx=q
                                recy=r
                                sflag=True
                if sflag:
                    aflag= False
                    for s in [o,o+1,o+2]:
                        if aflag:
                            break
                        for t in [p,p+1,p+2]:
                            if aflag:
                                break
                            if line[s][t]==0:
                                if linesus[s][t][f]==0:
                                    if s==recx:
                                        continue
                                    else:
                                        aflag=True
                    if not aflag:
                        this = list(set([0,3,6]).difference(set([p])))
                        for u in this:
                            for v in [u,u+1,u+2]:
                                if line[recx][v]==0:
                                    if linesus[recx][v][f]==0:
                                        linesus[recx][v][f]=f+1
                                        #print(recx,v,f)
                if sflag:
                    bflag= False
                    for w in [o,o+1,o+2]:
                        if bflag:
                            break
                        for z in [p,p+1,p+2]:
                            if bflag:
                                break
                            if line[w][z]==0:
                                if linesus[w][z][f]==0:
                                    if z==recy:
                                        continue
                                    else:
                                        bflag=True
                    if not bflag:
                        this = list(set([0,3,6]).difference(set([o])))
                        for aa in this:
                            for bb in [aa,aa+1,aa+2]:
                                if line[bb][recy]==0:
                                    if linesus[bb][recy][f]==0:
                                        linesus[bb][recy][f]=f+1
                                        #print(bb,recy,f)
        """Tips 6: If in a 'row or column', a number can only be in one big block, then it can't be in that big block in other rows or columns."""
        superbreak2=False
        for ab in range(9):
            if superbreak2:
                break
            cflag =False
            thflag=False
            lol=0
            where=0
            for acc in [0,1,2]:
                if thflag:
                    break
                if line[ab][acc]==0:
                    if linesus[ab][acc][f]==0:
                        lol+=1
                        if lol>1:
                            thflag=True
                            where+=1
            lol=0
            if not thflag:
                for acc in [3,4,5]:
                    if thflag:
                        break
                    if line[ab][acc]==0:
                        if linesus[ab][acc][f]==0:
                            lol+=1
                            if lol>1:
                                thflag=True
                                where+=1
            lol=0
            if not thflag:
                for acc in [6,7,8]:
                    if thflag:
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
                    if cflag:
                        break
                    for ae in [ad,ad+1,ad+2]:
                        if cflag:
                            break
                        if line[ab][ae]==0:
                            if linesus[ab][ae][f]==0:
                                cflag=True
                if not cflag:
                    this = list(set([nowx,nowx+1,nowx+2]).difference(set([ab])))
                    for ag in this:
                        for af in [nowy,nowy+1,nowy+2]:
                            if line[ag][af]==0:
                                if linesus[ag][af][f]==0:
                                    linesus[ag][af][f]=f+1
                                    #print(ag,af,f+1)

                superbreak2=True
        """Tips 7: If in a 'row or column', a number can only be in one big block, then it can't be in that big block in other rows or columns."""
        superbreak=False
        for ah in range(9):
            if superbreak2:
                break
            if superbreak:
                break
            tyflag=False
            dflag =False
            rot=0
            there=0
            for aii in [0,1,2]:
                if tyflag:
                    break
                if line[aii][ah]==0:
                    if linesus[aii][ah][f]==0:
                        rot+=1
                        if rot>1:
                            tyflag=True
                            there+=1
            rot=0
            if not tyflag:
                for aii in [3,4,5]:
                    if tyflag:
                        break
                    if line[aii][ah]==0:
                        if linesus[aii][ah][f]==0:
                            rot+=1
                            if rot>1:
                                tyflag=True
                                there+=1
            rot=0
            if not tyflag:
                for aii in [6,7,8]:
                    if tyflag:
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
                    if dflag:
                        break
                    for ak in [aj,aj+1,aj+2]:
                        if dflag:
                            break
                        if line[ak][ah]==0:
                            if linesus[ak][ah][f]==0:
                                dflag=True
                if not dflag:
                    this = list(set([nowy,nowy+1,nowy+2]).difference(set([ah])))
                    for al in this:
                        for am in [nowx,nowx+1,nowx+2]:
                            if line[am][al]==0:
                                if linesus[am][al][f]==0:
                                    linesus[am][al][f]=f+1
                                    #print(am,al,f)
                superbreak=True
        """Tips 8: blocks removal - if in a column, a number can only be in one big block, then it can't be in that big block in other rows."""
        superbreak3 = False
        for an in range(9):             
            if superbreak3:
                break
            regions = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            inblock = [0,0,0]
            for region in regions:# every 3 columns
                for col in region:# every column in the 3 columns, ex:0,1,2
                    colp=col//3
                    if line[an][col] == 0 and linesus[an][col][f] == 0:
                        inblock[colp]=1
            if sum(inblock) == 1:
                block_index = inblock.index(1)
                block_start = block_index * 3
                block_end = block_start + 3
                #print(an, block_start, block_end, f)
                if an <=2:
                    nowx=0
                elif an <=5:    
                    nowx=3
                else :
                    nowx=6
                for i in range(nowx, nowx + 3):
                    if i == an:
                        continue
                    for j in range(block_start, block_end):
                        if line[i][j] == 0 and linesus[i][j][f] == 0:
                            linesus[i][j][f] = f + 1
                            #print (i, j, f + 1)
                superbreak3 = True
        """Tips 9: blocks removal - if in a row, a number can only be in one big block, then it can't be in that big block in other columns."""
        superbreak4 = False
        for am in range(9):             
            if superbreak4:
                break
            regions = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            inblock = [0,0,0]
            for region in regions:# every 3 columns
                for col in region:# every column in the 3 columns, ex:0,1,2
                    colp=col//3
                    if line[col][am] == 0 and linesus[col][am][f] == 0:
                        inblock[colp]=1
            if sum(inblock) == 1:
                block_index = inblock.index(1)
                block_start = block_index * 3
                block_end = block_start + 3
                #print(an, block_start, block_end, f)
                if am <=2:
                    nowx=0
                elif am <=5:    
                    nowx=3
                else :
                    nowx=6
                for i in range(nowx, nowx + 3):
                    if i == am:
                        continue
                    for j in range(block_start, block_end):
                        if line[j][i] == 0 and linesus[j][i][f] == 0:
                            linesus[j][i][f] = f + 1
                            #print (j, i, f + 1)
                superbreak3 = True
        """Tips 10: Naked pairs - if in a row, two cells can only be the same two numbers, then those two numbers can be removed from other cells in that row."""
        for an in range(9):
            pair_positions = []
            for i in range(9):
                if line[an][i] == 0:
                    possible_numbers = [num + 1 for num in range(9) if linesus[an][i][num] == 0]
                    if len(possible_numbers) == 2:
                        pair_positions.append((i, possible_numbers))
            for idx1 in range(len(pair_positions)):
                for idx2 in range(idx1 + 1, len(pair_positions)):
                    if pair_positions[idx1][1] == pair_positions[idx2][1]:
                        num1, num2 = pair_positions[idx1][1]
                        for k in range(9):
                            if k != pair_positions[idx1][0] and k != pair_positions[idx2][0] and line[an][k] == 0:
                                if linesus[an][k][num1 - 1] == 0:
                                    linesus[an][k][num1 - 1] = num1
                                if linesus[an][k][num2 - 1] == 0:
                                    linesus[an][k][num2 - 1] = num2
        """Tips 11: Naked pairs - if in a column, two cells can only be the same two numbers, then those two numbers can be removed from other cells in that column."""
        for an in range(9):
            pair_positions = []
            for i in range(9):
                if line[i][an] == 0:
                    possible_numbers = [num + 1 for num in range(9) if linesus[i][an][num] == 0]
                    if len(possible_numbers) == 2:
                        pair_positions.append((i, possible_numbers))
            for idx1 in range(len(pair_positions)):
                for idx2 in range(idx1 + 1, len(pair_positions)):
                    if pair_positions[idx1][1] == pair_positions[idx2][1]:
                        num1, num2 = pair_positions[idx1][1]
                        for k in range(9):
                            if k != pair_positions[idx1][0] and k != pair_positions[idx2][0] and line[k][an] == 0:
                                if linesus[k][an][num1 - 1] == 0:
                                    linesus[k][an][num1 - 1] = num1
                                if linesus[k][an][num2 - 1] == 0:
                                    linesus[k][an][num2 - 1] = num2
solveit()
OCOUNT=0
while not line.all():
    solveit()
    OCOUNT+=1
    if OCOUNT%100 == 0:
        #print(linesus[3,6])
        #print(linesus[3,7])
        #print(linesus[3,8])
        linesus = np.zeros((9, 9, 9), dtype=int)
        print("dumb way")
    if OCOUNT == 300:
#        for i in range(9):
#            for j in range(9):
#                print(linesus[i][j])
        break

print(line)
print(OCOUNT," moves")

