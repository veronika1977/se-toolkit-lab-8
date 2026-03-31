from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database import get_session
from backend.app.models.item import ItemRecord, ItemCreate

router = APIRouter()

@router.get("/")
async def get_items(session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(select(ItemRecord))
        items = result.scalars().all()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@router.head("/")
async def head_items(session: AsyncSession = Depends(get_session)):
    try:
        result = await session.execute(select(ItemRecord))
        items = result.scalars().all()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
