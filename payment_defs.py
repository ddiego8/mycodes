#It calculates gross pay

def datacollect():
    hrs = float(input('Enter Hours:'))
    rt = float(input('Enter rate:'))
    computepay(hrs, rt)

def calc_normal(hrs, rt):
    return float(hrs) * float(rt)

def calc_plus(hrs, rt):
    return (float(hrs-40)) * (float(rt*1.5)) + (40 * float(rt)) #It calculates ONLY the excedent time amongst the gross pay

def computepay(hrs, rt):
    if hrs > 40 :
        gp = calc_plus(hrs, rt)
    else:
        gp = calc_normal(hrs, rt)

    print('Pay:', gp)
    print('Good Bye')
    input()

datacollect()
