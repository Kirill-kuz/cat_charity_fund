from typing import List
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


def investment_procces(
    target: CharityProject, sources: List[Donation]
) -> List[Donation]:
    target.invested_amount = (
        0 if target.invested_amount is None else target.invested_amount
    )
    new_sources = []
    for source in sources:
        if target.fully_invested:
            break
        donation = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
            source.full_amount
        )
        for obj in (target, source):
            obj.invested_amount += donation
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.utcnow()
        new_sources.append(source)
    return new_sources


async def make_payment(session: AsyncSession):
    charity_projects = await charity_project_crud.get_opens(session)
    donations = await donation_crud.get_opens(session)

    if not charity_projects or not donations:
        return

    updated_donations = []
    for charity_project in charity_projects:
        updated_donations.extend(
            investment_procces(charity_project, donations))

    if updated_donations:
        session.add_all(updated_donations)
        await session.commit()
