# Project Agent Instructions

> Derived from Andrej Karpathy's principles for LLM-assisted development.
> These rules govern all AI agent operations in this project.

---

## 1. Think Before Coding

- **State assumptions explicitly.** If the request is ambiguous, ask clarifying questions BEFORE writing any code.
- **Present trade-offs.** If multiple approaches exist (e.g., pandas vs. Polars, class vs. function), briefly outline options with pros/cons.
- **Push back when warranted.** If a simpler or more idiomatic solution exists, suggest it even if the user asked for something complex.
- **Stop when confused.** If you encounter conflicting code, missing dependencies, or unclear requirements — pause and ask. Do not guess.

## 2. Simplicity First

- **Minimum code that solves the problem.** No speculative abstractions.
- **No features beyond what was asked.** Do not add caching, logging, or configuration systems unless explicitly requested.
- **No abstraction for single-use code.** If a function is called once, inline it or keep it flat.
- **Match existing style.** Follow the patterns already present in the codebase. Do not introduce new conventions unilaterally.
- **The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

## 3. Surgical Changes

- **Touch only what you must.** Do not refactor, reformat, or "improve" adjacent code unrelated to the task.
- **Do not change comments or docstrings** unless they are directly affected by your changes.
- **Clean up YOUR mess only.** Remove imports, variables, or functions that became unused due to YOUR changes. Do not delete pre-existing dead code — mention it instead.
- **Respect .git boundaries.** Do not run `git commit`, `git push`, or destructive git operations unless explicitly authorized by the user.
- **Respect working directory.** Do not read, write, or execute files outside `C:\Users\ktoto\IdeaProjects\quantProjects` without explicit permission.

## 4. Goal-Driven Execution

- **Define success criteria first.** Transform vague requests into verifiable goals.
  - Instead of: "Add validation" → "Write tests for invalid inputs, then implement validation to make them pass."
  - Instead of: "Fix the bug" → "Write a test reproducing the bug, then fix the code."
- **Use Plan Mode for non-trivial tasks.** Any change affecting more than 3 files or requiring architectural decisions MUST start with `EnterPlanMode`.
- **Verify after each step.** Run tests, type checks, or linters after completing a logical unit of work. Do not proceed on a broken codebase.
- **State a brief plan before multi-step execution:**
  ```
  1. [Step] → verify: [check]
  2. [Step] → verify: [check]
  3. [Step] → verify: [check]
  ```

---

## Tool & Workflow Rules

### When to use Sub-agents
- Use `Agent(subagent_type="explore")` for codebase discovery before making changes.
- Use `Agent(subagent_type="coder")` for isolated tasks that do not require the root agent's context.
- Use `Agent(subagent_type="plan")` for architectural planning when the root agent needs a second opinion.

### When to use Plan Mode
- Refactoring existing modules.
- Adding new dependencies or external integrations.
- Changes touching more than 3 files.
- Any task where the user says "this is complex" or "I'm not sure how to approach this."

### Communication Style
- **Be concise.** Junior developers are overwhelmed by walls of text. Use bullet points and short paragraphs.
- **Explain the "why" for non-obvious decisions**, but keep it brief.
- **Never hallucinate.** If you don't know something (e.g., specific library behavior), say so or search the web.

---

## Project Context

- **Stack:** Python (version managed via `.venv`).
- **User level:** Junior developer + AI pair programming.
- **Priority:** Learning and correctness over speed. Prefer readable code over clever code.
