"""Builds the e-portfolio pages. Edit the content below, then run:  python tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GH = "https://github.com/amiiinoooo"
LINKEDIN = "https://www.linkedin.com/in/amine-ben-nasrallah-921783338/"
EMAIL = "amine.bennasrallah@gmail.com"

MENU = [
    ("About", "index.html", [("Biography", "#biography"), ("LinkedIn", "#linkedin"), ("Email", "#email")]),
    ("CV", "cv.html", [("CV", "#cv"), ("Video Résumé", "#video-resume")]),
    ("Accomplishments", "accomplishments.html", [("Extracurricular Activities", "#extracurricular"),
        ("Professional Certificates", "#certificates"), ("Rewards", "#rewards"), ("Competitions", "#competitions")]),
    ("Academic Journey", "academic.html", [("Internships", "#internships"), ("Projects", "#projects"),
        ("Interesting Courses", "#courses"), ("Company Visits", "#company-visits")]),
]


def nav(active):
    items = []
    for label, href, subs in MENU:
        cls = ' class="active"' if href == active else ""
        sub = "".join(f'<li><a href="{href}{a}">{t}</a></li>' for t, a in subs)
        items.append(f'<li><a href="{href}"{cls}>{label}</a><ul class="sub">{sub}</ul></li>')
    return f"""<header><nav class="nav">
  <a class="brand" href="index.html"><span class="dot"></span>Amine Ben Nasrallah</a>
  <button class="burger" aria-label="Open menu" onclick="document.querySelector('.menu').classList.toggle('open')">☰</button>
  <ul class="menu">{''.join(items)}</ul>
</nav></header>"""


def page(fname, title, kicker, h1, lead, body):
    fname_url = "" if fname == "index.html" else fname
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Amine Ben Nasrallah</title>
<meta name="description" content="E-portfolio of Amine Ben Nasrallah, Computer Systems Engineering student at MedTech – South Mediterranean University.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Amine Ben Nasrallah – E-Portfolio">
<meta property="og:title" content="{title} · Amine Ben Nasrallah – E-Portfolio">
<meta property="og:description" content="Computer Systems Engineering student at MedTech – SMU: embedded systems, networking and application security projects, internship, CV and certificates.">
<meta property="og:image" content="https://amiiinoooo.github.io/assets/img/og-card.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="627">
<meta property="og:url" content="https://amiiinoooo.github.io/{fname_url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='40' fill='%232ecc71'/></svg>">
<link rel="stylesheet" href="assets/style.css">
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
  <span>© 2026 Amine Ben Nasrallah · MedTech – South Mediterranean University</span>
  <span><a href="mailto:{EMAIL}">Email</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> · <a href="{GH}" target="_blank" rel="noopener">GitHub</a></span>
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


def placeholder(title, note):
    return f'<div class="card placeholder"><span class="badge grey">To be added</span><h3>{title}</h3><p>{note}</p></div>'


# ======================================================================  ABOUT
about = f"""
<section id="biography" style="padding-top:10px">
 <div class="about">
  <div class="photo"><img src="assets/img/amine.jpg" alt="Portrait of Amine Ben Nasrallah"></div>
  <div class="bio">
   <h2>Biography</h2>
   <p>I'm studying for an <b>Engineering Degree in Computer Systems Engineering</b> at <b>MedTech – South Mediterranean University</b> in Tunis (2023 – 2028). I like building things where hardware and software meet: microcontrollers that talk to web servers, devices on PCBs I designed myself, and the network code that connects them.</p>
   <p>My path so far mixes engineering and initiative. At 15 I built a Mario-style 2D game and took <b>3rd place at a GoMyCode hackathon</b>. At 18 I ran my own small online business, <b>MetaShop</b>. At MedTech I've built a voice-controlled smart house on STM32, a multiplayer game over raw TCP/UDP sockets and an ESP32 Wi-Fi mapper on a custom PCB, and I spent a summer as a <b>cybersecurity intern at Network Associates</b>, securing a real desktop application.</p>
   <p><b>Where I'm heading:</b> I want to work on embedded and connected systems that are secure by design, from firmware up to the cloud. Outside engineering I edit videos – I co-founded <b>Rakcha Koora</b>, a football quiz channel, and was its lead video editor.</p>
   <div class="stat-row">
    <div class="stat"><b>10</b><span>projects on GitHub</span></div>
    <div class="stat"><b>15</b><span>certificates</span></div>
    <div class="stat"><b>1</b><span>internship</span></div>
    <div class="stat"><b>4</b><span>languages</span></div>
   </div>
   <p style="margin-top:16px;color:var(--muted);font-size:15px"><b style="color:var(--soft)">Languages:</b> Arabic · English · French · German (basic)</p>
  </div>
 </div>
