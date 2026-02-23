---
title: Quick Start
description: Get up and running with Minions Scheduler in minutes
---

## TypeScript

```typescript
import { createClient } from '@minions-scheduler/sdk';

const client = createClient();
console.log('Version:', client.version);
```

## Python

```python
from minions_scheduler import create_client

client = create_client()
print(f"Version: {client['version']}")
```

## CLI

```bash
scheduler info
```
