#!/usr/bin/env python3
"""
Product Check - Status overview of product validation

Usage:
    python product-check.py <product_dir>

Output:
    - T-tier completion status
    - Anti-bias challenge status
    - PMF score
    - Funnel stage
    - Suggested next steps (skills + actions)
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Fix Unicode on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# T-Series files
T_TIERS = [
    ("T-1", "t_minus1_rapid_validation.md"),
    ("T0", "t0_market_research.md"),
    ("T1", "t1_target_market.md"),
    ("T2", "t2_segmentation.md"),
    ("T3", "t3_segment_filter.md"),
    ("T4", "t4_personas.md"),
    ("T5", "t5_user_needs.md"),
    ("T6", "t6_underserved_needs.md"),
    ("T7", "t7_pmf.md"),
    ("T8", "t8_features.md"),
    ("T9", "t9_user_stories.md"),
    ("T9.5", "t9_5_offer_bridge.md"),
    ("T14", "t14_feedback_loop.md"),
]

AB_TIERS = [
    ("AB1", "ab1_counter_search.md"),
    ("AB2", "ab2_red_team.md"),
    ("AB3", "ab3_field_notes.md"),
    ("AB4", "ab4_user_interview.md"),
    ("AB5", "ab5_strategic_analysis.md"),
    ("AB6", "ab6_founder_insight.md"),
]

# Skill mapping per T-tier
TIER_SKILLS = {
    "T-1": ["brainstorm", "research"],
    "T0": ["market-research", "competitor-analysis"],
    "T1": ["market-segmentation", "user-discovery"],
    "T2": ["market-segmentation"],
    "T3": ["market-segmentation"],
    "T4": ["user-discovery", "problem-solving"],
    "T5": ["user-discovery", "problem-solving"],
    "T6": ["problem-solving", "pmf-validator"],
    "T7": ["pmf-validator", "analytics-feedback"],
    "T8": ["product-sale", "pricing-strategy"],
    "T9": ["product-sale", "onboarding-cro"],
    "T9.5": ["product-sale", "launch-strategy"],
}

# Funnel stage mapping
FUNNEL_STAGES = [
    ("Idea", ["T-1"], 25),
    ("Coffee Talk", ["T0", "T1", "T2", "T3"], 50),
    ("Deal", ["T4", "T5", "T6"], 75),
    ("Active", ["T7", "T8", "T9", "T9.5"], 90),
    ("PMF", ["T14"], 100),
]

# Gate dependencies
GATE_RULES = {
    "T0": ["T-1"],
    "T1": ["T0"],
    "T2": ["T0", "T1"],
    "T3": ["T0", "T1", "T2"],
    "T4": ["T3"],
    "T5": ["T3", "T4"],
    "T6": ["T3", "T4", "T5"],
    "AB1": ["T4"],
    "AB2": ["T4", "AB1"],
    "AB3": ["T4", "AB1", "AB2"],
    "AB4": ["T4", "AB1", "AB2", "AB3"],
    "AB5": ["T4", "AB1", "AB2", "AB3", "AB4"],
    "AB6": ["T4", "AB1", "AB2", "AB3", "AB4", "AB5"],
    "T7": ["T6", "AB1", "AB2", "AB3", "AB4"],
    "T8": ["T7"],
    "T9": ["T7", "T8"],
    "T9.5": ["T7", "T8", "T9"],
}


def get_state_path(product_dir):
    return Path(product_dir) / "02_Instance_Layer" / "execution" / "pipeline_state.json"


def load_state(product_dir):
    state_path = get_state_path(product_dir)
    if state_path.exists():
        with open(state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def check_tier_file(product_dir, tier_name, file_name):
    """Check if tier file exists and has content"""
    for base in ["02_Instance_Layer/T_Series", "data"]:
        path = Path(product_dir) / base / file_name
        if path.exists():
            size = path.stat().st_size
            if size > 500:
                return "complete", size
            elif size > 100:
                return "partial", size
            else:
                return "empty", size
    return "missing", 0


def get_current_funnel_stage(completed_tiers):
    """Determine which funnel stage the product is in"""
    for stage_name, tiers, progress in FUNNEL_STAGES:
        incomplete = [t for t in tiers if t not in completed_tiers]
        if incomplete:
            return stage_name, progress, incomplete
    return "PMF", 100, []


def get_next_action(completed_tiers, missing_tiers, product_dir):
    """Determine the next action based on current state"""
    # Find next incomplete tier with satisfied dependencies
    for tier_name, _ in T_TIERS + AB_TIERS:
        if tier_name not in completed_tiers:
            deps = GATE_RULES.get(tier_name, [])
            missing_deps = [d for d in deps if d not in completed_tiers]
            if not missing_deps:
                # This tier is ready to work on
                return tier_name
    return None


def format_skill_link(skill_name):
    """Format skill name as link"""
    return f"[[.claude/skills/{skill_name}/SKILL.md|{skill_name}]]"


def main():
    # Determine product_dir
    # If run via CLI (product-tower.js), it passes "." as arg from KIT_ROOT
    # If run directly, use script location
    if len(sys.argv) >= 2:
        # CLI invocation - use the path passed
        product_dir = Path(sys.argv[1])
        # If path is "." or doesn't exist, use script location
        if str(product_dir) == "." or not product_dir.exists():
            product_dir = Path(__file__).parent.parent
    else:
        product_dir = Path(__file__).parent.parent

    # Verify we're in a Product folder
    if not (product_dir / "package.json").exists():
        # Try parent
        product_dir = product_dir.parent
    if not (product_dir / "package.json").exists():
        print(f"Error: Not in a Product folder. package.json not found.")
        sys.exit(1)

    print("=" * 60)
    print("  PRODUCT CHECK - Product Tower Kit")
    print("=" * 60)
    print()

    # Load state
    state = load_state(product_dir)
    completed_tiers = set()
    pmf_score = None

    if state:
        completed_tiers = set(state.get("tiers_completed", {}).keys())
        pmf_data = state.get("pmf", {})
        pmf_score = pmf_data.get("adjusted")

    # Check T-tiers
    print("📊 T-SERIES STATUS")
    print("-" * 40)
    t_complete = 0
    t_partial = 0
    for tier_name, file_name in T_TIERS:
        if tier_name in completed_tiers:
            status = "✅"
            t_complete += 1
        else:
            tier_status, _ = check_tier_file(product_dir, tier_name, file_name)
            if tier_status == "complete":
                status = "✅"
                t_complete += 1
            elif tier_status == "partial":
                status = "🔶"
                t_partial += 1
            else:
                status = "❌"
        print(f"  {status} {tier_name}")

    print(f"\n  Completed: {t_complete}/{len(T_TIERS)} | Partial: {t_partial}")

    # Check AB-tiers
    print("\n🛡️ ANTI-BIAS CHALLENGES")
    print("-" * 40)
    ab_complete = 0
    for ab_name, file_name in AB_TIERS:
        if ab_name in completed_tiers:
            status = "✅"
            ab_complete += 1
        else:
            tier_status, _ = check_tier_file(product_dir, ab_name, file_name)
            if tier_status == "complete":
                status = "✅"
                ab_complete += 1
            else:
                status = "❌"
        print(f"  {status} {ab_name}")

    print(f"\n  Completed: {ab_complete}/{len(AB_TIERS)}")

    # PMF Score
    print("\n⭐ PMF SCORE")
    print("-" * 40)
    if pmf_score is not None:
        status = "✅" if pmf_score >= 30 else "⚠️"
        print(f"  {status} Score: {pmf_score}/50")
        if pmf_score >= 30:
            print(f"  🎉 PMF ACHIEVED - Ready to scale!")
        else:
            print(f"  📈 Need {30 - pmf_score} more points to reach PMF")
    else:
        print(f"  ❌ Not scored yet")
        print(f"  Run: product-tower pmf <raw_score> <penalty>")

    # Funnel Stage
    print("\n🎯 VALIDATION FUNNEL")
    print("-" * 40)
    stage_name, progress, incomplete = get_current_funnel_stage(completed_tiers)
    print(f"  📍 Stage: {stage_name}")
    print(f"  📊 Progress: {progress}%")

    # Next Action
    print("\n🚀 NEXT ACTION")
    print("-" * 40)
    next_tier = get_next_action(completed_tiers, incomplete, product_dir)
    if next_tier:
        print(f"  → Work on: {next_tier}")

        # Suggest skills
        skills = TIER_SKILLS.get(next_tier, [])
        if skills:
            print(f"  → Use skills: {', '.join(skills)}")

        # Show gate info
        deps = GATE_RULES.get(next_tier, [])
        if deps:
            print(f"  → Dependencies: {', '.join(deps)}")
    else:
        if stage_name == "PMF":
            print(f"  ✅ PMF COMPLETE - Consider scaling!")
        else:
            print(f"  → All tiers complete, mark T14 as done")

    # Suggestions
    print("\n💡 SUGGESTIONS")
    print("-" * 40)

    # Missing dependencies warning
    blocked_tiers = []
    for tier_name in T_TIERS + AB_TIERS:
        if tier_name not in completed_tiers:
            deps = GATE_RULES.get(tier_name, [])
            missing_deps = [d for d in deps if d not in completed_tiers]
            if missing_deps and tier_name not in blocked_tiers:
                blocked_tiers.append(tier_name)

    if blocked_tiers:
        print(f"  ⚠️ Blocked tiers: {', '.join(blocked_tiers[:3])}...")
        print(f"  → Complete dependencies first")

    # PMF warning
    if pmf_score and pmf_score < 25:
        print(f"  ⚠️ PMF score low - focus on validation")
        print(f"  → Use market-research skill for T0")
        print(f"  → Use user-discovery skill for T4-T6")

    # Success metrics
    print("\n📈 SUCCESS METRICS")
    print("-" * 40)
    total_tiers = len(T_TIERS) + len(AB_TIERS)
    actual_complete = t_complete + ab_complete - (len([t for t in completed_tiers if t in [x[0] for x in T_TIERS + AB_TIERS]]))
    print(f"  Total completion: {t_complete + ab_complete}/{total_tiers} tiers")
    print(f"  Funnel stage: {stage_name}")

    # Last updated
    if state and "updated_at" in state:
        last_updated = state["updated_at"][:10]
        print(f"\n  Last updated: {last_updated}")

    print("\n" + "=" * 60)
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)


if __name__ == "__main__":
    main()