"""
Minions Scheduler SDK — Type Schemas
Custom MinionType schemas for Minions Scheduler.
"""

from minions.types import FieldDefinition, FieldValidation, MinionType

schedule_type = MinionType(
    id="scheduler-schedule",
    name="Schedule",
    slug="schedule",
    description="A cron or interval-based trigger that activates an agent or workflow.",
    icon="🕐",
    schema=[
        FieldDefinition(name="name", type="string", label="name"),
        FieldDefinition(name="description", type="string", label="description"),
        FieldDefinition(name="cronExpression", type="string", label="cronExpression"),
        FieldDefinition(name="timezone", type="string", label="timezone"),
        FieldDefinition(name="targetAgentId", type="string", label="targetAgentId"),
        FieldDefinition(name="targetSkill", type="string", label="targetSkill"),
        FieldDefinition(name="status", type="select", label="status"),
        FieldDefinition(name="lastRunAt", type="string", label="lastRunAt"),
        FieldDefinition(name="nextRunAt", type="string", label="nextRunAt"),
        FieldDefinition(name="createdAt", type="string", label="createdAt"),
    ],
)

schedule_run_type = MinionType(
    id="scheduler-schedule-run",
    name="Schedule run",
    slug="schedule-run",
    description="A single execution instance triggered by a schedule.",
    icon="▶️",
    schema=[
        FieldDefinition(name="scheduleId", type="string", label="scheduleId"),
        FieldDefinition(name="triggeredAt", type="string", label="triggeredAt"),
        FieldDefinition(name="completedAt", type="string", label="completedAt"),
        FieldDefinition(name="status", type="select", label="status"),
        FieldDefinition(name="output", type="string", label="output"),
        FieldDefinition(name="errorMessage", type="string", label="errorMessage"),
    ],
)

trigger_type = MinionType(
    id="scheduler-trigger",
    name="Trigger",
    slug="trigger",
    description="An event-based trigger that fires when a condition is met.",
    icon="⚡",
    schema=[
        FieldDefinition(name="name", type="string", label="name"),
        FieldDefinition(name="eventType", type="string", label="eventType"),
        FieldDefinition(name="condition", type="string", label="condition"),
        FieldDefinition(name="targetAgentId", type="string", label="targetAgentId"),
        FieldDefinition(name="targetSkill", type="string", label="targetSkill"),
        FieldDefinition(name="isActive", type="boolean", label="isActive"),
        FieldDefinition(name="lastFiredAt", type="string", label="lastFiredAt"),
    ],
)

custom_types: list[MinionType] = [
    schedule_type,
    schedule_run_type,
    trigger_type,
]

