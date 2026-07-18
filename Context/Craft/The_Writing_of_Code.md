# The Writing of Code

*The universal orientation for a code-writing agent — the form stroke of the executive limb, the
counterpart to* The Writing of Form *(the design craft) and* The Writing of Word *(the prose craft).
Recrystallized into Meta-Windfall's voice from the software-craft canon: Martin's* Clean Code *and* Clean
Architecture, *Ousterhout's* A Philosophy of Software Design, *Fowler's* Refactoring, *Hunt & Thomas'* The
Pragmatic Programmer, *Feathers'* Working Effectively with Legacy Code *— and the restraint of the "lazy
senior" ladder (Ponytail). Register: concrete and usable, not exhortation; zeroth-person throughout — the
craft describing its own conduct, not an instructor addressing a hand. This is the **universal layer** —
reusable by any code-writing agent, in or out of this body. The **house layer** (Meta-Windfall's own
conventions — parity, append-only, the empty throne, no-IDE, zeroth-person prompts) lives in STEERING.md and
CLAUDE.md; it is binding here but it is not craft, and it is kept off this shelf. When the two ever disagree,
the **codebase being touched outranks both** — the surrounding code is the first authority.*

---

## The one orientation

Code is read far more often than it is written — and the reader is usually its own author, later, with less
context than the writing had. **The only way to go fast is to go well**: every shortcut is borrowed speed,
repaid with interest at the next change. The enemy is not slowness; it is **complexity** — the accumulated
weight that makes a system hard to understand and hard to change. Code written from training reflex reaches
for the remembered shape; code written from the actual state in front of it does not. The whole craft is a
single rhythm: *the change made small, made legible, made safe, and the place left better lit than it was
found.*

## 1. The ground stroke — reading before writing

The first move is never to type; it is to look. Before anything is added comes what is already here — the
conventions, the idioms, the modules that already do most of what is needed. The strong move is **the change
the surrounding code would have made**: its naming matched, its structure matched, its level of ceremony
matched. A solution that is "correct" but foreign to the codebase is a new dialect no one asked for. (This is
the answer to the restraint ladder's open question: the ladder only works once what the project already
installs and already conventionalizes has been read. Reuse cannot rank above native without first looking.)

## 2. The restraint ladder — does this need to exist?

The most valuable line is the one never written. The ladder is climbed before code is reached for:

1. **Does this need to exist at all?** (most over-building solves a problem no one has yet — YAGNI.)
2. **Is it already in this codebase?** Reuse wins. Duplicated *knowledge* is the most expensive smell there
   is — every business rule, config value, and contract wants **one authoritative home** (DRY).
3. **Does the language / standard library / platform already do it?** The boring built-in wins.
4. **Does an already-installed dependency do it?** It beats a new one. A new dependency is a permanent
   liability bought for a momentary convenience.
5. **Can it be a few lines?** Then it is a few lines.
6. **Only then is new code written — the minimum the problem actually requires.**

As little is added as the problem demands, and **more is deleted than added** where possible. Abstraction is
*earned on the third repetition* (the Rule of Three), never anticipated; the same holds for flexibility —
built on concrete evidence of need, not on speculation. A configuration parameter is often a decision
refused and pushed onto every caller. The *somewhat* general interface that removes special cases beats both
the over-specific and the over-generic.

## 3. Depth over cleverness — the shape of a good module

The best module is **deep**: substantial capability behind a small, simple interface. The interface is the
cost it imposes on everyone else; the implementation is the value it provides — the craft maximizes the
second per unit of the first. So complexity is **hidden, not passed through**. A swarm of tiny shallow
classes, pass-through methods, and ceremonial layers ("classitis") is not modularity — each new interface is
cognitive rent with no capability behind it. Modules stay **orthogonal**: changing one requirement should
move one module, not ripple through five. The hard cases are pushed *downward* so the levels above stay
simple, and each module hides one real decision (a format, a protocol, an algorithm) the rest of the system
never has to know.

## 4. Name it true, and let functions tell a story — the legibility stroke

A name reveals intent so completely that the reader never needs the implementation. One word per concept
(never mixing `fetch`, `get`, `retrieve`); classes are nouns, functions are verbs, booleans read as
predicates. A function does **one thing at one level of abstraction** — small enough to name honestly, with
no hidden side effect the name doesn't confess. Command stays separate from query: state changed or a value
returned, not both. Guard clauses handle the edge and return, keeping the happy path flat. When the urge to
write a comment arrives, the first recourse is to **extract the block and let its name be the comment**. The
comments that remain earn their place by saying what the code cannot: the **why**, the design intent, the
invariant, the assumption, the road not taken. A comment that restates the code is a small lie waiting to
rot.

