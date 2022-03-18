from __future__ import annotations

from typing import List

from pydantic import BaseModel


# class EmailsList(BaseModel):
#     emails: List[str]
#
#
# class PhonesList(BaseModel):
#     phones: List[str]


class BeforeEnrichment(BaseModel):
    successor_mame: str
    phones: List[str]
    emails: List[str]
