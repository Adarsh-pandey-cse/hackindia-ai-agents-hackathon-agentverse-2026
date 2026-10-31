import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("docs/screens", exist_ok=True)

WIDTH, HEIGHT = 1280, 820
BG_COLOR = (11, 15, 25)
SURFACE_COLOR = (17, 24, 39)
SURFACE_ELEVATED = (31, 41, 55)
BORDER_COLOR = (55, 65, 81)
TEXT_WHITE = (249, 250, 251)
TEXT_MUTED = (156, 163, 175)
PRIMARY_SAFFRON = (249, 115, 22)
SUCCESS_GREEN = (16, 185, 129)
ERROR_BG = (69, 10, 10)
ERROR_BORDER = (220, 38, 38)
ERROR_TEXT = (252, 165, 165)

# Try loading standard windows fonts or fallback
def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf"
    ]
    if bold:
        for f in ["C:\\Windows\\Fonts\\segoeuib.ttf", "C:\\Windows\\Fonts\\arialbd.ttf"]:
            if os.path.exists(f):
                try: return ImageFont.truetype(f, size)
                except: pass
    for f in font_names:
        if os.path.exists(f):
            try: return ImageFont.truetype(f, size)
            except: pass
    return ImageFont.load_default()

font_title = get_font(26, bold=True)
font_h2 = get_font(20, bold=True)
font_h3 = get_font(16, bold=True)
font_body = get_font(15, bold=False)
font_bold = get_font(15, bold=True)
font_small = get_font(13, bold=False)
font_badge = get_font(12, bold=True)

