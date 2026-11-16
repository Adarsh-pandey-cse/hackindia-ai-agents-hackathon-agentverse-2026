/**
 * Typed Agent Service & Safety Utilities
 * Demonstrates:
 * - Generics
 * - User-defined type guards (isTaskItem, isValidPriority)
 * - Exhaustiveness checking with never
 * - Immutable collection mapping
 */
import {
  TaskItem,
  PriorityLevel,
  ServiceResult,
  AgentAction,
  ExecutionTelemetry,
} from './types.js';

/**
 * Custom Type Guard for PriorityLevel
 */
export function isValidPriority(value: unknown): value is PriorityLevel {
  return typeof value === 'string' && ['HIGH', 'MEDIUM', 'LOW'].includes(value);
}

/**
 * Custom Type Guard to validate arbitrary JSON as a TaskItem
 */
export function isTaskItem(item: unknown): item is TaskItem {
  if (typeof item !== 'object' || item === null) return false;
  const t = item as Record<string, unknown>;
  return (
    typeof t.id === 'string' &&
    typeof t.topic === 'string' &&
    typeof t.category === 'string' &&
    isValidPriority(t.priority) &&
    typeof t.createdAt === 'string'
  );
}

/**
 * Exhaustive check utility for discriminated unions
 */
export function assertNever(x: never): never {
  throw new Error(`Unexpected object in exhaustive check: ${JSON.stringify(x)}`);
}

/**
 * Generic Filter with strict type preservation
 */
export function filterByPriority<T extends TaskItem>(
  tasks: readonly T[],
  priority: PriorityLevel
): T[] {
  return tasks.filter((t) => t.priority === priority);
}

/**
 * Action handler demonstrating discriminated union narrowing
 */
export function handleAgentAction(action: AgentAction): string {
  switch (action.type) {
    case 'ANALYZE':
      return `Analyzing query: ${action.payload.query} (limit: ${action.payload.limit})`;
    case 'EXECUTE':
      return `Executing task ${action.payload.taskId} (dryRun: ${action.payload.dryRun})`;
    case 'CANCEL':
      return `Cancelled task ${action.payload.taskId}: ${action.payload.reason}`;
    default:
      return assertNever(action);
  }
}

/**
 * Generic asynchronous task executor with typed telemetry
 */
export async function executeSafeTask<T>(
  task: TaskItem,
  handler: (t: TaskItem) => Promise<T>
): Promise<ServiceResult<T>> {
  const startTime = Date.now();
  try {
    const data = await handler(task);
    const telemetry: ExecutionTelemetry = {
      taskId: task.id,
      durationMs: Date.now() - startTime,
      confidence: 0.98,
      status: 'COMPLETED',
      timestamp: new Date().toISOString(),
    };

    return {
      success: true,
      data,
      timestamp: telemetry.timestamp,
    };
  } catch (err) {
    const errorMsg = err instanceof Error ? err.message : 'Unknown execution failure';
    return {
      success: false,
      error: errorMsg,
      timestamp: new Date().toISOString(),
    };
  }
}
