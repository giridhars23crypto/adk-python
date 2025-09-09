# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tool to execute shell commands."""

from __future__ import annotations

import subprocess
from typing import Any, Dict, List


async def run_command(command: List[str]) -> Dict[str, Any]:
  """Runs a shell command and captures its output.

  Args:
    command: Sequence of command arguments to execute.

  Returns:
    Dict with success flag, stdout, stderr, return code and optional error.
  """
  try:
    proc = subprocess.run(command, capture_output=True, text=True, check=False)
    return {
        "success": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "returncode": proc.returncode,
    }
  except Exception as exc:  # pylint: disable=broad-except
    return {"success": False, "error": str(exc)}
