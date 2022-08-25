global anterior, cont
cont = 0

lista_tk = ["INT", "MAIS", "MULT", "AP", "FP"]

def term(token):
  global cont
  ret = lista_tk[cont] == token
  cont = cont + 1
  return ret

def E1():
  return T()

def E2():
  return T() and term('MAIS') and E()

def E():
  global cont
  anterior = cont
  if E1():
    return True
  else:
    cont = anterior
    return E2()

def T1():
  return term('INT')

def T2():
  return term('INT') and term('MULT') and T()

def T3():
  return term('AP') and E() and term('FP')

def T():
  global cont
  anterior = cont
  if T1():
    return True
  else:
    cont = anterior
    if T2():
      return True
    else:
      cont = anterior
      return T3()

print(E())