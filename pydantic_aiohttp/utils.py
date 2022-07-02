from os import PathLike
from typing import Union

import aiofiles


async def read_file_by_chunk(file: Union[str, PathLike[str]]):
    async with aiofiles.open(file, 'rb') as f:
        chunk = await f.read(64 * 1024)

        while chunk:
            yield chunk
            chunk = await f.read(64 * 1024)
