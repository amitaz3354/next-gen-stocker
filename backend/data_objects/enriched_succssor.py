from __future__ import annotations

from typing import List

from pydantic import BaseModel


class PhoneNumbersSummaryItem(BaseModel):
    number: int
    is_valid: str
    country: str


class EmailsSummaryItem(BaseModel):
    email: str
    is_valid: str


class EnrichedSuccessor(BaseModel):
    successorName: str
    phone_numbers_summary: List[PhoneNumbersSummaryItem]
    emails_summary: List[EmailsSummaryItem]
