# Serves the Men's Precepts demo (one static page).
# Railway: root directory = repo root, Dockerfile path = work/product/precepts-demo/Dockerfile.
# no-cache so phones always pick up the newest version.
FROM caddy:2-alpine
COPY work/product/precepts-demo/Caddyfile /etc/caddy/Caddyfile
COPY work/product/precepts-demo/index.html /srv/index.html
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