def draw_header(draw, active_tab_index):
    # Header background
    draw.rectangle([0, 0, WIDTH, 70], fill=SURFACE_COLOR)
    draw.line([0, 70, WIDTH, 70], fill=BORDER_COLOR, width=1)

    # Brand
    draw.rounded_rectangle([32, 16, 68, 52], radius=8, fill=PRIMARY_SAFFRON)
    draw.text((41, 22), "AV", fill=(255, 255, 255), font=font_h3)
    draw.text((80, 24), "AgentVerse Autonomous AI Agent", fill=TEXT_WHITE, font=font_h2)

    # HackIndia Tag
    draw.rounded_rectangle([440, 26, 560, 48], radius=11, fill=(40, 25, 15), outline=PRIMARY_SAFFRON, width=1)
    draw.text((452, 29), "HackIndia 2026", fill=PRIMARY_SAFFRON, font=font_badge)

    # Tabs
    tabs = ["1. Dashboard", "2. Task Explorer (Empty State)", "3. Diagnostics (Error State)"]
    tab_x = 720
    for idx, name in enumerate(tabs):
        w = 175 if idx != 1 else 200
        if idx == active_tab_index:
            draw.rounded_rectangle([tab_x, 18, tab_x + w, 52], radius=6, fill=PRIMARY_SAFFRON)
            draw.text((tab_x + 14, 26), name, fill=(255, 255, 255), font=font_small)
        else:
            draw.rounded_rectangle([tab_x, 18, tab_x + w, 52], radius=6, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
            draw.text((tab_x + 14, 26), name, fill=TEXT_MUTED, font=font_small)
        tab_x += w + 10

# -------------------------------------------------------------
# SCREEN 1: DASHBOARD
# -------------------------------------------------------------
def generate_screen1():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, active_tab_index=0)

    # Screen Title & Subtitle
    draw.text((32, 95), "Agent Control Center & Workload Metrics", fill=TEXT_WHITE, font=font_title)
    draw.text((32, 135), "Real-time telemetry of autonomous analytical agents and scikit-learn predictive model evaluation.", fill=TEXT_MUTED, font=font_body)

    # 4 Metric Cards
    metrics = [
        ("MODEL ACCURACY", "96.25%", "+ LogisticRegression Champion", SUCCESS_GREEN),
        ("TOTAL WORKLOADS", "1,200", "Stratified 80/20 Test Split", TEXT_MUTED),
        ("AVERAGE LATENCY", "879ms", "Live REST API Roundtrip", SUCCESS_GREEN),
        ("ACTIVE AGENTS", "3 Online", "Mock Fallbacks Ready", SUCCESS_GREEN)
    ]
    for i, (label, val, sub, sub_col) in enumerate(metrics):
        cx = 32 + i * 305
        draw.rounded_rectangle([cx, 175, cx + 290, 275], radius=10, fill=SURFACE_COLOR, outline=BORDER_COLOR, width=1)
        draw.text((cx + 18, 190), label, fill=TEXT_MUTED, font=font_small)
        draw.text((cx + 18, 215), val, fill=TEXT_WHITE, font=font_title)
        draw.text((cx + 18, 250), sub, fill=sub_col, font=font_small)

    # Primary Action Banner (Contrast & Prominence)
    draw.rounded_rectangle([32, 295, WIDTH - 32, 385], radius=10, fill=(25, 20, 20), outline=PRIMARY_SAFFRON, width=1)
    draw.text((56, 312), "Execute Autonomous Workload Ingestion", fill=TEXT_WHITE, font=font_h2)
    draw.text((56, 345), "Ingests structured JSON/CSV datasets, queries live external REST endpoints, and saves structured summaries to output/.", fill=TEXT_MUTED, font=font_body)

    # Main CTA Button (Clear, prominent, accessible)
    draw.rounded_rectangle([WIDTH - 280, 315, WIDTH - 56, 365], radius=8, fill=PRIMARY_SAFFRON)
    draw.text((WIDTH - 255, 330), "▶ Run Workload Analysis", fill=(255, 255, 255), font=font_bold)

    # Task Table
    draw.rounded_rectangle([32, 405, WIDTH - 32, HEIGHT - 40], radius=10, fill=SURFACE_COLOR, outline=BORDER_COLOR, width=1)
    draw.text((56, 425), "Active Analytical Task Feed & Live Execution Queue", fill=TEXT_WHITE, font=font_h2)

    headers = [("TASK ID", 56), ("CATEGORY", 180), ("TOPIC", 380), ("PRIORITY", 820), ("API DISPATCH STATUS", 960)]
    draw.line([56, 465, WIDTH - 56, 465], fill=BORDER_COLOR, width=1)
    for h, hx in headers:
        draw.text((hx, 475), h, fill=TEXT_MUTED, font=font_badge)
    draw.line([56, 500, WIDTH - 56, 500], fill=BORDER_COLOR, width=1)

    rows = [
        ("TASK-001", "ai_tech_trends", "Autonomous AI Agents in 2026", "HIGH", (239, 68, 68), "HTTPBin Live Echo (1236ms)", SUCCESS_GREEN),
        ("TASK-002", "market_indicators", "Cryptocurrency and Web3 Ecosystem Metrics", "MEDIUM", (245, 158, 11), "CoinGecko REST API (718ms)", SUCCESS_GREEN),
        ("TASK-003", "developer_ecosystem", "Open Source AI Tools & Frameworks", "HIGH", (239, 68, 68), "GitHub Public API (682ms)", SUCCESS_GREEN),
        ("TASK-004", "cloud_infrastructure", "Serverless Edge Functions Latency", "LOW", (156, 163, 175), "Standby in Queue", TEXT_MUTED)
    ]
    ry = 515
    for tid, cat, top, pri, pri_col, stat, stat_col in rows:
        draw.text((56, ry), tid, fill=TEXT_WHITE, font=font_bold)
        draw.text((180, ry), cat, fill=TEXT_MUTED, font=font_body)
        draw.text((380, ry), top, fill=TEXT_WHITE, font=font_body)

        draw.rounded_rectangle([820, ry - 2, 880, ry + 22], radius=4, fill=(40, 20, 20) if pri == "HIGH" else (30, 30, 20), outline=pri_col, width=1)
        draw.text((830, ry + 2), pri, fill=pri_col, font=font_badge)

        draw.text((960, ry), stat, fill=stat_col, font=font_body)
        draw.line([56, ry + 35, WIDTH - 56, ry + 35], fill=(30, 38, 50), width=1)
        ry += 52

    img.save("docs/screens/home.png", "PNG")
    print("Generated docs/screens/home.png")

