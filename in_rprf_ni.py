# nc_rprf.py — RAW NC COMMAND — Python ESSENZ
def calc_omega(resonanz, balance, power, move):
    r = max(0,min(100,resonanz))/100
    b = max(0,min(100,balance))/100
    p = max(0,min(100,power))
    m = max(0,min(100,move))
    return r*b*(p/100)*(1+m/500)*100

def get_checks(t,d,power,feldlast,move,omega):
    def band(v,mi,ma,wmi,wma):
        return {"ok": mi<=v<=ma, "warn": (wmi<=v<mi) or (ma<v<=wma)}
    return [
        {"name":"MASS TRIAD SYNC", **band(d,0.60,0.85,0.30,1.00)},
        {"name":"POWER HEADROOM", **band(power,40,80,20,95)},
        {"name":"OMEGA BAND", **band(omega,50,90,25,120)},
        {"name":"FELDLAST", **band(feldlast,20,85,5,100)},
        {"name":"RESONANZ", **band(t,0.45,0.75,0.30,0.90)},
        {"name":"MOVE", **band(move,30,70,20,100)},
    ]
