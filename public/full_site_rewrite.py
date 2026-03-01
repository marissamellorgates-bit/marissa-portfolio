import re

with open('public/index.html', 'r') as f:
    html = f.read()

changes = 0

def safe_replace(old, new, label):
    global html, changes
    if old in html:
        html = html.replace(old, new)
        changes += 1
        print(f'\u2705 {label}')
        return True
    else:
        print(f'\u274c {label} - NOT FOUND')
        return False

# ==================================================================
# ABOUT PAGE - Home Preview (the short version on the home page)
# ==================================================================

safe_replace(
    'I close performance gaps — not just deliver content. I design and develop eLearning, instructor-led training, and blended programs that produce measurable business results. My work spans compliance training, technical onboarding, and operational readiness — built in Articulate 360, delivered through LMS, and evaluated against Kirkpatrick outcomes.',
    'Performance gaps closed — not just content delivered. eLearning, instructor-led training, and blended programs that produce measurable business results. Compliance training, technical onboarding, and operational readiness — built in Articulate 360, delivered through LMS, and evaluated against Kirkpatrick outcomes.',
    'About preview - voice fix'
)

safe_replace(
    'With 15+ years across corporate, nonprofit, and education environments, I bring needs analysis, storyboarding, SME collaboration, and accessible design (WCAG/508) to every project — plus AI-enhanced workflows that let me move faster without cutting corners on quality.',
    '15+ years across corporate, nonprofit, and education environments. Needs analysis, storyboarding, SME collaboration, and accessible design (WCAG/508) on every project — plus AI-enhanced workflows that move faster without cutting corners on quality.',
    'About preview - second paragraph voice fix'
)

# ==================================================================
# ABOUT PAGE - Full (page-about)
# ==================================================================

safe_replace(
    'I design eLearning, instructor-led training, and blended programs that reduce ramp-up time, improve compliance rates, and give organizations measurable confidence that their people can perform when it counts.',
    'eLearning, instructor-led training, and blended programs that reduce ramp-up time, improve compliance rates, and give organizations measurable confidence that their people can perform when it counts.',
    'About full - opening'
)

# Background section
safe_replace(
    "I've spent 15+ years designing learning across corporate operations, nonprofit programs, and K–12 education. That range is an asset: I've facilitated instructor-led training for 100+ adult professionals, built eLearning courses from needs analysis through LMS delivery, managed multi-stakeholder projects on budget and on schedule, and evaluated outcomes against real business metrics.",
    '15+ years designing learning across corporate operations, nonprofit programs, and K–12 education. That range means instructor-led training for 100+ adult professionals, eLearning courses built from needs analysis through LMS delivery, multi-stakeholder projects managed on budget and schedule, and outcomes evaluated against real business metrics.',
    'About - Background p1'
)

safe_replace(
    'Most recently, I designed compliance and operational readiness training for a fire protection company — including a branching Storyline 360 simulation that transformed a 32-page policy document into a scenario-based experience. The training is designed to reduce supervisor remedial training time, improve compliance assessment accuracy, and eliminate safety incidents tied to knowledge gaps.',
    'Most recently: compliance and operational readiness training for a fire protection company — including a branching Storyline 360 simulation that transformed a 32-page policy document into a scenario-based experience, targeting reduced remedial training time, improved compliance accuracy, and elimination of safety incidents tied to knowledge gaps.',
    'About - Background p2'
)

# What I Bring - condense heavily
safe_replace(
    'I own the full instructional design lifecycle. I conduct needs analysis and gap assessments, storyboard solutions with SMEs, develop in Articulate 360 (Storyline and Rise), produce video tutorials in Camtasia, administer LMS platforms (SCORM/xAPI), and evaluate training effectiveness using Kirkpatrick and learning analytics.',
    'Full instructional design lifecycle ownership: needs analysis and gap assessments, SME-collaborated storyboarding, development in Articulate 360 (Storyline and Rise), Camtasia video production, LMS administration (SCORM/xAPI), and Kirkpatrick evaluation.',
    'About - What I Bring p1'
)

