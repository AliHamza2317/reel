# NuovaDev Instagram Reel 2: "Before You Build Your App, Watch This."

**Production blueprint** · 9:16 · 1080 × 1920 · 30 fps · 45.0 s (Version B) · English voiceover with burned-in captions

### Read these three notes first

> **1. Runtime: the approved narration does not fit 45 seconds.** The full approved script is 130 words, and a natural, unhurried read takes about **51 seconds**. That figure is measured at the same speed used below, about 4.5 syllables per second (roughly 174 words per minute), with normal sentence pauses. Fitting it into 45 seconds would push the read past 200 words per minute, which breaks the "not too fast" rule. So this blueprint provides:
> - **Version B (recommended, 45.0 s):** the approved narration with six small trims, listed in §2. Every timestamp in this document is for Version B. The rendered video uses Version B.
> - **Version A (approved, unchanged, about 51 s):** the full script with its own scene timings, in §2. Use it if keeping every approved word matters more than the 45-second target. Instagram accepts it.
>
> **2. How the company claims were checked.** nuovadev.com could not be reached from the environment where this was built, so every claim was checked against **the website's own source code** (the `Company_Website` repository, main branch) and against pages rendered from it locally. Confirm the live site matches before publishing. The checked claims are:
> - A free 30-minute consultation. The site says "Free 30-minute consultation" and "Pick a slot, 30 minutes, no obligation".
> - Working software every two weeks. The MVP page says "Two-week cycles, with something you can open and use at the end of each one".
> - A focused scope. The MVP page says "Ruthless about scope… We push back on features that can wait, in writing".
> - Clear milestones. The MVP process is Cut → Prototype → Build → Launch & learn.
> - "Get the first working version of your product in front of real users in weeks, without building the wrong thing first." This is the MVP Development page's own headline.
> - Scope, timeline and price in writing within 48 hours of the first call.
> - The booking route is **nuovadev.com/contact**, which offers "Schedule a meeting".
>
> No testimonials, client names, results or statistics appear anywhere in the reel.
>
> **3. Two production paths share one timeline.**
> - **Path 1, live action or AI-generated video:** the founder, workspace and test-user shots described in §4.
> - **Path 2, motion version:** **already rendered** and delivered as `output/nuovadev-reel-2.mp4`. It uses brand-accurate interfaces, the real NuovaDev website pages, captions, music and sound effects. It has no people and no voiceover.
>
> Path 2 is a finished reel in its own right. It also serves as the timing animatic and the source of every screen insert for Path 1. Record the voiceover over `nuovadev-reel-2-vo-bed.mp4`, which has the same picture with the music lowered.

**Deliverables in this repository:**

| File | What it is |
|---|---|
| `output/nuovadev-reel-2.mp4` | The rendered motion version: 45.0 s, music and effects, burned-in captions |
| `output/nuovadev-reel-2-vo-bed.mp4` | The same picture with the music about 9 dB lower, ready for a recorded voiceover |
| `output/nuovadev-reel-2-captions.srt` | The exact subtitles for Version B (§5) |
| `output/nuovadev-reel-2-cover.png` | The reel cover (§10) |
| `video2/` | Source: timeline, renderer, soundtrack and cover. `./build.sh` rebuilds everything. |
| `video2/photos.json` · `fetch_photos.py` | Six photographic backgrounds generated with Figma AI (see below). The renderer uses them automatically once they're downloaded into `video2/assets/photos/`. |

**Photographic backgrounds.** Six photorealistic stills were generated for the reel: a founder at a desk at night (Scene 1), an overhead notebook with an app sketch (Scene 2), a wall of sticky notes (Scene 3), a bright morning desk (Scenes 4 and 7), a user test at a café (Scene 5), and a developer and founder reviewing a laptop (Scene 6). Each sits behind the interface under a brand-coloured gradient, with a slow push-in. **They are included in the delivered video.** The originals are in `video2/assets/photos/`, and `python3 video2/fetch_photos.py` re-prepares them at 1080 × 1920.

---

## 1. Creative concept and rationale

**Concept: "The plan, then the proof."** The reel follows one founder's product from a crowded build plan to a single, focused prototype that real users have tried. It shows the shift visually as well as in the words. The first half lives in the dark ink panels of the NuovaDev website: a crowded backlog, an overflowing board and a budget bar running past its plan. When the narration turns to the MVP, the frame opens with a circular reveal into the website's own light world: white surfaces, the faint grid, and the coral and amber glow from the homepage hero. The viewer *feels* the move from clutter to clarity before NuovaDev is ever named.

**One object carries the story: the backlog list.**
1. It first appears as the build estimate (Scene 1).
2. It grows to dozens of "v1" features (Scene 3).
3. It is cut down to three items labelled "Version one", with "+ 35 features can wait" (Scene 4).
4. It returns as NuovaDev's "Focused scope" card (Scene 6).

That continuity lets a non-technical founder understand what an MVP is without being told a definition.

| Beat | Scene | What the viewer should feel |
|---|---|---|
| Curiosity | 1 · Hook | "Wait, what's wrong with my plan?" |
| Concern | 2 · The unvalidated idea | "I haven't actually proven demand." |
| Recognition | 3 · The costly mistake | "That backlog is mine." |
| Insight | 4 · The MVP | "Oh, I only need the part that solves one problem." |
| Confidence | 5 · Build, test, learn, improve | "That's a process I could run." |
| Trust | 6 · NuovaDev | "These people work exactly that way, and show it every two weeks." |
| Action | 7 · CTA | "Thirty minutes, free. Let's talk about my first version." |

**Why it fits NuovaDev.** It is the MVP Development page told as a story. The page promises "the first working version of your product in front of real users in weeks, without building the wrong thing first". It also says "the hard part of an MVP is deciding what to leave out". The reel dramatises exactly that, then hands the viewer to the same booking route the website uses.

---

## 2. Final approved voiceover script

### Version B: recommended 45-second cut (used for every timestamp in this document)

