/**
 * TypeScript Entrypoint & Pipeline Demo
 * HackIndia "Ship Safer JavaScript with TypeScript" Skill
 */
import { TaskItem, AgentAction } from './types.js';
import {
  isTaskItem,
  filterByPriority,
  handleAgentAction,
  executeSafeTask,
} from './agentService.js';

export async function runTypedAgentDemo(): Promise<{
  validCount: number;
  highPriorityCount: number;
  actionMessage: string;
}> {
  const sampleTasks: unknown[] = [
    {
      id: 'TS-TASK-001',
      topic: 'Static Type Checking in Hackathons',
      category: 'developer_tools',
      priority: 'HIGH',
      status: 'PENDING',
      createdAt: new Date().toISOString(),
    },
    {
      id: 'TS-TASK-002',
      topic: 'Unchecked JavaScript Runtime Error Avoidance',
      category: 'code_quality',
      priority: 'MEDIUM',
      status: 'PENDING',
      createdAt: new Date().toISOString(),
    },
    { invalid: 'payload' },
  ];

  // 1. Narrow unknown payload using custom type guard
  const validatedTasks: TaskItem[] = sampleTasks.filter(isTaskItem);

  // 2. Filter using generic collection helper
  const highPriority = filterByPriority(validatedTasks, 'HIGH');

  // 3. Handle action via discriminated union
  const action: AgentAction = {
    type: 'EXECUTE',
    payload: { taskId: validatedTasks[0]?.id || 'TS-TASK-001', dryRun: false },
  };
  const actionMessage = handleAgentAction(action);

  // 4. Asynchronously execute safe task with typed promise
  await executeSafeTask(validatedTasks[0], async (t) => {
    return `Processed task ${t.id} successfully`;
  });

  return {
    validCount: validatedTasks.length,
    highPriorityCount: highPriority.length,
    actionMessage,
  };
}

export default runTypedAgentDemo;
