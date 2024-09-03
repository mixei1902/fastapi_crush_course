from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


# @app.post("/")
# async def add_task(task: STaskAdd):
#     return {"data": task}
#

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
