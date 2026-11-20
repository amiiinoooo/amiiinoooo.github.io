"""Builds the PREVIEW of the redesigned e-portfolio into /preview.
Run:  python tools/build_preview.py      (the live site is built by tools/build.py)"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "preview"
A = "../assets"  # shared images, certificates and CV live in the live site's assets folder
GH = "https://github.com/amiiinoooo"
LINKEDIN = "https://www.linkedin.com/in/amine-ben-nasrallah/"
EMAIL = "amine.bennasrallah@gmail.com"

MENU = [
    ("About", "index.html", [("Biography", "#biography"), ("LinkedIn", "#linkedin"), ("Email", "#email")]),
    ("CV", "cv.html", [("CV", "#cv"), ("Video résumé", "#video-resume")]),
    ("Accomplishments", "accomplishments.html", [("Extracurricular activities", "#extracurricular"),
        ("Professional certificates", "#certificates"), ("Rewards", "#rewards"), ("Competitions", "#competitions")]),
    ("Academic Journey", "academic.html", [("Internships", "#internships"), ("Projects", "#projects"),
        ("Interesting courses", "#courses"), ("Company visits", "#company-visits")]),
]

CHIP_ICON = ('<svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><rect x="5" y="5" width="12" height="12" rx="2" fill="#16263b" stroke="#d9a441" stroke-width="1.6"/>'
             + "".join(f'<path d="M{x} 1v3M{x} 18v3" stroke="#d9a441" stroke-width="1.6"/>' for x in (8, 11, 14))
             + "".join(f'<path d="M1 {y}h3M18 {y}h3" stroke="#d9a441" stroke-width="1.6"/>' for y in (8, 11, 14)) + "</svg>")


def nav(active):
    items = []
    for label, href, subs in MENU:
        cls = ' class="active" aria-current="page"' if href == active else ""
        sub = "".join(f'<li><a href="{href}{a}">{t}</a></li>' for t, a in subs)
        items.append(f'<li><a href="{href}"{cls}>{label}</a><ul class="sub">{sub}</ul></li>')
    return f"""<header><nav class="nav" aria-label="Main">
  <a class="brand" href="index.html">{CHIP_ICON}Amine Ben Nasrallah</a>
  <button class="burger" aria-label="Open menu" onclick="document.querySelector('.menu').classList.toggle('open')">☰</button>
  <ul class="menu">{''.join(items)}</ul>
</nav></header>"""


def page(fname, title, body, head=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0f1a2b">
<meta name="color-scheme" content="dark">
<meta name="robots" content="noindex">
<title>{title} · Amine Ben Nasrallah</title>
<meta name="description" content="E-portfolio of Amine Ben Nasrallah, Computer Systems Engineering student at MedTech – South Mediterranean University.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 22'><rect x='5' y='5' width='12' height='12' rx='2' fill='%2316263b' stroke='%23d9a441' stroke-width='1.6'/></svg>">
<link rel="stylesheet" href="style.css?v=1">
</head>
<body>
{nav(fname)}
<main>
{head}
{body}
</main>
<footer><div class="in">
  <span>© 2026 Amine Ben Nasrallah, MedTech – South Mediterranean University</span>
  <nav aria-label="Elsewhere"><a href="mailto:{EMAIL}">Email</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a><a href="{GH}" target="_blank" rel="noopener">GitHub</a></nav>
</div></footer>
<script src="site.js?v=1" defer></script>
</body>
</html>
"""
    (OUT / fname).write_text(html, encoding="utf-8")


def page_head(h1, lead):
    return f'<div class="page-head"><h1>{h1}</h1><p class="lead">{lead}</p></div>'


def tags(xs):
    return '<ul class="tags">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"


def acts(xs):
    return '<div class="acts">' + "".join(
        f'<a href="{u}"' + (' target="_blank" rel="noopener"' if u.startswith("http") or u.endswith(".pdf") else "") + f">{t}</a>"
        for t, u in xs) + "</div>"


