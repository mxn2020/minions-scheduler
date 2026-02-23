/**
 * @module @minions-scheduler/sdk/schemas
 * Custom MinionType schemas for Minions Scheduler.
 */

import type { MinionType } from 'minions-sdk';

export const scheduleType: MinionType = {
  id: 'scheduler-schedule',
  name: 'Schedule',
  slug: 'schedule',
  description: 'A cron or interval-based trigger that activates an agent or workflow.',
  icon: '🕐',
  schema: [
    { name: 'name', type: 'string', label: 'name' },
    { name: 'description', type: 'string', label: 'description' },
    { name: 'cronExpression', type: 'string', label: 'cronExpression' },
    { name: 'timezone', type: 'string', label: 'timezone' },
    { name: 'targetAgentId', type: 'string', label: 'targetAgentId' },
    { name: 'targetSkill', type: 'string', label: 'targetSkill' },
    { name: 'status', type: 'select', label: 'status' },
    { name: 'lastRunAt', type: 'string', label: 'lastRunAt' },
    { name: 'nextRunAt', type: 'string', label: 'nextRunAt' },
    { name: 'createdAt', type: 'string', label: 'createdAt' },
  ],
};

export const schedulerunType: MinionType = {
  id: 'scheduler-schedule-run',
  name: 'Schedule run',
  slug: 'schedule-run',
  description: 'A single execution instance triggered by a schedule.',
  icon: '▶️',
  schema: [
    { name: 'scheduleId', type: 'string', label: 'scheduleId' },
    { name: 'triggeredAt', type: 'string', label: 'triggeredAt' },
    { name: 'completedAt', type: 'string', label: 'completedAt' },
    { name: 'status', type: 'select', label: 'status' },
    { name: 'output', type: 'string', label: 'output' },
    { name: 'errorMessage', type: 'string', label: 'errorMessage' },
  ],
};

export const triggerType: MinionType = {
  id: 'scheduler-trigger',
  name: 'Trigger',
  slug: 'trigger',
  description: 'An event-based trigger that fires when a condition is met.',
  icon: '⚡',
  schema: [
    { name: 'name', type: 'string', label: 'name' },
    { name: 'eventType', type: 'string', label: 'eventType' },
    { name: 'condition', type: 'string', label: 'condition' },
    { name: 'targetAgentId', type: 'string', label: 'targetAgentId' },
    { name: 'targetSkill', type: 'string', label: 'targetSkill' },
    { name: 'isActive', type: 'boolean', label: 'isActive' },
    { name: 'lastFiredAt', type: 'string', label: 'lastFiredAt' },
  ],
};

export const customTypes: MinionType[] = [
  scheduleType,
  schedulerunType,
  triggerType,
];

