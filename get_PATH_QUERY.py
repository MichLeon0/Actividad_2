from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    Nombre:str
    Matricula: int
    Edad: int
    Carrera: str
    Genero: str
    Semestre: int
    Porcentaje: int
    Promedio: float
    Materias_Reprobadas: int
    

alumnos_list= [User(Nombre="ANGEL AGUILAR SALDIVAR", Matricula=202224429, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.89, Materias_Reprobadas=0),
               User(Nombre="ALEJANDRO AMADOR LAGUNES", Matricula=202213377, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.2, Materias_Reprobadas=1),
               User(Nombre="ERWIN AVENDAÑO VEGA", Matricula=202220926, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=52, Promedio=9.5, Materias_Reprobadas=0),
               User(Nombre="DIEGO CANNATA CARDENAS", Matricula=202229430, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=9.6, Materias_Reprobadas=0),
               User(Nombre="CARLOS CASTRO GASPAR", Matricula=202221488, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.14, Materias_Reprobadas=1),
               User(Nombre="ANDRES CRUZ ORTIZ", Matricula=202214537, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=64, Promedio=8.57, Materias_Reprobadas=0),
               User(Nombre="HECTOR ESCOBAR MARISCAL", Matricula=202126243, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.5, Materias_Reprobadas=2),
               User(Nombre="KEIRA GARRIDO AGUIRRE", Matricula=202230800, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=9.10, Materias_Reprobadas=0),
               User(Nombre="JOE GONZALEZ HERRERA", Matricula=202239938, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.88, Materias_Reprobadas=0),
               User(Nombre="PABLO IBARRA VALENCIA", Matricula=202241171, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.45, Materias_Reprobadas=0),
               User(Nombre="EDUARDO JUAREZ CORTES", Matricula=202262420, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.60, Materias_Reprobadas=0),
               User(Nombre="MICHELL LEON PAREDES", Matricula=202232284, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=9.10, Materias_Reprobadas=0),
               User(Nombre="JOHAN MARTINEZ GARCIA", Matricula=202263388, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=9.45, Materias_Reprobadas=0),
               User(Nombre="HECTOR MENDOZA MERINO", Matricula=202233780, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.10, Materias_Reprobadas=0),
               User(Nombre="FERNANDO MORALES CILIA", Matricula=202234180, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.60, Materias_Reprobadas=4),
               User(Nombre="DIEGO NAVA RIVERA", Matricula=202234640, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.7, Materias_Reprobadas=0),
               User(Nombre="ALFREDO NAVARRETE MONTES", Matricula=202234650, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.51, Materias_Reprobadas=0),
               User(Nombre="ANDY PEREZ PAVON", Matricula=202247824, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.6, Materias_Reprobadas=0),
               User(Nombre="GABRIEL RAMIREZ BAÑUELOS", Matricula=202248699, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=64, Promedio=9.8, Materias_Reprobadas=1),
               User(Nombre="JOSELYN RAMIREZ LIMA", Matricula=202248964, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=9.3, Materias_Reprobadas=0),
               User(Nombre="GUILLERMO SANCHEZ ORTEGA", Matricula=202253218, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=9.2, Materias_Reprobadas=0),
               User(Nombre="NELSON SOSA FRANCISCO", Matricula=202254416, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.9, Materias_Reprobadas=0),
               User(Nombre="JULIAN TENAHUA OLAYA", Matricula=202162286, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.9, Materias_Reprobadas=0),
               User(Nombre="LUIS TORRALBA CEREZO", Matricula=202255279, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.78, Materias_Reprobadas=1),
               User(Nombre="AARON TORRES CORTE", Matricula=202255315, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=64, Promedio=9.1, Materias_Reprobadas=0),
               User(Nombre="JOSUE TORRES ZAMORA", Matricula=202269113, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.65, Materias_Reprobadas=0),
               User(Nombre="ESMERALDA URBINA CINTO", Matricula=202269252, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=8.43, Materias_Reprobadas=0),
               User(Nombre="BRANDON VEGA RAMIREZ", Matricula=202256334, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=64, Promedio=9.12, Materias_Reprobadas=2),
               User(Nombre="JONATHAN VERGARA NAVARRO", Matricula=202270252, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.0, Materias_Reprobadas=0),
               User(Nombre="KALTUM VIVEROS GOMEZ", Matricula=202256742, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=7, Porcentaje=58, Promedio=8.5, Materias_Reprobadas=1),
               User(Nombre="MARCO BARBOSA CABRERA", Matricula=202133193, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.6, Materias_Reprobadas=0),
               User(Nombre="LUIS CLEMENTE CRUZ", Matricula=202259770, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=9.6, Materias_Reprobadas=0),
               User(Nombre="JORGE DAMIAN COCONE RAMIREZ", Matricula=202221609, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.4, Materias_Reprobadas=1),
               User(Nombre="JOSE ANTONIO DANIEL JIMENEZ", Matricula=202238037, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.8, Materias_Reprobadas=0),
               User(Nombre="ALEJANDRO GARCIA CONTRERAS", Matricula=202273840, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=52, Promedio=8.23, Materias_Reprobadas=0),
               User(Nombre="ERNESTO GONZALEZ LOZADA", Matricula=202123049, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=8.45, Materias_Reprobadas=0),
               User(Nombre="ARANTZA GORRAEZ REYES", Matricula=202123214, Edad=24, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=8, Porcentaje=58, Promedio=8.67, Materias_Reprobadas=0),
               User(Nombre="JOSUE GUZMAN LOPEZ", Matricula=202227012, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.6, Materias_Reprobadas=0),
               User(Nombre="ERIK LOPEZ ABUSTOS", Matricula=202232408, Edad=23, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.3, Materias_Reprobadas=0),
               User(Nombre="EVER LOPEZ RAMIREZ", Matricula=202228369, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.1, Materias_Reprobadas=1),
               User(Nombre="SOSTENES LUCAS SOSA", Matricula=202228463, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.5, Materias_Reprobadas=0),
               User(Nombre="MOISES MACHORRO PORTILLA", Matricula=202232944, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=7, Porcentaje=58, Promedio=9.8, Materias_Reprobadas=0),
               User(Nombre="DANIELA MANNY TOXQUI", Matricula=202137558, Edad=22, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=8.7, Materias_Reprobadas=0),
               User(Nombre="DIEGO ARMANDO MEJIA ARENAS", Matricula=202243775, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.9, Materias_Reprobadas=0),
               User(Nombre="VICTOR MENDOZA SAINZ", Matricula=202138595, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=52, Promedio=8.77, Materias_Reprobadas=1),
               User(Nombre="CRISTIAN PULIDO HERNANDEZ", Matricula=202089225, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=9.43, Materias_Reprobadas=0),
               User(Nombre="ROCIO RAMIREZ FABIAN", Matricula=202153429, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Femenino", Semestre=6, Porcentaje=58, Promedio=9.56, Materias_Reprobadas=2),
               User(Nombre="ALDO RAMIREZ JARILLO", Matricula=202248925, Edad=21, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=52, Promedio=8.45, Materias_Reprobadas=0),
               User(Nombre="JOSE ARMANDO RAMOS RAMOS", Matricula=202154423, Edad=20, Carrera="Ingeneria en tecnologias de la informacion", Genero="Masculino", Semestre=6, Porcentaje=58, Promedio=8.1, Materias_Reprobadas=0),
            ]

#FILTRON CON PATH------------------------------------------------------------------------------------

@app.get("/usuarios")
def get_all_users():
    return alumnos_list

@app.get("/userclassP/nombre/{nombre}")
async def get_by_nombre(nombre: str):
    users = filter(lambda user: user.Nombre.lower() == nombre.lower(), alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/matricula/{matricula}")
async def get_by_matricula(matricula: int):
    users = filter(lambda user: user.Matricula == matricula, alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/edad/{edad}")
async def get_by_edad(edad: int):
    users = list(filter (lambda user: user.Edad == edad, alumnos_list))
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/carrera/{carrera}")
async def get_by_carrera(carrera: str):
    users = filter(lambda user: user.Carrera.lower() == carrera.lower(), alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/genero/{genero}")
async def get_by_genero(genero: str):
    users = filter(lambda user: user.Genero.lower() == genero.lower(), alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/semestre/{semestre}")
async def get_by_semestre(semestre: int):
    users = filter(lambda user: user.Semestre == semestre, alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/porcentaje/{porcentaje}")
async def get_by_porcentaje(porcentaje: int):
    users = filter(lambda user: user.Porcentaje == porcentaje, alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/promedio/{promedio}")
async def get_by_promedio(promedio: float):
    users = filter(lambda user: user.Promedio == promedio, alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

@app.get("/userclassP/reprobadas/{materias}")
async def get_by_materias_reprobadas(materias: int):
    users = filter(lambda user: user.Materias_Reprobadas == materias, alumnos_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
#FILTRON CON QUERY------------------------------------------------------------------------------------

@app.get("/userclassQ/filtro1/")
async def filtro1(nombre: str, carrera: str):
    users = filter(lambda user: user.Nombre == nombre and user.Carrera == carrera, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/semestre/")
async def semestre(genero: str, semestre: int):
    users = filter(lambda user: user.Genero == genero and user.Semestre == semestre, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro3/")
async def filtro3(edad: int, porcentaje: int):
    users = filter(lambda user: user.Edad == edad and user.Porcentaje == porcentaje, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro4/")
async def filtro4(promedio: float, reprobadas: int):
    users = filter(lambda user: user.Promedio == promedio and user.Materias_Reprobadas == reprobadas, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro5/")
async def filtro5(carrera: str, semestre: int, genero: str):
    users = filter(lambda user: user.Carrera == carrera and user.Semestre == semestre and user.Genero == genero, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro6/")
async def filtro6(nombre: str, promedio: float):
    users = filter(lambda user: user.Nombre == nombre and user.Promedio == promedio, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro7/")
async def filtro7(matricula: int, edad: int):
    users = filter(lambda user: user.Matricula == matricula and user.Edad == edad, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro8/")
async def filtro8(porcentaje: int, genero: str):
    users = filter(lambda user: user.Porcentaje == porcentaje and user.Genero == genero, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro9/")
async def filtro9(semestre: int, promedio: float, reprobadas: int):
    users = filter(lambda user: user.Semestre == semestre and user.Promedio == promedio and user.Materias_Reprobadas == reprobadas, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}

@app.get("/userclassQ/filtro10/")
async def filtro10(nombre: str, carrera: str, porcentaje: int):
    users = filter(lambda user: user.Nombre == nombre and user.Carrera == carrera and user.Porcentaje == porcentaje, alumnos_list)
    try:
        return list(users)
    except:
        return {"error": "Nombre no encontrado"}
