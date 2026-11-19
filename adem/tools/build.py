"""Builds Adem Arroum's e-portfolio pages. Edit the content below, then run:  python tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "Adem Arroum"
EMAIL = "ademarroum2005@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/adem-arroum"
GITHUB = ""            # paste the GitHub profile URL here, e.g. "https://github.com/username"
TEAM_GH = "https://github.com/amiiinoooo"   # where the team projects' code is hosted

MENU = [
    ("About", "index.html", [("Biography", "#biography"), ("LinkedIn", "#linkedin"), ("Email", "#email")]),
    ("CV", "cv.html", [("CV", "#cv"), ("Video Résumé", "#video-resume")]),
    ("Accomplishments", "accomplishments.html", [("Extracurricular Activities", "#extracurricular"),
        ("Professional Certificates", "#certificates")]),
    ("Academic Journey", "academic.html", [("Projects", "#projects"), ("Interesting Courses", "#courses")]),
]


def nav(active):
    items = []
    for label, href, subs in MENU:
        cls = ' class="active"' if href == active else ""
        sub = "".join(f'<li><a href="{href}{a}">{t}</a></li>' for t, a in subs)
        items.append(f'<li><a href="{href}"{cls}>{label}</a><ul class="sub">{sub}</ul></li>')
    return f"""<header><nav class="nav">
  <a class="brand" href="index.html"><span class="dot"></span>{NAME}</a>
  <button class="burger" aria-label="Open menu" onclick="document.querySelector('.menu').classList.toggle('open')">☰</button>
  <ul class="menu">{''.join(items)}</ul>
</nav></header>"""


def footer_links():
    out = [f'<a href="mailto:{EMAIL}">Email</a>']
    if LINKEDIN:
        out.append(f'<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>')
    if GITHUB:
        out.append(f'<a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>')
    return " · ".join(out)


def page(fname, title, kicker, h1, lead, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {NAME}</title>
<meta name="description" content="E-portfolio of {NAME}, Computer Systems Engineering student at MedTech – South Mediterranean University.">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} · {NAME} – E-Portfolio">
<meta property="og:description" content="Computer Systems Engineering student at MedTech – SMU: IoT, embedded, networking and machine-learning team projects, CV and certificates.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='40' fill='%23d9622b'/></svg>">
<link rel="stylesheet" href="assets/style.css?v=3">
</head>
<body>
{nav(fname)}
<main>
<div class="hero">
  <div class="kicker"><span class="dot"></span>{kicker}</div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
</div>
{body}
</main>
<footer><div class="in">
  <span>© 2026 {NAME} · MedTech – South Mediterranean University</span>
  <span>{footer_links()}</span>
</div></footer>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def chips(xs):
    return '<div class="chips">' + "".join(f'<span class="chip">{x}</span>' for x in xs) + "</div>"


def links(xs):
    out = []
    for i, (t, u) in enumerate(xs):
        ext = ' target="_blank" rel="noopener"' if u.startswith("http") or u.endswith(".pdf") else ""
        out.append(f'<a class="btn{"" if i == 0 else " ghost"}" href="{u}"{ext}>{t}</a>')
    return '<div class="links">' + "".join(out) + "</div>"


def reflect(t):
    return f'<div class="reflect"><b>What I learned:</b> {t}</div>'


def placeholder(title, note, badge="To be added"):
    return f'<div class="card placeholder"><span class="badge grey">{badge}</span><h3>{title}</h3><p>{note}</p></div>'


# ======================================================================  ABOUT
linkedin_card = (f'<a class="card" id="linkedin" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ic">💼</span><h3>LinkedIn</h3><p>Experience, projects and certifications</p></a>'
                 if LINKEDIN else
                 '<div class="card placeholder" id="linkedin"><span class="ic">💼</span><h3>LinkedIn</h3><p>Profile link coming soon.</p></div>')
github_card = (f'<a class="card" href="{GITHUB}" target="_blank" rel="noopener"><span class="ic">💻</span><h3>GitHub</h3><p>{GITHUB.replace("https://", "")}</p></a>'
               if GITHUB else
               f'<a class="card" href="academic.html#projects"><span class="ic">💻</span><h3>Projects</h3><p>Team projects with code, slides and reports</p></a>')

about = f"""
<section id="biography" style="padding-top:10px">
 <div class="about">
  <div class="photo"><img src="assets/img/adem.jpg" alt="Portrait of Adem Arroum"></div>
  <div class="bio">
   <h2>Biography</h2>
   <p>I'm studying for an <b>Engineering Degree in Computer Systems Engineering</b> at <b>MedTech – South Mediterranean University</b> in Tunis (2023 – 2028), after finishing high school at Abu Loubaba in Gabès.</p>
   <p>I started with web development: in high school I built an <b>online appointment management system</b> for medical appointments with HTML, CSS, PHP, SQL and JavaScript. At MedTech I've worked in teams on seven projects – from IoT devices like a smart plug and a waste-sorting bin, to a voice-controlled smart house on STM32, a Wi-Fi mapper on a custom PCB, a machine-learning study and a multiplayer network game.</p>
   <p><b>Where I'm heading:</b> I want to build reliable software for real users, especially web applications and data-driven tools. Outside engineering I play football in tournaments and volunteer in my community.</p>
   <div class="stat-row">
    <div class="stat"><b>7</b><span>team projects</span></div>
    <div class="stat"><b>5</b><span>certificates</span></div>
    <div class="stat"><b>8</b><span>coding languages</span></div>
    <div class="stat"><b>4</b><span>languages</span></div>
   </div>
   <p style="margin-top:16px;color:var(--muted);font-size:15px"><b style="color:var(--soft)">Languages:</b> Arabic · English · French · German (basic)</p>
  </div>
 </div>