def learned(t):
    return f'<p class="learned"><em>What I learned:</em> {t}</p>'


# ----------------------------------------------------------------- pinout hero
def pinout():
    left = ["C", "Python", "Java", "SQL"]
    right = ["STM32", "ESP32", "TCP/UDP", "Altium"]
    ys = [112, 166, 220, 274]
    out = ['<svg class="pinout" viewBox="0 0 560 380" role="img" aria-label="A chip diagram labelled with my main skills: C, Python, Java, SQL, STM32, ESP32, TCP/UDP and Altium">',
           '<rect class="body" x="175" y="62" width="210" height="262" rx="8"/>',
           '<path class="notch" d="M262 62a18 18 0 0 0 36 0"/>',
           '<text class="chip-name" x="280" y="186" text-anchor="middle">ABN-2004</text>',
           '<text class="chip-sub" x="280" y="214" text-anchor="middle">Computer Systems Eng.</text>',
           '<text class="chip-sub" x="280" y="234" text-anchor="middle">MedTech – SMU, Tunis</text>']
    i = 0
    for n, (lab, y) in enumerate(zip(left, ys), start=1):
        out += [f'<path class="trace" style="--len:70;--i:{i}" d="M175 {y}h-70"/>',
                f'<circle class="pad" style="--i:{i}" cx="100" cy="{y}" r="6"/>',
                f'<text class="pin-label" style="--i:{i}" x="84" y="{y + 6}" text-anchor="end">{lab}</text>',
                f'<text class="num" x="184" y="{y + 4}">{n}</text>']
        i += 1
    for n, (lab, y) in enumerate(zip(right, reversed(ys)), start=5):
        out += [f'<path class="trace" style="--len:70;--i:{i}" d="M385 {y}h70"/>',
                f'<circle class="pad" style="--i:{i}" cx="460" cy="{y}" r="6"/>',
                f'<text class="pin-label" style="--i:{i}" x="476" y="{y + 6}">{lab}</text>',
                f'<text class="num" x="376" y="{y + 4}" text-anchor="end">{n}</text>']
        i += 1
    out.append("</svg>")
    return "".join(out)


# ======================================================================  ABOUT
about = f"""
<div class="hero">
  <div>
    <h1>Amine Ben Nasrallah</h1>
    <p class="lead">Computer Systems Engineering student building embedded, networked and secure systems – from firmware on a microcontroller to the server it talks to.</p>
  </div>
  {pinout()}
</div>

<section id="biography">
 <h2>Biography</h2>
 <div class="bio">
  <div class="portrait"><img src="{A}/img/amine.jpg" alt="Portrait of Amine Ben Nasrallah"></div>
  <div>
   <p>I'm studying for an <b>Engineering Degree in Computer Systems Engineering</b> at <b>MedTech – South Mediterranean University</b> in Tunis (2023 – 2028). I like building things where hardware and software meet: microcontrollers that talk to web servers, devices on PCBs I designed myself, and the network code that connects them.</p>
   <p>My path so far mixes engineering and initiative. At 15 I built a Mario-style 2D game and took <b>3rd place at a GoMyCode hackathon</b>. At 18 I ran my own small online business, <b>MetaShop</b>. At MedTech I've built a voice-controlled smart house on STM32, a multiplayer game over raw TCP/UDP sockets and an ESP32 Wi-Fi mapper on a custom PCB, and I spent a summer as a <b>cybersecurity intern at Network Associates</b>, securing a real desktop application.</p>
   <p><b>Where I'm heading:</b> I want to work on embedded and connected systems that are secure by design, from firmware up to the cloud. Outside engineering I edit videos – I co-founded <b>Rakcha Koora</b>, a football quiz channel, and was its lead video editor.</p>
   <div class="facts">
    <div><b>9</b><span>projects on GitHub</span></div>
    <div><b>15</b><span>certificates</span></div>
    <div><b>1</b><span>internship</span></div>
    <div><b>4</b><span>languages: Arabic, English, French, German (basic)</span></div>
   </div>
  </div>
 </div>
</section>

<section>
 <h2>Get in touch</h2>
 <p class="intro">E-mail or LinkedIn is the fastest way to reach me. All my code is on GitHub.</p>
 <div class="rows">
  <a class="row" id="email" href="mailto:{EMAIL}"><span class="k">Email</span><span class="v">{EMAIL}</span></a>
  <a class="row" id="linkedin" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="k">LinkedIn</span><span class="v">linkedin.com/in/amine-ben-nasrallah</span></a>
  <a class="row" href="{GH}" target="_blank" rel="noopener"><span class="k">GitHub</span><span class="v">github.com/amiiinoooo</span></a>
 </div>
</section>

<section>
 <h2>In this portfolio</h2>
 <div class="rows">
  <a class="row" href="academic.html#projects"><span class="k">Projects</span><span class="v">Embedded systems, networking, machine learning and IoT, with slides, reports and code.</span></a>
  <a class="row" href="academic.html#internships"><span class="k">Internship</span><span class="v">Cybersecurity internship at Network Associates, summer 2025.</span></a>
  <a class="row" href="accomplishments.html"><span class="k">Accomplishments</span><span class="v">Certificates, a hackathon podium, a business and a YouTube channel.</span></a>
  <a class="row" href="cv.html"><span class="k">CV</span><span class="v">My one-page CV and video résumé.</span></a>
 </div>
</section>
"""
page("index.html", "About", about)