safe_replace(
    'I design for accessibility from the start — WCAG 2.1, Section 508, and UDL principles informed by direct special education experience. I also integrate AI tools (ChatGPT, Claude, Gemini) into my design workflow for faster scenario development, content drafting, and iteration — which means I produce more, and higher-quality, deliverables in less time.',
    'Accessibility from the start — WCAG 2.1, Section 508, and UDL principles informed by direct special education experience. AI tools (ChatGPT, Claude, Gemini) integrated throughout the workflow for faster scenario development, content drafting, and iteration.',
    'About - What I Bring p2'
)

safe_replace(
    'And when off-the-shelf tools hit their limits, I build custom interactive prototypes in HTML/CSS/JavaScript.',
    'When off-the-shelf tools hit their limits, custom interactive prototypes get built in HTML/CSS/JavaScript.',
    'About - What I Bring p3'
)

safe_replace(
    'Across all of my work — from compliance simulations to holistic growth platforms — the same design principles hold: growth is cyclical, assessment should be authentic, and systems should surface imbalance rather than hide it.',
    'Across all projects — from compliance simulations to holistic growth platforms — the same principles hold: growth is cyclical, assessment should be authentic, and systems should surface imbalance rather than hide it.',
    'About - What I Bring closing'
)

# Design Philosophy
safe_replace(
    'I design learning as cycles, not checklists. Every project I build — whether it\'s a compliance simulation or a self-directed growth platform — is grounded in the same principle: real mastery comes from repeated loops of observation, practice, reflection, and adaptation. Content that doesn\'t serve a performance outcome gets cut.',
    'Learning as cycles, not checklists. Every project — whether a compliance simulation or a self-directed growth platform — is grounded in the same principle: real mastery comes from repeated loops of observation, practice, reflection, and adaptation. Content that doesn\'t serve a performance outcome gets cut.',
    'About - Design Philosophy p1'
)

safe_replace(
    'In corporate work, this means action mapping to connect business goals to observable behaviors, scenario-based practice where wrong answers carry real consequences, and Kirkpatrick evaluation to measure whether the training moved the needle.',
    'In corporate work: action mapping to connect business goals to observable behaviors, scenario-based practice where wrong answers carry real consequences, and Kirkpatrick evaluation to measure whether the training moved the needle.',
    'About - Design Philosophy p2'
)

safe_replace(
    'In every context, it means designing systems where learners encounter authentic tradeoffs, receive feedback that unfolds over time rather than instantly, and demonstrate competence to real people — not just automated scoring.',
    'In every context: systems where learners encounter authentic tradeoffs, receive feedback that unfolds over time, and demonstrate competence to real people — not automated scoring.',
    'About - Design Philosophy p3'
)

# ==================================================================
# IROL CASE STUDY
# ==================================================================

# The Approach
safe_replace(
    'I used action mapping to work backward from the business goal: technicians report accurately under IROL within required timelines. Every simulation decision maps to a real field error.',
    'Action mapping drove the design — working backward from the business goal: technicians report accurately under IROL within required timelines. Every simulation decision maps to a real field error documented by supervisors.',
    'IROL - Approach p1'
)

safe_replace(
    'The content detox was aggressive. From 32 pages of lecture material, I extracted 6 critical field decisions and built the entire simulation around practicing those decisions with realistic consequences. Reference content was separated into standalone Rise 360 modules — accessible when needed but not blocking the simulation.',
    'The content detox was aggressive: 32 pages of lecture material distilled to 6 critical field decisions. The entire simulation was built around practicing those decisions with realistic consequences. Reference content was separated into standalone Rise 360 modules — accessible when needed but not blocking the simulation.',
    'IROL - Approach p2'
)

# Course Architecture
safe_replace(
    'Rather than forcing everything into Storyline, I designed a multi-tool architecture: one Storyline simulation for complex branching decisions, and four Rise 360 modules for knowledge-based reference content. This demonstrates deliberate tool selection — each tool used where it\'s strongest.',
    'Rather than forcing everything into Storyline, the course uses a multi-tool architecture: one Storyline simulation for complex branching decisions, and four Rise 360 modules for knowledge-based reference content — each tool used where it\'s strongest.',
    'IROL - Course Architecture'
)

# AI-Enhanced Workflow - condense
safe_replace(
    'I integrated AI tools throughout the production process — scenario scripting, variable logic, content analysis, quiz bank generation, and visual asset creation. Every AI output went through SME review before inclusion. AI accelerated production by approximately 40%, freeing time for design decisions and SME collaboration.',
    'AI tools accelerated production by approximately 40% — scenario scripting, variable logic, content analysis, quiz bank generation, and visual asset creation. Every AI output went through SME review before inclusion.',
    'IROL - AI workflow'
)

