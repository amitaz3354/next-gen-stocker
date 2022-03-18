from enricher_template import EnricherTemplate
from neutrino_api.controllers.telephony import Telephony
from enriched_succssor import PhoneNumbersSummaryItem
from typing import List


class PhoneEnricher(EnricherTemplate):

    @staticmethod
    def enrich(controller: Telephony, data_list: List[str]) -> List[PhoneNumbersSummaryItem]:
        res_list = []

        for phone in data_list:
            res = controller.hlr_lookup(number=phone)

            as_dict = {"number": phone,
                       "is_valid": res.number_valid,
                       "country": res.country}

            summary_item = PhoneNumbersSummaryItem.parse_obj(as_dict)
            res_list.append(summary_item)

        return res_list
