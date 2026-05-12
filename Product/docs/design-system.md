---
status: draft
type: documentation
owner: MR.D
last_updated: 2026-05-12
tags: [design-system, UI, UX, T11, tokens, components]
pmf_impact: medium
---

# Design System - T11 UI/UX Standards

## Overview

Design System defines the **visual language** and **component specs** for T11 (UI Design) and beyond. It ensures consistent UI across the product.

**Applies to:** T11-T14 (Build Phase via ClaudeKit)

---

## Token Architecture (3-Layer)

```
Primitive → Semantic → Component
```

### Primitive Tokens

Raw values (colors, spacing, typography):

| Token | Value | Usage |
|-------|-------|-------|
| `--color-blue-500` | #3B82F6 | Links, primary actions |
| `--color-gray-100` | #F3F4F6 | Backgrounds |
| `--spacing-4` | 1rem | Standard padding |
| `--font-size-base` | 16px | Body text |
| `--radius-md` | 6px | Cards, buttons |

### Semantic Tokens

Meaning-based aliases:

| Token | Value | Maps to |
|-------|-------|---------|
| `--color-primary` | #3B82F6 | `--color-blue-500` |
| `--color-surface` | #F3F4F6 | `--color-gray-100` |
| `--space-component` | 1rem | `--spacing-4` |
| `--text-body` | 16px | `--font-size-base` |
| `--radius-card` | 6px | `--radius-md` |

### Component Tokens

Specific to components:

| Token | Value | Usage |
|-------|-------|-------|
| `--button-primary-bg` | var(--color-primary) | Primary button background |
| `--button-primary-hover` | #2563EB | Primary button hover |
| `--input-border` | 1px solid #D1D5DB | Input borders |
| `--card-shadow` | 0 1px 3px rgba(0,0,0,0.1) | Card elevation |

---

## Color Palette

### Primary

| Name | Hex | Usage |
|------|-----|-------|
| Primary | #3B82F6 | CTAs, links, active states |
| Primary Dark | #2563EB | Hover states |
| Primary Light | #93C5FD | Backgrounds, disabled |

### Neutral

| Name | Hex | Usage |
|------|-----|-------|
| Surface | #F9FAFB | Page backgrounds |
| Card | #FFFFFF | Card backgrounds |
| Border | #E5E7EB | Borders, dividers |
| Text Primary | #111827 | Headings, body |
| Text Secondary | #6B7280 | Captions, hints |
| Text Muted | #9CA3AF | Placeholders |

### Semantic

| Name | Hex | Usage |
|------|-----|-------|
| Success | #10B981 | Confirmations, checks |
| Warning | #F59E0B | Warnings, alerts |
| Error | #EF4444 | Errors, destructive |
| Info | #3B82F6 | Informational |

---

## Typography Scale

| Name | Size | Line Height | Weight | Usage |
|------|------|-------------|--------|-------|
| Display | 36px | 1.2 | 700 | Hero headlines |
| H1 | 30px | 1.3 | 700 | Page titles |
| H2 | 24px | 1.4 | 600 | Section headers |
| H3 | 20px | 1.4 | 600 | Card titles |
| Body | 16px | 1.5 | 400 | Body text |
| Small | 14px | 1.5 | 400 | Secondary text |
| Caption | 12px | 1.4 | 400 | Labels, hints |

---

## Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Tight gaps |
| `--space-2` | 8px | Icon gaps |
| `--space-3` | 12px | Inline spacing |
| `--space-4` | 16px | Component padding |
| `--space-6` | 24px | Card padding |
| `--space-8` | 32px | Section gaps |
| `--space-12` | 48px | Page sections |

---

## Component Specifications

### Button

| Variant | Background | Text | Border | Hover |
|---------|------------|------|--------|-------|
| Primary | #3B82F6 | #FFFFFF | none | #2563EB |
| Secondary | transparent | #3B82F6 | 1px #3B82F6 | #EFF6FF |
| Ghost | transparent | #6B7280 | none | #F3F4F6 |
| Destructive | #EF4444 | #FFFFFF | none | #DC2626 |

**States:** default, hover, active, disabled, loading

### Input

| State | Border | Background |
|-------|--------|------------|
| Default | 1px #D1D5DB | #FFFFFF |
| Focus | 2px #3B82F6 | #FFFFFF |
| Error | 1px #EF4444 | #FEF2F2 |
| Disabled | 1px #E5E7EB | #F9FAFB |

### Card

| Property | Value |
|----------|-------|
| Background | #FFFFFF |
| Border | 1px #E5E7EB |
| Radius | 8px |
| Shadow | 0 1px 3px rgba(0,0,0,0.1) |
| Padding | 24px |

### Badge

| Variant | Background | Text |
|---------|------------|------|
| Default | #F3F4F6 | #374151 |
| Primary | #EFF6FF | #1D4ED8 |
| Success | #ECFDF5 | #065F46 |
| Warning | #FFFBEB | #92400E |
| Error | #FEF2F2 | #991B1B |

---

## Accessibility Rules

| Rule | Requirement |
|------|-------------|
| Color contrast | 4.5:1 minimum for text |
| Focus indicators | Visible on keyboard nav |
| Touch targets | 44x44px minimum |
| ARIA labels | On icons, interactive elements |
| Screen reader | Logical reading order |

---

## Responsive Breakpoints

| Breakpoint | Min Width | Usage |
|------------|-----------|-------|
| Mobile | 320px | Phones |
| Tablet | 768px | Tablets |
| Desktop | 1024px | Laptops |
| Wide | 1280px | Large screens |

---

## Implementation

```bash
# Install design tokens
npm install @your-org/design-tokens

# Use in component
import { button, card, input } from '@your-org/design-tokens';

const PrimaryButton = button.variants.primary;
```

---

## ClaudeKit Integration

Use ClaudeKit skills for implementation:

| Task | Command |
|------|---------|
| Create component | `/ck:frontend-design --type component` |
| Apply design system | `/ck:ui-styling --tokens` |
| Review UI compliance | `/ck:web-design-guidelines` |

---

## References

- ClaudeKit `ck:frontend-design` skill
- ClaudeKit `ck:ui-styling` skill
- ClaudeKit `ck:ui-ux-pro-max` skill
- `docs/harness-system.md` (T13 quality layer)

---

*Product Kit T11 UI Design Layer*