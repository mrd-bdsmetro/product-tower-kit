// Product Tower Kit — Invariant Checks
// Static contracts for package structure, SKILL.md validity, and gate consistency.

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
let passed = 0;
let failed = 0;

function read(relativePath) {
  return fs.readFileSync(path.join(ROOT, relativePath), 'utf8');
}

function readJson(relativePath) {
  return JSON.parse(read(relativePath));
}

function exists(relativePath) {
  return fs.existsSync(path.join(ROOT, relativePath));
}

function check(name, fn) {
  try {
    fn();
    console.log(`  [OK] ${name}`);
    passed++;
  } catch (err) {
    console.log(`  [FAIL] ${name}: ${err.message}`);
    failed++;
  }
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

// === PACKAGE ===
console.log('\n[Package]');
const pkg = readJson('package.json');

check('package name is product-tower-kit', () => {
  assert(pkg.name === 'product-tower-kit', `actual: ${pkg.name}`);
});

check('package has bin entry', () => {
  assert(pkg.bin && pkg.bin['product-tower'], 'missing bin.product-tower');
});

check('package has files array', () => {
  assert(Array.isArray(pkg.files) && pkg.files.length > 0, 'missing files array');
});

check('license is proprietary', () => {
  assert(pkg.license && pkg.license.includes('SEE LICENSE'), `actual: ${pkg.license}`);
});

// === CLI ===
console.log('\n[CLI]');
check('bin/product-tower.js has shebang', () => {
  const content = read('bin/product-tower.js');
  assert(content.startsWith('#!/usr/bin/env node'), 'missing shebang');
});

check('bin/product-tower.js maps commands correctly', () => {
  const content = read('bin/product-tower.js');
  const requiredCommands = ['init', 'check', 'complete', 'pmf', 'status', 'assess', 'naming'];
  for (const cmd of requiredCommands) {
    assert(content.includes(`'${cmd}'`) || content.includes(`"${cmd}"`), `missing command mapping: ${cmd}`);
  }
});

// === SKILLS ===
console.log('\n[Skills]');
const expectedSkills = [
  'product-tower',
  'market-research',
  'market-segmentation',
  'user-discovery',
  'pmf-validator',
  'pricing-strategy',
  'competitor-analysis',
  'deep-research-parser',
  'analytics-feedback',
  'delivery-tower',
  'sales-tower',
  'product-sale'
];

for (const skill of expectedSkills) {
  check(`skill exists: ${skill}`, () => {
    assert(exists(`.claude/skills/${skill}/SKILL.md`), 'SKILL.md not found');
  });

  check(`skill has frontmatter: ${skill}`, () => {
    const content = read(`.claude/skills/${skill}/SKILL.md`);
    assert(content.startsWith('---\n'), 'missing YAML frontmatter');
    assert(content.includes('name:'), 'missing name field');
    assert(content.includes('description:'), 'missing description field');
  });
}

// === AGENTS ===
console.log('\n[Agents]');
const expectedAgents = [
  'product-planner',
  'market-researcher',
  'anti-bias-challenger',
  'pmf-validator',
  'feature-scoper'
];

for (const agent of expectedAgents) {
  check(`agent exists: ${agent}`, () => {
    assert(exists(`.claude/agents/${agent}.md`), 'agent file not found');
  });

  check(`agent has required sections: ${agent}`, () => {
    const content = read(`.claude/agents/${agent}.md`);
    assert(content.includes('## Role'), 'missing Role section');
    assert(content.includes('## Behavior'), 'missing Behavior section');
    assert(content.includes('## Activation'), 'missing Activation section');
  });
}

// === COMMANDS ===
console.log('\n[Commands]');
const expectedCommands = [
  'pt-init',
  'pt-research',
  'pt-validate',
  'pt-scope',
  'pt-assess',
  'pt-status',
  'pt-report'
];

for (const cmd of expectedCommands) {
  check(`command exists: ${cmd}`, () => {
    assert(exists(`.claude/commands/${cmd}.md`), 'command file not found');
  });

  check(`command has Usage section: ${cmd}`, () => {
    const content = read(`.claude/commands/${cmd}.md`);
    assert(content.includes('## Usage'), 'missing Usage section');
  });
}

// === HOOKS ===
console.log('\n[Hooks]');
const expectedHooks = ['gate-check.sh', 'pmf-alert.sh', 'tier-progress.sh'];

for (const hook of expectedHooks) {
  check(`hook exists: ${hook}`, () => {
    assert(exists(`.claude/hooks/${hook}`), 'hook file not found');
  });
}

check('settings.json has hook config', () => {
  const settings = readJson('.claude/settings.json');
  assert(settings.hooks, 'missing hooks config');
  assert(settings.hooks.PreToolUse || settings.hooks.PostToolUse || settings.hooks.SessionStart, 'no hook events configured');
});

// === RULES ===
console.log('\n[Rules]');
const expectedRules = ['product-workflow', 'gate-enforcement', 'anti-bias-rules'];

for (const rule of expectedRules) {
  check(`rule exists: ${rule}`, () => {
    assert(exists(`.claude/rules/${rule}.md`), 'rule file not found');
  });
}

// === GATE CONSISTENCY ===
console.log('\n[Gate Consistency]');
check('gate_checker.py has all tiers', () => {
  const code = read('scripts/gate_checker.py');
  const requiredTiers = ['T-1', 'T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'AB1', 'AB2', 'AB3', 'AB4', 'AB5', 'AB6', 'T7', 'T8', 'T9', 'T9.5', 'T14'];
  for (const tier of requiredTiers) {
    assert(code.includes(`"${tier}"`), `missing tier: ${tier}`);
  }
});

check('gate_checker.py has all commands', () => {
  const code = read('scripts/gate_checker.py');
  const requiredCommands = ['init', 'check', 'complete', 'pmf', 'status', 'assess', 'naming'];
  for (const cmd of requiredCommands) {
    assert(code.includes(`"${cmd}"`), `missing command: ${cmd}`);
  }
});

check('PMF threshold is 30/50', () => {
  const code = read('scripts/gate_checker.py');
  assert(code.includes('PMF_THRESHOLD = 30') || code.includes('PMF_THRESHOLD=30'), 'PMF threshold not set to 30');
});

// === SKILL CROSS-REFERENCES ===
console.log('\n[Skill Cross-References]');
check('master orchestrator references all sub-skills', () => {
  const content = read('.claude/skills/product-tower/SKILL.md');
  const requiredRefs = ['market-research', 'market-segmentation', 'user-discovery', 'pmf-validator', 'pricing-strategy'];
  for (const ref of requiredRefs) {
    assert(content.includes(ref), `missing reference to: ${ref}`);
  }
});

// === SUMMARY ===
console.log(`\n${'='.repeat(50)}`);
console.log(`Invariant Results: ${passed} passed, ${failed} failed`);
if (failed > 0) process.exit(1);
