# The Codex - Mastering Python's Import Mysteries

## Overview
The Codex explores Python's module and package import mechanics in Python 3.10+. Set in an alchemical laboratory theme, this subject covers package initialization (__init__.py), export controls (__all__ / namespace control), absolute versus relative import pathways, nested module access, and breaking circular import dependencies (ImportError: cannot import name ... from partially initialized module).

---

## Technical Requirements & Guidelines

* Language: Python 3.10+
* Code Style: Strict adherence to flake8 linter standards.
* Type Hinting: Mandatory across all functions (mypy compliant).
* Constraints:
  * Modifying sys.path is strictly forbidden.
  * Only imports of standard built-ins and custom project modules are permitted.
  * Built-in functions eval() and exec() are strictly forbidden.
  * All functions must be simple, concise, and return descriptive strings.

---

## Repository Structure

.
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── grimoire/
│   │   ├── __init__.py
│   │   ├── dark_spellbook.py
│   │   ├── dark_validator.py
│   │   ├── light_spellbook.py
│   │   └── light_validator.py
│   ├── potions.py
│   └── transmutation/
│       ├── __init__.py
│       └── recipes.py
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_alembic_2.py
├── ft_alembic_3.py
├── ft_alembic_4.py
├── ft_alembic_5.py
├── ft_distillation_0.py
├── ft_distillation_1.py
├── ft_transmutation_0.py
├── ft_transmutation_1.py
├── ft_transmutation_2.py
├── ft_kaboom_0.py
└── ft_kaboom_1.py

---

## Exercises Summary

| Part | Concept | Key Modules & Files | Description |
| :--- | :--- | :--- | :--- |
| Part I: The Alembic | Package Initialization & Exposure | ft_alembic_0.py .. 5.py, elements.py, alchemy/__init__.py | Distinguishes local modules from package submodules and controls package attribute exposure via __init__.py. |
| Part II: Distillation | Nested Imports & Package Aliases | ft_distillation_0.py, 1.py, alchemy/potions.py | Accesses nested elements across modules and exposes package-level aliases (e.g., alchemy.heal). |
| Part III: The Great Transmutation | Absolute vs. Relative Imports | ft_transmutation_0.py .. 2.py, alchemy/transmutation/recipes.py | Combines absolute (from alchemy.elements import ...) and explicit relative (from ..potions import ...) import pathways. |
| Part IV: Avoid the Explosion | Resolving Circular Dependencies | ft_kaboom_0.py, ft_kaboom_1.py, alchemy/grimoire/* | Demonstrates circular import errors in dark magic and resolves them using deferred imports in light magic. |

---

## Exercise Details

### Part I: The Alembic
* Concepts: Top-level scripts vs. package modules, import pkg vs. from pkg import mod, selective symbol exposure.
* Key Mechanics:
  * elements.py (root) defines create_fire() and create_water().
  * alchemy/elements.py defines create_earth() and create_air().
  * alchemy/__init__.py exposes create_air() directly at the alchemy package level while intentionally hiding create_earth() to demonstrate AttributeError handling on restricted imports.

### Part II: Distillation
* Concepts: Cross-module dependencies within packages, package-level function aliases.
* Key Mechanics:
  * alchemy/potions.py imports element creators from root elements.py and alchemy/elements.py to produce healing_potion() and strength_potion().
  * alchemy/__init__.py maps heal as a direct package-level alias for healing_potion.

### Part III: The Great Transmutation
* Concepts: Absolute imports vs. relative imports (., ..).
* Key Mechanics:
  * alchemy/transmutation/recipes.py implements lead_to_gold().
  * Demonstrates syntax rules:
    * Absolute: from alchemy.elements import create_air
    * Relative: from ..potions import strength_potion
  * Packaging alchemy/transmutation/__init__.py allows cascading package imports (import alchemy -> alchemy.transmutation.recipes).

### Part IV: Avoid the Explosion
* Concepts: Circular import loops, execution context, resolution techniques (deferred/function-level imports, interface restructuring).
* Key Mechanics:
  * Dark Magic (ft_kaboom_1.py): dark_spellbook.py and dark_validator.py perform top-level mutual imports, throwing ImportError: cannot import name ... from partially initialized module.
  * Light Magic (ft_kaboom_0.py): light_spellbook.py defers importing validate_ingredients inside the function scope or passes data cleanly, eliminating the circular loop.

---

## Testing & Quality Assurance

Verify strict compliance with formatting standards (flake8) and static typing (mypy):

# Check formatting standards
flake8 .

# Check static typing across functional scripts
mypy ft_alembic_0.py ft_alembic_1.py ft_alembic_2.py ft_alembic_3.py ft_alembic_5.py
mypy ft_distillation_0.py ft_distillation_1.py
mypy ft_transmutation_0.py ft_transmutation_1.py ft_transmutation_2.py
mypy ft_kaboom_0.py

(Note: ft_alembic_4.py and ft_kaboom_1.py are intentionally excluded from passing mypy/runtime checks, as they are specifically designed to demonstrate attribute errors and circular import exceptions).