# ======================================================================  CV
cv = f"""
<section id="cv">
 <h2>Curriculum vitae</h2>
 <p class="intro">My current one-page CV.</p>
 <a class="btn" href="{A}/docs/Amine-Ben-Nasrallah-CV.pdf" target="_blank" rel="noopener">Download CV (PDF)</a>
 <iframe class="pdf" src="{A}/docs/Amine-Ben-Nasrallah-CV.pdf#view=FitH" title="CV of Amine Ben Nasrallah"></iframe>
</section>

<section id="video-resume">
 <h2>Video résumé</h2>
 <p class="intro">A short video introducing myself, my projects and what I'm looking for.</p>
 <div class="empty"><div><h3>Video coming soon</h3><p>It will be published here shortly.</p></div></div>
</section>
"""
page("cv.html", "CV", cv, page_head("CV", "Education, experience, projects and skills on one page."))

# ======================================================================  ACCOMPLISHMENTS
certs = [
    ("Trees and Graphs: Basics", "University of Colorado Boulder", "May 2026", "trees-and-graphs.pdf"),
    ("Agile Project Management", "Google", "Apr 2026", "agile-project-management.pdf"),
    ("PCB Basic Design Course", "Altium Education", "Apr 2026", "altium-pcb-design.pdf"),
    ("C Programming: Getting Started", "Dartmouth College & IMT", "Dec 2025", "c-programming.pdf"),
    ("Design Thinking: Ideas to Action", "University of Virginia", "Nov 2025", "design-thinking.pdf"),
    ("Hands-on Introduction to Linux Commands and Shell Scripting", "IBM", "Oct 2025", "linux-shell-scripting.pdf"),
    ("Create a Record of Students using Abstraction in Java", "Coursera Project Network", "Apr 2024", "java-abstraction-students.pdf"),
    ("Learn Java and JavaFX by Creating a Graphical Calculator", "Coursera Project Network", "Apr 2024", "javafx-calculator.pdf"),
    ("Java Inheritance, Composition and Aggregation", "Coursera Project Network", "Mar 2024", "java-inheritance.pdf"),
    ("Creating a Portfolio Using Weebly", "Coursera Project Network", "Mar 2024", "weebly-portfolio.pdf"),
    ("Study Skills for University Success", "University of California, Irvine", "Feb 2024", "study-skills.pdf"),
    ("Introduction to Object-Oriented Programming with Java", "LearnQuest", "Feb 2024", "oop-java.pdf"),
    ("Introduction to Python", "Coursera Project Network", "Jan 2024", "intro-python.pdf"),
    ("Programming Fundamentals", "Duke University", "Nov 2023", "programming-fundamentals.pdf"),
    ("Introduction to C Programming: Variables, Input, Output", "Coursera Project Network", "Oct 2023", "intro-c.pdf"),
]
cert_rows = "".join(
    f'<tr><td>{t}</td><td class="issuer">{o}</td><td class="date">{d}</td><td class="open"><a href="{A}/certificates/{f}" target="_blank" rel="noopener">View</a></td></tr>'
    for t, o, d, f in certs)

