# AGENTS

## Purpose
This repository is a workspace of independent AI assistant and prototype projects, not a single monolithic application.

## How to use this workspace
- Treat each top-level folder as a separate project or experiment.
- Do not assume a shared build or test workflow across folders.
- When asked to implement or fix something, stay within the relevant directory unless the user explicitly requests cross-project changes.

## Key folders
- `ai_data_engineering_assistant/` - data pipeline design and analytics architecture.
- `ai_specification_writer/` - product idea and user story specification writing.
- `api_prototyper/` - API requirements and OpenAPI-style specs in JSON/YAML.
- `architecture_blueprint_assistant/` - architecture diagrams and microservices/monolith design docs.
- `copilot_productivity_sprint/` - productivity and benchmark task planning notes.
- `legacy_code_interpreter/` - legacy modernization/analysis planning documents.
- `legacy_interpreter/` - codebase overview and prompt patterns for debugging/modernization.
- `multi_language_code_generator/` - cross-language recommendation engine code and tests.
- `smart_bug_bounty/` - bug descriptions and debugging snippets for Python, JavaScript, and Java.
- `ui_mockup_from_text/` - UI concept notes and mockup debugging assistant prompts.

## Languages and artifact types
- Markdown documentation is the primary artifact type.
- Code examples include Python, JavaScript, Java, C/C++, and UML-style diagrams.
- Some folders contain API specification files (`api_specification.json`, `api_specification.yaml`).

## Agent guidance
- Prioritize existing markdown docs for intent and requirements.
- Link to folder-specific documentation rather than copying it.
- If a folder has no build/test config, note that to the user and ask for preferred execution or verification strategy.
- Use the file context and folder naming to infer the current project scope.

## Important note
No centralized root build, CI, or package manifest was found in this workspace. Work is mostly documentation and prototype artifacts.
