import os

def get_extension(path):
    return os.path.splitext(path)[1]

def get_mime_type(extension):
    if extension == ".txt":
        return "text/plain"
    elif extension == ".html":
        return "text/html"
    elif extension == ".gif":
        return "image/gif"
    elif extension == ".jpg":
        return "image/jpeg"
    else:
        return "application/octet-stream"