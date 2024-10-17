from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


async def get_open_charity_projects(
    session: AsyncSession
) -> List[CharityProject]:
    open_charity_projects = (
        await charity_project_crud.get_opens(session))
    return open_charity_projects


async def get_open_donations(
    session: AsyncSession
) -> List[Donation]:
    donations = await donation_crud.get_opens(session)
    return donations


async def make_payment(session: AsyncSession):
    charity_projects = await get_open_charity_projects(session)
    donations = await get_open_donations(session)

    if not charity_projects or not donations:
        return

    updated_entities = []

    for donation in donations:
        free_money = donation.full_amount - donation.invested_amount

        for index, charity in enumerate(charity_projects):
            if charity.fully_invested:
                continue

            need_money = charity.full_amount - charity.invested_amount

            if free_money > need_money:
                donation.invested_amount += need_money
                free_money -= need_money
                charity.close()
                updated_entities.append(charity)

            elif free_money < need_money:
                charity.invested_amount += free_money
                donation.close()
                updated_entities.append(donation)
                updated_entities.append(charity)
                del charity_projects[index]
                break

            else:
                charity.close()
                donation.close()
                updated_entities.extend([charity, donation])
                del charity_projects[index]
                break

    if updated_entities:
        session.add_all(updated_entities)
        await session.commit()
