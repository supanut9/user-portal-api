from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from . import schemas
from . import crud
from ..database import get_session

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/", response_model=schemas.ProfileRead, status_code=status.HTTP_201_CREATED)
async def handle_create_profile(
    profile: schemas.ProfileCreate, 
    db: AsyncSession = Depends(get_session)
):
    db_profile = await crud.get_profile_by_user_id(session=db, user_id=profile.user_id)
    if db_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Profile already registered for this user"
        )
    return await crud.create_profile(session=db, profile=profile)