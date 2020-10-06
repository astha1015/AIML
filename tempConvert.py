import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # TODO implement
    logger.debug(event)
    celcius = float(event["currentIntent"]["slots"]["temp"])
    faren = float ((celcius * (9/5)) +32)
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction" : {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message" : {
                "contentType" : "PlainText",
                "content": "The farenheit equivalent is: "+ str(faren)
            }
        }
    }
