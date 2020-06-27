from app.api.models import NoteSchema
from app.db import database, notes


async def post(payload: NoteSchema):
    query = notes.insert().values(
        title=payload.title,
        description=payload.description,
    )
    return await database.execute(query=query)