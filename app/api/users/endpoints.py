from fastapi import APIRouter, HTTPException
from app.api.users.schemas import BubbleUserGet, BubbleUserCreate
from typing import List
import uuid
from exercise import send_slack_message, slack_url  # Correct import
from app.api.users.schemas import db_users

router = APIRouter(
    prefix='/bubble_users'
)

@router.get('/', response_model=List[BubbleUserGet])
async def get_users():
    return db_users

@router.get('/{bubble_id}', response_model=BubbleUserGet)  # Return a single user model
async def get_user(bubble_id: str):
    # Iterate over the users in the db_users list
    for existing_user in db_users:
        # Compare the bubble_id
        if existing_user.bubble_id == bubble_id:
            return existing_user

    # If user is not found, raise an HTTPException
    raise HTTPException(status_code=404, detail="User not found")

@router.post('/', response_model=BubbleUserGet)
async def create_user(user: BubbleUserCreate):
    # Check if user with the same bubble_id already exists
    for existing_user in db_users:
        # Use the correct attribute `bubble_id` for BubbleUserGet model
        if existing_user.bubble_id == user.bubbleId:
            send_slack_message(slack_url,f"Attempted to create a user with bubble_id {user.bubbleId}, but the user already exists.")
            raise HTTPException(status_code=400, detail="User already exists")

    # Create a new user with UUID and timestamps
    new_user = BubbleUserGet(
        id=uuid.uuid4(),
        first_name=user.firstName,
        last_name=user.lastName,
        gender=user.gender,
        email=user.email,
        bubble_id=user.bubbleId
    )

    # Append the new user to the database
    db_users.append(new_user)
    return new_user