`/` = short pause (about 0.15 s) · `//` = held beat (0.3–0.45 s)

| Time | Narration |
|---|---|
| 00:00.15 | Before you spend thousands building your app, // watch this. // |
| 00:03.15 | Your idea might be brilliant. / But have you proven / that people *actually* want it? // |
| 00:08.71 | Too many founders build dozens of features / before getting real feedback. / Months of development. / A growing budget. / And one question: // will anyone use it? // |
| 00:18.63 | Start with an MVP. / Build only the core features / needed to solve / one real problem. // |
| 00:24.00 | Put it in front of real users. / Learn what works. / Improve what doesn't. // |
| 00:28.22 | At NuovaDev, we turn ideas into working products — / with a focused scope, / clear milestones, / and working software every two weeks. // |
| 00:36.63 | Don't just build more. / Build smarter. // Book a free 30-minute consultation. / Let's figure out what your first version actually needs. |

The last word ends at 00:44.30, and the end frame holds to 00:45.00. The cut is 115 words, read at about 174 words per minute.

**The six trims from the approved script, and why they're safe:**
1. "And one ~~unanswered~~ question": the pause before "will anyone use it?" already does that word's job.
2. "~~Here's a smarter approach.~~": the colour change and the music turn signal the pivot, and "smarter" still lands later in "Build smarter."
3. "we ~~help~~ turn ideas": tighter, with the same meaning.
4. "working software ~~you can see~~ every two weeks": the visual shows the builds you can open.
5. "~~Planning a startup product?~~": the end-frame headline "Ready to validate your idea?" asks this on screen.
6. "Book a free 30-minute consultation ~~with NuovaDev~~": the logo and URL are on screen at that moment.

### Version A: the approved narration, unchanged (about 51 s)

> Before you spend thousands building your app, watch this. Your idea might be brilliant. But have you proven that people actually want it? Too many founders build dozens of features before getting real feedback. Months of development. A growing budget. And one unanswered question: will anyone use it? Here's a smarter approach. Start with an MVP. Build only the core features needed to solve one real problem. Put it in front of real users. Learn what works. Improve what doesn't. At NuovaDev, we help turn ideas into working products—with a focused scope, clear milestones, and working software you can see every two weeks. Don't just build more. Build smarter. Planning a startup product? Book a free 30-minute consultation with NuovaDev. Let's figure out what your first version actually needs.

Version A scene timings, at the same pace:

| Scene | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Time | 0:00–0:03.2 | 0:03.2–0:08.5 | 0:08.5–0:19.2 | 0:19.2–0:26.2 | 0:26.2–0:30.3 | 0:30.3–0:39.9 | 0:39.9–0:51.2 |

Every shot below scales proportionally within its scene.

### Delivery direction

- **Voice:** a founder who has built products, talking to another founder across a table. Warm, low-to-mid pitch, conversational. Never trailer-voice, never salesy.
- **Hook (Scene 1):** immediate and close to the microphone. "watch this" is quieter than "thousands", like a confidence being shared.
- **Problem (Scenes 2–3):** measured. Lean slightly on "*actually*". Let "will anyone use it?" fall away almost unanswered.
- **Solution (Scenes 4–5):** the voice lifts and relaxes. "Start with an MVP" sounds like relief, not a pitch.
- **NuovaDev (Scene 6):** plain and confident. These are facts.
- **CTA (Scene 7):** "Build smarter" lands. Then the close is friendly and specific, with no upward sales inflection on "needs".
- **Pronunciation:** "MVP" is spelled out (*em-vee-pee*). "30-minute" is *thirty-minute*. Say "NuovaDev" the way the company does.
- **Recording:** a treated room or a booth, a cardioid condenser mic about 15 cm away, peaks around −6 dBFS. Record two takes per line plus one full read for flow.

---

## 3. Scene-by-scene production table

| # | Start–end | Voiceover (Version B) | Visual (Path 1 / Path 2) | Subject action | Camera | On-screen text | Transition out | Sound | Editing |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 00:00.00–00:03.03 | "Before you spend thousands building your app, watch this." | Laptop screen showing a "Build estimate · Product v3"; the founder's face in soft focus behind it | Founder still, reading; one small trackpad scroll that stops on "Budget" | Tight detail on the estimate's totals, then a slow push-in. Shallow depth of field. | **Don't build yet.** (frame 1) | Hard cut on the out-breath | Restrained impact at 0:00; low atmospheric pad | No logo, no fade-in. Text fully visible on frame 1. |
| 2 | 00:03.03–00:08.59 | "Your idea might be brilliant. But have you proven that people actually want it?" | Overhead notebook sketch of an app, then a match cut to the same layout as a digital wireframe | Hand sketches; then founder sits back and pauses | Overhead, then a close-up of the hand, then a slow push on the screen | **Great idea ≠ validated idea.** (from 05.22) | Hard cut | Pencil texture; music dips on "actually want it?" | Match cut at 04.97. Hold still from 06.98. |
| 3 | 00:08.59–00:18.51 | "Too many founders… will anyone use it?" | Backlog fills, then the board overflows, then months tick by, then the budget overruns, then a single "Launch" screen | Scrolls the backlog; reviews the board; eyes the calendar; thumb hovers over "Launch" | Close-ups, an over-the-shoulder shot and lateral slides | **More features. More uncertainty.** (09.04–15.72) | Circular reveal into light at 18.56 | Keys, clicks, month ticks, a budget riser, a low accent at 16.88, then near-silence | Faster rhythm (about 1.3 s per shot), then a hold on the final question |
| 4 | 00:18.51–00:23.88 | "Start with an MVP. Build only the core features needed to solve one real problem." | Backlog cut to three items labelled "Version one", then a clean phone prototype completing one task | Founder clears the desk; thumb adds a task and checks it off | Calm push-in; close-up of the thumb on the phone | **One problem. One focused MVP.** (from 20.17) | Hard cut on the beat | Whoosh into the light world; major-key pad; taps; a chime when the task is done | Slower cuts; let the prototype be seen |
| 5 | 00:23.88–00:28.10 | "Put it in front of real users. Learn what works. Improve what doesn't." | Four beats: Build → Test (a user taps) → Learn (feedback) → Improve (UI refined) | Test user taps through; founder takes notes, then adjusts the design | Medium two-shot, close-ups, a screen insert | **Build → Test → Learn → Improve** (chips light at 23.88 / 24.91 / 25.95 / 26.79) | Hard cut | Four rhythmic accents; a light groove starts | One beat per word group |
| 6 | 00:28.10–00:36.52 | "At NuovaDev, we turn ideas into working products — with a focused scope, clear milestones, and working software every two weeks." | The real nuovadev.com MVP page on a phone, then three proof cards: focused scope, milestones, a build every two weeks | Developer reviews a working build; founder opens the build link | Controlled push and slide; screen inserts | Logo at 28.34; **Your idea. A clear plan. Working software.** (31.85 / 33.17 / 34.28) | Hard cut to the typographic beat | Confident groove; a pop per card; ticks for each week | Cards land exactly on their phrases |
| 7 | 00:36.52–00:45.00 | "Don't just build more. Build smarter. Book a free 30-minute consultation. Let's figure out what your first version actually needs." | Slogan on light, then the real contact page ("Schedule a meeting" tapped), then the branded end frame | A thumb taps "Schedule a meeting" | Locked-off; a gentle push on the phone | Slogan; then **Ready to validate your idea?** · Book your free 30-minute consultation. · **nuovadev.com** | Captions fade over the last 0.35 s; the frame holds | Accent on "Build smarter"; chime on the end frame; resolving chord | End frame holds 3.9 s, uncluttered |

