from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from . import schemas, services
from ..database import get_session
from .. import dependencies

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/", response_model=schemas.ProfileRead, status_code=status.HTTP_201_CREATED)
async def handle_create_profile(
    profile: schemas.ProfileCreate,
    db: AsyncSession = Depends(get_session)
):
    """
    API endpoint to create a new profile.
    The business logic is handled by the service layer.
    """
    return await services.create_new_profile(session=db, profile=profile)


@router.get("/{user_id}", response_model=schemas.ProfileRead)
async def handle_get_profile(
    user_id: str,
    db: AsyncSession = Depends(get_session),
):
    """
    API endpoint to retrieve a user profile by their user_id.
    The business logic is handled by the service layer.
    """
    return await services.get_user_profile(session=db, user_id=user_id)