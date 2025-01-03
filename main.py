import json
from typing import Literal

import aiohttp
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import config

app = FastAPI()


@app.get("/{id}.{ext}")
async def get_user_avatar(
    id: int, ext: Literal["jpg", "jpeg", "png", "webp", "gif"], size: int = 4096
):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Authorization": f"Bot {config.token}",
            "Content-Type": "application/json",
        }
        async with session.get(
            f"https://discord.com/api/v10/users/{id}", headers=headers
        ) as resp:
            resp_json = json.loads(await resp.text())

    if resp_json["avatar"] is None:
        # Fallback to default avatar if user's avatar is not set
        if resp_json["discriminator"] in ["0", "0000"]:
            default_avatar_index = (int(resp_json["id"]) >> 22) % 6
        else:
            default_avatar_index = int(resp_json["discriminator"]) % 5

        return RedirectResponse(
            f"https://cdn.discordapp.com/embed/avatars/{default_avatar_index}.png", 301
        )
    else:
        avatar_url = f"https://cdn.discordapp.com/avatars/{id}/{resp_json['avatar']}.{ext}?size={size}"
        return RedirectResponse(avatar_url, 301)


@app.get("/{id}")
async def route_to_png(id: int, size: int = 4096):
    return await get_user_avatar(id, "png", size)


uvicorn.run(app, host=config.host, port=config.port)
