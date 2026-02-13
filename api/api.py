from fastapi import APIRouter,Depends,HTTPException, status
from Models.Task_schemas import Create,Show,Update,ShowTask
from Auth.Dependencies import get_current_user,require_role
from Database.database import Base,engine,get_db
from sqlalchemy.orm import Session
from Models.table import Task,Users

router=APIRouter(prefix="/CRUD/v1",tags=["CRUD"])
Base.metadata.create_all(bind=engine)

@router.post("/Create",response_model=Show)
def Create(request:Create,db:Session = Depends(get_db),current_user=Depends(get_current_user)):
    Create_task=Task(task=request.Task,description=request.Description,owner_id=current_user.id)
    db.add(Create_task)
    db.commit()
    db.refresh(Create_task)
    return Create_task

@router.get("/task/{id}",response_model=Show)
def Get_Task(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task=db.query(Task).filter(Task.id==id,Task.owner_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with the id {id} is not available")
    
    return task

@router.get("/tasks")
def Tasks(db:Session=Depends(get_db),current_user=Depends(require_role("admin"))):
        try:  
            tasks=db.query(Task).filter(Task.owner_id==current_user.id).all()
            return tasks
        except:
            return ("Not Enough Permissions")

@router.patch("/tasks/{task_id}", response_model=Show)
def update_task(
    task_id: int,
    updated_data: Update,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id,Task.owner_id == current_user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    
    if updated_data.title is not None:
        task.task = updated_data.title

    if updated_data.description is not None:
        task.description = updated_data.description

    db.commit()
    db.refresh(task)

    return task

@router.delete("/{id}")
def delete_todo(id: int,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    db_todo = db.query(Task).filter(id==Task.id,Task.owner_id == current_user.id).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Only owner or admin can delete
    if current_user.role != "admin" and db_todo.owner_id != current_user.id:
      raise HTTPException(status_code=403, detail="Not authorized to delete this todo")

    db.delete(db_todo)
    db.commit()

    return {"message": "Deleted successfully"}