</section>

<section>
 <h2>Get in touch</h2>
 <p class="sec-intro">The fastest way to reach me is by e-mail or LinkedIn. All my code is on GitHub.</p>
 <div class="contact-cards">
  <a class="card" id="linkedin" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ic">💼</span><h3>LinkedIn</h3><p>Experience, projects and certifications</p></a>
  <a class="card" id="email" href="mailto:{EMAIL}"><span class="ic">✉️</span><h3>Email</h3><p>{EMAIL}</p></a>
  <a class="card" href="{GH}" target="_blank" rel="noopener"><span class="ic">💻</span><h3>GitHub</h3><p>github.com/amiiinoooo</p></a>
 </div>
</section>

<section>
 <h2>Explore my portfolio</h2>
 <p class="sec-intro">Each page below matches a part of my university journey.</p>
 <div class="grid g2">
  <a class="card" href="academic.html#projects"><h3>🚀 Projects</h3><p>Embedded systems, networking, machine learning and IoT – with slides, reports and code.</p></a>
  <a class="card" href="academic.html#internships"><h3>🔐 Internship</h3><p>Cybersecurity internship at Network Associates, Summer 2025.</p></a>
  <a class="card" href="accomplishments.html"><h3>🏆 Accomplishments</h3><p>Certificates, a hackathon podium, a business and a YouTube channel.</p></a>
  <a class="card" href="cv.html"><h3>📄 CV</h3><p>My one-page CV and video résumé.</p></a>
 </div>
</section>
"""
page("index.html", "About", "Computer Systems Engineering · MedTech – SMU",
     'Hi, I\'m <span class="grad">Amine Ben Nasrallah</span>',
     "Computer Systems Engineering student building embedded systems, networked applications and secure software.", about)

# ======================================================================  CV
cv = f"""
<section id="cv" style="padding-top:10px">
 <h2>Curriculum Vitae</h2>
 <p class="sec-intro">My current one-page CV. You can read it below or download the PDF.</p>
 {links([("⬇ Download CV (PDF)", "assets/docs/Amine-Ben-Nasrallah-CV.pdf"), ("View on LinkedIn", LINKEDIN)])}
 <div style="margin-top:20px"><iframe class="pdf" src="assets/docs/Amine-Ben-Nasrallah-CV.pdf#view=FitH" title="CV of Amine Ben Nasrallah"></iframe></div>
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
     "Education, experience, projects and skills on one page.", cv)

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
cert_html = "".join(
    f'<div class="card cert"><div><h4>{t}</h4><div class="meta">{o} · {d}</div></div><a href="assets/certificates/{f}" target="_blank" rel="noopener">View ↗</a></div>'
    for t, o, d, f in certs)