</section>

<section>
 <h2>Get in touch</h2>
 <p class="sec-intro">The fastest way to reach me is by e-mail.</p>
 <div class="contact-cards">
  {linkedin_card}
  <a class="card" id="email" href="mailto:{EMAIL}"><span class="ic">✉️</span><h3>Email</h3><p>{EMAIL}</p></a>
  {github_card}
 </div>
</section>

<section>
 <h2>Explore my portfolio</h2>
 <p class="sec-intro">Each page below matches a part of my university journey.</p>
 <div class="grid g2">
  <a class="card" href="academic.html#projects"><h3>🚀 Projects</h3><p>IoT, embedded systems, networking and machine learning – with slides, reports and code.</p></a>
  <a class="card" href="academic.html#courses"><h3>📚 Courses</h3><p>The courses that shaped how I think about engineering.</p></a>
  <a class="card" href="accomplishments.html"><h3>🏆 Accomplishments</h3><p>Certificates, football tournaments and volunteering.</p></a>
  <a class="card" href="cv.html"><h3>📄 CV</h3><p>My CV and video résumé.</p></a>
 </div>
</section>
"""
page("index.html", "About", "Computer Systems Engineering · MedTech – SMU",
     'Hi, I\'m <span class="grad">Adem Arroum</span>',
     "Computer Systems Engineering student building web applications, IoT systems and data-driven tools.", about)

# ======================================================================  CV
cv = f"""
<section id="cv" style="padding-top:10px">
 <h2>Curriculum Vitae</h2>
 <p class="sec-intro">My current CV. You can read it below or download the PDF.</p>
 {links([("⬇ Download CV (PDF)", "assets/docs/Adem-Arroum-CV.pdf")])}
 <div style="margin-top:20px"><iframe class="pdf" src="assets/docs/Adem-Arroum-CV.pdf#view=FitH" title="CV of Adem Arroum"></iframe></div>
</section>

