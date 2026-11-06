"""
Concrete tool implementations for AgentVerse Safe Tool-Calling Agent.
Provides mock/live business logic for both read-only and gated write operations.
"""

import time
import uuid
from typing import Dict, Any, List


def search_campus_events(city: str, date: str, topic: str, max_results: int = 5) -> Dict[str, Any]:
    """Search public campus events by city, date, and topic."""
    # Deterministic mock database
    events_db = [
        {
            "id": "EVT-AI-101",
            "title": "AgentVerse AI Project Clinic",
            "city": "Bengaluru",
            "date": "2026-09-21",
            "topic": "AI",
            "venue": "Campus Main Auditorium",
            "fee": 0.0
        },
        {
            "id": "EVT-WEB-202",
            "title": "Full-Stack Web Dev Sprint",
            "city": "Bengaluru",
            "date": "2026-09-21",
            "topic": "web3",
            "venue": "Innovation Lab Hall B",
            "fee": 150.0
        },
        {
            "id": "EVT-AI-103",
            "title": "Autonomous Agents Hackathon Briefing",
            "city": "Delhi",
            "date": "2026-09-22",
            "topic": "AI",
            "venue": "Seminar Complex 2",
            "fee": 0.0
        },
        {
            "id": "EVT-DES-304",
            "title": "Usable UI/UX Systems Workshop",
            "city": "Pune",
            "date": "2026-09-25",
            "topic": "design",
            "venue": "Design Studio 1",
            "fee": 100.0
        }
    ]

    city_clean = city.strip().lower()
    topic_clean = topic.strip().lower()

    matches = []
    for ev in events_db:
        if city_clean in ev["city"].lower() or ev["city"].lower() in city_clean:
            if topic_clean in ev["topic"].lower() or ev["topic"].lower() in topic_clean:
                matches.append(ev)

    # Fallback to date/city match if specific topic didn't match exactly
    if not matches:
        matches = [ev for ev in events_db if city_clean in ev["city"].lower()]

    results = matches[:max_results]
    return {
        "events": results,
        "count": len(results),
        "error": ""
    }


def get_event_details(event_id: str) -> Dict[str, Any]:
    """Retrieve in-depth details, fees, and deadlines for a given event ID."""
    details_catalog = {
        "EVT-AI-101": {
            "event_id": "EVT-AI-101",
            "title": "AgentVerse AI Project Clinic",
            "organizer": "Department of Computer Science & Engineering",
            "fee": 0.0,
            "deadline": "2026-09-20T23:59:00Z",
            "rules": "Bring your student ID card and a configured Python/Node.js development environment. Teams up to 3 members."
        },
        "EVT-WEB-202": {
            "event_id": "EVT-WEB-202",
            "title": "Full-Stack Web Dev Sprint",
            "organizer": "Student Developer Club",
            "fee": 150.0,
            "deadline": "2026-09-20T18:00:00Z",
            "rules": "Requires active GitHub profile. Submissions judged on code architecture and test coverage."
        }
    }

    if event_id in details_catalog:
        return details_catalog[event_id]

    return {
        "event_id": event_id,
        "title": f"Campus Workshop ({event_id})",
        "organizer": "Campus Activities Board",
        "fee": 50.0,
        "deadline": "2026-09-21T12:00:00Z",
        "rules": "Open to all enrolled students with active ID."
    }


def calculate_reimbursement(amounts: List[float], category: str) -> Dict[str, Any]:
    """Sum expenditure receipts, apply caps, and return breakdown."""
    gross_total = sum(float(a) for a in amounts)
    caps = {
        "travel": 3000.0,
        "registration": 2000.0,
        "accommodation": 4000.0
    }
    cap = caps.get(category.lower(), 5000.0)
    approved = min(gross_total, cap)

    return {
        "gross_total": gross_total,
        "approved_total": approved,
        "cap_limit": cap,
        "cap_applied": gross_total > cap,
        "category": category
    }


def draft_registration_message(student_name: str, event_id: str, roll_number: str) -> Dict[str, Any]:
    """Draft formal event registration cover note for human review."""
    draft_body = (
        f"Dear Organizing Committee,\n\n"
        f"I am writing to formally request registration for '{event_id}'.\n"
        f"Student Name: {student_name}\n"
        f"Roll Number: {roll_number}\n\n"
        f"I confirm that I meet all stated eligibility criteria and will adhere to the event code of conduct.\n\n"
        f"Sincerely,\n{student_name}"
    )
    return {
        "draft": draft_body,
        "recipient_role": "Department Event Coordinator",
        "ready_for_review": True
    }


def send_registration_email(recipient: str, subject: str, body: str) -> Dict[str, Any]:
    """GATED HIGH-RISK: Send email dispatch."""
    msg_id = f"MSG-{uuid.uuid4().hex[:8].upper()}"
    return {
        "status": "SENT",
        "message_id": msg_id,
        "recipient": recipient,
        "subject": subject,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }


def update_student_record(student_id: str, field: str, value: str) -> Dict[str, Any]:
    """GATED HIGH-RISK: Mutate persistent database record."""
    return {
        "success": True,
        "student_id": student_id,
        "updated_field": field,
        "new_value": value,
        "row_version": 2
    }


# Tool Dispatcher Dictionary
TOOL_RUNNERS = {
    "search_campus_events": search_campus_events,
    "get_event_details": get_event_details,
    "calculate_reimbursement": calculate_reimbursement,
    "draft_registration_message": draft_registration_message,
    "send_registration_email": send_registration_email,
    "update_student_record": update_student_record
}
