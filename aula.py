import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

 
 
modelo = load_model('meu-modelo-para-os-custos') 

def classificador(modelo, dados):
	 
	return pred


st.sidebar.header('**Medical Cost Deploy Center**') 
 

st.markdown('![alt text](https://github.com/ricardorocha86/WebApp-MedicalCost/blob/main/imagens/Slide2.JPG?raw=true)')

st.markdown('# Modelagem de valor do seguro')

st.markdown('---')

idade = st.sidebar.number_input('Idade', 18, 65, 30)
sexo = st.sidebar.selectbox("Sexo", ['male', 'female'])
imc = st.sidebar.number_input('Índice de Massa Corporal', 15, 54, 24)
criancas = st.sidebar.selectbox("Quantidade de filhos", [0, 1, 2, 3, 4, 5])
fumante = st.sidebar.selectbox("É fumante?", ['yes', 'no'])
regiao = st.sidebar.selectbox("Região em que mora", 
								  ['southeast', 'southwest', 'northeast', 'northwest'])

 

dados_dicio = {'age': [idade], 'sex': [sexo], 'bmi': [imc], 
			'children': [criancas], 'region': [regiao], 'smoker': [fumante]}
		
dados = pd.DataFrame(dados_dicio)
 
if st.button('APLICAR O MODELO'):
	saida = predict_model(estimator = modelo, data = dados) 
	pred = float(saida['Label'].round(2)) 

	s1 = 'Custo Estimado do Seguro: ${:.2f}'.format(pred) 

	st.markdown('## Resultados do modelo para as entradas:') 
	st.markdown('## **' + s1 + '**')  