acc = f"""
<section id="extracurricular">
 <h2>Extracurricular activities</h2>
 <p class="intro">What I've built and taken part in outside the classroom.</p>
 <div class="rows">
  <div class="row"><div class="k">MetaShop<small>Founder, Oct 2022 – Jul 2023</small></div><div class="v">
   <p>I started and ran MetaShop on my own: an online business selling digital gift cards (PlayStation, Apple, Steam, Epic Games and more) at affordable prices in Tunisia.</p>
   <ul class="points">
    <li>Managed the entire operation: sourcing, pricing, order handling, payments and customer service.</li>
    <li>Processed 86+ orders for 35+ customers, generating ~10K TND in sales – about half of customers came back for repeat orders.</li>
    <li>Promoted it on Instagram with a public reviews section and clear ordering guides to build trust.</li>
    <li>Funded by a private investor.</li>
   </ul>
   {learned("running a business taught me to own every detail, answer customers fast and keep promises – the same habits I now bring to team projects.")}
  </div></div>
  <div class="row"><div class="k">Rakcha Koora<small>Co-founder and lead video editor, Feb – Aug 2024</small></div><div class="v">
   <p>Co-founded Rakcha Koora, a football quiz channel run by a team of four, where we recorded and played the quizzes on camera.</p>
   <ul class="points">
    <li>Lead video editor for all content: long-form YouTube episodes (25–35 min), YouTube Shorts, Instagram Reels and TikTok videos.</li>
    <li>Managed the channel's social media across YouTube, Instagram and TikTok.</li>
    <li>Reached 23K+ views, 400+ followers and 600+ likes across all platforms.</li>
   </ul>
   {learned("editing for an audience is about rhythm and clarity – cut what doesn't serve the story. It made me better at presentations and demos too.")}
   {acts([("Watch the channel", "https://www.youtube.com/@RakchaKoora")])}
  </div></div>
  <div class="row"><div class="k">Fitness For Engineering<small>Podcast, COM307, fall 2026</small></div><div class="v">
   <p>A 20-minute group podcast on nutrition, physical activity, supplements and healthy habits for engineering students. I presented the nutrition chapter and edited the final video with captions, chapter cards and topic visuals.</p>
   {acts([("Watch the podcast", "https://drive.google.com/file/d/1SKUTouVrSy8AX6TrqLF8PAniJvcxRDsR/view?usp=sharing")])}
  </div></div>
  <div class="row"><div class="k">Youth organization<small>Volunteer, 2017 – 2018</small></div><div class="v">
   <p>Member of a non-profit youth association promoting education, culture and solidarity.</p>
  </div></div>
 </div>
</section>

<section id="certificates">
 <h2>Professional certificates</h2>
 <p class="intro">Fifteen online courses from universities and companies that extend what I learn at MedTech.</p>
 <div class="table-wrap"><table>
  <thead><tr><th>Course</th><th class="issuer">Issuer</th><th>Date</th><th></th></tr></thead>
  <tbody>{cert_rows}</tbody>
 </table></div>
</section>

<section id="rewards">
 <h2>Rewards</h2>
 <div class="rows">
  <div class="row"><div class="k">3rd place<small>GoMyCode Hackathon, 2019</small></div><div class="v"><p>Podium finish for a Mario-style 2D game I built at 15.</p></div></div>
  <div class="row"><div class="k">Best Idea<small>Spark Program, BIAT Foundation, 2017</small></div><div class="v"><p>Received the Best Idea certificate in the BIAT Foundation's Spark program.</p></div></div>
 </div>
</section>

<section id="competitions">
 <h2>Competitions</h2>
 <div class="rows">
  <div class="row"><div class="k">GoMyCode Hackathon<small>2019, age 15</small></div><div class="v">
   <p>At 15, I built a simple Mario-like 2D game during the GoMyCode hackathon and placed 3rd.</p>
   {learned("this was the moment I realised I could build something real on my own, under pressure. It's why I chose engineering.")}
  </div></div>
 </div>
</section>
"""
page("accomplishments.html", "Accomplishments", acc,
     page_head("Accomplishments", "Extracurricular activities, certificates, rewards and competitions."))

