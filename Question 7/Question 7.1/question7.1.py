def change1(L1, L2):
    fop = open('input_coordinates_7_1.txt','r')
    data = fop.readlines()[1:]
    data= [dt.strip().split('\t') for dt in data]
    data = [[int(l[0]),int(l[1])] for l in data]
    index = []
    for i in range(len(data)):
        index.append(L1*data[i][0]+data[i][1])
    op = open('output_index_7_1.txt','w')
    for inx in index:
        op.write(str(inx)+'\n')


# change1(L1=50, L2=57)


def change2(L1, L2):
    fop = open('input_index_7_1.txt','r')
    data = fop.readlines()[1:]

    data = [int(l.strip()) for l in data]
    index = []
    for i in range(len(data)):
        index.append([data[i]//L1,data[i]%L1])
    op = open('output_coordinates_7_1.txt','w')
    for inx in index:
        op.write(str(inx[0])+' '+str(inx[1])+'\n')

change2(L1=50, L2=57)