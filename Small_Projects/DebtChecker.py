#### This program is made for checking how much money needs to pay each one.
# It explains who owes who and how much it owes.

def calcular_deudas(pagos, total):
    # Calculate the amount each person should have paid

    pago_justo = total / len(pagos)

    # Calculate how much each person owes
    deudas = {persona: pago - pago_justo for persona, pago in pagos.items()}

    # Determinar quién debe dinero a quién
    deudores = {persona: -deuda for persona, deuda in deudas.items() if deuda < 0}
    acreedores = {persona: deuda for persona, deuda in deudas.items() if deuda > 0}

    # Assign debtors to creditors
    asignacion = {}
    for deudor, deuda in deudores.items():
        asignacion[deudor] = {}
        while deuda > 0.01:  # Assuming we don't care about differences less than 1 cent
            for acreedor, credito in acreedores.items():
                if credito > 0:
                    pago = min(deuda, credito)
                    asignacion[deudor][acreedor] = pago
                    deuda -= pago
                    acreedores[acreedor] -= pago

    return asignacion

# Example
total = float(input("Bill total?: "))
n = int(input("How many people is going to pay?: "))
pagos = {}
for i in range(n):
    nombre = input(f"Please put the name of the person number  {i+1}: ")
    pago = float(input(f"How much {nombre} paid?: "))
    pagos[nombre] = pago

print(calcular_deudas(pagos, total))
