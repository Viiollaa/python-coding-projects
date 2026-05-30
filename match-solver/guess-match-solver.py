allowed = set("ABCDabcd0123456789@#$!_")
char = ("ABCDabcd0123456789@#$!_")
rank= { c: i for i, c in enumerate(char)}

def t (password): 
    if len(password) not in (3,4,5): 
        return "F"
    for c in password: 
        if c not in allowed:
            return "F"  
    if len(set(password)) != len(password): 
        return "F"
    
    has_upper = any(c in "ABCD" for c in password )
    has_symbol = any(c in "@#$!_" for c in password )
    if not has_symbol and not has_upper: 
        return ("F")
    if not has_symbol or not has_upper: 
        return ("F")

    return ("T")


def s(password): 
    x,y = password
    a = 0 
    b = 0
    used = [False] *len(y)
    for i in range (len(x)): 
        if x[i]==y[i]: 
            a+= 1 
            used[i]= True
            
    for i in range(len(x)): 
        if x[i]!= y[i]: 
            for j in range  (len(y)): 
                if not used[j] and x[i]== y[j]: 
                    b+= 1
                    used[j]= True
                    break 
    return (f'{a}A{b}B')

def g ():
    n = int(input())
    guesses = {}
    for _ in range(n):
        g, ge = input().split()
        a = int(ge[0])
        b = int(ge[2])
        l = len(g)

        if l not in guesses:
            guesses[l] = []
        guesses[l].append((g, a, b))

    return guesses
def match (password,glist): 
    for g, a , b in glist: 
        if s([password,g])!= f"{a}A{b}B": 
            return False 
    return True
    
def generate (l, char,use,current,result,glist): 
    if len(current) == l: 
        pw = "". join(current)
        if t(pw) == "T" and match (pw,glist): 
            result.append(pw)
        return
    for c in char: 
        if c not in use: 
            use.add(c)
            current.append(c)

            generate (l,char,use,current,result,glist)

            current.pop()
            use.remove(c)
def solve_length (l,glist): 
    impossible= set ()

    for g,a,b in glist: 
        if a == 0 and b == 0: 
            for c in g: 
                impossible.add(c)

    useable = [c for c in char if c not in impossible]
    result = []
    generate (l,useable,set(),[],result,glist)
    return result

def sortpass (password): 
    return sorted(password, key = lambda pw: [rank[c] for c in pw])


def main (): 
    mode = input()
    if mode == "T": 
        x = []
        amount = int(input())
        for i in range (amount): 
            password = input()
            a = t(password)
            x.append (a)
        print("".join (x))
        
    if mode == "S": 
        result = []
        amount = int(input())
        for i in range (amount): 
            password = input().split()
            c = s(password)
            result.append(c)
        print("\n".join(result))
    
    if mode == "G":
        guess = g() 

        for l in sorted(guess):
            ans = solve_length(l,guess[l])
            ans = sortpass(ans)
            print(" ". join(ans))
         

main ()