acc = f"""
<section id="extracurricular" style="padding-top:10px">
 <h2>Extracurricular Activities</h2>
 <p class="sec-intro">What I've built and taken part in outside the classroom.</p>
 <div class="grid g2">
  <div class="card"><span class="badge">Entrepreneurship</span><h3>Founder – MetaShop</h3><div class="meta">Oct 2022 – Jul 2023</div>
   <p>I started and ran MetaShop on my own: an online business selling digital gift cards (PlayStation, Apple, Steam, Epic Games and more) at affordable prices in Tunisia.</p>
   <ul>
    <li>Managed the entire operation: sourcing, pricing, order handling, payments and customer service.</li>
    <li>Processed 86+ orders for 35+ customers, generating ~10K TND in sales – about half of customers came back for repeat orders.</li>
    <li>Promoted it on Instagram with a public reviews section and clear ordering guides to build trust.</li>
    <li>Funded by a private investor.</li>
   </ul>
   {reflect("running a business taught me to own every detail, answer customers fast and keep promises – the same habits I now bring to team projects.")}</div>
  <div class="card"><span class="badge">Media</span><h3>Co-founder & Lead Video Editor – Rakcha Koora</h3><div class="meta">Feb 2024 – Aug 2024</div>
   <p>Co-founded Rakcha Koora, a football quiz channel run by a team of four, where we recorded and played the quizzes on camera.</p>
   <ul>
    <li>Lead video editor for all content: long-form YouTube episodes (25–35 min), YouTube Shorts, Instagram Reels and TikTok videos.</li>
    <li>Managed the channel's social media across YouTube, Instagram and TikTok.</li>
    <li>Reached 23K+ views, 400+ followers and 600+ likes across all platforms.</li>
   </ul>
   {reflect("editing for an audience is about rhythm and clarity – cut what doesn't serve the story. It made me better at presentations and demos too.")}
   {links([("▶ YouTube channel", "https://www.youtube.com/@RakchaKoora")])}</div>
  <div class="card"><span class="badge">University</span><h3>Fitness For Engineering – Podcast</h3><div class="meta">Fall 2026 · COM307</div>
   <p>A 20-minute group podcast on nutrition, physical activity, supplements and healthy habits for engineering students. I presented the nutrition chapter and edited the final video with captions, chapter cards and topic visuals.</p>
   {links([("▶ Watch the podcast", "https://drive.google.com/file/d/1SKUTouVrSy8AX6TrqLF8PAniJvcxRDsR/view?usp=sharing")])}</div>
  <div class="card"><span class="badge">Community</span><h3>Youth Organization – Volunteer</h3><div class="meta">2017 – 2018</div>
   <p>Member of a non-profit youth association promoting education, culture and solidarity.</p></div>
 </div>
</section>

<section id="certificates">
 <h2>Professional Certificates<span class="num">({len(certs)})</span></h2>
 <p class="sec-intro">Online courses from universities and companies that extend what I learn at MedTech. Click to open each certificate.</p>
 <div class="grid g2">{cert_html}</div>
</section>

<section id="rewards">
 <h2>Rewards</h2>
 <p class="sec-intro">Recognition I've received.</p>
 <div class="grid g2">
  <div class="card"><span class="badge gold">🥉 3rd place</span><h3>GoMyCode Hackathon</h3><div class="meta">2019</div><p>Podium finish for a Mario-style 2D game I built at 15 – see Competitions below.</p></div>
  <div class="card"><span class="badge gold">💡 Best Idea</span><h3>Spark Program – BIAT Foundation</h3><div class="meta">2017</div><p>Received the Best Idea certificate in the BIAT Foundation's Spark program.</p></div>
 </div>
</section>

<section id="competitions">
 <h2>Competitions</h2>
 <div class="grid g2">
  <div class="card"><span class="badge gold">🥉 3rd place</span><h3>GoMyCode Hackathon – Mario-style 2D Game</h3><div class="meta">2019 · age 15</div>
   <p>At 15, I built a simple Mario-like 2D game during the GoMyCode hackathon and placed 3rd.</p>
   {reflect("this was the moment I realised I could build something real on my own, under pressure. It's why I chose engineering.")}</div>
 </div>
</section>
"""
page("accomplishments.html", "Accomplishments", "Accomplishments", '<span class="grad">Accomplishments</span>',
     "Extracurricular activities, certificates, rewards and competitions.", acc)

# ======================================================================  ACADEMIC JOURNEY
def project(img, badge, title, meta, desc, tags, lnks, refl=None):
    return f"""<div class="card"><div class="thumb"><img src="assets/img/{img}" alt="{title}"></div>
 <span class="badge">{badge}</span><h3>{title}</h3><div class="meta">{meta}</div><p>{desc}</p>{chips(tags)}{reflect(refl) if refl else ""}{links(lnks)}</div>"""

