#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const KIT_ROOT = path.resolve(__dirname, '..');
const SCRIPTS_DIR = path.join(KIT_ROOT, 'scripts');

const args = process.argv.slice(2);
const command = args[0];

function getPython() {
  const isWin = os.platform() === 'win32';
  const venvPython = isWin
    ? path.join(KIT_ROOT, '.venv', 'Scripts', 'python.exe')
    : path.join(KIT_ROOT, '.venv', 'bin', 'python3');

  if (fs.existsSync(venvPython)) return venvPython;

  try {
    execSync('python3 --version', { stdio: 'ignore' });
    return 'python3';
  } catch {
    return 'python';
  }
}

function runPython(script, args = []) {
  const python = getPython();
  const scriptPath = path.join(SCRIPTS_DIR, script);
  const cwd = KIT_ROOT;
  try {
    execSync(`${python} "${scriptPath}" ${args.join(' ')}`, {
      stdio: 'inherit',
      cwd: cwd
    });
  } catch (e) {
    process.exit(e.status || 1);
  }
}

function runNode(script, args = []) {
  const scriptPath = path.join(SCRIPTS_DIR, script);
  const cwd = KIT_ROOT;
  try {
    execSync(`node "${scriptPath}" ${args.join(' ')}`, {
      stdio: 'inherit',
      cwd: cwd
    });
  } catch (e) {
    process.exit(e.status || 1);
  }
}

function showHelp() {
  console.log(`
Product Tower Kit v${require('../package.json').version}

Usage:
  product-tower <command> [options]

Commands:
  init                    Initialize project with data/ directory
  check <tier>            Check gate for tier (T0, T1, ..., T14, AB1-AB6)
  complete <tier>         Mark tier as complete
  pmf <raw> <penalty>     Set PMF score with penalty
  status                  Show pipeline status
  assess                  Quick health check
  product-check           Full product status + skill suggestions
  naming                  Show file naming convention
  convert                 Show T9.5 conversion prompt (ClaudeKit upsell)
  version                 Show version

Examples:
  product-tower init
  product-tower check T1
  product-tower complete T0
  product-tower pmf 44 -4
  product-tower status
  product-tower product-check
`);
}

if (!command || command === 'help' || command === '--help' || command === '-h') {
  showHelp();
  process.exit(0);
}

if (command === 'version' || command === '--version' || command === '-v') {
  console.log(require('../package.json').version);
  process.exit(0);
}

const scriptMap = {
  init: 'gate_checker.py',
  check: 'gate_checker.py',
  complete: 'gate_checker.py',
  pmf: 'gate_checker.py',
  status: 'gate_checker.py',
  assess: 'gate_checker.py',
  naming: 'gate_checker.py',
  'product-check': 'product-check.py',
  convert: 'convert.js'
};

if (scriptMap[command]) {
  const scriptArgs = args.slice(1);
  if (command === 'convert') {
    runNode(scriptMap[command], scriptArgs);
  } else {
    runPython(scriptMap[command], [process.cwd(), command, ...scriptArgs]);
  }
} else {
  console.error(`Unknown command: ${command}`);
  showHelp();
  process.exit(1);
}
