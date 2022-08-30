def list_oper(a,b,oper='add'):
    c=[]
    if oper=='add':
        for i in range(len(a)):
            c.append(a[i]+b[i])
    elif oper=='sub':
        for i in range(len(a)):
            c.append(a[i]-b[i])
    elif oper=='mult':
        for i in range(len(a)):
            c.append(a[i]*b[i])
    elif oper=='div':
        for i in range(len(a)):
            c.append(a[i]/b[i])
    return c
def matrix_oper(a,b,oper='add'):
    c=[]
    for i in range(len(a)):
        if oper=='add':
            c.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='sub':
            c.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='mult':
            c.append(list_oper(a[i],b[i],oper=oper))
        elif oper=='div':
            c.append(list_oper(a[i],b[i],oper=oper))
    return c
def get_elem_index(a,elem=None):
    if elem=='min':
        return min(a),a.index(min(a))
    elif elem=='max':
        return max(a),a.index(max(a))
    else:
        return elem,a.index(elem)
def get_average(ext_list):
    if len(ext_list)>0:
        return sum(ext_list)/len(ext_list)
    return 0
def get_min_max_avg(existences):
    result=[]
    for exist in existences:
        if len(exist)>0:
            result.append([min(exist),get_average(exist),max(exist)])
        else:
            result.append([0 for i in range(3)])
    return result
def get_avg_per_patient(meds,n_pat):
    if n_pat>0:
        return sum(meds)/n_pat
    return 0
def main():
    n,k = 0,0
    while n<1 or k<1:
        ini_data=input().split(' ')
        n,k,m=int(ini_data[0]),int(ini_data[1]),int(ini_data[2])
    actual_ex,req_ex,bra_count=[],[],[]
    for i in range(n):
        read_ex = list(map(lambda x: int(x), input().split(' ')))
        actual_ex.append(read_ex)
        req_ex.append([0 for i in range(k)])
        bra_count.append(0)
    for i in range(m):
        read_info=input().split(' ')
        bra,med_type,n_dosis,s,d=int(read_info[0]),int(read_info[1]), int(read_info[2]), int(read_info[3]), int(read_info[4])
        if 0<bra<=n and 0<med_type<=k and n_dosis>= 0:
            if s<90 and d<70:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 140<=s<150 and 95<=d<100:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 150<=s<170 and 100<=d<110:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif 170<=s<190 and 110<=d<120:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif s>=190 and d>=120:
                req_ex[bra-1][med_type-1]+=n_dosis
            elif s>=150 and d<100:
                req_ex[bra-1][med_type-1]+= n_dosis
            bra_count[bra-1]+= 1
    final_ex=matrix_oper(actual_ex,req_ex,oper='sub')
    min_max_avg=get_min_max_avg(req_ex)
if __name__ == "__main__":
    main()