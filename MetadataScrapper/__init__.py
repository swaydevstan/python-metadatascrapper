import logging
import json
import azure.functions as func
import metadata_parser

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    url = req.params.get('url')
    page = metadata_parser.MetadataParser(url)

    if url:
        return json.dumps(page.metadata)
    else:
        return func.HttpResponse(
             "Enter a URL to view the metadata",
             status_code=200
        )
