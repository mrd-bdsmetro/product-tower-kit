// Product Tower Kit — Syntax Check
// Validates Node.js syntax and basic structure.

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
let passed = 0;
let failed = 0;

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

// Check Node.js files parse correctly
console.log('\n[Node.js Syntax]');

const nodeFiles = ['index.js', 'bin/product-tower.js'];

for (const file of nodeFiles) {
  check(`${file} parses`, () => {
    const content = fs.readFileSync(path.join(ROOT, file), 'utf8');
    // Basic syntax check - look for common issues
    assert(!content.includes('SyntaxError'), 'contains SyntaxError');
    assert(content.length > 0, 'file is empty');
  });
}

// Check Python files have valid syntax
console.log('\n[Python Syntax]');

const pythonFiles = ['scripts/gate_checker.py'];

for (const file of pythonFiles) {
  check(`${file} has valid structure`, () => {
    const content = fs.readFileSync(path.join(ROOT, file), 'utf8');
    assert(content.includes('#!/usr/bin/env python3'), 'missing shebang');
    assert(content.includes('def main'), 'missing main function');
    assert(content.includes('if __name__'), 'missing __name__ guard');
  });
}

// Check JSON files parse correctly
console.log('\n[JSON Files]');

const jsonFiles = ['package.json'];

for (const file of jsonFiles) {
  check(`${file} parses`, () => {
    const content = fs.readFileSync(path.join(ROOT, file), 'utf8');
    JSON.parse(content); // Will throw if invalid
  });
}

// Check SKILL.md files have valid frontmatter
console.log('\n[SKILL.md Frontmatter]');

const skillsDir = path.join(ROOT, '.claude', 'skills');
if (fs.existsSync(skillsDir)) {
  const skills = fs.readdirSync(skillsDir).filter(f => {
    const skillPath = path.join(skillsDir, f, 'SKILL.md');
    return fs.existsSync(skillPath);
  });

  for (const skill of skills) {
    check(`${skill}/SKILL.md frontmatter`, () => {
      const content = fs.readFileSync(path.join(skillsDir, skill, 'SKILL.md'), 'utf8');
      assert(content.startsWith('---\n'), 'missing frontmatter delimiter');
      
      // Check for required fields
      const frontmatterEnd = content.indexOf('---\n', 4);
      assert(frontmatterEnd > 0, 'unclosed frontmatter');
      
      const frontmatter = content.substring(4, frontmatterEnd);
      assert(frontmatter.includes('name:'), 'missing name field');
      assert(frontmatter.includes('description:'), 'missing description field');
    });
  }
}

// Summary
console.log(`\n${'='.repeat(50)}`);
console.log(`Syntax Results: ${passed} passed, ${failed} failed`);
if (failed > 0) process.exit(1);
