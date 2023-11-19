#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author by me@xiexianbin.cn
# function: list registry.k8s.io repos
# date 2023-11-19

##
# repos, ref https://explore.ggcr.dev/?repo=registry.k8s.io
# install gcrane, ref https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md
# go install github.com/google/go-containerregistry/cmd/gcrane@latest
##

import argparse
import json
import os
import subprocess
import time
from typing import Any, Dict, List, Tuple

CURRENT_PATH = os.getcwd()

parser = argparse.ArgumentParser(description='get registry.k8s.io images list')
parser.add_argument('--registry', '-r', help='get registry.k8s.io images list', action=argparse.BooleanOptionalAction,
                    default=False, type=bool)
args = parser.parse_args()


def bash(command: str, force=False, debug=False):
  args = ['bash', '-c', command]

  subp = subprocess.Popen(args, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
  stdout, stderr = subp.communicate()
  code = subp.poll()
  if debug:
    print(f"Run bash: {command}, ret is {code}, stderr is {stderr}")

  if not stdout and not stderr:
    print(f"Run bash: {command}, ret is {code}")

  if force:
    return code, stdout, stderr
  return code


class Gcrane(object):

  def __init__(self) -> None:
    pass

  @staticmethod
  def ls_contents(repo: str) -> (bool, Dict | Any):
    code, stdout, _ = bash(f'gcrane ls --json {repo} | jq .', force=True, debug=True)
    if code == 0:
      return True, json.loads(stdout)
    return False, stdout


class Registry(object):

  def __init__(self):
    self.registry_url = 'registry.k8s.io'
    self.out_path = os.path.join(CURRENT_PATH, '../registry.k8s.io/all-repos.txt')

  def ls_contents(self, repo: str) -> Tuple[bool, str | List[str]]:
    ok, result = Gcrane.ls_contents(f'{repo}')
    if ok is False:
      return False, result

    if len(result.get('tags', [])) > 0:
      return True, repo

    repos = []
    for child in result.get('child', []):
      print(f'  ==> parse f"{repo}/{child}" ...')
      try:
        ok, result_ = self.ls_contents(f'{repo}/{child}')
        if ok is False:
          print(f'ls tags for {repo}/{child}: {result_}')
          continue

        if isinstance(result_, str):
          repos.append(result_)
        elif isinstance(result_, list):
          for i in result_:
            repos.append(i)

        # sleep
        time.sleep(0.1)
      except Exception as e:
        repos.append(f'# {repo}/{child}')
        print(f'  == parse f"{repo}/{child}" e: {e}, skip ==')
    return True, repos

  def images(self):
    os.system(f'[ -f {self.out_path} ] && mv {self.out_path} {self.out_path}.{int(time.time())}')
    f = open(self.out_path, 'w')

    code, stdout, _ = bash('curl -sL "https://registry.k8s.io/v2/tags/list" | jq .', force=True, debug=True)
    if code != 0:
      raise Exception('list images err')
    repos = json.loads(stdout)
    for repo in repos.get('child', []):
      # repo = 'build-image'
      try:
        print(f'==> parse {repo} ...')
        ok, result = self.ls_contents(f'{self.registry_url}/{repo}')
        print(ok, result)
        if ok is False:
          f.write(f'# {self.registry_url}/{repo}\n')
          print(f'parse {repo}: {result}')
          continue

        if isinstance(result, str):
          f.write(f'{result}\n')
        elif isinstance(result, list):
          if len(result) > 0:
            f.write(f'# {self.registry_url}/{repo}\n')
            lines = "\n".join(result)
            f.write(f'{lines}\n')
          else:
            f.write(f'# {self.registry_url}/{repo}\n')

        f.flush()
        time.sleep(0.1)
      except Exception as e:
        print(f'== parse {repo} e: {e}, skip ==')
    f.close()


if __name__ == '__main__':
  try:
    Registry().images()
  except Exception as e:
    print(e)
    raise
