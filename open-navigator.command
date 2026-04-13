#!/bin/bash
# Double-click in Finder: starts a tiny local server and opens the roadmap in your browser.
# Use this instead of file:// links (those often fail when clicked from chat or some apps).
cd "$(dirname "$0")" || exit 1
PORT=8765
URL="http://127.0.0.1:${PORT}/navigator.html"

if ! lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  python3 -m http.server "$PORT" >/dev/null 2>&1 &
  sleep 0.5
fi

open "$URL"
