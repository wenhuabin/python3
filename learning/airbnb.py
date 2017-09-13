
def paginate(num, results):

    if len(results) <= 1:
        return results

    ids = []
    sids = []
    sidx = []
    list = []
    tlist = []

    for val in results:
        ids.append(val.split(',')[0])

    for i in range(len(ids)):
        if not ids[i] in sids and len(sids) < num:
            sids.append(ids[i])
            sidx.append(i)
        else:
            tlist.append(results[i])

    for i in range(len(sidx)):
        list.append(results[sidx[i]])

    lcount = num - len(sids) 
    if len(list) == num:
        list.append("")
        list += paginate(num, tlist)
    elif lcount >= len(tlist):
        list += results
    else:
        for i in range(lcount):
            list.append(tlist.pop(0))
        print(tlist)
        list.append("")
        list += paginate(num, tlist)

    return list

if __name__ == '__main__':
    num = 8
    results = [
        '1,28,103.2,Sans',
        '4,5,100.2,Sans',
        '1,8,99.6,Sans',
        '1,10,98.0,Sans',
        '8,16,90.5,Sans',
        '1,29,83.3,Sans',
        '4,20,80.0,Sans']
    results = ['4,20,80.0,Sans']
    print(paginate(num, results))

