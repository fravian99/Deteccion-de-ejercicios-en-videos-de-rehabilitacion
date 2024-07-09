import os
import secrets
from fastapi.responses import StreamingResponse
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def save_file(opened_file, ext, approute):
    random_hex = secrets.token_hex(10)
    filename = random_hex + "." + ext
    abs_filename = os.path.join(approute, filename)
    with open(abs_filename, "wb") as file:
        try:
            contents = opened_file.file.read()
            file.write(contents)
        except Exception as ex:
            raise ex

    return  filename

def delete_file(file, approute):
    try:
        filename = os.path.join(approute, file)
        os.remove(filename)
    except Exception as ex:
        raise ex
    return True

def open_video(filename, approute):
    video_path = os.path.join(approute, filename)

    def iterfile(video_path):
        with open(video_path, mode="rb") as file_like:
            yield from file_like
    
    return StreamingResponse(iterfile(video_path), media_type="video/mp4")