# ==================================================================
# TUTORIAL CASE STUDY
# ==================================================================

# SME Collaboration - condense
safe_replace(
    'The operations manager served as the subject matter expert for this project. He had built the custom application and understood every field, workflow, and edge case — but that depth of knowledge was part of the challenge. The gap between what the SME knew intuitively and what a technician needed to understand on day one was significant.',
    'The operations manager who built the application served as SME — understanding every field, workflow, and edge case. But that depth was the challenge: the gap between engineering-level knowledge and day-one task performance was significant.',
    'Tutorial - SME intro'
)

safe_replace(
    'My role was to bridge that gap. I conducted working sessions with the SME to map the complete invoicing workflow, identify the critical steps where errors were most likely, and distinguish between need-to-know and nice-to-know information. The SME understood the system at an engineering level; I translated that into a task-level learning sequence that followed the technician\'s actual workflow on-site — open the app, select the customer, enter line items, review totals with the customer, capture their signature on the device, and submit.',
    'Working sessions mapped the complete invoicing workflow, identified high-error steps, and separated need-to-know from nice-to-know. The engineering-level system knowledge was translated into a task-level sequence following the technician\'s actual workflow: open the app, select the customer, enter line items, review totals, capture signature, submit.',
    'Tutorial - SME process'
)

# Storyboarding
safe_replace(
    'Before recording anything, I storyboarded the full tutorial — mapping each screen, the actions the learner would see, and the narration that would accompany each step. This served two purposes: it gave the SME a concrete artifact to review and approve before production began, and it ensured the tutorial followed a logical task sequence rather than a feature tour.',
    'The full tutorial was storyboarded before recording — mapping each screen, user action, and narration. This gave the SME a reviewable artifact before production began and ensured the tutorial followed a task sequence rather than a feature tour.',
    'Tutorial - Storyboarding p1'
)

safe_replace(
    'The script was written in plain, direct language — no jargon, no assumptions about technical comfort level. Each step was narrated as an action ("Tap the customer name field, then select from the dropdown") rather than a description ("The customer name field allows you to choose from existing customers"). This distinction matters for field technicians who need to do, not just understand.',
    'The script used action-oriented language — "Tap the customer name field, then select from the dropdown" rather than "The customer name field allows you to choose from existing customers." Field technicians need to do, not just understand.',
    'Tutorial - Storyboarding p2'
)

# Production - heavy condensing
safe_replace(
    'I produced the tutorial in Camtasia using screen capture of the live application. Rather than narrating the tutorial myself, I directed the subject matter expert to record the voiceover — a deliberate choice. Field technicians trust a voice from their own organization over an outside narrator, and the SME naturally speaks the techs\' language. My role shifted to directing the recording session: cueing each segment, coaching pacing, and deciding when a take was good enough.',
    'The tutorial was produced in Camtasia using screen capture of the live application, with the SME recording voiceover rather than an outside narrator — field technicians trust a voice from their own organization. The production role shifted to directing: cueing segments, coaching pacing, and deciding when takes were good enough.',
    'Tutorial - Production p1'
)

safe_replace(
    'Key production decisions included recording audio in short segments (one step at a time) rather than a single continuous pass, using zoom-and-pan to focus attention on the relevant area of the screen during each step, adding callout annotations to highlight critical fields, and pacing the narration to match a first-time user\'s speed — deliberately slower than an expert would move through the interface.',
    'Key production choices: short audio segments (one step at a time), zoom-and-pan to focus attention on the active screen area, callout annotations on critical fields, and pacing matched to a first-time user — deliberately slower than an expert.',
    'Tutorial - Production p2'
)

safe_replace(
    'The tutorial was structured as a single, linear walkthrough of the complete invoicing workflow. For a distributed field team accessing this asynchronously, one cohesive video they can follow start-to-finish and rewatch as needed was more practical than a fragmented module series that requires navigation.',
    'A single linear walkthrough — one cohesive video to follow start-to-finish and rewatch as needed — was more practical for a distributed field team than a fragmented module series requiring navigation.',
    'Tutorial - Production p3'
)

