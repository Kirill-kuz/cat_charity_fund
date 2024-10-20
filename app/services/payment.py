from typing import List
from datetime import datetime

from app.core import Base


def investment_procces(
    target: Base, sources: List[Base]
) -> List[Base]:
    new_sources = []
    for source in sources:
        if target.fully_invested:
            break
        if source.invested_amount is None:
               source.invested_amount = 0
        if target.invested_amount is None:
               target.invested_amount = 0
        donation = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
        )
        for obj in (target, source):
            obj.invested_amount += donation
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.utcnow()
        new_sources.append(source)
    return new_sources
