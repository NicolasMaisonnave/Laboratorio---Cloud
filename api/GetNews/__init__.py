import azure.functions as func
from azure.data.tables import TableServiceClient
import os
import json

async def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Conexión a Table Storage
        conn_str = os.environ["AzureWebJobsStorage"]
        table_service = TableServiceClient.from_connection_string(conn_str)
        table_client = table_service.get_table_client("NewsTable")

        # Consultar todas las noticias
        entities = table_client.query_entities("PartitionKey eq 'News'")
        news_list = [{"title": e["Title"], "content": e["Content"]} for e in entities]

        return func.HttpResponse(json.dumps(news_list), mimetype="application/json", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
