# Serves the Men's Precepts demo (one static page).
# Railway: root directory = repo root, Dockerfile path = work/product/precepts-demo/Dockerfile.
FROM caddy:2-alpine
COPY work/product/precepts-demo/index.html /srv/index.html
CMD ["sh", "-c", "caddy file-server --root /srv --listen :${PORT:-8080}"]
