# minions-scheduler

**Schedules, cron triggers, and timed execution definitions**

Built on the [Minions SDK](https://github.com/mxn2020/minions).

---

## Quick Start

```bash
# TypeScript / Node.js
npm install @minions-scheduler/sdk minions-sdk

# Python
pip install minions-scheduler

# CLI (global)
npm install -g @minions-scheduler/cli
```

---

## CLI

```bash
# Show help
scheduler --help
```

---

## Python SDK

```python
from minions_scheduler import create_client

client = create_client()
```

---

## Project Structure

```
minions-scheduler/
  packages/
    core/           # TypeScript core library (@minions-scheduler/sdk on npm)
    python/         # Python SDK (minions-scheduler on PyPI)
    cli/            # CLI tool (@minions-scheduler/cli on npm)
  apps/
    web/            # Playground web app
    docs/           # Astro Starlight documentation site
    blog/           # Blog
  examples/
    typescript/     # TypeScript usage examples
    python/         # Python usage examples
```

---

## Development

```bash
# Install dependencies
pnpm install

# Build all packages
pnpm run build

# Run tests
pnpm run test

# Type check
pnpm run lint
```

---

## Documentation

- Docs: [scheduler.minions.help](https://scheduler.minions.help)
- Blog: [scheduler.minions.blog](https://scheduler.minions.blog)
- App: [scheduler.minions.wtf](https://scheduler.minions.wtf)

---

## License

[MIT](LICENSE)
