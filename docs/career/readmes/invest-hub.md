<!-- PRIVATE REPO: sanitized from https://github.com/devzurc/invest-hub on 2026-07-31 -->

# Trade Intelligence OS (`invest-hub`)

Self-hosted research, streaming lakehouse, scanner, risk, and paper-trading platform.

**Intelligence first, execution second. Open-source first.**

## Start here

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/project/MAP.md`](docs/project/MAP.md)
3. [`docs/project/STATUS.md`](docs/project/STATUS.md) · [`.ai/state/`](.ai/state/)
4. **Continue in a new chat:** [`docs/project/NEXT_SESSION.md`](docs/project/NEXT_SESSION.md)

## Commands

```bash
make doctor
make verify
make audit
uv sync --all-packages
docker compose -f infrastructure/docker/compose.yml up -d
curl -s [REDACTED_URL]
```

Ports and publisher: [`docs/operations/`](docs/operations/).