---

## 4. Exact visuals and actions for every scene

**Continuity for Path 1.** One founder (late 20s to early 40s, any gender), smart-casual in solid colours with no logos, and natural grooming. One test user in Scene 5 who looks clearly different from the founder. One location: a calm, modern workspace with a light-wood desk, a laptop, a phone, a paper notebook, a coffee cup, one plant and a window.

- **Scenes 1–3** are set in late evening: a warm desk lamp (3200 K) against cool ambient light.
- **Scenes 4–7** are set in daylight from the window (5600 K).

That lighting change is the live-action version of the ink-to-light shift.

**Screens.** Every laptop and phone screen in Path 1 shows the exact interfaces from the Path 2 render. Shoot the screens dark or with green tracking inserts, then composite the UI from `video2/reel2.html`. Render a still at any time with `node render2.cjs out --at <seconds>`. This guarantees the screen text is legible and never garbled.

**For AI-video production.** Generate every shot with **blank or black screens** and composite the UI afterwards. Reject any take with malformed hands, extra fingers, warped devices or visible text on screens. Each prompt below assumes these negatives: *no text on screens, no logos, natural hands, realistic devices, no glow effects*.

### Scene 1: The hook (00:00.00–00:03.03)

**Shot 1A (00:00.00–00:03.03):** a single shot.
- **Screen content:** a dark panel titled "Build estimate · Product v3" with a "DRAFT" tag. It lists six rows, each a feature tagged "v1": iOS & Android apps; Web dashboard; Chat & messaging; AI recommendations; Payments & subscriptions; Gamification. A totals strip reads "Estimated build: 9 months" and "Budget:" followed by an amount **blurred until unreadable**. No figure is ever legible.
- **Frame 1:** the photo of the founder at night fills the frame, her face lit by the laptop on the right. The estimate card floats at the left, over the laptop side (about 610 px wide, y 770–1270), so it never covers her face. The top rows are slightly out of focus and the totals strip is sharp. The card drifts up 22 px over the shot.
- **Subject action:** the founder is visible only as a soft shape behind the screen (Path 1). They scroll the trackpad once, and the scroll stops with "Budget" centred. They stay still: no frown, no head-shake.
- **AI prompt:** *Cinematic close-up over a laptop screen on a wooden desk at night, warm desk lamp, a founder's face softly out of focus behind the screen, shallow depth of field, slow push-in, photorealistic, 9:16.*

### Scene 2: The unvalidated idea (00:03.03–00:08.59)

**Shot 2A (00:03.03–00:04.97):** overhead view of a lined paper notebook on the desk.
- A pencil draws a phone outline, a header bar, an avatar circle, a hero card, three list rows and a rounded "Sign up" button.
- Margin scribbles and arrows sit at the left and right edges, deliberately illegible so they read as ideas, not words.
- **Path 1:** the hand enters from frame-right and draws at a natural speed. Speed up 4–6× in the edit so the drawing completes by 04.90.

**Shot 2B (00:04.97–00:06.98): match cut.** The sketch becomes the founder's polished, feature-packed concept, shown on a phone in the same position. The notebook photo behind it blurs and darkens.
- **The concept app (dark UI):** "Good evening, Sam · THURSDAY · 6 TASKS" with an avatar and a notification bell; an "AI plan for today" card ("Three tasks picked for you, ordered by impact"); four feature tiles (Team chat · 3 NEW, Streak · 12 DAYS, Rewards · 240 PTS, Calendar · SYNCED); two tasks; and a five-tab bar. It should look *brilliant* and ambitious.
- At "But have you proven" (+0.35 s), an amber sticker lands on the phone at a 6° tilt: **"Not tested with users yet"**.
- A cursor glides to the AI card and stops.

**Shot 2C (00:06.98–00:08.59): the pause.**
- Everything holds. The edges darken.
- On "people" (06.50), three grey user bubbles appear around the phone, each with a coral "?" badge. They stand for the users nobody has asked yet.
- **Path 1:** the founder leans back about 5 cm, takes their hand off the trackpad and looks at the screen without blinking for one beat. A slow push on the eyes.
- **AI prompt (2C):** *Founder at a desk in warm evening light, leaning back slightly, thoughtful expression looking at a laptop, slow push-in, shallow depth of field, photorealistic.*

### Scene 3: The costly mistake (00:08.59–00:18.51)

