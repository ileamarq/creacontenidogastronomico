import streamlit as st
import requests
import os

st.header('Creador de Contenido Gastronómico')  
text = st.text_input('Nombre de la receta')

base_url = "https://api.dify.ai/v1"
path = "/completion-messages"
my_secret = os.environ['DIFY_APP_SECRET']

headers = {
  "Authorization": f"Bearer {my_secret}",
  "Content-Type": "application/json"
}

data = {
  "inputs": {
   "text": text,
 },

"response_mode": "blocking",
"user": "crea contenido gastronomico"
}

url_completa = base_url + path
if st.button('Generar receta'):
  response = requests.post(url_completa, json=data, headers=headers)

  if response.status_code == 200:
   st.success("Receta Obenida Exitosamente")

   result = response.json()
  # Imprimir la respuesta
   st.markdown("### Receta generada:")
   st.markdown(result["answer"])
  else:
   st.error("Error al generar la receta")
st.write("¡Gracias por usar la aplicación! ¡Hasta luego!")




