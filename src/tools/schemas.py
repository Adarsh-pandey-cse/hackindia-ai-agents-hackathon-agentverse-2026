"""
Tool Schemas for AgentVerse Safe Tool-Calling Agent.
Defines JSON schemas, risk classifications (low/high), input parameters,
output contracts, and validation rules according to HackIndia standards.
"""

from typing import Dict, Any, List

TOOL_SCHEMAS: List[Dict[str, Any]] = [
    {
        "name": "search_campus_events",
        "description": "Search public campus events by city, date, and topic. Use this when the user asks for events to attend, not when they want to register.",
        "risk": "low",
        "requires_approval": False,
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Indian city name, for example Bengaluru, Pune, Delhi, or Jaipur."
                },
                "date": {
                    "type": "string",
                    "description": "Date in YYYY-MM-DD format."
                },
                "topic": {
                    "type": "string",
                    "description": "Event topic, for example AI, web3, design, finance, or open source."
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of events to return. Use 1 to 10."
                }
            },
            "required": ["city", "date", "topic", "max_results"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "events": {
                    "type": "array",
                    "description": "List of matching public events with id, title, date, venue, and fee."
                },
                "error": {
                    "type": "string",
                    "description": "Empty string when successful, otherwise an error message."
                }
            }
        },
        "example_call": {
            "name": "search_campus_events",
            "arguments": {
                "city": "Bengaluru",
                "date": "2026-09-21",
                "topic": "AI",
                "max_results": 5
            }
        }
    },
    {
        "name": "get_event_details",
        "description": "Get rules, venue, registration fee, and deadline for a specific event by event_id.",
        "risk": "low",
        "requires_approval": False,
        "input_schema": {
            "type": "object",
            "properties": {
                "event_id": {
                    "type": "string",
                    "description": "Unique identifier of the campus event, e.g. EVT-AI-101."
                }
            },
            "required": ["event_id"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "event_id": {"type": "string"},
                "title": {"type": "string"},
                "organizer": {"type": "string"},
                "fee": {"type": "number"},
                "deadline": {"type": "string"},
                "rules": {"type": "string"}
            }
        },
        "example_call": {
            "name": "get_event_details",
            "arguments": {
                "event_id": "EVT-AI-101"
            }
        }
    },
    {
        "name": "calculate_reimbursement",
        "description": "Calculate total admissible expense amount from line item bills and determine student copay.",
        "risk": "low",
        "requires_approval": False,
        "input_schema": {
            "type": "object",
            "properties": {
                "amounts": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "List of expenditure receipts in INR."
                },
                "category": {
                    "type": "string",
                    "description": "Expense category (e.g. 'travel', 'registration', 'accommodation')."
                }
            },
            "required": ["amounts", "category"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "total": {"type": "number"},
                "approved_total": {"type": "number"},
                "cap_applied": {"type": "boolean"},
                "category": {"type": "string"}
            }
        },
        "example_call": {
            "name": "calculate_reimbursement",
            "arguments": {
                "amounts": [450.0, 1200.0, 350.0],
                "category": "travel"
            }
        }
    },
    {
        "name": "draft_registration_message",
        "description": "Draft a formal event registration message or reimbursement cover note for user review before sending.",
        "risk": "low",
        "requires_approval": False,
        "input_schema": {
            "type": "object",
            "properties": {
                "student_name": {
                    "type": "string",
                    "description": "Full name of the participating student."
                },
                "event_id": {
                    "type": "string",
                    "description": "Event identifier to register for."
                },
                "roll_number": {
                    "type": "string",
                    "description": "Student institutional roll / ID number."
                }
            },
            "required": ["student_name", "event_id", "roll_number"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "draft": {"type": "string"},
                "recipient_role": {"type": "string"}
            }
        },
        "example_call": {
            "name": "draft_registration_message",
            "arguments": {
                "student_name": "Adarsh Pandey",
                "event_id": "EVT-AI-101",
                "roll_number": "CS2026-881"
            }
        }
    },
    {
        "name": "send_registration_email",
        "description": "Transmit formal registration email or reimbursement claim to department faculty. HIGH RISK: Triggers external email dispatch.",
        "risk": "high",
        "requires_approval": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "recipient": {
                    "type": "string",
                    "description": "Destination email address (e.g. hod_cs@campus.edu.in)."
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject header."
                },
                "body": {
                    "type": "string",
                    "description": "Complete text body of the dispatch."
                }
            },
            "required": ["recipient", "subject", "body"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "message_id": {"type": "string"},
                "timestamp": {"type": "string"}
            }
        },
        "example_call": {
            "name": "send_registration_email",
            "arguments": {
                "recipient": "faculty_advisor@campus.edu.in",
                "subject": "Registration Request: EVT-AI-101",
                "body": "Dear Professor, I would like to attend..."
            }
        }
    },
    {
        "name": "update_student_record",
        "description": "Commit or mutate records in institutional student database. HIGH RISK: Modifies persistent production database state.",
        "risk": "high",
        "requires_approval": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Unique student identifier."
                },
                "field": {
                    "type": "string",
                    "description": "Database column to update (e.g. 'registered_events', 'reimbursement_status')."
                },
                "value": {
                    "type": "string",
                    "description": "New value to write to the persistent database record."
                }
            },
            "required": ["student_id", "field", "value"]
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "success": {"type": "boolean"},
                "student_id": {"type": "string"},
                "updated_field": {"type": "string"},
                "row_version": {"type": "integer"}
            }
        },
        "example_call": {
            "name": "update_student_record",
            "arguments": {
                "student_id": "STU-2026-90",
                "field": "registered_events",
                "value": "EVT-AI-101"
            }
        }
    }
]

TOOL_MAP: Dict[str, Dict[str, Any]] = {tool["name"]: tool for tool in TOOL_SCHEMAS}
APPROVAL_REQUIRED_TOOLS = {tool["name"] for tool in TOOL_SCHEMAS if tool.get("requires_approval", False)}


def get_tool_schema(name: str) -> Dict[str, Any]:
    """Retrieve full tool schema by tool name."""
    if name not in TOOL_MAP:
        raise ValueError(f"Unknown tool: '{name}'. Available: {list(TOOL_MAP.keys())}")
    return TOOL_MAP[name]


def is_approval_required(name: str) -> bool:
    """Return True if tool requires human approval gate before execution."""
    return name in APPROVAL_REQUIRED_TOOLS
