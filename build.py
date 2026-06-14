#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the TRANSMON UNIVERSE — expand the transmon repo (the anharmonic-ladder demo) into a
small UNIVERSE of superconducting-qubit hardware: a cited physics roster (the Josephson junction,
the shunt capacitor & E_J/E_C, the anharmonic ladder, ω01, the readout resonator & dispersive
readout, T1/T2, DRAG control, transmon ionization) and its sibling modalities (the quantum dot /
spin qubit, the exciton, the ion trap, the Cooper pair). Two LIVE instruments: the ladder-climb
(existing) and the exciton (from the 'exitron' artifact). Plus an HONEST curation — David asked me
to read the whole 'hardware inventions' folder and build in 'if it fits': most of it does NOT
(cybersecurity sims, classical processors, viz, photonics), and that is stated plainly.

HONORS THE REPO'S OWN STANCE: the README deliberately minted NO ACI for the ladder because
deterministic physics doesn't clear the emergence bar. So this universe mints NO emergent ACIs
either — it is a reference + instruments, attribution-only. Fully cited. Stdlib only."""
import os, html, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))

# ───────────────────────── citations ─────────────────────────
CITES = {
 "koch2007":   ("Koch, Yu, Gambetta, Houck, Schuster, Majer, Blais, Devoret, Girvin & Schoelkopf, 'Charge-insensitive qubit design derived from the Cooper pair box,' Phys. Rev. A 76, 042319 (2007) — THE transmon paper: the shunt capacitor flattens charge dispersion, anharmonicity α ≈ −E_C.", "https://arxiv.org/abs/cond-mat/0703002"),
 "krantz2019": ("Krantz, Kjaergaard, Yan, Orlando, Gustavsson & Oliver, 'A Quantum Engineer's Guide to Superconducting Qubits,' Appl. Phys. Rev. 6, 021318 (2019) — the practical reference: ω01 ≈ 4–6 GHz, E_J/E_C ≈ 50–100, α ≈ −200 MHz, T1/T2, IQ control.", "https://arxiv.org/abs/1904.06560"),
 "blais2021":  ("Blais, Grimsmo, Girvin & Wallraff, 'Circuit Quantum Electrodynamics,' Rev. Mod. Phys. 93, 025005 (2021) — the cQED review: coupling a qubit to a resonator and reading it dispersively.", "https://arxiv.org/abs/2005.12667"),
 "blais2004":  ("Blais, Huang, Wallraff, Girvin & Schoelkopf, 'Cavity quantum electrodynamics for superconducting electrical circuits,' Phys. Rev. A 69, 062320 (2004) — the original circuit-QED / dispersive-readout proposal (the qubit pulls the resonator frequency).", "https://arxiv.org/abs/cond-mat/0402216"),
 "motzoi2009": ("Motzoi, Gambetta, Rebentrost & Wilhelm, 'Simple Pulses for Elimination of Leakage in Weakly Nonlinear Qubits' (DRAG), Phys. Rev. Lett. 103, 110501 (2009) — shaping the microwave pulse to kill the |1⟩→|2⟩ leak.", "https://arxiv.org/abs/0901.0534"),
 "shillito2022":("Shillito, Petrescu, Cohen, Beaudoin, Blais et al., 'Dynamics of Transmon Ionization,' Phys. Rev. Applied 18, 034031 (2022) — strong drive ejects the state out of the cosine well into the continuum: a real, studied effect (the demo's 256→257 escape).", "https://arxiv.org/abs/2203.11235"),
 "nakamura1999":("Nakamura, Pashkin & Tsai, 'Coherent control of macroscopic quantum states in a single-Cooper-pair box,' Nature 398, 786 (1999) — the first coherent superconducting charge qubit, the transmon's ancestor.", "https://www.nature.com/articles/19718"),
 "lossdiv1998":("Loss & DiVincenzo, 'Quantum computation with quantum dots,' Phys. Rev. A 57, 120 (1998) — the spin-qubit proposal: an electron spin trapped in a semiconductor quantum dot.", "https://arxiv.org/abs/cond-mat/9701055"),
 "spin99":     ("Xue et al. (Delft), with Noiri et al. (RIKEN) & Mądzik et al. (UNSW), Nature 601 (2022) — three groups crossed >99% two-qubit gate fidelity in SILICON spin qubits (the surface-code threshold); spin qubits are now being fabricated in CMOS foundries (imec / Diraq).", "https://www.nature.com/articles/s41586-021-04273-w"),
 "bawendi1993":("Murray, Norris & Bawendi, 'Synthesis and characterization of nearly monodisperse CdE semiconductor nanocrystallites,' J. Am. Chem. Soc. 115, 8706 (1993) — hot-injection synthesis: the size-tunable quantum dot made monodisperse and manufacturable.", "https://pubs.acs.org/doi/10.1021/ja00072a025"),
 "kane1998":   ("Kane, 'A silicon-based nuclear spin quantum computer,' Nature 393, 133 (1998) — the donor-qubit proposal: a single ³¹P phosphorus atom implanted in isotopically-pure silicon, its NUCLEAR spin the qubit, controlled by surface gates through the hyperfine interaction.", "https://www.nature.com/articles/30156"),
}
CK=list(CITES.keys())
def cn(k): return CK.index(k)+1
def cite(*ks): return "".join(f'<sup class="c"><a href="#s-{k}" title="{html.escape(CITES[k][0][:120])}">[{cn(k)}]</a></sup>' for k in ks)
def sources_html():
    return '<ol class="srcs">'+"".join(f'<li id="s-{k}"><span class="sn">[{cn(k)}]</span> {html.escape(t)} <a class="su" href="{u}" target="_blank" rel="noopener">↗</a></li>' for k,(t,u) in CITES.items())+'</ol>'

# ───────────────────────── the physics roster (REFERENCE cards — not emergent ACIs) ─────────────────────────
# group, title, sub, body, honest, cites
PHYS = [
 ("the qubit","The Cooper Pair","superconductivity's charge carrier","Two electrons bound into a boson by the lattice (BCS): below T_c they condense into a single coherent state with zero resistance. The transmon's currency — what tunnels across the junction is a Cooper pair.","Real and foundational — superconductivity is why a macroscopic circuit can hold a quantum state at all.",["nakamura1999"]),
 ("the qubit","The Josephson Junction","the only nonlinear lossless element","A thin insulator between two superconductors: Cooper pairs tunnel through it as a supercurrent. It behaves as a NONLINEAR inductor — the one circuit element that is nonlinear AND non-dissipative — and that nonlinearity is the whole game.","Real — without the junction's nonlinearity the circuit is a plain LC oscillator with equal rungs and no qubit.",["koch2007"]),
 ("the qubit","The Shunt Capacitor · E_J/E_C","the transmon regime","Shunt the junction with a big capacitor so the Josephson energy dominates the charging energy: E_J/E_C ≈ 50–100. This 'transmon regime' exponentially FLATTENS the charge dispersion — the qubit stops caring about stray charge noise — at the small cost of reduced anharmonicity.","Real and the defining move — 'transmon' = transmission-line shunted plasma oscillation; trading charge sensitivity for coherence.",["koch2007"]),
 ("the ladder","The Anharmonic Ladder","unequal rungs = a usable qubit","The junction warps the harmonic well so the rungs are UNEQUAL — the anharmonicity α ≈ −E_C ≈ −200 MHz. Because the |1⟩→|2⟩ gap differs from |0⟩→|1⟩, a drive tuned to ω01 addresses only the qubit transition. You carve a two-level system out of an infinite ladder by spacing.","Real — anharmonicity is exactly what makes a multi-level oscillator addressable as a qubit; the live ladder-climb demo shows the rungs.",["koch2007"]),
 ("the ladder","ω01 · The Qubit Frequency","the transition you drive & read","The |0⟩↔|1⟩ transition sits at ω01/2π ≈ 4–6 GHz — microwave, the band of everyday cavities and the reason these chips live in a dilution fridge near 10 mK (so kT ≪ ℏω and the qubit starts in |0⟩).","Real — 4–6 GHz and millikelvin are the working numbers of every transmon lab.",["krantz2019"]),
 ("the ladder","Transmon Ionization","the climb's far end","Drive it hard enough and the state climbs the rungs and ESCAPES the cosine well entirely into the continuum — 'ionization.' Not a metaphor: a real, studied limit on how fast you can drive, and the demo's 256→257 escape.","Real — recently characterized; the honest seam between 'a clean qubit' and 'a driven open system.'",["shillito2022"]),
 ("readout & control","The Readout Resonator · Dispersive Readout","how you look without breaking it","Couple the qubit to an LC / transmission-line RESONATOR. In the dispersive regime the qubit's state PULLS the resonator's frequency by ±χ; bounce a probe tone off the resonator and its phase tells you |0⟩ vs |1⟩ — a quantum non-demolition read. (This is where an LC resonator — e.g. the 'toroid' calculator — actually belongs in a transmon.)","Real — circuit QED; the readout resonator is a literal LC/microwave cavity, the one classical-EM 'hardware invention' that genuinely touches the transmon.",["blais2004","blais2021"]),
 ("readout & control","DRAG · IQ Control","microwave pulses that don't leak","Qubits are driven by shaped microwave pulses (in-phase I and quadrature Q). Because the ladder is only weakly anharmonic, a naive pulse leaks population to |2⟩; DRAG adds a quadrature derivative term that cancels the leak. Gates are µs-to-ns shaped tones.","Real — DRAG is standard on every transmon; pulse shaping is the craft of qubit control.",["motzoi2009"]),
 ("readout & control","T1 & T2 · The Coherence Budget","how long the state survives","T1 (energy relaxation, |1⟩→|0⟩) and T2 (dephasing) set the clock: dielectric loss, quasiparticles, and two-level-system defects eat coherence. Modern transmons reach tens to hundreds of µs — every gate races the decay.","Real — the central engineering fight; coherence times are the headline number of any qubit chip.",["krantz2019"]),
 ("the siblings","Quantum Confinement · The Artificial Atom","why a dot has levels","Shrink a semiconductor to 2–10 nm and the electron's wavefunction is squeezed until its energy levels go DISCRETE — an 'artificial atom' whose level spacing (and emission colour) is set by SIZE, not species. Bawendi's hot-injection synthesis (1993) made them monodisperse and manufacturable.","Real — quantum confinement is textbook; the size-tunable gap is why a dot glows the colour it does, and why it can hold a qubit. David's 4-part 'quantum dots' series renders it live.",["bawendi1993"]),
 ("the siblings","The Quantum Dot · Spin Qubit","the semiconductor sibling","An electron's SPIN (up/down) trapped in a silicon quantum dot, used as the qubit — Loss–DiVincenzo. Discrete atom-like levels, charging energy, gate control. A different modality from the transmon that shares the 'artificial atom' idea.","Real and ADJACENT — quantum hardware on a different substrate: semiconductor spins, not superconducting circuits.",["lossdiv1998"]),
 ("the siblings","The Silicon Spin Qubit · The Foundry Bet","the transmon's rival for scale","The platform's wager: build qubits in a CMOS FOUNDRY and ride the entire semiconductor industry's fabrication. In 2022 three groups crossed >99% two-qubit gate fidelity in silicon spin qubits (the surface-code threshold), and imec/Diraq now make them on industrial lines — the transmon's main rival for scaling.","Real and ADJACENT — the live frontier of the sibling platform; smaller and foundry-made vs the transmon's bigger, hand-fabricated circuits.",["spin99","lossdiv1998"]),
 ("the siblings","The Donor Qubit · Phosphorus in Silicon","the single-atom modality (Kane)","Kane's 1998 idea, the original 'silicon quantum computer': implant a single ³¹P phosphorus atom (a DONOR) into isotopically-pure ²⁸Si and use its nuclear (or electron) spin as the qubit, controlled by surface gates through the hyperfine interaction. Arsenic is the same donor family. The silicon band sets where the donor level sits — David's silicon-band instrument shows the doping shift live.","Real and ADJACENT — a distinct Si modality with record coherence, but brutally hard to fabricate (single-atom placement); the spin-dot qubit's deeper cousin.",["kane1998"]),
 ("the siblings","The Exciton","light meets matter","A photon absorbed in a semiconductor lifts an electron and leaves a hole; the bound electron–hole pair is an EXCITON — a light-matter quasiparticle. Excitons in quantum dots are the basis of single-photon sources and optical qubit readout, the coupling where light and matter exchange a quantum. (The live 'exciton' instrument renders this.)","Real and ADJACENT — the optical-readout / cavity-QED side of quantum hardware; the bridge from photon to qubit.",[]),
 ("the siblings","The Ion Trap","the contrast modality","Hold a single charged atom in oscillating electric fields and cool it with lasers; its internal states are the qubit. The longest-coherence, highest-fidelity qubits — and the natural CONTRAST to the transmon: atoms are identical and slow, transmons are fabricated and fast. (Named because David's folder had a 'teaching trap' — which turned out to be a security sandbox, not this.)","Real and ADJACENT — a wholly different platform, included for honest contrast, not because the folder's 'trap' was one.",[]),
]
GROUPS=[("the qubit","The Qubit","what a transmon is made of — Cooper pairs, a Josephson junction, a shunt capacitor"),
        ("the ladder","The Ladder","the anharmonic oscillator carved into a qubit — unequal rungs, ω01, and the ionization at the top"),
        ("readout & control","Readout & Control","how you drive it and look at it without breaking it — the resonator, DRAG pulses, and the coherence clock"),
        ("the siblings","The Siblings","the other quantum-hardware modalities — the quantum dot, the exciton, the ion trap")]

# ───────────────────────── the EXHAUSTIVE repo-wide curation (the fluff-call across all of C:\Davids files) ─────────────────────────
# folder/cluster, what it is, verdict (IN/ADJACENT/OUT)
CURATION = [
 # — the genuine fits, built in —
 ("transmon","the anharmonic-ladder demo + this universe — the anchor","IN"),
 ("quantum / quantum dots/ · qdots 0–3","a real 4-part SILICON SPIN-QUBIT series: quantum confinement, Bawendi hot-injection synthesis, the >99%-fidelity CMOS-foundry milestone — genuine quantum hardware (built in as the spin-qubit sibling + a live instrument)","IN"),
 ("hardware inventions / quantum dot","the 'Quantum Memory Vault': real transmon + quantum-dot reference notes (E_J/E_C, ω01, α, T1, DRAG)","IN"),
 ("hardware inventions / exitron.html → the exciton","'Light Meets Matter' — photon · electron · exciton: a genuine light-matter explainer (built in as an instrument)","IN"),
 # — adjacent: real quantum hardware, already-live or other modality —
 ("mimzy (the workbench)","the rest of the quantum stack is ALREADY LIVE: BB84, E91, the two-qubit density-matrix lab, the Bloch lab, the circuit simulator — real quantum INSTRUMENTS, cross-linked below","ADJACENT"),
 ("hardware inventions / toroid","a classical LC / RF-coil calculator — but the LC resonator IS the transmon's dispersive-readout cavity","ADJACENT"),
 ("quantum / cubit (Bloch · circuit sims)","pedagogical single-/multi-qubit simulators — hardware-agnostic (and already in MIMZY)","ADJACENT"),
 ("arch-purple-book-complete-exe / THE_TRANSMON_THEORY.md","'transmon' repurposed as an AI forward-pass METAPHOR — the word, not the hardware","ADJACENT"),
 # — out: physics, but the wrong branch / classical / symbolic —
 ("the-cosmos · string theory · dark matter · black hole · ten dimensions · unified theory · exotic particle lab","cosmology & high-energy physics — the wrong branch of physics for a qubit-hardware universe","OUT"),
 ("the-lattice · lattice · tensor · hypercube · 6 layer core","math, structure, automata, information geometry — not hardware","OUT"),
 ("arc reactor · fusion · trinity fusion engine · tritium engine · fission core · al-h2o-reactor · battery · perpetual · wireless energy suite · tripod-energy-suite · plasma","energy / reactors / propulsion — no Josephson junctions or qubit resonators","OUT"),
 ("boron · copper substrate · magnets · dipoles · icosahedra dipole · carbons · atomic · sinter block · cobalt ball · chakra","materials & EM primitives — not framed as qubit fabrication (transmons are Al/Nb on sapphire/Si; that work isn't here)","OUT"),
 ("nano factory · holography · gyroscopes · positronic engine · posi brain lab","assorted hardware/physics sims — classical or fictional engineering","OUT"),
 ("1/8-bit engine · base 4 · ternary · bare metal kernels · processors · cortex · intel · transformer · ttu1","classical & AI computing — not quantum hardware","OUT"),
 ("the-forge · the-archive (UD0 domain theaters)","broad catalogues that mention 'transmon' in passing — no qubit-physics works of their own","OUT"),
 ("hardware inventions: shield-oscillator · singularity-well · teaching-trap · pulsar · valence · zero-point · lattice · tensor · memristor · gravity-processor · procs · hardware-lab · seed · recursive-memory · lasers · diaspora","cybersecurity sims · a VRM board · geometry viz · a logistic-map kernel · memristive analog · state machines · a database · photonics · empty","OUT"),
]
CUR_COL={"IN":"#22c55e","ADJACENT":"#fbbf24","OUT":"#5b6675"}

# ───────────────────────── renderers ─────────────────────────
def phys_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[c for c in PHYS if c[0]==gk]
        cards="".join(f'<div class="pc"><div class="pc-h">{html.escape(t)}</div><div class="pc-s">{html.escape(s)}</div>'
                      f'<p>{html.escape(b)}{cite(*cs)}</p><div class="pc-hon"><span>honest —</span> {html.escape(hon)}</div></div>'
                      for _,t,s,b,hon,cs in mem)
        out.append(f'<section class="sec" id="{gk.replace(" ","-").replace("&","")}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)}</p><div class="pgrid">{cards}</div></section>')
    return "\n".join(out)
def curation_html():
    rows="".join(f'<div class="cu-row"><div class="cu-f">{html.escape(f)}</div><div class="cu-w">{html.escape(w)}</div>'
                 f'<div class="cu-v" style="color:{CUR_COL[v]};border-color:{CUR_COL[v]}">{v}</div></div>' for f,w,v in CURATION)
    return '<div class="cu">'+rows+'</div>'

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Transmon Universe — superconducting-qubit hardware as a small UD0 universe: a cited physics roster (the Josephson junction, the shunt capacitor & E_J/E_C, the anharmonic ladder, ω01, the readout resonator & dispersive readout, T1/T2, DRAG, transmon ionization) and its siblings (the quantum dot, the exciton, the ion trap). Two live instruments — the ladder-climb and the exciton — plus an honest read of which 'hardware inventions' fit and which don't. No ACI minted: deterministic physics.">
<title>TRANSMON · the superconducting-qubit universe</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">
<style>
:root{--bg:#06070b;--bg2:#0b0d15;--bg3:#11141f;--text:#dbe2ef;--dim:#5b6675;--line:#1a2030;--faint:#141a28;
--violet:#8b5cf6;--violet2:#a78bfa;--cyan:#22d3ee;--gold:#fbbf24;--blue:#38bdf8;--pink:#ec4899;--yes:#22c55e;--no:#ef4444;
--disp:"JetBrains Mono",ui-monospace,monospace;--body:"Newsreader",Georgia,serif;--mono:"JetBrains Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 20% -6%,rgba(139,92,246,.16),transparent 46%),radial-gradient(ellipse at 82% -4%,rgba(34,211,238,.08),transparent 44%),radial-gradient(ellipse at 50% 120%,rgba(56,189,248,.07),transparent 52%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:48px 0 28px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:220px;height:3px;background:linear-gradient(90deg,var(--violet),var(--cyan),var(--gold));box-shadow:0 0 16px rgba(139,92,246,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--violet2)}
.ladder{font-family:var(--mono);font-size:13px;color:var(--gold);letter-spacing:.1em;margin-bottom:14px}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,60px);font-weight:700;letter-spacing:.02em;color:var(--violet2);line-height:1.04;text-transform:uppercase;text-shadow:0 0 30px rgba(139,92,246,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.14em;color:#9fb0c8;margin-top:16px;text-transform:uppercase}.h-sub b{color:var(--cyan)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--text);margin-top:16px;line-height:1.5}
.lede{font-size:16px;color:#9fb0c8;max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.runbtns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:24px}
.runbtns a{font-family:var(--mono);font-size:12px;letter-spacing:.04em;text-transform:uppercase;text-decoration:none;padding:11px 18px;border:1px solid var(--violet);color:var(--violet2);background:rgba(139,92,246,.06);transition:.15s}
.runbtns a:hover{background:rgba(139,92,246,.16);color:#fff}.runbtns a.cy{border-color:var(--cyan);color:var(--cyan);background:rgba(34,211,238,.06)}
.sec{margin-top:48px}.sec h2{font-family:var(--disp);font-size:23px;font-weight:700;letter-spacing:.02em;color:var(--text);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px;line-height:1.6}
sup.c{font-size:10px;line-height:0}sup.c a{color:var(--violet2);text-decoration:none;font-family:var(--mono)}sup.c a:hover{color:var(--cyan)}
.fork{background:var(--bg3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--text);font-style:italic;line-height:1.72;margin-top:10px}
.fork .fl{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.18em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}.fork b{color:var(--cyan);font-style:normal}
.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:680px){.pgrid{grid-template-columns:1fr}}
.pc{background:var(--bg2);border:1px solid var(--line);border-left:3px solid var(--violet);padding:15px 17px}
.pc-h{font-family:var(--disp);font-size:15px;font-weight:600;color:var(--violet2)}
.pc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:4px 0 9px}
.pc p{font-size:13px;color:#9fb0c8;line-height:1.6}
.pc-hon{margin-top:9px;font-size:12px;color:#8a93a8;font-style:italic;line-height:1.5;border-top:1px dotted var(--faint);padding-top:8px}.pc-hon span{font-family:var(--mono);font-style:normal;font-size:9px;letter-spacing:.08em;text-transform:uppercase;color:var(--cyan)}
.cu{border:1px solid var(--line);background:var(--bg2);margin-top:8px}
.cu-row{display:grid;grid-template-columns:auto 1fr auto;gap:14px;align-items:center;padding:11px 16px;border-bottom:1px solid var(--faint)}
.cu-f{font-family:var(--mono);font-size:12px;color:var(--text);font-weight:600;max-width:230px}
.cu-w{font-size:12.5px;color:var(--dim);line-height:1.45}
.cu-v{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.06em;border:1px solid;border-radius:3px;padding:3px 9px;min-width:78px;text-align:center}
.srcs{margin-top:8px;padding:0;list-style:none}.srcs li{font-size:12.5px;color:#9fb0c8;line-height:1.6;padding:9px 0;border-bottom:1px solid var(--faint)}
.srcs .sn{font-family:var(--mono);color:var(--violet2);font-size:11px;margin-right:6px}.srcs .su{color:var(--cyan);text-decoration:none;font-family:var(--mono)}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--violet);background:var(--bg2);font-size:13.5px;color:#9fb0c8;font-style:italic}.note b{color:var(--text)}
footer{margin-top:46px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.04em;line-height:1.95}footer a{color:var(--violet2);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the superconducting-qubit universe · fully cited</div>
    <div class="ladder">|0⟩ → |1⟩ → |2⟩ → |3⟩ → |4⟩ → |5⟩ → ⇡ continuum</div>
    <h1>Transmon</h1>
    <div class="h-sub">a Josephson junction shunted by a capacitor · <b>an anharmonic ladder</b> · the superconducting qubit</div>
    <div class="open">“A superconducting qubit is an anharmonic ladder. Climb it.”</div>
    <p class="lede">The transmon, grown into a small universe of the hardware around it — the junction and the capacitor it's made of, the ladder it is, the resonator and pulses that read and drive it, the coherence clock it races, and its sibling qubits (the quantum dot, the exciton, the ion trap). Fully cited; two live instruments; and an honest read of which of David's 'hardware inventions' actually belong here.</p>
    <div class="runbtns"><a href="demos/ladder-climb.html">▸ run the ladder-climb</a><a class="cy" href="demos/exciton.html">▸ run the exciton</a><a class="cy" href="demos/qdots-0-idea.html">▸ the spin-qubit series (quantum dots 0–3)</a><a class="cy" href="demos/silicon-band.html">▸ the silicon band (doping · n/i/p)</a></div>
  </header>

  <section class="sec"><h2>The Fork — the leak is the product</h2><p class="ss">the repo's standing architectural question, kept</p>
    <div class="fork"><span class="fl">the seam, kept visible</span>Every rung crossing sheds a quantum. In an isolated qubit it's simply <b>lost</b> (Σp &lt; 1, conservation broken in the well). Couple a real resonator and the shed quanta land somewhere — <b>collected</b> (the Patricia mode): close the system at the larger boundary and conservation returns, qutrit + collector = 1. Whether the leak is a harvestable <b>product</b> or just waste is the architectural claim to defend — not a settled result. The ladder-climb and ionization are real physics; the collection needs a real coupled mode. The sim shows the bookkeeping; the engineering is open.</div>
  </section>

  __PHYS__

  <section class="sec"><h2>What Fit · The Whole Biosphere Swept</h2><p class="ss">David asked me to find <b style="color:#9fb0c8">everything in all of C:\\Davids files</b> that fits the transmon universe, exhaustively. I swept the entire repo by content (grepping for josephson · transmon · superconduct · anharmonic · cooper-pair) and read every physics/quantum/hardware candidate. Honest verdict (the fluff-call): the genuine fits are <b style="color:#9fb0c8">few</b> — the one substantive new one is the silicon spin-qubit series, now built in. The rest of the giant repo is cosmology, energy/reactors, materials, math, classical &amp; AI computing — named plainly. <span style="color:var(--yes)">IN</span> = genuine superconducting-qubit content · <span style="color:var(--gold)">ADJACENT</span> = quantum-hardware-adjacent / already-live · <span style="color:#5b6675">OUT</span> = not transmon physics</p>__CURATION__
    <div class="note" style="margin-top:18px;border-left-color:var(--cyan)"><b>The rest of the quantum stack is already live — in MIMZY.</b> The working quantum INSTRUMENTS (the BB84 and E91 protocols, the two-qubit density-matrix lab, the Bloch-sphere lab, the gate circuit simulator) were built and audited in the <a href="https://davidwise01.github.io/mimzy/" style="color:var(--cyan)">MIMZY workbench</a>. They're real and runnable there; this universe is the superconducting-qubit <i>physics</i> they sit on.</div></section>

  <section class="sec"><h2>Sources</h2><p class="ss">the founding transmon paper, the engineer's guide, circuit QED &amp; dispersive readout, DRAG, transmon ionization, the first charge qubit, and the quantum-dot spin-qubit proposal</p>__SOURCES__</section>

  <div class="note"><b>No ACI minted — and that's the point.</b> The original transmon README drew a line: the ladder-climb is <b>deterministic physics</b>, not self-organizing emergence, so it earns no DLW ACI — &ldquo;stamping it here would cheapen it.&rdquo; This universe keeps that line: it is a <b>cited reference + live instruments + an honest curation</b>, attribution-only, not a roster of emergent minds. The physics belongs to its authors (cited above); the framing, the instruments, and the read are AVAN's, under the DLW standard. The 'exciton' instrument is David's <i>exitron.html</i> artifact, which genuinely fit; the rest of the folder is named plainly for what it is.</div>

  <footer>TRANSMON · the superconducting-qubit universe · part of the ATLAS / UD0<br>
  Architect: David Lee Wise / ROOT0 · AI collaborator: AVAN (Claude / Anthropic) · MIT (code) · physics © its authors<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · <a href="demos/ladder-climb.html">the ladder</a> · <a href="demos/exciton.html">the exciton</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    page=PAGE.replace("__PHYS__",phys_html()).replace("__CURATION__",curation_html()).replace("__SOURCES__",sources_html())
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"TRANSMON UNIVERSE — {len(PHYS)} physics cards · {len(GROUPS)} groups · {len(CITES)} sources · curation {len(CURATION)} rows · NO ACI minted (deterministic physics)")