# ======================================================================  ACADEMIC JOURNEY
CARDS = {'smarthouse.jpg': 'https://repository-images.githubusercontent.com/1461697195/69c3c946-08f9-4628-987f-34917e8310fa', 'rps-arena.jpg': 'https://repository-images.githubusercontent.com/1444759593/e1ce9cdd-9b7b-48c5-8d4e-eae54e940e62', 'wifi-mapper.jpg': 'https://repository-images.githubusercontent.com/1461694837/6f955a87-7ba6-4346-9b0f-979de7cdd3ee', 'ml-segments.jpg': 'https://repository-images.githubusercontent.com/1461696590/fb4a655c-c0bc-4e9c-802d-3145f2df3a6b', 'ecosort.jpg': 'https://repository-images.githubusercontent.com/1461693039/f0fd98db-6065-4368-a2ac-ee5e29505416', 'plugjuice.jpg': 'https://repository-images.githubusercontent.com/1461696204/773da8f6-6223-4cec-a193-1d00cd8d9ab2'}


def shot(img, alt):
    src = CARDS.get(img)
    if src:
        return f'<div class="shot"><img src="{src}" alt="{alt}" loading="lazy" onerror="this.onerror=null;this.src=\'{A}/img/{img}\'"></div>'
    return f'<div class="shot"><img src="{A}/img/{img}" alt="{alt}" loading="lazy"></div>'


def project(img, title, meta, desc, tg, lnks, refl=None):
    return f"""<article class="proj">{shot(img, title + " project card")}
 <div><h3>{title}</h3><p class="meta">{meta}</p><p>{desc}</p>{tags(tg)}{learned(refl) if refl else ""}{acts(lnks)}</div></article>"""


