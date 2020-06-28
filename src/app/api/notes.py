from typing import List

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


@router.get('/{id}', response_model=NoteDB)
async def get_note(id: int):
    note = await crud.get(id)

    if not note:
        raise HTTPException(status_code=404, detail='Note not found')

    return note


@router.get('/', response_model=List[NoteDB])
async def get_all_notes():
    return await crud.get_all()