import streamlit as st
import pandas as pd

from azure.storage.blob import BlobServiceClient

StorageAccountName1 = "storagealisamiento"
StorageAccountKey1 = "QSrEesxEZvyPyYKOtOzHSOsYueT9Zgv7c0tYT953aRBmSMGCBc8fDTrd0O96c/LeEspOTMVomTdJCgWjTVJFjg=="

blobService = BlobServiceClient(account_url="https://" + StorageAccountName1 + ".blob.core.windows.net", credential=StorageAccountKey1)

def write_dataframe_to_csv_blob(df, container, path, sep, decimal, blob_service, header=True):
    csv_string = df.to_csv(index=False, header=header, sep = sep, decimal = decimal, date_format='%Y-%m-%d')
    try:
        result = blob_service.get_blob_client(container, path).upload_blob(csv_string, blob_type="BlockBlob", overwrite=True)
    except:
        result = blob_service.get_blob_client(container, path).upload_blob(csv_string, blob_type="BlockBlob", overwrite=True)
    return result

st.image(image='logoEroski.png')

st.title('Carga Diaria Plataforma')
st.header('Subir el archivo en formato EXCEL con la carga diaria de la plataforma')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name=1)
    write_dataframe_to_csv_blob(df, 'datauser', '4d_nueva_planificacion_plataforma.csv', ";", ".", blobService, header=True)
    st.header("archivo guardado correctamente")
    st.write(uploaded_file)
