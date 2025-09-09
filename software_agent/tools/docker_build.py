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

"""Docker image build tool for the software agent sample."""

from __future__ import annotations

import subprocess
from typing import Any, Dict


async def docker_build(context_path: str, image_tag: str) -> Dict[str, Any]:
  """Builds a Docker image from the given context.

  Args:
    context_path: Directory used as the Docker build context.
    image_tag: Tag for the resulting image (for example, "my-app:latest").

  Returns:
    Dict containing success flag, stdout, stderr and return code.
  """
  try:
    proc = subprocess.run(
        ["docker", "build", "-t", image_tag, context_path],
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "success": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "returncode": proc.returncode,
    }
  except Exception as exc:  # pylint: disable=broad-except
    return {"success": False, "error": str(exc)}
