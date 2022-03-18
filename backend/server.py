import json

from fastapi import FastAPI
from neutrino_api.neutrino_api_client import NeutrinoApiClient

from apis_payloads import BeforeEnrichment
from email_enricher import EmailEnricher
from enriched_succssor import EnrichedSuccessor
from phone_enricher import PhoneEnricher

app = FastAPI()


def connect_to_client() -> NeutrinoApiClient:
    user_id = "amit_az3354"
    api_key = "1FANb7Rwh3rVzN0VJewvpyYDXUbgo2RUVEuG7Bmnxi1mIsfr"
    return NeutrinoApiClient(user_id, api_key)


client = connect_to_client()


# todo - make it rubost
@app.post("/enrich/")
async def enrich_all(raw_data: BeforeEnrichment):
    phone_summary = PhoneEnricher.enrich(controller=client.telephony, data_list=raw_data.phones)
    email_summary = EmailEnricher.enrich(controller=client.security_and_networking, data_list=raw_data.emails)
    enriched_successor = EnrichedSuccessor(successor_name=raw_data.successor_mame,
                                           phone_numbers_summary=phone_summary,
                                           emails_summary=email_summary)
    return json.loads(enriched_successor.json())

# @app.post("/enrich/phones/")
# async def enrich_phones(phones: PhonesList):
#     controller = client.telephony
#     return PhoneEnricher.enrich(controller=controller, data_list=phones.phones)
#
#
# @app.post("/enrich/mails/")
# async def enrich_mails(emails: EmailsList):
#     controller = client.security_and_networking
#     return EmailEnricher.enrich(controller=controller, data_list=emails.emails)
