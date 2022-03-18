from enricher_template import EnricherTemplate
from enriched_succssor import EmailsSummaryItem
from neutrino_api.controllers.security_and_networking import SecurityAndNetworking
from typing import List


class EmailEnricher(EnricherTemplate):

    @staticmethod
    def enrich(controller: SecurityAndNetworking,
               data_list: List[str]) -> List[EmailsSummaryItem]:
        res_list = []

        for mail in data_list:
            res = controller.email_verify(mail)

            as_dict = {"email": res.email,
                       "is_valid": res.smtp_status}

            summary_item = EmailsSummaryItem.parse_obj(as_dict)
            res_list.append(summary_item)

        return res_list
