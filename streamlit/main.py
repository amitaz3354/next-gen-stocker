import streamlit as st
import requests
from backend.server import enrich_phones, enrich_mails
from backend.data_objects.enriched_succssor import PhoneNumbersSummaryItem
from backend.data_objects.apis_payloads import PhonesList
import json

st.set_page_config(page_title="Bug report", page_icon="🐞", layout="centered")

st.title("🐞 Successor metadata validator")

form = st.form(key="annotation")

backend_ep1 = "http://fastapi:8000/enrich/phones/"


def post_to_phones_api(phone_numbers: str):
    as_list = phone_numbers.split()
    as_obj = PhonesList(phones=as_list)
    requests.post(url=backend_ep1, json=json.loads(as_obj.json()))


with form:
    cols = st.columns((1, 1))
    name = cols[0].text_input("Enter successor name")
    phone_numbers = cols[1].text_input("Enter phones")
    cols = st.columns(2)
    emails = cols[0].text_input("Enter mails")
    submitted = st.form_submit_button(label="Submit")

if submitted:
    post_to_phones_api(phone_numbers)
    st.text(enrichment.json())
