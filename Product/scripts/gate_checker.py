#!/usr/bin/env python3
"""
Product Tower — Gate Enforcement System v1.0

Usage:
    python gate_checker.py <project_dir> init
    python gate_checker.py <project_dir> check <tier>
    python gate_checker.py <project_dir> complete <tier>
    python gate_checker.py <project_dir> pmf <raw> <penalty>
    python gate_checker.py <project_dir> status
    python gate_checker.py <project_dir> assess
    python gate_checker.py <project_dir> naming
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

# Fix Unicode on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# NAMING CONVENTION
NAMING_CONVENTION = {
    "T-1": "data/t_minus1_rapid_validation.md",
    "T0": "data/t0_market_research.md",
    "T1": "data/t1_target_market.md",
    "T2": "data/t2_segmentation.md",
    "T3": "data/t3_segment_filter.md",
    "T4": "data/t4_personas.md",
    "T5": "data/t5_user_needs.md",
    "T6": "data/t6_underserved_needs.md",
    "AB1": "data/ab1_counter_search.md",
    "AB2": "data/ab2_red_team.md",
    "AB3": "data/ab3_field_notes.md",
    "AB4": "data/ab4_user_interview.md",
    "AB5": "data/ab5_strategic_analysis.md",
    "AB6": "data/ab6_founder_insight.md",
    "T7": "data/t7_pmf.md",
    "T8": "data/t8_features.md",
    "T9": "data/t9_user_stories.md",
    "T9.5": "data/t9_5_offer_bridge.md",
    "T0-CP": "data/t0_competitive_map.md",
    "T14": "data/t14_feedback_loop.md",
}

# GATE RULES
GATE_RULES = {
    "T-1": {"requires_tiers": [], "name": "Rapid Validation"},
    "T0": {"requires_tiers": ["T-1"], "name": "Market Research"},
    "T1": {"requires_tiers": ["T0"], "name": "Target Market"},
    "T2": {"requires_tiers": ["T0", "T1"], "name": "Market Segmentation"},
    "T3": {"requires_tiers": ["T0", "T1", "T2"], "name": "Segment Filter"},
    "T4": {"requires_tiers": ["T3"], "name": "User Personas"},
    "T5": {"requires_tiers": ["T3", "T4"], "name": "User Needs"},
    "T6": {"requires_tiers": ["T3", "T4", "T5"], "name": "Unmet Needs"},
    "AB1": {"requires_tiers": ["T4"], "name": "Counter-Search"},
    "AB2": {"requires_tiers": ["T4", "AB1"], "name": "Red Team"},
    "AB3": {"requires_tiers": ["T4", "AB1", "AB2"], "name": "Field Observation"},
    "AB4": {"requires_tiers": ["T4", "AB1", "AB2", "AB3"], "name": "User Interview"},
    "AB5": {"requires_tiers": ["T4", "AB1", "AB2", "AB3", "AB4"], "name": "Strategic Analysis"},
    "AB6": {"requires_tiers": ["T4", "AB1", "AB2", "AB3", "AB4"], "name": "Founder Insight"},
    "T7": {"requires_tiers": ["T6", "AB1", "AB2", "AB3", "AB4"], "name": "PMF Validation"},
    "T8": {"requires_tiers": ["T7"], "name": "Feature Set"},
    "T9": {"requires_tiers": ["T7", "T8"], "name": "User Stories"},
    "T9.5": {"requires_tiers": ["T7", "T8", "T9"], "name": "Offer Bridge"},
    "T0-CP": {"requires_tiers": ["T0"], "name": "Competitive Positioning"},
    "T14": {"requires_tiers": ["T9.5"], "name": "Feedback Loop"},
}

PMF_THRESHOLD = 30
PMF_SCALE = 50


def get_state_path(project_dir):
    return Path(project_dir) / "pipeline_state.json"


def load_state(project_dir):
    state_path = get_state_path(project_dir)
    if state_path.exists():
        with open(state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def save_state(project_dir, state):
    state_path = get_state_path(project_dir)
    state["updated_at"] = datetime.now().isoformat()
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def cmd_init(project_dir):
    data_dir = Path(project_dir) / "data"
    data_dir.mkdir(exist_ok=True)
    
    state = {
        "project": Path(project_dir).name,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "version": "1.0.0",
        "tiers_completed": {},
        "tiers_skipped": {},
        "anti_bias": {
            "AB1": {"status": "pending", "file": NAMING_CONVENTION["AB1"]},
            "AB2": {"status": "pending", "file": NAMING_CONVENTION["AB2"]},
            "AB3": {"status": "pending", "file": NAMING_CONVENTION["AB3"]},
            "AB4": {"status": "pending", "file": NAMING_CONVENTION["AB4"]},
        },
        "pmf": {"raw": None, "adjusted": None, "penalty": 0, "scale": PMF_SCALE, "threshold": PMF_THRESHOLD},
    }
    save_state(project_dir, state)
    print(f"✅ Product Tower initialized: {project_dir}")
    print(f"📁 Created: {data_dir}")
    print(f"📄 State: {get_state_path(project_dir)}")


def cmd_check(project_dir, tier):
    state = load_state(project_dir)
    if not state:
        print("❌ Not initialized. Run: product-tower init")
        sys.exit(1)
    
    if tier not in GATE_RULES:
        print(f"❌ Unknown tier: {tier}")
        sys.exit(1)
    
    rule = GATE_RULES[tier]
    completed = set(state.get("tiers_completed", {}).keys())
    required = set(rule["requires_tiers"])
    missing = required - completed
    
    if missing:
        print(f"🛑 GATE BLOCK: {tier} ({rule['name']})")
        print(f"   Missing: {', '.join(sorted(missing))}")
        print(f"   Complete those first, or: force skip {tier}")
        sys.exit(1)
    else:
        print(f"✅ GATE PASS: {tier} ({rule['name']})")
        sys.exit(0)


def cmd_complete(project_dir, tier):
    state = load_state(project_dir)
    if not state:
        print("❌ Not initialized. Run: product-tower init")
        sys.exit(1)
    
    if tier not in GATE_RULES:
        print(f"❌ Unknown tier: {tier}")
        sys.exit(1)
    
    state["tiers_completed"][tier] = {"completed_at": datetime.now().isoformat()}
    save_state(project_dir, state)
    print(f"✅ {tier} marked complete")


def cmd_pmf(project_dir, raw, penalty):
    state = load_state(project_dir)
    if not state:
        print("❌ Not initialized. Run: product-tower init")
        sys.exit(1)
    
    raw_score = float(raw)
    penalty_val = float(penalty)
    adjusted = raw_score + penalty_val
    
    state["pmf"]["raw"] = raw_score
    state["pmf"]["penalty"] = penalty_val
    state["pmf"]["adjusted"] = adjusted
    save_state(project_dir, state)
    
    status = "GO ✅" if adjusted >= PMF_THRESHOLD else "NO-GO ❌"
    print(f"⭐ PMF Score: {raw_score}/50 (penalty: {penalty_val})")
    print(f"   Adjusted: {adjusted}/50")
    print(f"   Threshold: {PMF_THRESHOLD}/50")
    print(f"   Decision: {status}")


def cmd_status(project_dir):
    state = load_state(project_dir)
    if not state:
        print("❌ Not initialized. Run: product-tower init")
        sys.exit(1)
    
    completed = list(state.get("tiers_completed", {}).keys())
    skipped = list(state.get("tiers_skipped", {}).keys())
    pmf = state.get("pmf", {})
    ab = state.get("anti_bias", {})
    
    print(f"📊 PIPELINE STATUS — {state.get('project', 'Unknown')}")
    print(f"")
    print(f"Completed: {' '.join(completed) if completed else '(none)'}")
    print(f"Skipped: {' '.join(skipped) if skipped else '(none)'}")
    print(f"")
    print(f"PMF: {pmf.get('raw', 'not scored')} (adjusted: {pmf.get('adjusted', 'not scored')})")
    print(f"Anti-Bias: " + " ".join([f"{k} {'✅' if v['status']=='completed' else '⏳'}" for k, v in ab.items()]))


def cmd_assess(project_dir):
    state = load_state(project_dir)
    if not state:
        print("❌ Not initialized. Run: product-tower init")
        sys.exit(1)
    
    completed = set(state.get("tiers_completed", {}).keys())
    
    tiers = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T9.5"]
    score = 0
    print(f"🏗️ PRODUCT TOWER ASSESSMENT — {state.get('project', 'Unknown')}")
    print(f"")
    
    for tier in tiers:
        if tier in completed:
            file_path = Path(project_dir) / NAMING_CONVENTION.get(tier, "")
            if file_path.exists():
                size = file_path.stat().st_size
                if size > 1000:
                    print(f"  {tier}: ✅ 3/3 (Proven)")
                    score += 3
                else:
                    print(f"  {tier}: 🟢 2/3 (Validated)")
                    score += 2
            else:
                print(f"  {tier}: 🟡 1/3 (Guaranteed)")
                score += 1
        else:
            print(f"  {tier}: ❌ 0/3 (Not done)")
    
    print(f"")
    print(f"TOWER SCORE: {score}/33")


def cmd_naming():
    print("📋 FILE NAMING CONVENTION")
    print("")
    for tier, path in sorted(NAMING_CONVENTION.items()):
        print(f"  {tier:6} → {path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: gate_checker.py <project_dir> <command> [args]")
        sys.exit(1)
    
    project_dir = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) > 2 else "status"
    
    if command == "init":
        cmd_init(project_dir)
    elif command == "check":
        tier = sys.argv[3] if len(sys.argv) > 3 else ""
        cmd_check(project_dir, tier)
    elif command == "complete":
        tier = sys.argv[3] if len(sys.argv) > 3 else ""
        cmd_complete(project_dir, tier)
    elif command == "pmf":
        raw = sys.argv[3] if len(sys.argv) > 3 else "0"
        penalty = sys.argv[4] if len(sys.argv) > 4 else "0"
        cmd_pmf(project_dir, raw, penalty)
    elif command == "status":
        cmd_status(project_dir)
    elif command == "assess":
        cmd_assess(project_dir)
    elif command == "naming":
        cmd_naming()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