# Delivery - condense
safe_replace(
    'The completed tutorial is delivered via a direct link emailed to technicians. This was a deliberate delivery choice — no LMS login, no course enrollment, no barriers between the technician and the training. A field technician can pull it up on the same mobile device they\'ll use for invoicing, watch it before their first customer interaction, and rewatch specific steps as needed. The same link works for onboarding new hires and as a refresher for existing staff.',
    'Delivered via a direct emailed link — no LMS login, no enrollment, no barriers. A field technician pulls it up on the same mobile device they use for invoicing, watches before their first customer interaction, and rewatches as needed. Same link for new hires and refreshers.',
    'Tutorial - Delivery'
)

# Design Decisions - condense all four
safe_replace(
    'Task sequence over feature tour.',
    'Task sequence over feature tour:',
    'Tutorial - Design Decision 1 header'
)

safe_replace(
    'The tutorial follows the technician\'s real on-site workflow, not the application\'s menu structure. A technician standing in front of a customer doesn\'t think "I need to access the customer module" — they think "I need to invoice this job and get a signature." The tutorial mirrors that thinking.',
    'The tutorial mirrors how technicians think on-site — "I need to invoice this job and get a signature" — not how the app\'s menus are organized.',
    'Tutorial - Design Decision 1 body'
)

safe_replace(
    'Single video over modular series.',
    'Single video over modular series:',
    'Tutorial - Design Decision 2 header'
)

safe_replace(
    'For a simple, linear workflow delivered to a non-technical audience asynchronously, one complete walkthrough is easier to access, easier to follow, and easier to rewatch than navigating between modules.',
    'For a linear workflow delivered to a non-technical audience asynchronously, one complete walkthrough beats navigating between modules.',
    'Tutorial - Design Decision 2 body'
)

safe_replace(
    'Script-first production.',
    'Script-first production:',
    'Tutorial - Design Decision 3 header'
)

safe_replace(
    'Storyboarding and scripting before recording eliminated rework, gave the SME a reviewable artifact before production investment, and ensured the narration was tight and action-oriented rather than improvised.',
    'Storyboarding before recording eliminated rework and gave the SME a reviewable artifact before production investment.',
    'Tutorial - Design Decision 3 body'
)

safe_replace(
    'Zero-barrier mobile delivery.',
    'Zero-barrier mobile delivery:',
    'Tutorial - Design Decision 4 header'
)

safe_replace(
    'No logins, no LMS, no enrollment. One link, accessible on the same mobile device technicians use for invoicing. This was the right choice for a field team that performs customer-facing transactions on their phones throughout the day.',
    'One link, same mobile device, no logins — the right choice for a field team doing customer-facing transactions on phones all day.',
    'Tutorial - Design Decision 4 body'
)

# ==================================================================
# PERMACOGNITION CASE STUDY
# ==================================================================

# Design Challenge
safe_replace(
    'Most learning frameworks are built for a single domain — professional skills, academic content, or personal development — delivered to a single audience in a single format. I needed a framework that could organize growth across every dimension of a person\'s life, adapt to radically different audiences (children, families, adult professionals), and scale from facilitated in-person experiences to self-directed digital delivery.',
    'Most learning frameworks serve a single domain, audience, and delivery format. PermaCognition needed to do more: organize growth across every dimension of a person\'s life, adapt to radically different audiences — children, families, adult professionals — and scale from facilitated experiences to self-directed digital delivery.',
    'PermaCognition - Design Challenge p1'
)

safe_replace(
    'The core question wasn\'t "what content do learners need?" It was: how do people actually grow — and can you design a system that mirrors that process?',
    'The core design question: how do people actually grow, and can a system mirror that process?',
    'PermaCognition - Design Challenge p2'
)

# Framework Architecture - shorten dramatically
safe_replace(
    'The answer came from permaculture design principles applied to human development — a methodology I call PermaCognition. The framework organizes growth across three life domains: Land (spiritual, physical, psychological, passion), Sea (intellectual, financial, career), and Sky (family, social, environment). Every learner\'s growth is mapped across all three domains simultaneously, and the system detects imbalance — if one domain is neglected, it surfaces naturally.',
    'PermaCognition applies permaculture design principles to human development. Growth is organized across three life domains — Land (spiritual, physical, psychological), Sea (intellectual, financial, career), and Sky (family, social, environment) — and the system surfaces imbalance when any domain is neglected.',
    'PermaCognition - Framework p1'
)

