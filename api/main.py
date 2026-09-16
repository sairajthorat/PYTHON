from fastapi import FastAPI, HTTPException

app = FastAPI()

# Temporary database
users = {}

# ID counter
next_id = 1


# CREATE
@app.post("/users")
def create_user(user: dict):
    global next_id

    users[next_id] = user

    response = {
        "id": next_id,
        "user": user
    }

    next_id += 1

    return response


# READ - Get all users
@app.get("/users")
def get_users():
    return users


# READ - Get one user
@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user_id,
        "user": users[user_id]
    }



# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = user

    return {
        "id": user_id,
        "user": user
    }




# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }
