import io
import asyncio
import json

from fastapi import FastAPI, Request, File, Query
from youtube_dl import YoutubeDL

import whisper

#openai.api_key = "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"
audio_downloader = YoutubeDL({'format':'bestaudio/best', 'outtmpl':'audio.mp3'})
app = FastAPI()


@app.post('/')
def add_audio(request: Request):
    data = request.form()
    fields = asyncio.run(data)
    model_type = fields['model_type']
    youtube = fields['youtube']
    audio_downloader.extract_info(youtube)
    model = whisper.load_model(model_type)
    result = model.transcribe("audio.mp3")
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this : " + result["text"],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    """

    return {"result": result}
    
