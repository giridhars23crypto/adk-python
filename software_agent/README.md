# Software Agent Sample

This sample demonstrates a sequential pipeline that generates Python code,
writes it to a file, creates a Dockerfile, then builds and runs the resulting
container.

## Agents

The pipeline is defined in `root_agent.yaml` and executes five sub-agents in
order:

1. `code_generator_agent.yaml` – produces Python source code.
2. `file_writer_agent.yaml` – saves the generated code to `generated_code.py`
   using the `write_files` tool.
3. `dockerfile_generator_agent.yaml` – writes a Dockerfile that exposes port
   8000 and runs `generated_code.py` on startup.
4. `docker_builder_agent.yaml` – builds a Docker image with the `docker_build`
   tool.
5. `docker_runner_agent.yaml` – runs the image via the `run_command` tool using
   the exposed port.

## Tools

Tools for this sample live in `software_agent/tools` and are referenced with the
`software_agent.tools` module path:

- `write_files`: writes contents to disk.
- `docker_build`: invokes `docker build`.
- `run_command`: executes arbitrary shell commands.

Run the pipeline with ADK's runner to see the generated code executed inside a
Docker container.
