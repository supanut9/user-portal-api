from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from . import models, schemas

async def get_profile_by_user_id(session: AsyncSession, user_id: str):
    """
    Retrieves a single profile from the database by user_id.
    """
    result = await session.exec(select(models.Profile).where(models.Profile.user_id == user_id))
    return result.first()


async def create_profile(session: AsyncSession, profile: schemas.ProfileCreate):
    """
    Creates a new profile record in the database.
    """
    db_profile = models.Profile.model_validate(profile)
    session.add(db_profile)
    await session.commit()
    await session.refresh(db_profile)
    return db_profile