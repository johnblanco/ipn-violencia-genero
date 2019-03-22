def fix_situacion(sit):
    if sit=='Formalizada':
        return 'Formalizado'
    return sit

def fix_fecha(mes):
    arr = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 
           'Octubre', 'Noviembre', 'Diciembre']
    
    m = "{:02d}".format(arr.index(mes)+1)

    return m

def add_columns(row, genero):
    if genero == 'varones':
        return row['Abuso sexual varones'] + row['Abuso sexual especialmente agravado varones'] + row['Abuso sexual sin contacto corporal varones']
    else:
        return row['Abuso sexual mujeres'] + row['Abuso sexual especialmente agravado mujeres'] + row['Abuso sexual sin contacto corporal mujeres']

def change_abuso(row):
    a = row['Abuso sexual']
    b = row['Abuso sexual especialmente agravado']
    c = row['Abuso sexual sin contacto corporal']
    return a + b + c

def by_population(row, col):
    diez_miles = row['poblacion']/10000
    return row[col] / diez_miles