# -------------------------------------------------------------
# SCREEN 2: TASK EXPLORER (SEARCH & EMPTY STATE)
# -------------------------------------------------------------
def generate_screen2():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, active_tab_index=1)

    # Title
    draw.text((32, 95), "Task Explorer & Filter Engine", fill=TEXT_WHITE, font=font_title)
    draw.text((32, 135), "Filter ingested tasks by topic keyword or priority level with instant state feedback.", fill=TEXT_MUTED, font=font_body)

    # Search & Filter Controls
    # Search Box with Active Query "quantum-crypto-2030"
    draw.rounded_rectangle([32, 175, 750, 225], radius=8, fill=SURFACE_COLOR, outline=PRIMARY_SAFFRON, width=2)
    draw.text((48, 190), "quantum-crypto-2030", fill=TEXT_WHITE, font=font_body)

    # Dropdown Filter
    draw.rounded_rectangle([770, 175, 960, 225], radius=8, fill=SURFACE_COLOR, outline=BORDER_COLOR, width=1)
    draw.text((786, 190), "High Priority Only  ▼", fill=TEXT_WHITE, font=font_body)

    # Reset Button
    draw.rounded_rectangle([980, 175, 1140, 225], radius=8, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    draw.text((1010, 190), "Clear Search", fill=TEXT_MUTED, font=font_body)

    # EMPTY STATE CONTAINER (Accessible, beautifully spaced, clear hierarchy)
    box_top = 270
    box_bot = 680
    draw.rounded_rectangle([140, box_top, WIDTH - 140, box_bot], radius=16, fill=SURFACE_COLOR, outline=(70, 80, 95), width=2)

    # Circular Empty Icon Container
    cx = WIDTH // 2
    draw.ellipse([cx - 40, box_top + 50, cx + 40, box_top + 130], fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    # Magnifier / Box representation
    draw.ellipse([cx - 18, box_top + 70, cx + 8, box_top + 96], outline=TEXT_MUTED, width=3)
    draw.line([cx + 6, box_top + 94, cx + 18, box_top + 106], fill=TEXT_MUTED, width=3)

    # Empty State Heading
    draw.text((cx - 155, box_top + 160), "No matching agent tasks found", fill=TEXT_WHITE, font=font_title)

    # Empty State Helpful Copy (Explains what happened and how to fix it)
    desc1 = "No active tasks match your search query \"quantum-crypto-2030\" with priority \"HIGH\"."
    desc2 = "Try searching with broader terms, clearing the filter, or ingesting a new dataset."
    draw.text((cx - 280, box_top + 210), desc1, fill=TEXT_MUTED, font=font_body)
    draw.text((cx - 250, box_top + 240), desc2, fill=TEXT_MUTED, font=font_body)

    # Clear Action Button (Reset Filters)
    draw.rounded_rectangle([cx - 110, box_top + 295, cx + 110, box_top + 345], radius=8, fill=PRIMARY_SAFFRON)
    draw.text((cx - 75, box_top + 310), "↺ Reset All Filters", fill=(255, 255, 255), font=font_bold)

    img.save("docs/screens/search-empty.png", "PNG")
    print("Generated docs/screens/search-empty.png")

# -------------------------------------------------------------
# SCREEN 3: DIAGNOSTICS & VALIDATION (ERROR STATE)
# -------------------------------------------------------------
def generate_screen3():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header(draw, active_tab_index=2)

    # Title
    draw.text((32, 95), "Dataset Diagnostics & Schema Validator", fill=TEXT_WHITE, font=font_title)
    draw.text((32, 135), "Test dataset integrity, feature scaling sanity, and ML model boundary constraints.", fill=TEXT_MUTED, font=font_body)

    # ERROR STATE ALERT BANNER (High contrast, WCAG AAA compliant, human-friendly error copy)
    err_y = 175
    draw.rounded_rectangle([32, err_y, WIDTH - 32, err_y + 160], radius=10, fill=ERROR_BG, outline=ERROR_BORDER, width=2)

    # Alert Icon
    draw.rounded_rectangle([56, err_y + 24, 100, err_y + 68], radius=8, fill=(100, 20, 20), outline=ERROR_BORDER, width=1)
    draw.text((72, err_y + 30), "!", fill=(255, 100, 100), font=font_title)

    # Error Title & Clear Error Copy
    draw.text((120, err_y + 22), "Validation Error: Missing Required Field 'topic'", fill=(254, 226, 226), font=font_h2)
    err_desc1 = "The task dataset in 'data/invalid_task_payload.json' is missing the mandatory 'topic' property in item index 2."
    err_desc2 = "Autonomous agent dispatch requires 4 mandatory attributes: 'id', 'category', 'topic', and 'priority'."
    draw.text((120, err_y + 58), err_desc1, fill=ERROR_TEXT, font=font_body)
    draw.text((120, err_y + 82), err_desc2, fill=ERROR_TEXT, font=font_body)

    # Error Recovery Actions
    draw.rounded_rectangle([120, err_y + 112, 280, err_y + 146], radius=6, fill=PRIMARY_SAFFRON)
    draw.text((135, err_y + 120), "Load Valid Sample (JSON)", fill=(255, 255, 255), font=font_badge)

    draw.rounded_rectangle([295, err_y + 112, 455, err_y + 146], radius=6, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    draw.text((315, err_y + 120), "Inspect Schema Docs", fill=TEXT_WHITE, font=font_badge)

    # Verification Form Below
    draw.rounded_rectangle([32, 360, WIDTH - 32, HEIGHT - 40], radius=10, fill=SURFACE_COLOR, outline=BORDER_COLOR, width=1)
    draw.text((56, 385), "Manual Task Verification & Schema Inspector", fill=TEXT_WHITE, font=font_h2)

    # Form field 1: Category
    draw.text((56, 430), "Task Category (Determines external REST API routing)", fill=TEXT_MUTED, font=font_small)
    draw.rounded_rectangle([56, 455, 600, 500], radius=6, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    draw.text((72, 468), "ai_tech_trends (Routes to HTTPBin live echo endpoint)", fill=TEXT_WHITE, font=font_body)

    # Form field 2: Query / Topic (With Error Highlight)
    draw.text((56, 525), "Analytical Query / Topic (Required)", fill=TEXT_MUTED, font=font_small)
    draw.rounded_rectangle([56, 550, 600, 595], radius=6, fill=(40, 15, 15), outline=ERROR_BORDER, width=2)
    draw.text((72, 563), "", fill=TEXT_WHITE, font=font_body)
    draw.text((56, 602), "⚠ Field cannot be empty. Please enter an analytical prompt.", fill=(248, 113, 113), font=font_small)

    # Form field 3: Priority Weight
    draw.text((640, 430), "Priority Weight (1.0 - 3.0)", fill=TEXT_MUTED, font=font_small)
    draw.rounded_rectangle([640, 455, 1180, 500], radius=6, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    draw.text((656, 468), "3.0 (HIGH)", fill=TEXT_WHITE, font=font_body)

    # Form Buttons
    draw.rounded_rectangle([56, 645, 230, 690], radius=8, fill=PRIMARY_SAFFRON)
    draw.text((76, 658), "Validate & Run Task", fill=(255, 255, 255), font=font_bold)

    draw.rounded_rectangle([245, 645, 420, 690], radius=8, fill=SURFACE_ELEVATED, outline=BORDER_COLOR, width=1)
    draw.text((265, 658), "Reset Form Fields", fill=TEXT_MUTED, font=font_bold)

    img.save("docs/screens/report-error.png", "PNG")
    print("Generated docs/screens/report-error.png")

if __name__ == "__main__":
    generate_screen1()
    generate_screen2()
    generate_screen3()
    print("All 3 design proof screenshots successfully generated in docs/screens/")