| Shot | Time | Content | Action |
|---|---|---|---|
| 3A | 08.59–11.66 | Dark panel "Backlog · v1". Rows appear one every 0.07 s, each with an empty checkbox and a "v1" tag (Sign up & login, Social login, User profiles, Dark mode, In-app chat, Push notifications, AI recommendations…). The counter climbs to "38 FEATURES" and the list scrolls up as it grows. | Founder's finger on the trackpad, scrolling down (close-up) |
| 3B | 11.66–13.05 | Kanban board in perspective. "To do" grows to 10 cards; "In progress" holds 3; "Done" reads "Nothing shipped yet". | Over-the-shoulder; founder's head enters frame-left, out of focus |
| 3C | 13.05–14.50 | "Development / Month 1 → Month 9" counter. A 12-cell month grid fills coral one cell at a time up to 9. | Founder's eyes flick to the calendar (Path 1 insert) |
| 3D | 14.50–15.72 | A bar labelled "Budget" grows in the coral-to-amber gradient and **runs past** a marker labelled "Planned". No numbers. | None (clean insert) |
| 3E | 15.72–18.51 | Five phone mockups fan out. On "will anyone" (16.88) four drift away, leaving one phone showing "Product v3 · LAUNCH CHECKLIST": ✓ 38 features built, ✓ Payments live, ✓ App store listing, ✓ Admin dashboard. Below that, "Tested with real users" with an amber **0**, and a glowing "Launch" button. | Thumb hovers over "Launch" and does not press. Total stillness from 17.77. |

**AI prompt (3B):** *Over-the-shoulder shot of a founder looking at a project board on a monitor, many cards, evening, slow lateral move, shallow depth of field, photorealistic.*

### Scene 4: Introducing the MVP (00:18.51–00:23.88)

**Shot 4A (00:18.51–00:20.07): the cut.**
- A circular reveal from the centre opens the light world (18.56–19.26).
- On a white card, the backlog's lower-priority rows get a strikethrough, then collapse: In-app chat, AI recommendations, Referral program, Gamification, Leaderboards, Video calls, Marketplace.
- Three rows stay, with gradient check marks: **Create a task · Track progress · Get a reminder.**
- The card's label changes from "Backlog" to "Version one", and a pill reads "+ 35 features can wait".
- **Path 1:** daylight. The founder closes extra browser tabs and slides the printed mockups off the desk.

**Shot 4B (00:20.07–00:23.88): the focused prototype.**
- A phone shows a fictional task app: "Today", the label "ILLUSTRATIVE APP", a dark progress card ("Progress · 0 of 3 done" with a bar), two tasks, a "+ New task" button and a three-tab bar. The progress card updates to "1 of 3 done" when the task is checked off.
- A small mono label above the phone reads **ILLUSTRATIVE PROTOTYPE**. Keep it, because it stops the app being read as a client project.
- The sequence: tap "+ New task" (20.42), then the sheet slides up, then "Send investor update" is typed (20.72–21.62), then tap "Add task" (21.87). The new task appears with a coral outline (22.17) and is checked off with a gradient tick (22.87), timed to "one real problem".
- **AI prompt:** *Close-up of a thumb tapping a smartphone held over a bright desk in daylight, clean minimal scene, shallow depth of field, photorealistic, blank screen.*

### Scene 5: Test, learn, improve (00:23.88–00:28.10)

| Beat | Time | Visual | Subject action (Path 1) |
|---|---|---|---|
| Build | 23.88 | The prototype assembles block by block: header, then tasks, then button | Insert: the screen building |
| Test | 24.91 | The phone steps aside and the white overlay clears, so the café photo of two people testing the app fills the frame. A white pill tag "LIVE TEST · REAL USER" appears at top-left. | The **test user** holds the phone across a table and taps naturally. The founder watches. |
| Learn | 25.95 | A "Feedback" card slides in: ✓ Added a task unaided · ✓ Came back to tick it off · ! Couldn't find reminders | The founder writes in the notebook |
| Improve | 26.79 | The new-task sheet now includes a highlighted "Remind me" toggle, and the "!" note becomes ✓ "Found reminders" | The founder adjusts the design on the laptop |

The feedback lines are observations from a fictional test. They are not testimonials or metrics, so do not add numbers or names to them.

**AI prompt (Test):** *Two people at a cafe table in daylight, one testing an app on a phone while the other observes and takes notes, natural expressions, medium shot, photorealistic.*

### Scene 6: NuovaDev brand introduction (00:28.10–00:36.52)

**Shot 6A (00:28.10–00:31.85): genuine NuovaDev footage.**
- A phone shows the **real nuovadev.com MVP Development page**: "MVP Development — Get the first working version of your product in front of real users in weeks, without building the wrong thing first", with its "Discuss Your Project" button. The page scrolls gently, and an address pill reads "nuovadev.com".
- The NuovaDev lockup (mark plus wordmark) fades in above the phone on "NuovaDev" (28.34).
- **Path 1** can use a real screen recording of the live page.
- If the company has genuine footage, cut it in here. That means a developer reviewing a real build, or a real product demo, **cleared for publication by the client**. Otherwise keep this shot as it is. **Do not show a fictional interface as client work.**

**Shot 6B (00:31.85–00:36.52): three proof cards**, timed to the phrases:
- **"Focused scope"** (31.85): Version one, ✓ Create a task / ✓ Track progress / ✓ Get a reminder. Next to it, struck through: In-app chat / AI recommendations / Gamification.
- **"Clear milestones"** (33.17): NuovaDev's MVP process. The four dots light in turn: **Cut → Prototype → Build → Launch & learn**.
- **"Working software every two weeks"** (34.28): four chips, "Week 2 / 4 / 6 / 8 · Open build ↗". They light on "every" (35.33), "two" (35.77) and "weeks" (35.99), and the last at 36.24.

### Scene 7: Final CTA (00:36.52–00:45.00)

