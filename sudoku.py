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
    yz_failed_records={}
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
        """Tips 5: Pointing pairs - If in a big block, a number can only be in one row or one column, then it can't be in that row or column in other big blocks."""
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
        """Tips 12: Hidden pairs - if in a row, two numbers can only be in the same two cells, then all other numbers can be removed from those two cells."""
        for an in range(9):
            position_map = {}
            for i in range(9):
                if line[an][i] == 0:
                    for num in range(9):
                        if linesus[an][i][num] == 0:
                            if num + 1 not in position_map:
                                position_map[num + 1] = []
                            position_map[num + 1].append(i)
            pairs = [(num, positions) for num, positions in position_map.items() if len(positions) == 2]
            for idx1 in range(len(pairs)):
                for idx2 in range(idx1 + 1, len(pairs)):
                    if pairs[idx1][1] == pairs[idx2][1]:
                        num1, num2 = pairs[idx1][0], pairs[idx2][0]
                        for pos in pairs[idx1][1]:
                            for other_num in range(1, 10):
                                if other_num != num1 and other_num != num2 and linesus[an][pos][other_num - 1] == 0:
                                    linesus[an][pos][other_num - 1] = other_num
        """Tips 13: Hidden pairs - if in a column, two numbers can only be in the same two cells, then all other numbers can be removed from those two cells."""
        for an in range(9):
            position_map = {}
            for i in range(9):
                if line[i][an] == 0:
                    for num in range(9):
                        if linesus[i][an][num] == 0:
                            if num + 1 not in position_map:
                                position_map[num + 1] = []
                            position_map[num + 1].append(i)
            pairs = [(num, positions) for num, positions in position_map.items() if len(positions) == 2]
            for idx1 in range(len(pairs)):
                for idx2 in range(idx1 + 1, len(pairs)):
                    if pairs[idx1][1] == pairs[idx2][1]:
                        num1, num2 = pairs[idx1][0], pairs[idx2][0]
                        for pos in pairs[idx1][1]:
                            for other_num in range(1, 10):
                                if other_num != num1 and other_num != num2 and linesus[pos][an][other_num - 1] == 0:
                                    linesus[pos][an][other_num - 1] = other_num
        """Tips 14: Naked triples - if in a row, three cells can only be the same three numbers, then those three numbers can be removed from other cells in that row."""
        for an in range(9):
            triple_positions = []
            for i in range(9):
                if line[an][i] == 0:
                    possible_numbers = [num + 1 for num in range(9) if linesus[an][i][num] == 0]
                    if 2 <= len(possible_numbers) <= 3:
                        triple_positions.append((i, possible_numbers))
            for idx1 in range(len(triple_positions)):
                for idx2 in range(idx1 + 1, len(triple_positions)):
                    for idx3 in range(idx2 + 1, len(triple_positions)):
                        combined = set(triple_positions[idx1][1] + triple_positions[idx2][1] + triple_positions[idx3][1])
                        if len(combined) == 3:
                            num1, num2, num3 = combined
                            for k in range(9):
                                if k not in [triple_positions[idx1][0], triple_positions[idx2][0], triple_positions[idx3][0]] and line[an][k] == 0:
                                    if linesus[an][k][num1 - 1] == 0:
                                        linesus[an][k][num1 - 1] = num1
                                    if linesus[an][k][num2 - 1] == 0:
                                        linesus[an][k][num2 - 1] = num2
                                    if linesus[an][k][num3 - 1] == 0:
                                        linesus[an][k][num3 - 1] = num3
        """Tips 15: Naked triples - if in a column, three cells can only be the same three numbers, then those three numbers can be removed from other cells in that column."""
        for an in range(9):
            triple_positions = []
            for i in range(9):
                if line[i][an] == 0:
                    possible_numbers = [num + 1 for num in range(9) if linesus[i][an][num] == 0]
                    if 2 <= len(possible_numbers) <= 3:
                        triple_positions.append((i, possible_numbers))
            for idx1 in range(len(triple_positions)):
                for idx2 in range(idx1 + 1, len(triple_positions)):
                    for idx3 in range(idx2 + 1, len(triple_positions)):
                        combined = set(triple_positions[idx1][1] + triple_positions[idx2][1] + triple_positions[idx3][1])
                        if len(combined) == 3:
                            num1, num2, num3 = combined
                            for k in range(9):
                                if k not in [triple_positions[idx1][0], triple_positions[idx2][0], triple_positions[idx3][0]] and line[an][k] == 0:
                                    if linesus[k][an][num1 - 1] == 0:
                                        linesus[k][an][num1 - 1] = num1
                                    if linesus[k][an][num2 - 1] == 0:
                                        linesus[k][an][num2 - 1] = num2
                                    if linesus[k][an][num3 - 1] == 0:
                                        linesus[k][an][num3 - 1] = num3
        """Tips 16: Hidden triples - if in a row, three numbers can only be in the same three cells, then all other numbers can be removed from those three cells."""
        for an in range(9):
            position_map = {}
            for i in range(9):
                if line[an][i] == 0:
                    for num in range(9):
                        if linesus[an][i][num] == 0:
                            if num + 1 not in position_map:
                                position_map[num + 1] = []
                            position_map[num + 1].append(i)
            triples = [(num, positions) for num, positions in position_map.items() if len(positions) == 3]
            for idx1 in range(len(triples)):
                for idx2 in range(idx1 + 1, len(triples)):
                    for idx3 in range(idx2 + 1, len(triples)):
                        combined = set(triples[idx1][1] + triples[idx2][1] + triples[idx3][1])
                        if len(combined) == 3:
                            num1, num2, num3 = triples[idx1][0], triples[idx2][0], triples[idx3][0]
                            for pos in combined:
                                for other_num in range(1, 10):
                                    if other_num != num1 and other_num != num2 and other_num != num3 and linesus[an][pos][other_num - 1] == 0:
                                        linesus[an][pos][other_num - 1] = other_num
        """Tips 17: Hidden triples - if in a column, three numbers can only be in the same three cells, then all other numbers can be removed from those three cells."""
        for an in range(9):
            position_map = {}
            for i in range(9):
                if line[i][an] == 0:
                    for num in range(9):
                        if linesus[i][an][num] == 0:
                            if num + 1 not in position_map:
                                position_map[num + 1] = []
                            position_map[num + 1].append(i)
            triples = [(num, positions) for num, positions in position_map.items() if len(positions) == 3]
            for idx1 in range(len(triples)):
                for idx2 in range(idx1 + 1, len(triples)):
                    for idx3 in range(idx2 + 1, len(triples)):
                        combined = set(triples[idx1][1] + triples[idx2][1] + triples[idx3][1])
                        if len(combined) == 3:
                            num1, num2, num3 = triples[idx1][0], triples[idx2][0], triples[idx3][0]
                            for pos in combined:
                                for other_num in range(1, 10):
                                    if other_num != num1 and other_num != num2 and other_num != num3 and linesus[an][pos][other_num - 1] == 0:
                                        linesus[pos][an][other_num - 1] = other_num
        """Tips 18 xy wing - if a cell can put xy, and sees two cells in different ways that can put xz and yz, then z can be removed from any cell that sees both those cells."""
        # to avoid repeated failed attempts, we record the failed xz locations(upon confirming yz) for each xy, ex:{(xy_i, xy_j):[(xz_i1, xz_j1), (xz_i2, xz_j2)]}
        for an in range(9):
            for i in range(9):
                if line[an][i] == 0:
                    possible_numbers = [num + 1 for num in range(9) if linesus[an][i][num] == 0]
                    if len(possible_numbers) == 2:
                        x, y = possible_numbers
                        z= None
                        xz_locations = []
                        #print("found xy at", an, i, ":", x, y)
                        #look for same block first, then row, then column. if found xz and yz that meet the condition, do it and return
                        flag_first_found = False
                        for j in range(an//3*3, an//3*3+3):
                            if flag_first_found:
                                break
                            for k in range(i//3*3, i//3*3+3):
                                #print("yz_failed_records:", yz_failed_records)
                                if (j == an and k == i) or line[j][k] != 0:
                                    continue
                                if (an, i) in yz_failed_records and (j, k) in yz_failed_records[(an, i)]:
                                    #print("skipped", (j, k), "for", (an, i))
                                    continue
                                if flag_first_found:
                                    break
                                possible_numbers_jk = [num + 1 for num in range(9) if linesus[j][k][num] == 0]
                                if len(possible_numbers_jk) == 2:
                                    #check if they share one number with (x,y), also need to be different row and column to (an,i)
                                    if ((x in possible_numbers_jk) != (y in possible_numbers_jk)) and (j != an) and (k != i):
                                        z = possible_numbers_jk[0] if possible_numbers_jk[0] not in (x, y) else possible_numbers_jk[1]
                                        #print("cell found xz at", j, k, ":", possible_numbers_jk)
                                        xz_locations.append((j, k))
                                        flag_first_found = True
                                        #print("z is", z)
                                        #now redefine xy if neeeded
                                        if x in possible_numbers_jk:
                                            x = x
                                            y = y
                                        else:
                                            x, y = y, x
                        #look in the same row
                        for j in range(9):
                            if (j == i) or line[an][j] != 0:
                                continue
                            possible_numbers_j = [num + 1 for num in range(9) if linesus[an][j][num] == 0]
                            #need check if possicle numbers j lenth is 2, and 
                            if len(possible_numbers_j) == 2:
                                if flag_first_found:
                                    #print([an ,j],[y,z], possible_numbers_j, x)
                                    if possible_numbers_j == [z, y] or possible_numbers_j == [y, z]:
                                        #print("really checked, last chance",x, y, possible_numbers_j, z)
                                        #print(flag_first_found, xz_locations)
                                        #print("found yz at", an, j, ":", possible_numbers_j)
                                        #remove z from any cell that sees both (an,j) and xz_locations, including seeing by same line or in sanme block
                                        for thex in range(9):
                                            for they in range(9):
                                                #bypass the cell that is xz or yz itself
                                                if (thex == an and they == j) or any(thex == xz_i and they == xz_j for (xz_i, xz_j) in xz_locations):
                                                    continue
                                                #if:  (the cell is in xz's block ,or in same row as xz, or in same column as xz) and (the cell is in yz's block ,or in same row as yz, or in same column as yz) and (is not xz or yz)
                                                for (xz_i, xz_j) in xz_locations:
                                                    if line[thex][they] == 0 and linesus[thex][they][z-1] == 0:
                                                        in_xz_block = (thex // 3 == xz_i // 3) and (they // 3 == xz_j // 3)
                                                        in_yz_block = (thex // 3 == an // 3) and (they // 3 == j // 3)
                                                        same_row_as_xz = (thex == xz_i)
                                                        same_col_as_xz = (they == xz_j)
                                                        same_row_as_yz = (thex == an)
                                                        same_col_as_yz = (they == j)
                                                        if (in_xz_block or same_row_as_xz or same_col_as_xz) and (in_yz_block or same_row_as_yz or same_col_as_yz):
                                                            linesus[thex][they][z-1] = z
                                                            print("removed", z, "from", thex, they)
                                                            print("xy suspect is", an, i, ":", x, y)
                                                            print("xz suspect is", xz_i, xz_j, ":", x, z)
                                                            print("yz suspect is", an, j, ":", y, z)
                                                            return
                                    else:
                                        if (an, i) not in yz_failed_records:
                                            yz_failed_records[(an, i)] = []
                                        yz_failed_records[(an, i)].append(xz_locations[0])
                                        #print(yz_failed_records)

                                if not flag_first_found:
                                    if (x in possible_numbers_j) != (y in possible_numbers_j):
                                        if (an ,i) in yz_failed_records and (an, j) in yz_failed_records[(an ,i)]:
                                            #print("skipped", (an, j), "for", (an, i))
                                            continue
                                        z = possible_numbers_j[0] if possible_numbers_j[0] not in (x, y) else possible_numbers_j[1]
                                        #print("found xz at", an, j, ":", possible_numbers_j)
                                        xz_locations.append((an, j))
                                        #print("z is", z)
                                        #print("x is", x, "y is", y)
                                        flag_first_found = True
                                        #now redefine xy if neeeded
                                        if x in possible_numbers_j:
                                            x = x
                                            y = y
                                        else:
                                            x, y = y, x
                                        break
                        #look in the same column
                        for j in range(9):
                            if (j == an) or line[j][i] != 0:
                                continue
                            if not flag_first_found:
                                break
                            possible_numbers_j = [num + 1 for num in range(9) if linesus[j][i][num] == 0]
                            if len(possible_numbers_j) == 2:
                                if possible_numbers_j == [z,y] or possible_numbers_j == [y, z]:
                                    #print("really checked, last chance",x, y, possible_numbers_j, z)
                                    #print("found yz at", j, i, ":", possible_numbers_j)
                                    #remove z from any cell that sees both (j,i) and xz_location, including seeing by same line or in sanme block
                                    for thex in range(9):
                                        for they in range(9):
                                            #bypass the cell that is xz or yz itself
                                            if (thex == j and they == i) or (thex == xz_locations[0][0] and they == xz_locations[0][1]):
                                                continue

                                            #if:  (the cell is in xz's block ,or in same row as xz, or in same column as xz) and (the cell is in yz's block ,or in same row as yz, or in same column as yz) and (is not xz or yz)
                                            for (xz_i, xz_j) in xz_locations:
                                                if line[thex][they] == 0 and linesus[thex][they][z-1] == 0:
                                                    in_xz_block = (thex // 3 == xz_i // 3) and (they // 3 == xz_j // 3)
                                                    in_yz_block = (thex // 3 == j // 3) and (they // 3 == i // 3)
                                                    same_row_as_xz = (thex == xz_i)
                                                    same_col_as_xz = (they == xz_j)
                                                    same_row_as_yz = (thex == j)
                                                    same_col_as_yz = (they == i)
                                                    if (in_xz_block or same_row_as_xz or same_col_as_xz) and (in_yz_block or same_row_as_yz or same_col_as_yz):
                                                        linesus[thex][they][z-1] = z
                                                        print("removed", z, "from", thex, they)
                                                        print("xy suspect is", an, i, ":", x, y)
                                                        print("xz suspect is", xz_i, xz_j, ":", x, z)
                                                        print("yz suspect is", j, i, ":", y, z)
                                                        return    
                                else:
                                    if (an, i) not in yz_failed_records:
                                        yz_failed_records[(an, i)] = []
                                    yz_failed_records[(an, i)].append((j, i))
                                    #print(yz_failed_records)
solveit()
OCOUNT=0
while not line.all():
    solveit()
    OCOUNT+=1
    if OCOUNT%100 == 0:
        #linesus = np.zeros((9, 9, 9), dtype=int)
        print("dumb way")

    if OCOUNT == 200:
        #for i in range(9):
            #for j in range(9):
                #if line[i][j] == 0:
                    #print(linesus[i][j])
        break

print(line)
print(OCOUNT," moves")

