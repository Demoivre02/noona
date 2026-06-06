#!/usr/bin/env python3
"""Local dev server with correct MIME types for WASM/GLB."""

import http.server
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".wasm": "application/wasm",
        ".glb": "model/gltf-binary",
        ".webp": "image/webp",
        ".mp3": "audio/mpeg",
        ".m4a": "audio/mp4",
    }

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = int(os.environ.get("PORT", "8080"))
    with http.server.ThreadingHTTPServer(("", port), Handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()