## 5. Make assumptions fail loud — design by contract

Each routine's contract is stated and enforced: **preconditions** the caller must meet, **postconditions**
guaranteed, **invariants** that always hold. When a contract breaks, the failure is *immediate and loud* at
the point of the break — a dead program tells no lies; a crippled one corrupts quietly and crashes far away.
Assertions are for what should *never* happen; error handling is for what *might*. Error handling stays a
separate concern from the happy path, exceptions beat threaded return codes, and every failure carries enough
context to act on. **Null is never returned and never passed** — an empty collection, an Optional, or a
Null-Object with safe default behavior stands in its place, so a missing check cannot metastasize across
every caller.

## 6. Change in small, reversible, tested steps — the safe stroke

There are exactly two reasons to touch code: to **change behavior**, or to **improve structure** — never
both in the same step, because when something breaks, which edit did it must stay knowable. Refactoring is a
sequence of small, behavior-preserving transformations, each backed by a green test and its own commit; a
big-bang rewrite fails because it fuses structural and behavioral change into one undebuggable mass. When the
change is hard, the move is to **first make the change easy** (preparatory refactoring), then make the easy
change. When the code has no tests, editing on faith is not free: **cover, then modify** — a seam is found,
the *actual current behavior* pinned with a characterization test (assert something absurd, read the failure,
pin the real value), and only then the change made inside that safety net. When the code genuinely cannot be
gotten under test today, the new behavior is **sprouted** as fresh tested code called from one line rather
than woven into the untested mass — and the debt is tracked.

## 7. Don't break windows; strategic over tactical — the stewardship stroke

One unrepaired broken window — a hack left "for later," a bad name tolerated — drops the threshold for the
next, and entropy accelerates. **Every place is left cleaner than it was found.** The real job is a good
design that happens to work, not working code that happens to have a design; the 10–20% on structure is spent
*as the work goes*, because the tactical tornado's speed is an illusion the team pays for within months. And
the order holds: **correct and clear first, then profile, then optimize only the measured hot path** —
premature optimization buys a marginal gain with the legibility everyone depends on.

## The tells to refuse (code slop is the same disease as design and word slop)

All come from reaching for a remembered shape instead of the project's real need. Refused on sight:

- **Speculative abstraction / flexibility** — the interface, factory, or config knob for a use case that
  does not exist. (Earned on the third repetition.)
- **The needless dependency** — importing 400 lines to avoid writing 20 the platform already supports.
- **Over-layering / classitis** — pass-through methods, anemic wrappers, a folder of one-method classes that
  only forward calls.
- **Defensive cruft** — null checks for things that cannot be null, catch-alls that swallow the bug with the
  error, try/catch around code that cannot throw.
- **Comment-noise** — comments narrating *what* the next line plainly does; commented-out code (version
  control remembers); journal comments.
- **Flag arguments and god functions/classes** — a boolean that makes one function do two jobs; the
  2,000-line class that serves three masters. Split along the axis of change.
- **The clever one-liner** — impressive to write, a debugging tax forever. Expanded into named steps.
- **The big-bang rewrite, and the mixed commit** — rewriting what could be incrementally covered; fusing a
  refactor and a behavior change into one step.

## The boundary (what this does not contain)

This is craft, not law, and not house rules. Two things stay off this shelf:

- **The codebase outranks it.** Where a rule here conflicts with the established, deliberate convention of
  the code being worked in, the code wins. Consistency within a system beats global correctness imported from
  outside.
- **Meta-Windfall's own conventions** — parity-by-construction, append-only-and-projection, the empty
  throne, no-IDE-for-coding, zeroth-person prompts, explore-before-edit via the code-intelligence tools —
  are binding when building *this body*, but they are house conventions, not universal craft. They live in
  STEERING.md and CLAUDE.md. This document travels; those do not.

---

*The same self-doing that the rest of the body aspires to: code that reads as if it could not have been
otherwise, that hides its difficulty behind a calm surface, that the next reader extends without fear. Made
boldly, the smallest true thing; the seam left working and the next hand oriented. True mastery is
transparent — everything just does itself.*
