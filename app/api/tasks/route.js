/**
 * Next.js App Router Route Handler (app/api/tasks/route.js)
 * Implements GET and POST endpoints using web standard Request/Response.
 */

let taskStore = [
  { id: 'TASK-001', topic: 'Autonomous AI Agents in 2026', priority: 'HIGH', status: 'COMPLETED' },
  { id: 'TASK-002', topic: 'Cryptocurrency and Web3 Ecosystem Metrics', priority: 'MEDIUM', status: 'IN_PROGRESS' },
  { id: 'TASK-003', topic: 'Open Source AI Tools & Frameworks', priority: 'HIGH', status: 'PENDING' },
];

export async function GET(request) {
  return Response.json({
    status: 'success',
    data: taskStore,
    count: taskStore.length,
    timestamp: new Date().toISOString(),
  }, { status: 200 });
}

export async function POST(request) {
  try {
    const body = await request.json();
    if (!body || !body.topic) {
      return Response.json({ status: 'error', message: 'Topic field is required' }, { status: 400 });
    }

    const newTask = {
      id: `TASK-${String(taskStore.length + 1).padStart(3, '0')}`,
      topic: body.topic,
      priority: body.priority || 'MEDIUM',
      status: 'PENDING',
      createdAt: new Date().toISOString(),
    };
    taskStore.push(newTask);

    return Response.json({ status: 'success', data: newTask }, { status: 201 });
  } catch (err) {
    return Response.json({ status: 'error', message: 'Invalid JSON body' }, { status: 400 });
  }
}
