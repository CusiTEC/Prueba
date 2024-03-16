import streamlit as st
import pickle
import numpy as np

def main():
    st.title("Aplicación con múltiples pestañas")

    # Crear un panel lateral para colocar los enlaces a las pestañas
    st.sidebar.title("Navegación")
    pestañas = ["Página 1", "Página 2"]
    seleccion = st.sidebar.radio("Ir a", pestañas)

    # Mostrar el contenido de la pestaña seleccionada
    if seleccion == "Página 1":
        mostrar_pagina1()
    elif seleccion == "Página 2":
        mostrar_pagina2()

def mostrar_pagina1():
    st.header("Página 1")

    st.title('Aplicación de ML   de diserción estudiantil')
    
    with open('modelotree.pkl', 'rb') as archivo:
        miarbol = pickle.load(archivo)
    
    # Ahora puedes usar miarbol dentro de este bloque
    
    st.write("Ingrese los valores de entrada:")
    
    # Permitir al usuario ingresar manualmente cada valor de x_input
    x_input = []
    #-----------------------------VARIABLES-------------------------------
    #SEX
    genero = st.radio("Género", options=["Masculino", "Femenino"])
    # Mapear las opciones a 0 y 1
    if genero == "Femenino":
        x_input.append(0)
    else:
        x_input.append(1)
        
    #EDAD
    edad = st.number_input("Edad", min_value=11, max_value=18, step=1)
    x_input.append(edad)
    
    #EDUCACION DE LA MADRE
    niveles_educativos = ["Ninguno", "Primario", "Secundario", "Superior No Universitario","Superior Universitario"]
    nivel_educativo = st.selectbox("Nivel Educativo de la Madre", options=niveles_educativos)
    
    # Mapear las opciones a 0, 1, 2, 3
    if nivel_educativo == "Ninguno":
        x_input_nivel_educativo = 0
    elif nivel_educativo == "Primario":
        x_input_nivel_educativo = 1
    elif nivel_educativo == "Secundario":
        x_input_nivel_educativo = 2
    elif nivel_educativo == "Superior No Universitario":
        x_input_nivel_educativo = 3
    elif nivel_educativo == "Superior Universitario":
        x_input_nivel_educativo = 4
    x_input.append(x_input_nivel_educativo)
    
    #EDUCACION DEL PADRE
    niveles_educativosf = ["Ninguno", "Primario", "Secundario", "Superior No Universitario","Superior Universitario"]
    nivel_educativof = st.selectbox("Nivel Educativo del Padre", options=niveles_educativosf)
    
    # Mapear las opciones a 0, 1, 2, 3
    if nivel_educativof == "Ninguno":
        x_input_nivel_educativof = 0
    elif nivel_educativof == "Primario":
        x_input_nivel_educativof = 1
    elif nivel_educativof == "Secundario":
        x_input_nivel_educativof = 2
    elif nivel_educativof == "Superior No Universitario":
        x_input_nivel_educativof = 3
    elif nivel_educativof == "Superior Universitario":
        x_input_nivel_educativof = 4
    x_input.append(x_input_nivel_educativof)
    
    #MADRE TRABAJA
    trabajoM = st.radio("La madre Trabajo", options=["No trabaja", "Trabaja"])
    # Mapear las opciones a 0 y 1
    if trabajoM == "No trabaja":
        x_input.append(0)
    else:
        x_input.append(1)
        
    #PADRE TRABAJA
    trabajoP = st.radio("El padre Trabaja", options=["No trabaja", "Trabaja"])
    # Mapear las opciones a 0 y 1
    if trabajoP == "No trabaja":
        x_input.append(0)
    else:
        x_input.append(1)
    
    #TIEMPO EN IR AL COLEGIO
    go_schoolf= ["Menos de 15 min", "Menos de 15 min", "De 30 min a 1 hora", "Mas de 1 hora"]
    go_schoolx= st.selectbox("Tiempo demora en ir al colegio", options=go_schoolf)
    
    # Mapear las opciones a 0, 1, 2, 3
    if go_schoolx == "Menos de 15 min":
        x_input_nivel = 1
    elif go_schoolx == "Menos de 15 min":
        x_input_nivel = 2
    elif go_schoolx == "De 30 min a 1 hora":
        x_input_nivel = 3
    elif go_schoolx == "Mas de 1 hora":
        x_input_nivel = 4
    x_input.append(x_input_nivel)
    
    #TIEMPO SEMANAL DE ESTUDIO
    go_schools= ["Menos de 2 horas", "De 2 a 5 horas", "De 5 a 10 horas", "Mas de 10 horas"]
    go_schoola= st.selectbox("Tiempo semanal de estudio", options=go_schools)
    
    # Mapear las opciones a 0, 1, 2, 3
    if go_schoola == "Menos de 2 horas":
        x_input_nivel = 1
    elif go_schoola == "De 2 a 5 horas":
        x_input_nivel = 2
    elif go_schoola == "De 5 a 10 horas":
        x_input_nivel = 3
    elif go_schoola == "Mas de 10 horas":
        x_input_nivel = 4
    x_input.append(x_input_nivel)
   
    #NUMERO DE FRACASOS
    fracaso = st.number_input("Numero de fracasos", min_value=0, max_value=4, step=1)
    x_input.append(fracaso)
    
    #APOYO EDUCACIONAL
    educaciont = st.radio("Tiene apoyo educacional", options=["No tiene", "Si tiene"])
    # Mapear las opciones a 0 y 1
    if educaciont == "No tiene":
        x_input.append(0)
    else:
        x_input.append(1)
    
    #SALE CON AMIGOS
    salir = st.number_input("De 1 al 5 que tanto sale con amigos", min_value=1, max_value=5, step=1)
    x_input.append(salir)
    
    #ESTADO DE SALUD
    salud = st.number_input("De 1 al 5 estado de salud", min_value=1, max_value=5, step=1)
    x_input.append(salud)
    
    #NUMERO DE AUSENCIAS
    ausencia = st.number_input("Ausencias (cantidad de dias)", min_value=0, max_value=93, step=1)
    x_input.append(ausencia)
    
    #DONDE VIVE?
    zonav= st.radio("Donde vive", options=["Rural", "Urbano"])
    # Mapear las opciones a 0 y 1
    if zonav == "Rural":
        x_input.append(1)
    else:
        x_input.append(0)
    
    #ESTADO DE LOS PADRES
    estadoparents = st.radio("Estado de convivenica de los padres", options=["Juntos", "Separados"])
    # Mapear las opciones a 0 y 1
    if estadoparents == "Juntos":
        x_input.append(0)
    else:
        x_input.append(1)
    
    #QUIERE CURSAR ESTUDIOS SUPERIORES
    highsuper = st.radio("Quiere cursar estudios superiores", options=["No Quiere", "Si Quiere"])
    # Mapear las opciones a 0 y 1
    if highsuper == "No Quiere":
        x_input.append(0)
    else:
        x_input.append(1)
    
    #TIENE ACCESO A INTERNET
    accesonet = st.radio("Tiene acceso a internet", options=["No tiene", "Si tiene"])
    # Mapear las opciones a 0 y 1
    if accesonet == "No tiene":
        x_input.append(0)
    else:
        x_input.append(1)
        
    #APOYO EDUCACIONAL FAMILIAR
    educacionf = st.radio("Tiene apoyo educativo familiar", options=["No tiene", "Si tiene"])
    # Mapear las opciones a 0 y 1
    if educacionf == "No tiene":
        x_input.append(0)
    else:
        x_input.append(1)
    
    
    # Botón para realizar la predicción
    if st.button('Realizar predicción'):
        
        respuesta = 0
        resultado = int(model_prediction(x_input, miarbol))
        
        st.write('El resultado de la predicción es:', resultado)
        respuesta = resultado

        
        if respuesta == 3:
            st.write("Alto Riesgo de deserción")
        elif respuesta == 2:
            st.write("Medio Riesgo de deserción")
        elif respuesta == 1:
            st.write("Bajo Riesgo de deserción")
        elif respuesta == 0:
            st.write("Ningun Riesgo de deserción")
        else:
            print("Valor de respuesta no válido")

def mostrar_pagina2():
    st.header("Página 2")
    # URL del dashboard de Look Studio
    url_dashboard = "https://lookerstudio.google.com/embed/reporting/4ffd3212-cba9-4dee-8158-686daf0d97c3/page/ggFtD"

    # Mostrar el dashboard en un componente iframe
    st.markdown(f'<iframe src="{url_dashboard}" width="1000" height="600"></iframe>', unsafe_allow_html=True)




def model_prediction(x_in, model):
    x = np.reshape(x_in, (1, -1))  # Corregir el reshape
    preds = model.predict(x)
    return preds

# Interfaz gráfica con Streamlit
    
 
if __name__ == "__main__":
    main()
