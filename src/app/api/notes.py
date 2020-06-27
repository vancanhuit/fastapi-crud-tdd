from fastapi import APIRouter, HTTPException

from app.api import crud
from app.api.models import NoteSchema, NoteDB


router = APIRouter()


@router.post('/', response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response = {
        'id': note_id,
        'title': payload.title,
        'description': payload.description
    }

    return response