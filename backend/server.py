from fastapi import FastAPI
from backend.data_objects.apis_payloads import PhonesList, EmailsList
from neutrino_api.neutrino_api_client import NeutrinoApiClient
from backend.neutrino_wrapper.phone_handling.phone_enricher import PhoneEnricher
from backend.neutrino_wrapper.email_handling.email_enricher import EmailEnricher

app = FastAPI()


def connect_to_client() -> NeutrinoApiClient:
    user_id = "amit_az3354"
    api_key = "1FANb7Rwh3rVzN0VJewvpyYDXUbgo2RUVEuG7Bmnxi1mIsfr"
    return NeutrinoApiClient(user_id, api_key)


client = connect_to_client()


@app.post("/enrich/phones/")
async def enrich_phones(phones: PhonesList):
    controller = client.telephony
    return PhoneEnricher.enrich(controller=controller, data_list=phones.phones)


@app.post("/enrich/mails/")
async def enrich_mails(emails: EmailsList):
    controller = client.security_and_networking
    return EmailEnricher.enrich(controller=controller, data_list=emails.emails)