<section id="video-resume">
 <h2>Video Résumé</h2>
 <p class="sec-intro">A short video introducing myself, my projects and what I'm looking for.</p>
 <div class="card placeholder video-ph"><div><span class="badge grey">Coming soon</span><h3>Video résumé in production</h3><p>The video will be published here shortly.</p></div></div>
 <!-- When the video is ready, replace the card above with:
 <div style="aspect-ratio:16/9"><iframe style="width:100%;height:100%;border:0;border-radius:18px" src="https://www.youtube.com/embed/VIDEO_ID" title="Video résumé" allowfullscreen></iframe></div> -->
</section>
"""
page("cv.html", "CV", "Curriculum Vitae", 'My <span class="grad">CV</span>',
     "Education, skills, certificates and projects.", cv)

# ======================================================================  ACCOMPLISHMENTS
certs = [
    ("Programming Fundamentals", "Coursera", "2023"),
    ("Introduction to Object-Oriented Programming", "Coursera", "2023"),
    ("Programming with Java", "Coursera", "2023"),
    ("Introduction to Python", "Coursera", "2023"),
    ("Introduction to C", "Coursera", "2023"),
]
cert_html = "".join(f'<div class="card cert"><div><h4>{t}</h4><div class="meta">{o} · {d}</div></div></div>' for t, o, d in certs)

acc = f"""
<section id="extracurricular" style="padding-top:10px">
 <h2>Extracurricular Activities</h2>
 <p class="sec-intro">What I do outside the classroom.</p>
 <div class="grid g2">
  <div class="card"><span class="badge">Sport</span><h3>Football Tournaments</h3>
   <p>I've played in many football tournaments. Competing as a team taught me to communicate under pressure and to keep going after a bad result.</p></div>
  <div class="card"><span class="badge">Community</span><h3>Volunteer – Community Clean-ups</h3><div class="meta">2018</div>
   <p>Took part in local community clean-up events organised by youth associations.</p></div>
  <div class="card"><span class="badge">Tech</span><h3>Web Development</h3>
   <p>I coded simple websites on my own, which led to my high-school appointment management system.</p></div>
 </div>
</section>

<section id="certificates">
 <h2>Professional Certificates<span class="num">({len(certs)})</span></h2>
 <p class="sec-intro">Online courses that extend what I learn at MedTech.</p>
 <div class="grid g2">{cert_html}</div>
</section>