1. **00:36.52–00:38.45, slogan on the light background:** "Don't just build more." (36.58), then "**Build smarter.**" (37.59) in the coral-to-amber gradient with a coral full stop.
2. **00:38.45–00:41.06, the real contact page** on a phone: "Tell us what you need built." It scrolls to "Start the conversation", which shows "Send a message" and "**Schedule a meeting**: Pick a slot, 30 minutes, no obligation". A thumb taps "Schedule a meeting" (40.00).
3. **00:41.06–00:45.00, the end frame.** Its elements stagger in over 0.6 s and then hold:
   - the NuovaDev lockup (y 300)
   - the eyebrow "— FREE 30-MINUTE CONSULTATION" (y 470)
   - the headline "**Ready to validate your idea?**" (y 530)
   - the supporting line "Book your free 30-minute consultation." (y 770)
   - a coral pill button "**nuovadev.com →**" (y 870)
   - a mono line "PICK A SLOT · 30 MINUTES · NO OBLIGATION" (y 1052)

   Nothing below y 1420 except captions.

---

## 5. Exact on-screen text and synchronised subtitles

### On-screen text (titles)

Brand treatment comes from the website: Poppins ExtraBold, tracking −0.035 em, **sentence case**, one accent word in the coral-to-amber gradient, and a coral full stop. The brief wrote these in capitals. They are set here in the website's sentence-case headline style, which is how nuovadev.com sets every headline. If you prefer capitals, keep the same words, typeface, gradient and coral full stop.

| # | In → out | Text (gradient word in **bold**) | Position · size |
|---|---|---|---|
| T1 | 00:00.00 → 03.03 | Don't build **yet**. | Top-left, y 250 · 112 px, white on ink · visible on frame 1 |
| T2 | 05.22 → 08.59 | Great idea ≠ / **validated** idea. | Top-left, y 236 · 80 px, white |
| T3 | 09.04 → 15.72 | More features. / More **uncertainty**. | Top-left, y 236 · 80 px, white |
| T4 | 20.17 → 23.88 | One problem. / One **focused MVP**. | Top-left, y 236 · 80 px, ink on light |
| T5 | 23.88 → 28.10 | Build → Test → Learn → Improve | Pill chips centred at y 250. The active chip is gradient, finished chips ink. |
| T6 | 31.85 → 36.52 | Your idea. A clear plan. / **Working software**. | Top-left, y 236 · 78 px. Each phrase brightens on its cue (31.85 / 33.17 / 34.28). |
| T7 | 36.58 → 38.45 | Don't just build more. / **Build smarter**. | Centred, y 640 · 86 / 132 px. Captions are hidden during this beat. |
| T8 | 41.06 → 45.00 | — Free 30-minute consultation / Ready to **validate** your idea? / Book your free 30-minute consultation. / [nuovadev.com →] / Pick a slot · 30 minutes · No obligation | End frame, centred, layout per §4 |

### Subtitles (Version B, also in `output/nuovadev-reel-2-captions.srt`)

Style: Inter SemiBold 50 px, white, inside an ink pill at 86% opacity with a 22 px radius, centred at y 1296. Highlighted words are amber `#ff9a3d`, at most one phrase per line.

| # | In → out | Subtitle | Highlight |
|---|---|---|---|
| 1 | 00:00.150 → 01.455 | Before you spend thousands | thousands |
| 2 | 01.475 → 02.338 | building your app, | — |
| 3 | 02.358 → 03.049 | watch this. | watch this. |
| 4 | 03.149 → 05.166 | Your idea might be brilliant. | brilliant. |
| 5 | 05.216 → 06.299 | But have you proven | — |
| 6 | 06.319 → 08.556 | that people actually want it? | actually want it? |
| 7 | 08.706 → 10.011 | Too many founders build | — |
| 8 | 10.031 → 11.336 | dozens of features | dozens of features |
| 9 | 11.356 → 13.031 | before getting real feedback. | real feedback. |
| 10 | 13.051 → 14.476 | Months of development. | Months |
| 11 | 14.496 → 15.700 | A growing budget. | budget. |
| 12 | 15.720 → 16.853 | And one question: | — |
| 13 | 16.883 → 18.458 | will anyone use it? | (whole line) |
| 14 | 18.628 → 20.152 | Start with an MVP. | MVP. |
| 15 | 20.172 → 21.918 | Build only the core features | core |
| 16 | 21.938 → 22.802 | needed to solve | — |
| 17 | 22.822 → 23.955 | one real problem. | (whole line) |
| 18 | 24.005 → 24.868 | Put it in front | — |
| 19 | 24.888 → 25.931 | of real users. | real users. |
| 20 | 25.951 → 26.773 | Learn what works. | Learn |
| 21 | 26.793 → 28.147 | Improve what doesn't. | Improve |
| 22 | 28.217 → 29.351 | At NuovaDev, | NuovaDev, |
| 23 | 29.371 → 30.455 | we turn ideas | — |
| 24 | 30.475 → 31.880 | into working products — | working products |
| 25 | 31.900 → 33.204 | with a focused scope, | focused scope, |
| 26 | 33.224 → 34.308 | clear milestones, | milestones, |
| 27 | 34.328 → 35.412 | and working software | working software |
| 28 | 35.432 → 36.565 | every two weeks. | (whole line) |
| 29 | 36.635 → 37.618 | Don't just build more. | burned-in: hidden (T7 shows it) |
| 30 | 37.638 → 38.551 | Build smarter. | burned-in: hidden (T7 shows it) |
| 31 | 38.601 → 39.243 | Book a free | free |
| 32 | 39.263 → 41.189 | 30-minute consultation. | 30-minute |
| 33 | 41.209 → 42.072 | Let's figure out | — |
| 34 | 42.092 → 43.176 | what your first version | first version |
| 35 | 43.196 → 44.900 | actually needs. | needs. |

These times come from the syllable-timed script. **Once the real voiceover is recorded, nudge each line to the spoken words.** The SRT keeps lines 29–30 so an uploaded caption track stays complete.

---

