/**
 * TypeScript Domain Models & Type Definitions
 * HackIndia "Ship Safer JavaScript with TypeScript" Skill
 */

export type PriorityLevel = 'HIGH' | 'MEDIUM' | 'LOW';

export type TaskStatus = 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'FAILED';

export interface TaskItem {
  readonly id: string;
  readonly topic: string;
  readonly category: string;
  readonly priority: PriorityLevel;
  status: TaskStatus;
  retryCount?: number;
  metadata?: Record<string, unknown>;
  readonly createdAt: string;
}

export interface UserSession {
  readonly userId: string;
  readonly email: string;
  readonly role: 'developer' | 'admin' | 'guest';
  readonly token: string;
  readonly expiresAt: number;
}

export interface ExecutionTelemetry {
  readonly taskId: string;
  readonly durationMs: number;
  readonly confidence: number;
  readonly status: TaskStatus;
  readonly timestamp: string;
}

/**
 * Generic API / Service Result Envelope
 */
export interface ServiceResult<T> {
  readonly success: boolean;
  readonly data?: T;
  readonly error?: string;
  readonly timestamp: string;
}

/**
 * Discriminated Union for Agent Action Dispatching
 */
export type AgentAction =
  | { type: 'ANALYZE'; payload: { query: string; limit: number } }
  | { type: 'EXECUTE'; payload: { taskId: string; dryRun: boolean } }
  | { type: 'CANCEL'; payload: { taskId: string; reason: string } };
