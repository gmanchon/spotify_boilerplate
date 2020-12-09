
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def web_root(request: Request):

    # get songs from spotify
    songs = [{
      "genre": "Hard rock",
      "title": "Thunderstruck",
      "length": "4:52"
    }, {
      "genre": "Hard rock",
      "title": "Fire Your Guns",
      "length": "2:53"
    }, {
      "genre": "Hard rock",
      "title": "Moneytalks",
      "length": "3:48"
    }, {
      "genre": "Hard rock",
      "title": "The Razors Edge",
      "length": "4:22"
    }, {
      "genre": "Hard rock",
      "title": "Mistress for Christmas",
      "length": "3:59"
    }, {
      "genre": "Hard rock",
      "title": "Rock Your Heart Out",
      "length": "4:06"
    }, {
      "genre": "Hard rock",
      "title": "Are You Ready",
      "length": "4:10"
    }, {
      "genre": "Hard rock",
      "title": "Got You by the Balls",
      "length": "4:30"
    }, {
      "genre": "Hard rock",
      "title": "Shot of Love",
      "length": "3:56"
    }, {
      "genre": "Hard rock",
      "title": "Let's Make It",
      "length": "3:32"
    }, {
      "genre": "Hard rock",
      "title": "Goodbye and Good Riddance to Bad Luck",
      "length": "3:13"
    }, {
      "genre": "Hard rock",
      "title": "If You Dare",
      "length": "3:08"
    }]

    # render template
    return templates.TemplateResponse("item.html", {"request": request, "songs": songs})


@app.get("/spotify_response")
def spotify_callback(token):
    return {"resp": token}
