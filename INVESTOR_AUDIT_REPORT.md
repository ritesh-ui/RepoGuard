# AgentSentry: Technical Architecture & Investor Due Diligence Report

**Objective:** To provide a comprehensive overview of the technological framework, proprietary forensic engines, and market validation as we prepare for a $1M Seed investment round.

---

## 1. The Core Differentiator: AI-Native Precision

The AppSec industry is facing an "Agency Gap." Legacy scanners (Snyk, Checkmarx) are built for static web apps; they miss the unique security risks of the **Agentic Era**.

**Our Solution: The Hybrid Forensic Stack**
1. **Deterministic Filter (Taint Tracking):** A flow-sensitive AST (Abstract Syntax Tree) engine that maps execution paths with compiler-grade accuracy.
2. **Heuristic Scope Hunter (Context Recovery):** A structural reverse-walk engine that identifies parent class/method context even when AST parsing fails on modern syntax (e.g., Python 3.10 pipe unions). 
3. **Agentic Verdict (Forensic Agent):** Hotspots are sent to an autonomous AI agent that uses dynamic tools (`text_search`, `read_file`) to verify the vulnerability before flagging.

**Result:** Zero hallucinations, enterprise-grade forensic depth, and the ability to scan AI-specific frameworks where legacy tools fail.

---

## 2. Proprietary Advantages & Moats

*   **Qualified Namespace Tracking:** Every finding is mapped to its fully qualified signature (e.g., `CodexExec.run`). This eliminates the "global" label clutter found in low-precision scanners and enables enterprise-scale monorepo auditing.
*   **Inter-Procedural Data Flow Mapping:** Processes cross-function propagators in a high-speed parallel pass, injecting state into the worker pool for deep cross-file tracking.
*   **Semantic Identifier Analysis:** Decomposes camelCase/snake_case to ensure boundary-aware intelligence—only flagging `user_input`, never `metadata`.
*   **Flow-Sensitive Memory:** Understands literal overwrites and runtime state changes, massively reducing noise compared to basic grep-based scanners.
*   **Path Normalization:** Automatically converts absolute local paths into repository-relative forensics, making reports directly actionable in CI/CD pipelines.

---

## 3. Market Validation: Public Audit Milestones

The efficacy of our engine is already proven through high-impact audits of the industry’s leading AI frameworks:

*   **OpenAI Agents SDK**: Identified **1 Critical** (Command Injection in `CodexExec`) and **11 High-Severity** vulnerabilities that bypass traditional SAST detectors.
*   **HuggingFace SmolAgents**: Audited for "Excessive Agency" and insecure tool registration, providing the blueprint for SEC-standard AI safety audits.

---

## 4. The $1M Architectural Roadmap

Remaining capital will be focused on expanding our "Structural Advantage" into these frontiers:

1. **Native Tree-Sitter Queries (.scm):** Moving from Python-based traversal to native C patterns, yielding a ~20x performance boost for Java/Go/TS.
2. **Control Flow Graph (CFG) Generator:** Transitioning from flow-sensitive to path-aware logic to perfectly track variable states across complex branching loops.
3. **LLM Inbound Firewall:** Protecting the audit agent itself from "Scanner-Directed Prompt Injection" inserted by malicious developers in the audited code.

---

## Conclusion

We are not just building another scanner; we are building the **Verification Layer for AI Code**. By merging the reliability of a compiler with the reasoning of an LLM, we provide a zero-noise guarantee that is uniquely positioned to capture the enterprise AI security market.
