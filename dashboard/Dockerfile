# Builds Interconnected HQ from the repo on every deploy, then serves it.
# Railway: root directory = repo root, Dockerfile path = dashboard/Dockerfile.
FROM python:3.12-alpine AS build
RUN apk add --no-cache tzdata
ARG RAILWAY_GIT_COMMIT_SHA=""
ENV RAILWAY_GIT_COMMIT_SHA=${RAILWAY_GIT_COMMIT_SHA}
WORKDIR /src
COPY tools ./tools
COPY company/direction.md ./company/direction.md
COPY pipeline/tracker.md ./pipeline/tracker.md
COPY work/bd/outbox ./work/bd/outbox
COPY logs ./logs
RUN mkdir -p dashboard && python3 tools/dashboard.py

FROM caddy:2-alpine
COPY --from=build /src/dashboard/index.html /srv/index.html
CMD ["sh", "-c", "caddy file-server --root /srv --listen :${PORT:-8080}"]
