from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, UploadFile
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
from fastapi.staticfiles import StaticFiles
import requests


app = FastAPI()
templates = Jinja2Templates(directory="./main_web")
app.mount("/static", StaticFiles(directory="static"), name="static")

##MAIN PAGE
@app.get("/api")
def main_api(request : Request) :
  
  return templates.TemplateResponse("index.html", {"request": request})

##GITHUB USER INFORMATION
@app.get("/api/githubUser&&name={name}")
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
  openimg = Image.open("./images/laughEmoji.jpeg")
  img = ImageDraw.Draw(openimg)
  font = ImageFont.truetype("./fonts/ObelixProB-cyr.ttf", 80)
  _, _, w, h = img.textbbox((0,0), text, font=font)
  W, H = openimg.size
  img.text(((W-w)/2, 450), text=text, fill=(255, 255, 255), align = "center", font=font, stroke_fill = (0,0,0), stroke_width=2)
  bytes = BytesIO()
  openimg.save(bytes, format="PNG")
  bytes.seek(0)
  return StreamingResponse(BytesIO(bytes.read()), media_type="image/png")

## DRAKE MEME API
@app.get("/api/drakeMeme&&text1={text1}&text2={text2}")
async def read_root(text1 : str, text2 : str) :
  openimg = Image.open("./images/drakeMeme.jpeg")
  img = ImageDraw.Draw(openimg)
  font = ImageFont.truetype("./fonts/ObelixProB-cyr.ttf", 20)
  _, _, w, h = img.textbbox((0,0), text1, font=font)
  W, H = openimg.size
  img.text((300, 100), text=text1, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width=2)
  img.text((300,350), text = text2, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width = 2)
  bytes = BytesIO()
  openimg.save(bytes, format="PNG")
  bytes.seek(0)
  return StreamingResponse(BytesIO(bytes.read()), media_type="image/png")

## WILL MEME API
@app.get("/api/willMeme&&text={text}")
async def read_root(text : str) :
  openimg = Image.open("./images/willMeme.jpeg")
  img = ImageDraw.Draw(openimg)
  font = ImageFont.truetype("./fonts/ObelixProB-cyr.ttf", 50)
  _,_, w, h = img.textbbox((0,0), text, font=font)
  W, H = openimg.size
  img.text((400, 300), text=text, fill=(255, 255, 255), font=font, stroke_fill = (0,0,0), stroke_width=2)
  byt = BytesIO()
  openimg.save(byt, format="PNG")
  byt.seek(0)
  return StreamingResponse(BytesIO(byt.read()), media_type="image/png")
  
@app.get("/api/binaryConvert&&number=")

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port = 8000)