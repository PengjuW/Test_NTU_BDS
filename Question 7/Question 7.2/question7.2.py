def change1(L1=4, L2=8, L3=5, L4=9, L5=6, L6=7):
    fop = open('input_coordinates_7_2.txt','r')
    data = fop.readlines()[1:]
    data= [dt.strip().split('\t') for dt in data]
    data = [[int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5])] for l in data]
    index = []

    for i in range(len(data)):

        index.append(L2*L3*L4*L5*L6*data[i][0]+L3*L4*L5*L6*data[i][1]+L4*L5*L6*data[i][2]+L5*L6*data[i][3]+L6*data[i][4]+data[i][5])
    op = open('output_index_7_2.txt','w')
    for inx in index:
        op.write(str(inx)+'\n')


change1(L1=4, L2=8, L3=5, L4=9, L5=6, L6=7)


def change2(L1=4, L2=8, L3=5, L4=9, L5=6, L6=7):
    fop = open('input_index_7_2.txt','r')
    data = fop.readlines()[1:]

    data = [int(l.strip()) for l in data]
    index = []
    for i in range(len(data)):
        k1 = data[i]//(L2*L3*L4*L5*L6)
        k2 = (data[i] -k1*L2*L3*L4*L5*L6)//(L3*L4*L5*L6)
        t = ( L4 * L5 * L6)
        k3 = (data[i]-k1*L2*L3*L4*L5*L6-k2*L3*L4*L5*L6)//t

        k4 = (data[i]-k1*L2*L3*L4*L5*L6-k2*L3*L4*L5*L6 -k3*L4*L5*L6) // (L5*L6)
        k5 = (data[i]-k1*L2*L3*L4*L5*L6-k2*L3*L4*L5*L6 -k3*L4*L5*L6-k4*L5*L6) // (L6)
        k6 =  (data[i]-k1*L2*L3*L4*L5*L6-k2*L3*L4*L5*L6 -k3*L4*L5*L6-k4*L4*L5*L6-k5*L5*L6) % (L6)
        index.append([k1,k2,k3,k4,k5,k6])
    op = open('output_coordinates_7_2.txt','w')
    for inx in index:
        op.write(str(inx[0])+' '+str(inx[1])+' '+str(inx[2])+' '+str(inx[3])+' '+str(inx[4])+' '+str(inx[5])+'\n')

change2(L1=4, L2=8, L3=5, L4=9, L5=6, L6=7)