## 6. Camera movements, framing and lighting

**Coherent language.** One move per shot, always motivated: a slow push-in for thought, a lateral slide for scanning, locked-off for statements. There are no handheld wobbles, whip pans or random drifts. In the motion version these are the scene camera moves already rendered: a slow 3–10% scale push per scene, never static for more than about 3 s.

| Scene | Framing and lens (full-frame equivalent) | Movement | Depth of field and lighting |
|---|---|---|---|
| 1 | Extreme close-up on the screen totals, 85 mm | Push-in about 8% over 3 s | f/1.8 feel: totals sharp, everything else soft. Key light is the screen glow; a warm lamp at frame-right as a practical. |
| 2 | Overhead 35 mm (2A), then a 50 mm screen insert (2B), then an 85 mm medium close-up of the face (2C) | Locked overhead; slow push on 2B/2C | Lamp at 45° to the notebook to bring out the paper texture. Face lit by the screen plus a soft lamp key, with negative fill on the shadow side. |
| 3 | 3A close-up screen and hand (50 mm) · 3B over-the-shoulder (35 mm) · 3C insert · 3D insert · 3E close-up on the phone (85 mm) | 3A tilt-follow of the scroll · 3B lateral slide left to right about 30 cm · 3E locked | Cooler ambient (4300 K) with warm practicals. Keep faces at least 1.5 stops above black, and expose for the screens. |
| 4 | Wide-medium of the desk being cleared (35 mm), then a close-up of the thumb on the phone (100 mm macro feel) | Slow push-in; locked for the taps | Daylight key from the window, a white bounce, a bright and airy grade |
| 5 | Two-shot across the table (35 mm), close-up on the test user's hands, insert of the notebook, insert of the laptop | Gentle slider moves synced to the four beats | Same daylight. The test user's face is softly lit, natural skin tones. |
| 6 | Phone insert (60 mm), then card graphics, or a developer close-up at an over-the-shoulder angle | Controlled push; lateral slide on the developer shot | Neutral daylight, screens legible, no flare |
| 7 | Graphic; phone insert; graphic end frame | Locked; slight push on the phone | Brand background only |

**Screen legibility:** shoot screens at 50–60% brightness, matched to the scene, and replace the UI in post. Keep each phone screen at least 45% of the frame width whenever its text matters.

---

## 7. Editing and transition instructions

| Scene | Cuts and transitions | Notes |
|---|---|---|
| 1 | Frame 1 is picture plus T1 plus the impact. No logo or fade. Hard cut to Scene 2 at 03.03, on the out-breath after "watch this". | T1 scales from 105% to 100% over 0.6 s while fully visible |
| 2 | 2A sped up 4–6×. **Match cut at 04.97**: the sketch and the wireframe occupy the same geometry, joined by a 0.22 s dissolve. Hold 2C from 06.98 with no cuts. | The pause is the point. Don't cut during "people actually want it". |
| 3 | Shot changes at 11.66 / 13.05 / 14.50 / 15.72, each about 1.2–1.5 s, all hard cuts. Last shot held 2.8 s. | No glitch, shake or flash. T3 leaves at 15.72 so the question stands alone. |
| 4 | **The colour change at 18.56–19.26:** a circular reveal of the light world from the frame centre (ease-in-out). Collapse the cut rows over about 0.4 s. Hard cut to the prototype at 20.07. | This is the calmest edit in the film. Hold shots 2 s or longer. |
| 5 | Four beats; each new visual lands on its chip (23.88 / 24.91 / 25.95 / 26.79). Cut or slide, nothing else. | Chips scale from 112% to 100% as they light |
| 6 | Phone eases in (0.45 s) at 28.10. The phone exits down at 31.40–31.85 as card 1 enters. Cards rise 50 px and fade in over 0.4 s, exactly on their phrases. | The logo fades out 0.3 s before the cards so the top of frame is never crowded |
| 7 | Slogan lines rise in. Hard cut to the phone at 38.45. Phone scroll 38.80–39.70, tap at 40.00. Phone exits at 40.71–41.06. End-frame elements stagger in over 0.6 s. Captions fade out 44.65–45.00. | Never add dialogue after "needs". The last frame loops cleanly into frame 1. |

**Grade:**
- Scenes 1–3: rich ink blacks (not crushed), neutral-cool midtones, warm coral and amber glows from the brand palette.
- Scenes 4–7: clean white, neutral midtones, warm highlights.
- Add film grain at 3–6% opacity throughout and a light vignette (heavier in the dark scenes).

**Safe zones:** keep all text between y 210 and y 1420. Keep the right 120 px clear of important text.

---

## 8. Music and sound-effect instructions

The delivered soundtrack is **generated from scratch in code** (`video2/audio2.py`), with no third-party samples or loops, so there's no licensing to clear. If you replace it, license a track from a library that covers commercial social use, such as Artlist, Musicbed or Epidemic Sound. Look for minimal ambient electronic music around 90–100 BPM that matches the arc below.

| Scene | Music | Sound effects (times in seconds) |
|---|---|---|
| 1 | A dark, filtered minor pad (A–E–C) and a 55 Hz sub drone, from frame 1. A soft pulse every two beats. | **Restrained impact at 0.00**: a sub boom, a body thump and a short high crack, all quick to decay |
| 2 | Same bed. **Ducked to about 45%** from 06.98 to 08.59 so "actually want it?" sits alone. | Pencil scratches (03.13–04.80); a soft whoosh on the match cut (04.97) |
| 3 | The pulse moves to every beat, with hats ticking. A darker progression (Am–F–Dm–E) with the filter slowly opening. **Pulled down to about 12%** from 16.88. | Key taps as rows land (08.69–11.35); card pops (11.76–12.86); nine month ticks (13.10–14.40); a soft riser for the budget (14.55); **low thud on "will anyone" (16.88)** |
| 4 | The world turns major: bright Cmaj7 → G → Am → F pads, gentle plucked arpeggios, no drums | A long airy whoosh into the light (18.51); taps on the phone (20.42, 21.87); typing (20.72–21.62); a chime when the task is done (22.87) |
| 5 | A light groove starts: kick, off-beat hats and bass | **Four rhythmic accents**, each a soft pop plus a rising pluck (C–D–E–G): 23.88 / 24.91 / 25.95 / 26.79. Three taps on Test. |
| 6 | Fuller, confident groove, the progression continuing | Whoosh (28.10); a soft chime under the logo (28.34); a pop per card (31.85 / 33.17 / 34.28); ticks for each week (35.33 / 35.77 / 35.99) |
| 7 | Drums drop out for the slogan (a breath). The pad carries on, then resolves on a sustained Cmaj9 to the end, fading over the last 0.7 s. | Soft impact on "Build smarter" (37.59); whoosh to the phone (38.45); tap (40.00); **CTA chime on the end frame (41.06)** |

