
import httpx

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"

async def get_users_with_posts():
    async with httpx.AsyncClient() as client:
        users = (await client.get(USERS_URL)).json()
        posts = (await client.get(POSTS_URL)).json()

    user_map = {u["id"]: u for u in users}
    for u in user_map.values():
        u["posts"] = []

    for p in posts:
        user_map[p["userId"]]["posts"].append(p)

    return {"users": list(user_map.values())}
