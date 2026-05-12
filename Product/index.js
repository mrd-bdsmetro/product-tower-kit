#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const KIT_ROOT = __dirname;
const SKILLS_DIR = path.join(KIT_ROOT, '.claude', 'skills');
const SCRIPTS_DIR = path.join(KIT_ROOT, 'scripts');

function getVersion() {
  const pkg = JSON.parse(fs.readFileSync(path.join(KIT_ROOT, 'package.json'), 'utf8'));
  return pkg.version;
}

function getSkills() {
  if (!fs.existsSync(SKILLS_DIR)) return [];
  return fs.readdirSync(SKILLS_DIR).filter(f => {
    const skillPath = path.join(SKILLS_DIR, f, 'SKILL.md');
    return fs.existsSync(skillPath);
  });
}

module.exports = {
  KIT_ROOT,
  SKILLS_DIR,
  SCRIPTS_DIR,
  getVersion,
  getSkills,
  version: getVersion()
};