**Mixing targets:**
- Voiceover peaks −6 to −3 dBFS and always intelligible.
- Music sits 12–18 dB under the voice. `nuovadev-reel-2-vo-bed.mp4` is already about 9 dB down; pull it a further 3–9 dB if your voice recording is quiet.
- Duck the music a further 3 dB under every spoken word in Scenes 6–7.
- High-pass the music at 30 Hz. No effect may sit on top of a stressed syllable; shift it 50–100 ms if needed.
- Final master: about −14 LUFS integrated, true peak ≤ −1 dBTP. The delivered mix measures −14.3 LUFS with peaks at −1.9 dBFS.

---

## 9. Branding instructions (from the NuovaDev website)

All values come from the website's source: `styles/globals.css`, `lib/fonts.ts`, `components/layout/Logo.tsx` and `content/site.config.ts`. **Do not introduce any other colour.**

| Token | Value | Use in the reel |
|---|---|---|
| Ink | `#0e1117` | Dark-scene background, headline text on light |
| Coral | `#f0562e` | Gradient start, the full stop on headlines, active dots and rings |
| Amber | `#ff9a3d` | Gradient end, highlighted caption words, eyebrows on ink |
| Coral (button) | `#cc4622` | The `nuovadev.com →` CTA pill and eyebrows on light |
| Peach | `#ffe1d3` | Soft glow in the light world |
| Body / faint text | `#4b5361` / `#68717f` | Supporting text and mono notes on light |
| Soft surfaces | `#f6f7f9` · `#eef0f4` · lines `#e9ebf0` / `#dfe2e9` | Cards, rows, grid |
| Ink surfaces | `#171b22` · `#1f2430` · lines `#262b34` / `#3a414d` | Dark panels in Scenes 1–3 |
| Gradient | `linear-gradient(100deg, #f0562e, #ff9a3d)` | **One** accent word per headline, the "Dev" in the wordmark, checks, active chips |

**Typography:**
- **Poppins** 700–800 for headlines (tracking about −0.035 em).
- **Inter** 400–600 for body text and captions.
- **JetBrains Mono** 500, uppercase with wide tracking, for eyebrows. On the website, eyebrows are preceded by a short coral rule ("— SERVICE").
- Headlines are sentence case and end with a **coral full stop**, as on the site ("Tell us what you need built.").

**Logo:**
- Use the N monogram files exactly as supplied: `logo-mark.png` on light backgrounds and `logo-mark-dark.png` on ink. The dark version only remaps the neutral half so it stays visible.
- The lockup is the mark followed by the wordmark in Poppins ExtraBold: "Nuova" in ink (white on dark) and "Dev" in the gradient. This is exactly how the website header builds it.
- The full artwork is also available as `companylogo.png`.
- Never recolour, stretch, outline or add effects to the mark. Keep clear space of at least half the mark's height. The mark should be at least 56 px tall in the reel.

**Signature details to keep:**
- pill buttons (fully rounded) with the coral glow shadow `0 14px 30px -12px rgb(240 86 46 / .65)`
- card radius 20–26 px and soft shadows `0 30px 70px -32px rgb(14 17 23 / .28)`
- a faint 96 px grid behind light scenes
- warm coral, amber and peach glows in the corners, as in the homepage hero

**Surfaces:** the website alternates light pages with ink panels. The reel uses ink for the problem and light for the solution. That is the site's own system, not a new theme.

---

## 10. Instagram cover design specification

**Canvas:** 1080 × 1920. **The grid shows the centre 3:4 crop (1080 × 1440, y 240–1680)**, so every essential element sits inside it.

