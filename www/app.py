import logging; logging.basicConfig(level=logging.INFO)

import asyncio
import os
import json
import time

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Hello,Blog!</h1>')