R = lambda r: f"{GH}/{r}"
B = lambda r, p: f"{GH}/{r}/blob/main/{p}"
projects = "".join([
    project("smarthouse.jpg", "Embedded Systems", "SmartHouse – Voice-Controlled Home on STM32", "ECE355 · Fall 2025 · team of 5",
        "Talk to your house: a mobile app sends voice commands to an n8n workflow running a local LLM (Ollama), which turns them into HTTP commands for an STM32 board. The STM32, programmed in C with an ESP8266 web server, controls the door, window, light and fan.",
        ["C", "STM32", "ESP8266", "n8n", "Ollama"], [("Code", R("smart-house-stm32")), ("Slides", B("smart-house-stm32", "docs/slides.pdf")), ("Report", B("smart-house-stm32", "docs/final-report.pdf"))],
        "connecting an AI layer to real hardware means designing a strict, simple command format – the LLM is flexible, the microcontroller is not."),
    project("rps-arena.jpg", "Networking", "RPS Arena – Multiplayer Game over TCP/UDP", "CS411 Computer Networks · Fall 2026",
        "Real-time rock-paper-scissors built on raw sockets. One Python game server handles accounts, rooms and scores over TCP and heartbeats, chat and countdown over UDP, for both a Tkinter desktop client and a Flask web client published over HTTPS.",
        ["Python", "TCP/UDP", "Flask", "Tkinter", "PBKDF2"], [("Code", R("RPS_arena")), ("Slides", B("RPS_arena", "docs/RPS.pdf")), ("Design doc", B("RPS_arena", "docs/communication-design.pdf"))],
        "choosing TCP or UDP is a trade-off per message type, not per app – reliability for game state, speed for heartbeats."),
    project("wifi-mapper.jpg", "Hardware", "Wi-Fi Signal Mapper – ESP32 on a Custom PCB", "ISS396 Junior Project · Spring 2026",
        "A handheld ESP32 device on a PCB I designed in Altium, in a 3D-printed enclosure. It measures Wi-Fi strength around a building and a Flask back-end with a Tkinter interface turns the readings into a heatmap.",
        ["ESP32", "Altium", "3D printing", "Flask"], [("Code", R("wifi-signal-mapper")), ("Slides", B("wifi-signal-mapper", "docs/presentation.pdf")), ("Report", B("wifi-signal-mapper", "docs/final-report.pdf"))],
        "a PCB forces you to commit early – every mistake costs a re-order, so design reviews matter."),
    project("ml-segments.jpg", "Machine Learning", "Customer Segmentation & Demand Prediction", "CS280 Artificial Intelligence · Spring 2026",
        "On the Online Retail II dataset, I built RFM features and used K-Means to split customers into VIP, Loyal, At-Risk and Lost segments, then compared Logistic Regression, KNN and Random Forest to predict demand.",
        ["Python", "scikit-learn", "pandas", "K-Means"], [("Code", R("customer-segmentation-demand-prediction")), ("Report", B("customer-segmentation-demand-prediction", "docs/report.pdf"))],
        "most of the work in ML is cleaning and shaping the data; the model choice comes last."),
    project("ecosort.jpg", "IoT", "EcoSort – Smart Waste-Sorting Bin", "ISS296 Sophomore Project · Spring 2025",
        "A bin that detects the type of waste with sensors and uses servo flaps to sort it into the right compartment, with a Flask dashboard showing the fill level of each bin. Designed in SolidWorks.",
        ["Raspberry Pi", "Python", "Flask", "MySQL", "SolidWorks"], [("Code", R("ecosort")), ("Slides", B("ecosort", "docs/EcoSort.pdf")), ("Report", B("ecosort", "docs/final-report.pdf"))]),
    project("plugjuice.jpg", "IoT", "PlugJuice – Smart Plug", "ISS196 Freshman Project · Spring 2024",
        "An IoT smart plug that tracks energy consumption in real time, protects against voltage spikes and can be switched remotely, with a consumption dashboard. Enclosure designed in SolidWorks.",
        ["IoT", "JavaScript", "Python", "SolidWorks"], [("Code", R("smart-plug")), ("Slides", f"{GH}/smart-plug/blob/main/docs/PLUG%20JUICE.pdf")]),
    project("carnet.jpg", "Startup", "Carnet – Car-Management App Concept", "ISS197 · Fall 2025",
        "A startup concept for a car-management app: market study, business-opportunity screening, feasibility and a final pitch.",
        ["Design Thinking", "Market study", "Pitch"], [("Project", R("carnet")), ("Pitch deck", B("carnet", "docs/pitch-deck.pdf"))]),
])