safe_replace(
    'Within each domain, learners pursue projects — the core unit of growth. Each project progresses through a 7-stage macro-cycle grounded in learning science: Discovery Process → Knowledge Accumulation → Experiential Learning → Prefrontal Insights → Community Extension → Utilize Abundance → Synthesis. Each stage maps to a distinct cognitive function — from identifying a core interest, to gathering and applying knowledge, to accessing higher-order thinking, to extending learning outward through community, and finally synthesizing mastery and preparing for the next cycle.',
    'Within each domain, learners pursue projects through a 7-stage macro-cycle: Discovery Process → Knowledge Accumulation → Experiential Learning → Prefrontal Insights → Community Extension → Utilize Abundance → Synthesis. Each stage maps to a distinct cognitive function.',
    'PermaCognition - Framework p2'
)

safe_replace(
    'A deliberate UX decision shaped how learners experience these stages. Rather than exposing academic terminology, I translated each stage into a natural growth metaphor: Seed → Soil → Root → Stem → Bloom → Fruit → Harvest. This wasn\'t decoration — it was a design choice rooted in the framework\'s permaculture foundation. The metaphor gives learners an intuitive mental model of progression ("I\'m in the Root stage — I\'m building foundations") without requiring them to understand the underlying curriculum architecture. The academic structure drives the design; the nature language drives the experience.',
    'A deliberate UX translation shapes the learner experience: each stage maps to a natural growth metaphor — Seed → Soil → Root → Stem → Bloom → Fruit → Harvest — providing an intuitive mental model of progression without requiring instructional design literacy. The academic structure drives the design; the nature language drives the experience.',
    'PermaCognition - Framework UX'
)

safe_replace(
    'Gating advancement between stages is a micro-cycle loop: Observation → Analysis → Implementation → Reflection. Learners must complete a defined number of micro-cycles before progressing — ensuring depth, not just completion. Every action is a loop, not a checkbox.',
    'Advancement between stages is gated by a micro-cycle loop: Observation → Analysis → Implementation → Reflection. The pattern is fractal — the micro-cycle mirrors the macro-cycle, which mirrors the learner\'s larger growth trajectory. Every action is a loop, not a checkbox.',
    'PermaCognition - Framework gating'
)

safe_replace(
    'The framework follows a fractal spiral pattern: the micro-cycle mirrors the macro-cycle, which mirrors the learner\'s larger growth trajectory. The system is intentionally open-ended — completing one project unlocks the next, with increasing autonomy at each level. There is no final stage.',
    '',
    'PermaCognition - Remove redundant fractal paragraph'
)

# Phase 1
safe_replace(
    'The first implementation was a 7-module self-paced eLearning course built on the PermieKids platform using WordPress and LearnDash LMS. Each module maps directly to a macro-cycle stage — Module 1: Discovery Process guides learners to identify a core interest aligned with their authentic self; Module 3: Experiential Learning moves them into hands-on application; Module 5: Community Extension pushes learning outward through micro social experiments with friends and family. I wrote learning objectives aligned to each stage\'s cognitive function, designed assessments around the micro-cycle loop, and built the content architecture for self-directed online delivery. This version validated that the framework could function in a fully digital, self-paced format — and that the nature growth metaphor translated to structured eLearning without losing its core logic.',
    'A 7-module self-paced course on WordPress/LearnDash. Each module maps to a macro-cycle stage — Discovery Process guides learners to identify a core interest; Experiential Learning moves them into hands-on application; Community Extension pushes learning outward through social experiments. Learning objectives align to each stage\'s cognitive function, with assessments built around the micro-cycle loop. This version validated that the framework could function in a fully digital, self-paced format without losing its core logic.',
    'PermaCognition - Phase 1'
)

# Phase 2
safe_replace(
    'I then piloted the framework with a beta cohort across 50+ locations nationwide, testing it in environments ranging from small family groups to large community settings. Each context revealed different facilitation needs and pacing requirements, but the macro-cycle structure and micro-cycle gating held across all of them. The Synthesis stage (Module 7) consistently produced the highest engagement — learners invested more effort when their audience was real people rather than an automated grading system.',
    'The framework was piloted across 50+ locations nationwide — from small family groups to large community settings. Each context revealed different facilitation needs and pacing requirements, but the macro-cycle structure and micro-cycle gating held across all of them. The Synthesis stage consistently produced the highest engagement: learners invested more effort when their audience was real people rather than an automated grading system.',
    'PermaCognition - Phase 2'
)