"""
page("accomplishments.html", "Accomplishments", "Accomplishments", '<span class="grad">Accomplishments</span>',
     "Extracurricular activities and certificates.", acc)

# ======================================================================  ACADEMIC JOURNEY
# Project cards: the same images used as the GitHub previews / LinkedIn thumbnails.
CARDS = {'smarthouse.jpg': 'https://repository-images.githubusercontent.com/1461697195/69c3c946-08f9-4628-987f-34917e8310fa', 'rps-arena.jpg': 'https://repository-images.githubusercontent.com/1444759593/e1ce9cdd-9b7b-48c5-8d4e-eae54e940e62', 'wifi-mapper.jpg': 'https://repository-images.githubusercontent.com/1461694837/6f955a87-7ba6-4346-9b0f-979de7cdd3ee', 'ml-segments.jpg': 'https://repository-images.githubusercontent.com/1461696590/fb4a655c-c0bc-4e9c-802d-3145f2df3a6b', 'ecosort.jpg': 'https://repository-images.githubusercontent.com/1461693039/f0fd98db-6065-4368-a2ac-ee5e29505416', 'plugjuice.jpg': 'https://repository-images.githubusercontent.com/1461696204/773da8f6-6223-4cec-a193-1d00cd8d9ab2'}


def thumb(img, alt):
    src = CARDS.get(img)
    if src:
        return f'<img src="{src}" alt="{alt}" onerror="this.onerror=null;this.src=\'assets/img/{img}\'">'
    return f'<img src="assets/img/{img}" alt="{alt}">'


def project(img, badge, title, meta, desc, tags, lnks, refl=None):
    return f"""<div class="card"><div class="thumb">{thumb(img, title)}</div>
 <span class="badge">{badge}</span><h3>{title}</h3><div class="meta">{meta}</div><p>{desc}</p>{chips(tags)}{reflect(refl) if refl else ""}{links(lnks)}</div>"""

R = lambda r: f"{TEAM_GH}/{r}"
B = lambda r, p: f"{TEAM_GH}/{r}/blob/main/{p}"
projects = "".join([
    project("plugjuice.jpg", "IoT", "PlugJuice – Smart Plug", "ISS196 Freshman Project · Spring 2024 · team project",
        "A smart plug that tracks energy consumption, protects devices from voltage spikes and surges, and can be controlled remotely, with a dashboard to monitor each plugged device. As a team we built a 3D prototype in SolidWorks, set up the sensors and circuits, and added the remote-control feature.",
        ["IoT", "JavaScript", "Python", "SolidWorks"], [("Code", R("smart-plug")), ("Slides", f"{TEAM_GH}/smart-plug/blob/main/docs/PLUG%20JUICE.pdf")],
        "my first hardware project: software only matters if the sensors and circuits underneath are reliable."),
    project("ecosort.jpg", "IoT", "EcoSort – Smart Waste-Sorting Bin", "ISS296 Sophomore Project · Spring 2025 · team project",
        "A smart bin that identifies the type of waste and sorts it into the right compartment, with a dashboard that tracks the fill level of each bin using SQL. Built with sensors and a Raspberry Pi programmed in Python, with a 3D prototype designed in SolidWorks.",
        ["Raspberry Pi", "Python", "SQL", "SolidWorks"], [("Code", R("ecosort")), ("Slides", B("ecosort", "docs/EcoSort.pdf")), ("Report", B("ecosort", "docs/final-report.pdf"))],
        "a dashboard is only useful if the data behind it is clean – we spent as much time on the database as on the sensors."),
    project("smarthouse.jpg", "Embedded Systems", "SmartHouse – Voice-Controlled Home on STM32", "ECE355 · Fall 2025 · team of 5",
        "A mobile app sends voice commands to an n8n workflow running a local LLM (Ollama), which turns them into HTTP commands for an STM32 board. The STM32, programmed in C with an ESP8266 web server, controls the door, window, light and fan.",
        ["C", "STM32", "ESP8266", "n8n", "Ollama"], [("Code", R("smart-house-stm32")), ("Slides", B("smart-house-stm32", "docs/slides.pdf")), ("Report", B("smart-house-stm32", "docs/final-report.pdf"))],
        "connecting an AI layer to hardware needs a strict, simple command format between the two."),
    project("carnet-card.jpg", "Startup", "Carnet – Car-Management App Concept", "ISS197 · Fall 2025 · team project",
        "A startup concept for a car-management app: market study, business-opportunity screening, feasibility and a final pitch.",
        ["Design Thinking", "Market study", "Pitch"], [("Project", R("carnet")), ("Pitch deck", B("carnet", "docs/pitch-deck.pdf"))],
        "a good product starts with a real problem and real users, not with the technology."),
    project("wifi-mapper.jpg", "Hardware", "Wi-Fi Signal Mapper – ESP32 on a Custom PCB", "ISS396 Junior Project · Spring 2026 · team of 5",
        "A handheld ESP32 device on a custom PCB designed in Altium, in a 3D-printed enclosure. It measures Wi-Fi strength room by room, and a Flask server with a Tkinter app turns the readings into a heatmap.",
        ["ESP32", "Altium", "Flask", "Tkinter"], [("Code", R("wifi-signal-mapper")), ("Slides", B("wifi-signal-mapper", "docs/presentation.pdf")), ("Report", B("wifi-signal-mapper", "docs/final-report.pdf"))],
        "working in Scrum sprints with a backlog kept a five-person hardware and software project on track."),
    project("ml-segments.jpg", "Machine Learning", "Customer Segmentation & Demand Prediction", "CS280 Artificial Intelligence · Spring 2026 · team of 5",
        "On the Online Retail II dataset, the team built RFM features and used K-Means to split customers into VIP, Loyal, At-Risk and Lost segments, then compared Logistic Regression, KNN and Random Forest to predict demand.",
        ["Python", "scikit-learn", "pandas", "K-Means"], [("Code", R("customer-segmentation-demand-prediction")), ("Report", B("customer-segmentation-demand-prediction", "docs/report.pdf"))],
        "most of the work in machine learning is preparing the data; the model choice comes last."),
    project("rps-arena.jpg", "Networking", "RPS Arena – Multiplayer Game over TCP/UDP", "CS411 Computer Networks · Fall 2026 · team project",
        "Real-time rock-paper-scissors built on raw sockets: one Python game server handles accounts, rooms and scores over TCP and heartbeats, chat and countdown over UDP, for a Tkinter desktop client and a Flask web client.",
        ["Python", "TCP/UDP", "Flask", "Tkinter"], [("Code", R("RPS_arena")), ("Slides", B("RPS_arena", "docs/RPS.pdf"))],
        "TCP and UDP are a trade-off per message: reliability for game state, speed for live updates."),
])

hs_project = f"""<div class="card"><span class="badge">Web Development</span><h3>Online Appointment Management System</h3><div class="meta">High school project</div>
 <p>A dynamic web application to manage medical appointments:</p>
 <ul>
  <li>Checks doctors' availability and schedules patient appointments by date and time.</li>
  <li>Verifies patient records and shows their medical history when it exists in the database.</li>
  <li>Stores and retrieves patient and doctor data in a structured SQL database.</li>
 </ul>
 {chips(["HTML", "CSS", "PHP", "SQL", "JavaScript"])}</div>"""

academic = f"""

