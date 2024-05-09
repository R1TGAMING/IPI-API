from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import uvicorn
import userGithub
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder
import json
from fastapi import Response
import youtubeuser
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from fastapi.responses import FileResponse, StreamingResponse

app = FastAPI()
templates = Jinja2Templates(directory="main_web")

##MAIN PAGE
@app.get("/api", response_class=HTMLResponse)
def main_api(request : Request) :
  return templates.TemplateResponse("index.html", {"request": request})

##GITHUB USER INFORMATION
@app.get("/api/githubuser&&name={name}")
def read_root(name : str):
  info = userGithub.get(name)
  
  infodata = {
    "name" : info["name"],
    "username": info["username"],
    "id" : info["id"],
    "bio" : info["bio"],
    "location" : info["location"],
    "avatar" : info["avatar"],
    "url" : info["url"],
    
  }
  json_str = json.dumps(infodata)
  return Response(content=json_str, media_type="application/json")

##YOUTUBE USER INFORMATION
#@app.get("/api/youtubeuser&&name={name}")
#def read_root(name : str) :
  #ytuser = youtubeuser.user.getUser(name)
  #ytdata = {
 #   "description" : ytuser["snippet"]["title"],
  #}
  #json_str = json.dumps(ytdata)
  #return Response(content=json_str, media_type="application/json")

## LAUGH EMOJI API
@app.get("/api/laughEmoji&&text={text}", response_class=Response)
async def read_root(text : str) :
  openimg = Image.open("./images/meme1.jpeg")
  img = ImageDraw.Draw(openimg)
  font = ImageFont.truetype("./fonts/ObelixProB-cyr.ttf", 80)
  _, _, w, h = img.textbbox((0,0), text, font=font)
  W, H = openimg.size
  img.text(((W-w)/2, 450), text=text, fill=(255, 255, 255), align = "center", font=font, stroke_fill = (0,0,0), stroke_width=2)
  bytes = BytesIO()
  openimg.save(bytes, format="PNG")
  bytes.seek(0)
  return StreamingResponse(BytesIO(bytes.read()), media_type="image/png")


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port = 8000)