# Phase 3
safe_replace(
    'The framework was then adapted for adult professional learners when I was contracted by Green Our Planet to design and deliver grant-funded professional development. I facilitated 3 multi-day instructor-led training institutes for groups of 100+ K–12 educators per event (300+ total), using the same scaffolded progression but reframed for teachers learning to integrate project-based and experiential methods into their own instruction.',
    'The framework scaled to adult professional learners through a contract with Green Our Planet to design and deliver grant-funded professional development — 3 multi-day training institutes for 100+ K–12 educators per event (300+ total), using the same scaffolded progression reframed for teachers integrating project-based and experiential methods.',
    'PermaCognition - Phase 3'
)

safe_replace(
    'The adaptation proved the framework\'s core design principle: the stage structure and micro-cycle logic remain constant while content, pacing, and facilitation adapt to the audience. The Synthesis stage translated naturally — educators presented implementation plans to peer groups and facilitators instead of sharing projects with community. This reduced redesign effort by roughly 60% compared to building from scratch.',
    'This proved the core design principle: stage structure and micro-cycle logic remain constant while content, pacing, and facilitation adapt to the audience. The Synthesis stage translated naturally — educators presented implementation plans to peer groups instead of community projects. Redesign effort dropped roughly 60%.',
    'PermaCognition - Phase 3 adaptation'
)

# Phase 4
safe_replace(
    'The current evolution is Trellis — a Progressive Web App that digitizes the full framework into a mobile-first, offline-capable platform. After three phases of implementation, the framework had proven itself across audiences and delivery formats, but it needed a system that could scale beyond a single LMS or facilitator.',
    'The current evolution is Trellis — a Progressive Web App that digitizes the full framework into a mobile-first, offline-capable platform. After three successful phases, the framework needed a system that could scale beyond a single LMS or facilitator.',
    'PermaCognition - Phase 4 p1'
)

safe_replace(
    'Trellis maps the user\'s growth across all three domains (Land, Sea, Sky), tracks project progression through the 7-stage macro-cycle, enforces micro-cycle gating, and surfaces domain imbalance through a prioritization engine that automatically adjusts daily focus based on which areas of life are being neglected. This is where the nature metaphor becomes more than UX language — projects are visualized as procedurally generated plants, and each stage of growth (Seed through Harvest) renders visually, giving learners an organic representation of their progress rather than a percentage bar. The academic architecture drives the system logic; the growth metaphor drives the interface.',
    'The platform maps growth across all three domains, tracks project progression through the macro-cycle, enforces micro-cycle gating, and surfaces domain imbalance through a prioritization engine that adjusts daily focus automatically. Projects are visualized as procedurally generated plants — each growth stage renders visually, replacing percentage bars with an organic representation of progress.',
    'PermaCognition - Phase 4 p2'
)

safe_replace(
    'The platform also introduces ecosystem-level design: individual growth connects to family units and community groups, enabling what the framework calls "community pollination" — where one person\'s Synthesis stage creates learning opportunities for others in their ecosystem.',
    'Trellis also introduces ecosystem-level design: individual growth connects to family units and community groups through "community pollination" — one person\'s Synthesis stage creates learning opportunities for others.',
    'PermaCognition - Phase 4 p3'
)

# Key Design Decisions - tighten
safe_replace(
    'Fractal logic over linear progression. Every action is a loop (Observation → Analysis → Implementation → Reflection), and the macro-cycle itself is a larger version of the same loop. This mirrors how real expertise develops — not as a sequence of topics, but as deepening cycles of practice and reflection.',
    'Fractal logic over linear progression. Every action is a loop, and the macro-cycle is a larger version of the same loop — mirroring how real expertise develops through deepening cycles, not topic sequences.',
    'PermaCognition - Key Decision 1'
)

