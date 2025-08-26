import azure.functions as func
from azure.data.tables import TableServiceClient
import os
import uuid
import json

async def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Obtener datos enviados
        data = req.get_json()
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return func.HttpResponse("Faltan campos 'title' o 'content'", status_code=400)

        # Conexión a Table Storage
        conn_str = os.environ["AzureWebJobsStorage"]
        table_service = TableServiceClient.from_connection_string(conn_str)
        table_client = table_service.get_table_client("NewsTable")

        # Crear la tabla si no existe
        try:
            table_client.create_table()
        except:
            pass  # Si ya existe, seguimos

        # Insertar noticia
        entity = {
            "PartitionKey": "News",
            "RowKey": str(uuid.uuid4()),
            "Title": title,
            "Content": content
        }
        table_client.create_entity(entity)

        return func.HttpResponse(json.dumps({"message": "Noticia agregada"}), mimetype="application/json", status_code=201)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