R = lambda r: f"{GH}/{r}"
B = lambda r, p: f"{GH}/{r}/blob/main/{p}"
projects = "".join([
    project("smarthouse.jpg", "SmartHouse: a voice-controlled home on STM32", '<span class="code">ECE355</span>, embedded systems, fall 2025, team of 5',
        "Talk to your house: a mobile app sends voice commands to an n8n workflow running a local LLM (Ollama), which turns them into HTTP commands for an STM32 board. The STM32, programmed in C with an ESP8266 web server, controls the door, window, light and fan.",
        ["C", "STM32", "ESP8266", "n8n", "Ollama"], [("Code", R("smart-house-stm32")), ("Slides", B("smart-house-stm32", "docs/slides.pdf")), ("Report", B("smart-house-stm32", "docs/final-report.pdf"))],
        "connecting an AI layer to real hardware means designing a strict, simple command format – the LLM is flexible, the microcontroller is not."),
    project("rps-arena.jpg", "RPS Arena: a multiplayer game over TCP/UDP", '<span class="code">CS411</span>, computer networks, fall 2026',
        "Real-time rock-paper-scissors built on raw sockets. One Python game server handles accounts, rooms and scores over TCP and heartbeats, chat and countdown over UDP, for both a Tkinter desktop client and a Flask web client published over HTTPS.",
        ["Python", "TCP/UDP", "Flask", "Tkinter", "PBKDF2"], [("Code", R("RPS_arena")), ("Slides", B("RPS_arena", "docs/RPS.pdf")), ("Design document", B("RPS_arena", "docs/communication-design.pdf"))],
        "choosing TCP or UDP is a trade-off per message type, not per app – reliability for game state, speed for heartbeats."),
    project("wifi-mapper.jpg", "Wi-Fi Signal Mapper: an ESP32 on a custom PCB", '<span class="code">ISS396</span>, junior project, spring 2026',
        "A handheld ESP32 device on a PCB I designed in Altium, in a 3D-printed enclosure. It measures Wi-Fi strength around a building and a Flask back-end with a Tkinter interface turns the readings into a heatmap.",
        ["ESP32", "Altium", "3D printing", "Flask"], [("Code", R("wifi-signal-mapper")), ("Slides", B("wifi-signal-mapper", "docs/presentation.pdf")), ("Report", B("wifi-signal-mapper", "docs/final-report.pdf"))],
        "a PCB forces you to commit early – every mistake costs a re-order, so design reviews matter."),
    project("ml-segments.jpg", "Customer segmentation and demand prediction", '<span class="code">CS280</span>, artificial intelligence, spring 2026',
        "On the Online Retail II dataset, I built RFM features and used K-Means to split customers into VIP, Loyal, At-Risk and Lost segments, then compared Logistic Regression, KNN and Random Forest to predict demand.",
        ["Python", "scikit-learn", "pandas", "K-Means"], [("Code", R("customer-segmentation-demand-prediction")), ("Report", B("customer-segmentation-demand-prediction", "docs/report.pdf"))],
        "most of the work in ML is cleaning and shaping the data; the model choice comes last."),
    project("ecosort.jpg", "EcoSort: a smart waste-sorting bin", '<span class="code">ISS296</span>, sophomore project, spring 2025',
        "A bin that detects the type of waste with sensors and uses servo flaps to sort it into the right compartment, with a Flask dashboard showing the fill level of each bin. Designed in SolidWorks.",
        ["Raspberry Pi", "Python", "Flask", "MySQL", "SolidWorks"], [("Code", R("ecosort")), ("Slides", B("ecosort", "docs/EcoSort.pdf")), ("Report", B("ecosort", "docs/final-report.pdf"))]),
    project("plugjuice.jpg", "PlugJuice: a smart plug", '<span class="code">ISS196</span>, freshman project, spring 2024',
        "An IoT smart plug that tracks energy consumption in real time, protects against voltage spikes and can be switched remotely, with a consumption dashboard. Enclosure designed in SolidWorks.",
        ["IoT", "JavaScript", "Python", "SolidWorks"], [("Code", R("smart-plug")), ("Slides", f"{GH}/smart-plug/blob/main/docs/PLUG%20JUICE.pdf")]),
    project("carnet-card.jpg", "Carnet: a car-management app concept", '<span class="code">ISS197</span>, startup engineering, fall 2025',
        "A startup concept for a car-management app: market study, business-opportunity screening, feasibility and a final pitch.",
        ["Design thinking", "Market study", "Pitch"], [("Project", R("carnet")), ("Pitch deck", B("carnet", "docs/pitch-deck.pdf"))]),
])

