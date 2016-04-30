#!/usr/bin/env python3
"""
Run the script with: `python3 test.py > output`
"""
import shlex, subprocess
import os
import time
import re
import sys


env = os.environ.copy()


def communicate(p):
    return map(
        lambda x: x.decode('utf-8') if x is not None else None,
        p.communicate())


def get_random_options(num):
    args = shlex.split(
        'scripts/kconfig/randomsymbols arch/x86/Kconfig %i' % num)
    p = subprocess.Popen(args, env=env, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = communicate(p)
    return list(filter(None, out.split('\n')))


re_diagnosis = re.compile(r'\t\[(.*)\]\n')
re_slicing = re.compile(r'Slicing.*--(\d+)ms \(.*\n')
re_diagnoses = re.compile(r'Generating.* (\d+)ms \(.*\n')
re_iterations = re.compile(r'\.(\d+) iterations.*\n')
re_fixes = re.compile(r'Converting.*\.(\d+)ms \(.*\n')
re_execution = re.compile(r'Execution.*: (\d+) ms.*\n')
re_error = re.compile(r'It is not possible to change the config.')


def do_iteration(option_name):
    args = shlex.split(
        'java -cp scripts/kconfig/RangeFix.jar '
        'ca.uwaterloo.gsd.rangeFix.KconfigMain '
        'scripts/kconfig/2.6.32.70.exconfig .config %s YES' % option_name)
    p = subprocess.Popen(args, env=env, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    time_until_timeout = 5 * 60

    start = time.time()
    while time_until_timeout > 0:
        time_until_timeout -= 1
        try:
            p.wait(1)
        except subprocess.TimeoutExpired:
            continue
        end = time.time()
        out, err = communicate(p)
        print('\n## out ##')
        print(out)
        print('\n## err ##')
        print(err)
        if re_error.match(out) is not None:
            return 'error'
        diagnoses = [
            list(filter(None, d.split(', ',)))
            for d in re_diagnosis.findall(out)]
        total = int((end - start) * 1000)
        slicing = int(re_slicing.search(out).group(1))
        try:
            generating = int(re_diagnoses.search(out).group(1))
        except AttributeError:
            return 'exception'
        iterations = int(re_iterations.search(out).group(1))
        fixes = int(re_fixes.search(out).group(1))
        execution = int(re_execution.search(out).group(1))
        return total, slicing, generating, fixes, execution, iterations, \
               diagnoses
    p.kill()
    return 'timeout'


output = []
for i, option in enumerate(get_random_options(200), 1):
    print('### {} {} ###'.format(i, option))
    print(i, option, file=sys.stderr)
    sys.stdout.flush()
    data = do_iteration(option)
    output.append((option, data))

print('\n### OUTPUT ###\n')
print(output)

print('\n### RESULTS ###\n')
for row in output:
    option, data = row
    print(option)
    if isinstance(data, str):
        print(data)
    else:
        total, slicing, generating, fixes, execution, iterations, diagnoses \
            = data
        print(
            'Total: {} ms, Slicing: {} ms, Diagnoses: {} ms, Fixes: {} ms, '
            'Execution: {} ms, Iterations: {}'.format(
                total, slicing, generating, fixes, execution, iterations))
        for diagnosis in diagnoses:
            print(diagnosis)
    print()
