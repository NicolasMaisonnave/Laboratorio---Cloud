import logging
import azure.functions as func
from datetime import datetime
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('LogAccess function processed a request.')

    # Simulamos el registro en Table Storage (localmente imprimimos)
    log_entry = {
        "PartitionKey": "AccessLog",
        "RowKey": str(uuid.uuid4()),
        "Timestamp": datetime.utcnow().isoformat()
    }

    logging.info(f"Log Entry: {log_entry}")

    return func.HttpResponse(
        "Access logged successfully",
        status_code=200
    )
