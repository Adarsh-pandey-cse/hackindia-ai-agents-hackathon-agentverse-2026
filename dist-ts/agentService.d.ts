/**
 * Typed Agent Service & Safety Utilities
 * Demonstrates:
 * - Generics
 * - User-defined type guards (isTaskItem, isValidPriority)
 * - Exhaustiveness checking with never
 * - Immutable collection mapping
 */
import { TaskItem, PriorityLevel, ServiceResult, AgentAction } from './types.js';
/**
 * Custom Type Guard for PriorityLevel
 */
export declare function isValidPriority(value: unknown): value is PriorityLevel;
/**
 * Custom Type Guard to validate arbitrary JSON as a TaskItem
 */
export declare function isTaskItem(item: unknown): item is TaskItem;
/**
 * Exhaustive check utility for discriminated unions
 */
export declare function assertNever(x: never): never;
/**
 * Generic Filter with strict type preservation
 */
export declare function filterByPriority<T extends TaskItem>(tasks: readonly T[], priority: PriorityLevel): T[];
/**
 * Action handler demonstrating discriminated union narrowing
 */
export declare function handleAgentAction(action: AgentAction): string;
/**
 * Generic asynchronous task executor with typed telemetry
 */
export declare function executeSafeTask<T>(task: TaskItem, handler: (t: TaskItem) => Promise<T>): Promise<ServiceResult<T>>;
//# sourceMappingURL=agentService.d.ts.map