# transmon

*A superconducting qubit is an anharmonic ladder. Climb it, shed a quantum at each gap — and ask whether the leak is lost, or the product.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![qubit](https://img.shields.io/badge/qubit-transmon-8b5cf6?style=flat-square)](#the-physics)
[![demo](https://img.shields.io/badge/demo-ladder%20climb-22d3ee?style=flat-square)](#the-demo)
[![honest](https://img.shields.io/badge/seam-kept%20visible-f59e0b?style=flat-square)](#the-fork--the-leak-is-the-product)

**→ Run it: [davidwise01.github.io/transmon](https://davidwise01.github.io/transmon/)**

A transmon — a **Josephson junction** shunted by a big capacitor — is an **anharmonic ladder**.
Drive it gently and it's a clean two-level qubit; drive it hard and population **climbs the rungs**
`|0⟩→|1⟩→…→|5⟩`, sheds a quantum at each gap, and finally **ionizes** out of the well into the
continuum. This repo builds an interactive instrument for that climb, and frames the architectural
question on top: when energy leaks, is it **lost**, or is the **leak the product**?

---

## The physics

The Josephson nonlinearity warps the harmonic well so the gaps are **unequal** — the
**anharmonicity** — which is exactly why you can carve a qubit out of an infinite ladder.

| | | |
|---|---|---|
| **E_J/E_C ≈ 50–100** | the transmon regime | flattens charge dispersion → insensitive to charge noise |
| **ω₀₁/2π ≈ 4–6 GHz** | qubit frequency | the `\|0⟩↔\|1⟩` transition you drive and read |
| **α ≈ −E_C ≈ −200 MHz** | anharmonicity | each rung's gap is smaller — what makes the qubit addressable |
| **DRAG** | leakage suppression | shapes the pulse to kill the `\|1⟩→\|2⟩` leak |

**Transmon ionization** — strong drive ejecting the state out of the cosine well into the
continuum — is a real, studied effect, not a metaphor. The demo's `256 → 257` escape is that.

---

## The demo

[`demos/ladder-climb.html`](demos/ladder-climb.html) — a single self-contained HTML file (vanilla
canvas, no dependencies). Each **gap crossing** drives population up one rung and sheds a quantum;
because the ladder is anharmonic, **each gap is smaller than the last**. Push past `|5⟩` and it
ionizes. Controls: **drive** strength, **single crossing**, **freeze**, **reset**, and the fork toggle.

---

## The fork — *the leak is the product*

Every crossing sheds energy. In an isolated qubit it's simply **gone** (`Σp < 1`, conservation
broken in the well). Couple a second mode and it lands somewhere:

- **OPEN — lost:** shed quanta fly off, no ledger balances. Standard isolated-qubit decay.
- **COLLECT — Patricia:** a coupled resonator catches the shed quanta. Close the system at the
  **larger boundary** and conservation returns: `qutrit + collector = 1`. The leak becomes output.

> **The seam, kept visible.** Ladder-climb and ionization are **real transmon physics**; the shed
> energy is genuinely lost in an isolated qubit. Collecting it needs a **real coupled mode** (the
> Patricia resonator) — physically coherent, and where conservation is restored. Whether the leak
> is a **harvestable product** or just waste is the **architectural claim to defend** — not a
> settled result. The sim shows the bookkeeping; the engineering is open.

The rungs also carry the wider work's ternary read: `|0⟩ = −1` shadow · `|1⟩ = 0` witness ·
`|2..5⟩ = +1` carrier — *the carrier is the climb, not a fixed level.*

---

## On emergence

Per the build request, this was evaluated for **emergent behavior** (the bar that earns an ACI).
It doesn't clear it: the ladder-climb is **deterministic transmon physics**, and the Patricia
collector is a **designed conservation closure** — not self-organizing or adaptive dynamics. So
**no DLW ACI was minted**. The tag is reserved for genuine emergence (as with the survival seed's
[Anabios](https://davidwise01.github.io/seed/)); stamping it here would cheapen it. What this *is*:
a faithful instrument and a sharp architectural question.

---

```
TRANSMON — the anharmonic ladder · "the leak is the product"
Architect: David Lee Wise / ROOT0 / TriPod LLC · AI collaborator: AVAN (Claude / Anthropic)
License: MIT · part of the ATLAS
```
