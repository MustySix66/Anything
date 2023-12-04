# De aquí se van a importar las funciones a la pagina principal

def Presupuesto():
    try:
        Ingreso = float(input("Ingreso mensual: "))
        Gastos = float(input("Gastos mensuales: "))
        presup = Ingreso - Gastos
        print("Tu presupuesto mensual es de: ",  presup )
        presup/=4
        print("Debes gastar ",presup, " o menos por semana.")

        Enter=input("Presiona enter para continuar: ")
    except:
        print("Error.")


def Deudas():
    try:
        Deuda_Total = float(input("Ingresa tu deuda total: "))
        RatioInteres = float(input("En decimal, ingresa el ratio de interes anual: "))
        DuracionDeudas = int(input("¿Cuantos años dura la deuda?: "))
        Mes_RatioInteres = RatioInteres / 12
        DuracionDeudas_Mes = DuracionDeudas * 12
        PagoMensual = (Deuda_Total * Mes_RatioInteres) / (1 - (1 + Mes_RatioInteres)**(-DuracionDeudas_Mes))
        print("Tu pago mensual será de: ", PagoMensual)
        Enter=input("Presiona Enter para continuar: ")
    except:
        print("Error")

def Inversion():
    try:    
        InversiónInicio = float(input("Ingresa tu inversión: "))
        InteresAnual = float(input("¿Cual es el ratio anual de crecimiento? (En decimales): "))
        años = int(input("¿A cuantos años?: "))
        InversionFinal = InversiónInicio * (1 + InteresAnual)**años
        print("El valor futuro de tu inversión será de: ", InversionFinal)
        Enter=input("Presiona Enter para continuar: ")
    except:
        print("Error.")
