import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # TODO implement
    logger.debug(event)
    
    amount = float(event["currentIntent"]["slots"]["amount"])
    frm = str(event["currentIntent"]["slots"]["from"]).upper()
    to = str(event["currentIntent"]["slots"]["to"]).upper()

    
    rates = {
        "USD" : 1.0,
        "EUR" : 0.85,
        "NPR" : 117.19,
        "INR" : 73.10,
        "YEN" : 105.77,
        "AUD" : 1.39,
        "HKD" : 7.75,
        "ZAR" : 16.61,
        "SEK" : 8.90,
        "BZR" : 5.58,
    }
    
    if frm in rates and to in rates:
        new = (amount/rates[frm]) * rates[to]
        
    
        return {
            "sessionAttributes": event["sessionAttributes"],
            "dialogAction" : {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message" : {
                    "contentType" : "PlainText",
                    "content": "The "+to +" equivalent is: "+ str("%.2f" % new)
                }
            }
        }
    else:
        return{
            "sessionAttributes": event["sessionAttributes"],
            "dialogAction" : {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message" : {
                    "contentType" : "PlainText",
                    "content": "The currency type is not in the system, please try again with a different type",
                }
            }
            
        }