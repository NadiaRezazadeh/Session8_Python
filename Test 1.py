def mul(f1,f2):
    result = {}
    result['s'] = f1['s']*f2['s']
    result['m'] = f1['m']*f2['m']
    return result

def sum(f1,f2):
    result = {}
    result['s'] = (f1['s']*f2['m'])+(f2['s']*f1['m'])
    result['m'] = f1['m']*f2['m']
    return result   

def div(f1,f2):
    result = {}
    result['s'] = f1['s']*f2['m']
    result['m'] = f1['m']*f2['s']
    return result

def sub(f1,f2):    
    result = {}
    result['s'] = (f1['s']*f2['m'])-(f2['s']*f1['m'])
    result['m'] = f1['m']*f2['m']
    return result

def show(f):
    print(f['s'],'/',f['m'])    

a = {'s':2,'m':3}
b = {'s':5,'m':4}

mul_result = mul(a,b)
sum_result = sum(a,b)
div_result = div(a,b)
sub_result = sub(a,b)

show(mul_result)
show(sum_result)
show(div_result)
show(sub_result)