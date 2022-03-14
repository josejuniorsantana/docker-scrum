from fastapi import APIRouter
from controller import scrum_controller, task_controller

router = APIRouter()
router.include_router(scrum_controller.router)
router.include_router(task_controller.router)