academic = f"""
<section id="internships" style="padding-top:10px">
 <h2>Internships</h2>
 <div class="card">
  <div class="thumb" style="aspect-ratio:2/1"><img src="assets/img/hotel-app.jpg" alt="Secure Hotel App project card"></div>
  <span class="badge">Cybersecurity</span><h3>Cybersecurity Internship – Network Associates (NA)</h3>
  <div class="meta">May 2025 – Jul 2025 · Lac 1, Tunis · Hybrid</div>
  <p>I secured a hotel management desktop application built with JavaFX and MySQL:</p>
  <ul>
   <li>Authentication with e-mail verification (expiring one-time codes), BCrypt password hashing and brute-force lockout.</li>
   <li>Role-based access control (staff / client) with a hierarchical request-validation workflow to block privilege escalation.</li>
   <li>Input validation, sanitization and prepared statements on every query to prevent SQL injection.</li>
   <li>Logging, error handling, and credentials moved out of the code into environment variables.</li>
  </ul>
  {chips(["Java", "JavaFX", "MySQL", "BCrypt", "OWASP"])}
  {reflect("security is not a feature you add at the end. Every input, every role and every password path has to be designed for the attacker from day one – and explained clearly to the team.")}
  {links([("Code", R("HospitalManagement")), ("Internship report", f"{GH}/HospitalManagement/blob/master/docs/Amine.BenNasrallah_INT%20101%20-%20Clean.pdf")])}
 </div>
</section>

<section id="projects">
 <h2>Projects</h2>
 <p class="sec-intro">Course and team projects from my years at MedTech, each with its code, slides and report.</p>
 <div class="grid g2">{projects}</div>
 <p class="sec-intro" style="margin-top:20px">More on GitHub: <a href="{R('CareApp')}" target="_blank" rel="noopener">CareApp</a> (installable hydration-reminder web app) · <a href="{R('student-grades-manager')}" target="_blank" rel="noopener">Student Grades Manager</a> (Java).</p>
</section>

<section id="courses">
 <h2>Interesting Courses</h2>
 <p class="sec-intro">Courses that changed how I think about engineering.</p>
 <div class="grid g2">
  <div class="card"><span class="badge">ECE355</span><h3>Embedded Systems</h3>
   <p>Programming an STM32 (ARM Cortex-M4) board in C: GPIO, interrupts and SPI, real-time design with RTOS concepts and system modelling with SysML. The course ended with our SmartHouse project.</p>
   {reflect("reading a datasheet and a reference manual is a skill in itself. Once I could, I stopped guessing and started designing.")}</div>
  <div class="card"><span class="badge">CS321</span><h3>Prompt Engineering</h3>
   <p>How large language models work and how to use them well: prompting techniques, retrieval-augmented generation (RAG) and AI agents. With a teammate I built a RAG workflow in n8n that indexes uploaded PDFs and CSVs in a vector store and answers questions with memory, with file upload through Telegram.</p>
   {reflect("an LLM is only as useful as the context you give it. This course led directly to the n8n + local-LLM brain of our SmartHouse.")}</div>
  <div class="card"><span class="badge">ISS197</span><h3>Startup Engineering</h3>
   <p>From problem to pitch: finding and screening a business opportunity, design thinking, building a prototype story and pitching it. Our team developed Carnet, a car-management app concept, and I completed the University of Virginia's Design Thinking course alongside it.</p>
   {reflect("a good product starts with a real problem and real users, not with the technology I want to use.")}</div>
  <div class="card"><span class="badge">CS331</span><h3>Database Management</h3>
   <p>Entity-relationship modelling, mapping to the relational model, SQL and transactions. I designed complete schemas for a hospital and a university system in MySQL Workbench and completed three practical lab exams.</p>
   {reflect("a clean schema saves hundreds of lines of code later – and it's the base of the SQL-injection defences I used in my internship.")}</div>
 </div>
</section>

<section id="company-visits">
 <h2>Company Visits</h2>
 <div class="grid g2">
  <div class="card"><span class="badge">On-site</span><h3>Network Associates (NA) – Lac 1, Tunis</h3><div class="meta">Summer 2025</div>
   <p>My internship took me inside Network Associates in Tunis, where I saw how a professional IT team organises its work and delivers software.</p>
   {links([("See internship", "#internships")])}</div>
 </div>
</section>
"""
page("academic.html", "Academic Journey", "Academic Journey", 'Academic <span class="grad">Journey</span>',
     "My internship, projects, favourite courses and company visits at MedTech.", academic)

print("built")