<section id="projects" style="padding-top:10px">
 <h2>Projects</h2>
 <p class="sec-intro">Team projects from my years at MedTech, each with its code, slides and report.</p>
 <div class="grid g2">{projects}</div>
 <h3 style="margin:34px 0 14px">Before MedTech</h3>
 <div class="grid g2">{hs_project}</div>
</section>

<section id="courses">
 <h2>Interesting Courses</h2>
 <p class="sec-intro">Courses that changed how I think about engineering.</p>
 <div class="grid g2">
  <div class="card"><span class="badge">ECE355</span><h3>Embedded Systems</h3>
   <p>Programming an STM32 (ARM Cortex-M4) board in C: GPIO, interrupts and SPI, real-time design with RTOS concepts and system modelling with SysML. The course ended with our SmartHouse project.</p>
   {reflect("hardware does exactly what you tell it – reading the datasheet carefully saves hours of debugging.")}</div>
  <div class="card"><span class="badge">CS321</span><h3>Prompt Engineering</h3>
   <p>How large language models work and how to use them well: prompting techniques, retrieval-augmented generation (RAG) and AI agents, with hands-on workflows in n8n.</p>
   {reflect("an LLM is only as useful as the context and instructions you give it.")}</div>
  <div class="card"><span class="badge">ISS197</span><h3>Startup Engineering</h3>
   <p>From problem to pitch: finding and screening a business opportunity, design thinking and pitching. Our team developed Carnet, a car-management app concept.</p>
   {reflect("validating the problem with real users comes before writing any code.")}</div>
  <div class="card"><span class="badge">CS331</span><h3>Database Management</h3>
   <p>Entity-relationship modelling, mapping to the relational model, SQL and transactions, with practical lab exams in MySQL.</p>
   {reflect("a well-designed schema makes the application code simpler and safer.")}</div>
 </div>
</section>

"""
page("academic.html", "Academic Journey", "Academic Journey", 'Academic <span class="grad">Journey</span>',
     "My projects and favourite courses at MedTech.", academic)

print("built")
