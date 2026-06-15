import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sistema Inteligente de Mantenimiento Predictivo",
    layout="wide"
)

st.title("🔧 Sistema Inteligente de Mantenimiento Predictivo")
st.subheader("Monitoreo de Bombas de Extracción")

modo = st.selectbox(
    "Seleccionar condición de operación",
    ["Operación Normal", "Posible Falla", "Falla Crítica"]
)

if modo == "Operación Normal":
    temperatura = 35
    corriente = 2.1
    vibracion = "Normal"
    estado = "🟢 Operación Normal"

elif modo == "Posible Falla":
    temperatura = 58
    corriente = 4.5
    vibracion = "Alta"
    estado = "🟡 Alerta Preventiva"

else:
    temperatura = 85
    corriente = 8.2
    vibracion = "Crítica"
    estado = "🔴 Falla Crítica"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperatura", f"{temperatura} °C")

with col2:
    st.metric("⚡ Corriente", f"{corriente} A")

with col3:
    st.metric("📈 Vibración", vibracion)

st.markdown("### Estado del Sistema")
st.info(estado)

st.divider()

datos = pd.DataFrame({
    "Hora":["10:00","10:10","10:20","10:30","10:40","10:50"],
    "Temperatura":[32,34,35,36,35,temperatura],
    "Corriente":[1.8,1.9,2.0,2.1,2.0,corriente]
})

st.subheader("📋 Historial de Operación")
st.dataframe(datos)

st.subheader("📊 Temperatura vs Tiempo")

fig1 = px.line(
    datos,
    x="Hora",
    y="Temperatura",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("📊 Corriente vs Tiempo")

fig2 = px.line(
    datos,
    x="Hora",
    y="Corriente",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("🚨 Alertas")

if modo == "Operación Normal":
    st.success("No se detectan anomalías.")
elif modo == "Posible Falla":
    st.warning("Posible desgaste mecánico detectado. Se recomienda inspección.")
else:
    st.error("Falla crítica detectada. Se recomienda mantenimiento inmediato.")