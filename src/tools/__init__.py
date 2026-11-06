"""
AgentVerse Safe Tool Calling System - Tools Package
"""

from .schemas import TOOL_SCHEMAS, TOOL_MAP, APPROVAL_REQUIRED_TOOLS, get_tool_schema, is_approval_required
from .implementations import (
    search_campus_events,
    get_event_details,
    calculate_reimbursement,
    draft_registration_message,
    send_registration_email,
    update_student_record,
    TOOL_RUNNERS
)

__all__ = [
    "TOOL_SCHEMAS",
    "TOOL_MAP",
    "APPROVAL_REQUIRED_TOOLS",
    "get_tool_schema",
    "is_approval_required",
    "search_campus_events",
    "get_event_details",
    "calculate_reimbursement",
    "draft_registration_message",
    "send_registration_email",
    "update_student_record",
    "TOOL_RUNNERS"
]