safe_replace(
    'Dual-layer naming: academic architecture, intuitive experience. The curriculum structure uses precise pedagogical terms (Discovery Process, Knowledge Accumulation, Experiential Learning, Prefrontal Insights, Community Extension, Utilize Abundance, Synthesis) to ensure each stage maps to a defined cognitive function. But learners never see these terms — they interact with the natural growth metaphor (Seed → Harvest), which provides an intuitive, motivating mental model without requiring instructional design literacy. This separation lets the framework serve both curriculum designers and end learners without compromising either experience.',
    'Dual-layer naming. Precise pedagogical terms (Discovery Process through Synthesis) map each stage to a cognitive function. Learners never see these — they interact with the growth metaphor (Seed → Harvest). This separation serves both curriculum designers and end learners without compromise.',
    'PermaCognition - Key Decision 2'
)

safe_replace(
    'Authentic assessment through community synthesis. The Synthesis stage requires learners to demonstrate mastery to real community members — not answer quiz questions. This creates intrinsic motivation and ensures transfer. If you can explain and defend your project to multiple audiences, you\'ve internalized the learning.',
    'Authentic assessment. The Synthesis stage requires demonstrating mastery to real community members — not answering quiz questions. This creates intrinsic motivation and ensures transfer.',
    'PermaCognition - Key Decision 3'
)

safe_replace(
    'Domain balance over single-track mastery. The three-domain model (Land/Sea/Sky) prevents the common failure mode of personal development systems: obsessive focus on one area at the expense of others. The system detects imbalance and adapts.',
    'Domain balance. The three-domain model prevents obsessive focus on one area at the expense of others. The system detects imbalance and adapts.',
    'PermaCognition - Key Decision 4'
)

safe_replace(
    'Context-adaptive architecture. The framework\'s stage structure and gating logic remain constant while content, pacing, and delivery format adapt to the audience. One architecture served children, families, and adult professionals across eLearning, ILT, and self-directed digital formats.',
    'Context-adaptive architecture. Stage structure and gating logic remain constant; content, pacing, and delivery adapt. One architecture served children, families, and adult professionals across four delivery formats.',
    'PermaCognition - Key Decision 5'
)

# Explore the Platform - tighten
safe_replace(
    'The interactive tutorial below walks through the complete Trellis framework — the three domains, seven growth stages, 18 plant archetypes, and the micro-cycle practice loop. This is the same onboarding experience new users encounter when they first open the app.',
    'This interactive tutorial walks through the Trellis framework — the same onboarding experience new users encounter.',
    'PermaCognition - Explore'
)

# Results
safe_replace(
    'Across all implementations, the framework produced consistent outcomes: 50%+ participant retention across multiple seasons in the family program, successful delivery to 300+ adult educators in ILT format, and validated self-paced completion in the eLearning version. The Synthesis stage consistently drove the highest engagement and deepest learning across every audience and delivery context.',
    'Consistent outcomes across all implementations: 50%+ retention across multiple seasons (family program), 300+ educators trained (ILT), and validated self-paced completion (eLearning). The Synthesis stage drove the highest engagement across every audience and delivery context.',
    'PermaCognition - Results'
)

# ==================================================================
# GLOBAL: Shrink embeds (56.25% padding to 40%)
# ==================================================================
embed_count = html.count('padding-bottom:56.25%')
if embed_count > 0:
    html = html.replace('padding-bottom:56.25%', 'padding-bottom:40%')
    changes += 1
    print(f'\u2705 Shrunk {embed_count} embeds from 56.25% to 40%')
else:
    print('\u274c No 56.25% embeds found')

# ==================================================================
# GLOBAL: Tighter spacing for case studies
# ==================================================================
spacing_style = '''<style>
#page-irol h2, #page-tutorial h2, #page-project-trellis h2 { margin-top: 2rem; margin-bottom: 0.75rem; }
#page-irol p, #page-tutorial p, #page-project-trellis p { margin-bottom: 0.75rem; }
</style>'''

if '</head>' in html:
    html = html.replace('</head>', spacing_style + '\n</head>')
    changes += 1
    print('\u2705 Added tighter case study spacing')

# ==================================================================
# SAVE
# ==================================================================
with open('public/index.html', 'w') as f:
    f.write(html)

print(f'\n{"="*50}')
print(f'TOTAL: {changes} changes applied')
print(f'{"="*50}')
print('\nRun:')
print('  git add public/')
print('  git commit -m "Full site voice and layout overhaul"')
print('  git push')
