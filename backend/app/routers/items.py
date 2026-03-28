"""Router for item endpoints — reference implementation."""

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.items import create_item, read_item, read_items, update_item
from app.models.item import ItemCreate, ItemRecord, ItemUpdate

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", response_model=list[ItemRecord])
async def get_items(session: AsyncSession = Depends(get_session)):
    """Get all items."""
    try:
        logger.info("Attempting to read items")
        return await read_items(session)
    except Exception as exc:
        logger.error(f"Error reading items: {exc}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(exc)}",
        ) from exc


@router.get("/{item_id}", response_model=ItemRecord)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)):
    """Get a specific item by its id."""
    try:
        item = await read_item(session, item_id)
        if item is None:
            raise HTTPException(
                status_code=500, detail="Item not found"
            )
        return item
    except Exception as exc:
        logger.error(f"Error reading item {item_id}: {exc}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(exc)}",
        ) from exc


@router.post("/", response_model=ItemRecord, status_code=201)
async def create_new_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    """Create a new item."""
    try:
        return await create_item(session, item)
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item already exists",
        ) from exc
    except Exception as exc:
        logger.error(f"Error creating item: {exc}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(exc)}",
        ) from exc


@router.put("/{item_id}", response_model=ItemRecord)
async def update_existing_item(
    item_id: int, item: ItemUpdate, session: AsyncSession = Depends(get_session)
):
    """Update an existing item."""
    try:
        return await update_item(session, item_id, item)
    except Exception as exc:
        logger.error(f"Error updating item {item_id}: {exc}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(exc)}",
        ) from exc