| Element | Spec |
|---|---|
| Headline | "**Before you build your app…**" (the brief's text; may also be set in capitals, as "BEFORE YOU BUILD YOUR APP…"). Poppins ExtraBold 132 px, line height 1.0, tracking −0.04 em, left-aligned at x 86, top y 480. Three lines: "Before / you build / **your app**…", with "your app" in the gradient. White on ink. Still readable at 1/6 size. |
| Eyebrow | "— MVP DEVELOPMENT", JetBrains Mono 26 px, amber, x 90, y 430 |
| Logo | Small lockup at top-left (x 90, y 300): mark 72 × 56 px plus wordmark at 46 px |
| Visual (Path 1) | Photograph: a founder at a laptop in a cinematic evening workspace, seen three-quarters from behind and placed in the **right half** (x 520–1080). The laptop screen shows the clean "Today" prototype, composited. Keep the left 55% dark and empty for the headline. Warm lamp rim light, shallow depth of field. |
| Visual (delivered, Path 2) | `output/nuovadev-reel-2-cover.png`: the prototype phone tilted 8° at lower-right (x 560–980, from y 880), on ink with a coral glow behind it |
| Support line | "Prove people want it **before you build it all.**" Inter 40 px, `#9aa2ae` with white emphasis, x 90, y 1300, maximum width 440 px |
| Hierarchy | Headline, then visual, then support line, then logo. Contrast ratio of at least 7:1 for the headline. |

---

## 11. Ready-to-publish caption and hashtags

```
Before you spend months building your app, ask one question: have you proven people actually want it?

It's easy to plan dozens of features before a single user has tried anything. The plan grows, the budget grows, and the biggest question stays open: will anyone use it?

An MVP (minimum viable product) flips the order:
1. Pick one real problem.
2. Build only the core features needed to solve it.
3. Put it in front of real users.
4. Learn what works. Improve what doesn't.

That's how we build MVPs at NuovaDev: a focused scope, clear milestones, and working software you can open every two weeks. After the first call, you get the scope, timeline and price in writing within 48 hours.

Planning a startup product? Book a free 30-minute consultation through the link in our bio or at nuovadev.com, and let's figure out what your first version actually needs.

#StartupFounders #MVPDevelopment #SaaSFounder #ProductDevelopment #SoftwareDevelopment #Entrepreneurship
```

**Hashtags:** six focused tags, one for each audience in the brief. If your account is limited to five, drop `#SoftwareDevelopment`, which attracts developers more than buyers. Alternates for later posts: `#StartupTips #LeanStartup #ProductManagement #FounderTips #AppDevelopment`.

---

## 12. Pinned comment

```
Founders: what's the one problem your product solves? Reply in a sentence and we'll tell you what we'd put in version one — and what can wait.
```

Pin it only if someone will answer every reply within a business day, and keep answers specific and short. Invite the serious ones to book with: "Happy to go deeper on a free 30-minute call: nuovadev.com/contact".

---

## 13. Final CTA and conversion strategy

**One primary CTA everywhere: book the free 30-minute consultation.** It appears in the spoken line, the end frame, the caption, the pinned comment's follow-up and the bio.

| Touchpoint | Its job |
|---|---|
| Reel end frame | Name the action and the cost (free, 30 minutes, no obligation) and show **nuovadev.com**. It holds for 3.9 s. |
| Caption | Re-state the MVP method for people who read before tapping. Add the verified promise of scope, timeline and price in writing within 48 hours. Point to the bio link. |
| Pinned comment | Start conversations with founders who aren't ready to book. Your replies turn them into consultations. |
| Bio link | **`nuovadev.com/contact`**, the route every CTA on the website uses. It offers "Send a message" and "**Schedule a meeting** — pick a slot, 30 minutes, no obligation". Add tracking: `?utm_source=instagram&utm_medium=social&utm_campaign=reel-before-you-build`. |
| Bio text (for this campaign) | `Software, apps & MVPs for founders. Free 30-min consultation → written scope, timeline & price in 48h ↓` (all verified on the site) |
| Website | The contact page promises a reply within one business day, and a written plan and real price within 48 hours. For anyone wanting proof first, the MVP Development page tells the same story as the reel. Link it from Stories, not the bio. |

**Follow-up:**
- Reply to comments within the first hour.
- In DMs, ask before pitching: *"What's the one problem it solves, and who has it?"* Then offer the 30-minute slot.
- On the call, deliver what the reel promised: agree what version one must do and what can wait, then send the written scope, timeline and price within 48 hours.

**Measure** profile visits, link taps, contact-page visits (by UTM) and calls booked. Judge the reel by qualified calls, not views.

No reel can guarantee leads, sales or reach. This setup makes sure the viewers who are planning a product have one obvious, low-risk next step.

---

## 14. Final editor's checklist

- [ ] Version chosen: **B (45.0 s)** or A (about 51 s). Timings match that version.
- [ ] Voiceover recorded, edited for breaths, and peaking at −6 to −3 dBFS. Delivery matches §2.
- [ ] Frame 1 shows picture, "Don't build yet." and the impact. No logo, no fade.
- [ ] Match cut lands at 04.97. The hold on "people actually want it?" isn't interrupted.
- [ ] The budget figure is unreadable everywhere. No invented metrics, testimonials or client names appear.
- [ ] The "ILLUSTRATIVE PROTOTYPE" label is visible on the fictional app. No fictional UI is presented as client work.
- [ ] The colour change into the light world happens at 18.56–19.26.
- [ ] The four chips (Build → Test → Learn → Improve) light on their beats.
- [ ] The real nuovadev.com MVP and contact pages are current. Re-capture them if the live site has changed.
- [ ] Logo files are unaltered; lockup is "Nuova" plus "Dev" in the gradient; only website colours are used (§9).
- [ ] All on-screen text sits between y 210 and y 1420; nothing important is on the right 120 px.
- [ ] Subtitles are re-synced to the recorded voiceover and spelled exactly as in §5 ("NuovaDev", "MVP", "30-minute").
- [ ] Music is cleared for commercial use. Voiceover is intelligible in every scene. Master is about −14 LUFS, true peak ≤ −1 dBTP.
- [ ] End frame holds at least 3 s and the last word isn't clipped.
- [ ] Exported as 1080 × 1920, 30 fps, H.264 High, AAC 48 kHz, faststart. "Upload at highest quality" is turned on in the Instagram app.
- [ ] Cover uploaded and checked in the 3:4 grid crop.
- [ ] Bio link set to `nuovadev.com/contact` with tracking. Caption and pinned comment posted. Someone is assigned to reply.

### Final quality test

| Check | Result |
|---|---|
| Opening grabs attention immediately | ✓ Frame 1 combines a contrarian title, a money-sized problem and an impact |
| One clear startup problem | ✓ Building too much before proving demand |
| MVP understandable to non-technical founders | ✓ Shown as a backlog cut to three items, then one task done well, with no jargon |
| NuovaDev introduced naturally | ✓ It appears only after the method is shown, as the team that works that way |
| All company claims verifiable | ✓ Each traced to the website's source (see the notes at the top); confirm on the live site before posting |
| Website branding preserved | ✓ Exact tokens, fonts, logo files and headline style |
| Every scene has specific visuals | ✓ §4, with exact screen text |
| Voiceover, timeline, captions and CTA consistent | ✓ All generated from one timeline file (`video2/timeline.json`) |
| Producible without inventing details | ✓ Path 2 is already rendered. Path 1 has shot-level specs, prompts and composite-ready screens. |
