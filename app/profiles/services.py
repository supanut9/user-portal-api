from fastapi import HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from . import crud, schemas

async def create_new_profile(session: AsyncSession, profile: schemas.ProfileCreate) -> schemas.ProfileRead:
    """
    Business logic to create a new profile.
    Checks if a profile already exists for the user before creating a new one.
    """
    # Business Rule: Check for existing profile
    db_profile = await crud.get_profile_by_user_id(session=session, user_id=profile.user_id)
    if db_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile already registered for this user"
        )
    
    # If no existing profile, proceed to create one
    return await crud.create_profile(session=session, profile=profile)

async def get_user_profile(session: AsyncSession, user_id: str) -> schemas.ProfileRead:
    """
    Business logic to retrieve a user profile.
    Handles the case where the profile is not found.
    """
    db_profile = await crud.get_profile_by_user_id(session=session, user_id=user_id)
    if db_profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return db_profile