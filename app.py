
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
        "name": "Song A",
        "genre": "Hip-Hop"
    },{
        "name": "Song B",
        "genre": "Pop"
    },{
        "name": "Song C",
        "genre": "Toto"
    }]

    # render template
    return templates.TemplateResponse("item.html", {"request": request, "songs": songs})


@app.get("/spotify_response")
def spotify_callback(token):
    return {"resp": token}