academic = f"""
<section id="internships">
 <h2>Internships</h2>
 <div class="intern">
  <div class="shot"><img src="https://repository-images.githubusercontent.com/995468095/0ce3ddfd-20d1-4fab-a3d3-5a492ae24a88" alt="Secure Hotel App project card" onerror="this.onerror=null;this.src='{A}/img/hotel-app.jpg'"></div>
  <h3>Cybersecurity Internship at Network Associates (NA)</h3>
  <p class="meta">May – July 2025, Lac 1, Tunis, hybrid</p>
  <p>I secured a hotel management desktop application built with JavaFX and MySQL:</p>
  <ul class="points">
   <li>Authentication with e-mail verification (expiring one-time codes), BCrypt password hashing and brute-force lockout.</li>
   <li>Role-based access control (staff and client) with a hierarchical request-validation workflow to block privilege escalation.</li>
   <li>Input validation, sanitization and prepared statements on every query to prevent SQL injection.</li>
   <li>Logging, error handling, and credentials moved out of the code into environment variables.</li>
  </ul>
  {tags(["Java", "JavaFX", "MySQL", "BCrypt", "OWASP"])}
  {learned("security is not a feature you add at the end. Every input, every role and every password path has to be designed for the attacker from day one – and explained clearly to the team.")}
  {acts([("Code", R("HospitalManagement")), ("Internship report", f"{GH}/HospitalManagement/blob/master/docs/Amine.BenNasrallah_INT%20101%20-%20Clean.pdf")])}
 </div>
</section>

<section id="projects">
 <h2>Projects</h2>
 <p class="intro">Course and team projects from my years at MedTech, each with its code, slides and report. Also on GitHub: <a href="{R('CareApp')}" target="_blank" rel="noopener">CareApp</a>, an installable hydration-reminder web app.</p>
 {projects}
</section>

<section id="courses">
 <h2>Interesting courses</h2>
 <p class="intro">Courses that changed how I think about engineering.</p>
 <div class="rows">
  <div class="row"><div class="k">Embedded Systems<small class="code">ECE355</small></div><div class="v">
   <p>Programming an STM32 (ARM Cortex-M4) board in C: GPIO, interrupts and SPI, real-time design with RTOS concepts and system modelling with SysML. The course ended with our SmartHouse project.</p>
   {learned("reading a datasheet and a reference manual is a skill in itself. Once I could, I stopped guessing and started designing.")}</div></div>
  <div class="row"><div class="k">Prompt Engineering<small class="code">CS321</small></div><div class="v">
   <p>How large language models work and how to use them well: prompting techniques, retrieval-augmented generation (RAG) and AI agents. With a teammate I built a RAG workflow in n8n that indexes uploaded PDFs and CSVs in a vector store and answers questions with memory, with file upload through Telegram.</p>
   {learned("an LLM is only as useful as the context you give it. This course led directly to the n8n + local-LLM brain of our SmartHouse.")}</div></div>
  <div class="row"><div class="k">Startup Engineering<small class="code">ISS197</small></div><div class="v">
   <p>From problem to pitch: finding and screening a business opportunity, design thinking, building a prototype story and pitching it. Our team developed Carnet, a car-management app concept, and I completed the University of Virginia's Design Thinking course alongside it.</p>
   {learned("a good product starts with a real problem and real users, not with the technology I want to use.")}</div></div>
  <div class="row"><div class="k">Database Management<small class="code">CS331</small></div><div class="v">
   <p>Entity-relationship modelling, mapping to the relational model, SQL and transactions. I designed complete schemas for a hospital and a university system in MySQL Workbench and completed three practical lab exams.</p>
   {learned("a clean schema saves hundreds of lines of code later – and it's the base of the SQL-injection defences I used in my internship.")}</div></div>
 </div>
</section>

<section id="company-visits">
 <h2>Company visits</h2>
 <div class="rows">
  <div class="row"><div class="k">Network Associates<small>Lac 1, Tunis, summer 2025</small></div><div class="v">
   <p>My internship took me inside Network Associates in Tunis, where I saw how a professional IT team organises its work and delivers software.</p>
   {acts([("See the internship", "#internships")])}</div></div>
 </div>
</section>
"""
page("academic.html", "Academic Journey", academic,
     page_head("Academic journey", "My internship, projects, favourite courses and company visits at MedTech."))

print("preview built")
