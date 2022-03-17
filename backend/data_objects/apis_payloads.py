from __future__ import annotations

from typing import List

from pydantic import BaseModel


class EmailsList(BaseModel):
    emails: List[str]


class PhonesList(BaseModel):
    phones: List[str]
