from flask import Flask, render_template_string, url_for
import socket
import datetime

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>StreamMock</title>
  <style>
    :root{
      --bg: #0f1720;
      --card: #0b1220;
      --accent: #00b0ff;
      --muted: #9aa6b2;
      --glass: rgba(255,255,255,0.04);
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg, var(--bg) 0%, #071018 100%);
      color:#e6eef6;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }
    header{
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:18px 28px;
      position:sticky;
      top:0;
      backdrop-filter: blur(6px);
      background: linear-gradient(180deg, rgba(3,6,10,0.6), rgba(3,6,10,0.15));
      z-index:10;
      border-bottom: 1px solid rgba(255,255,255,0.03);
    }
    .brand{display:flex;align-items:center;gap:12px}
    .logo{
      width:40px;height:40px;border-radius:6px;
      background: linear-gradient(135deg,#123a5f,var(--accent));
      display:inline-flex;align-items:center;justify-content:center;font-weight:700;color:white;
      box-shadow: 0 4px 18px rgba(0,0,0,0.6);
    }
    nav a{color:var(--muted);margin-right:18px;text-decoration:none;font-weight:600}
    .hostname{
      font-size:13px;
      background:var(--glass);
      padding:8px 12px;border-radius:12px;color:var(--muted);
      display:inline-flex;align-items:center;gap:8px;
    }
    main{padding:28px}
    .hero{
      display:grid;
      grid-template-columns: 1fr 360px;
      gap:24px;
      margin-bottom:28px;
    }
    .hero-card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
      padding:22px;border-radius:12px;box-shadow: 0 8px 30px rgba(2,6,12,0.6);
      display:flex;gap:18px;align-items:center;
    }
    .poster{
      width:280px;height:160px;border-radius:8px;flex-shrink:0;background-size:cover;background-position:center;
      box-shadow: 0 10px 30px rgba(2,6,12,0.7);
    }
    .meta h1{margin:0;font-size:26px}
    .meta p{color:var(--muted);margin:8px 0 14px}
    .btn{
      display:inline-block;padding:10px 16px;border-radius:8px;font-weight:700;
      background:var(--accent);color:#022; text-decoration:none;
      box-shadow: 0 6px 18px rgba(0,176,255,0.12);
    }
    .side-card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
      padding:16px;border-radius:12px;height:100%;
    }
    .row{margin-top:18px}
    .row h3{margin:8px 0 12px}
    .thumbnails{
      display:flex;gap:12px;overflow-x:auto;padding-bottom:6px;
    }
    .thumb{
      min-width:160px;height:92px;border-radius:8px;background-size:cover;background-position:center;flex:0 0 auto;
      box-shadow: 0 8px 24px rgba(2,6,12,0.6);
      position:relative;
    }
    .thumb .label{
      position:absolute;left:8px;bottom:8px;background:rgba(0,0,0,0.5);padding:6px 8px;border-radius:6px;font-size:13px;
    }
    footer{padding:28px;color:var(--muted);border-top:1px solid rgba(255,255,255,0.02);margin-top:28px}
    /* scrollbar small */
    .thumbnails::-webkit-scrollbar{height:8px}
    .thumbnails::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.06);border-radius:999px}
    @media(max-width:900px){
      .hero{grid-template-columns:1fr}
      .poster{width:180px;height:110px}
    }
  </style>
</head>
<body>
  <header>
    <div class="brand">
      <div class="logo">SM</div>
      <div>
        <div style="font-weight:800;font-size:18px">StreamMock</div>
        <div style="color:var(--muted);font-size:13px">Your sample streaming UI</div>
      </div>
    </div>

    <nav>
      <a href="#">Home</a>
      <a href="#">Movies</a>
      <a href="#">TV</a>
      <a href="#">My List</a>
    </nav>

    <div class="hostname">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="opacity:.85"><path d="M12 2L2 7v7c0 5 5 9 10 9s10-4 10-9V7l-10-5z" stroke="white" stroke-opacity=".9" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Host: {{ hostname }}
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="hero-card">
        <div class="poster" style="background-image:url('https://picsum.photos/seed/hero/800/450')"></div>
        <div class="meta">
          <h1>Featured: The Sample Story</h1>
          <p>Watch the critically acclaimed sample series. A demo layout to showcase a streaming grid, hero and playback button.</p>
          <div style="display:flex;gap:12px;align-items:center">
            <a class="btn" href="#">Play</a>
            <div style="color:var(--muted)">• 2h 12m • 2024 • Drama</div>
          </div>
        </div>
      </div>

      <aside class="side-card">
        <div style="font-weight:700;margin-bottom:8px">Now Showing</div>
        <div style="display:flex;gap:8px;flex-direction:column">
          <div style="display:flex;gap:8px;align-items:center">
            <div style="width:56px;height:56px;border-radius:6px;background-image:url('https://picsum.photos/seed/1/200/200');background-size:cover"></div>
            <div>
              <div style="font-weight:700">Sample Film 1</div>
              <div style="color:var(--muted);font-size:13px">PG • 1h 45m</div>
            </div>
          </div>

          <div style="display:flex;gap:8px;align-items:center">
            <div style="width:56px;height:56px;border-radius:6px;background-image:url('https://picsum.photos/seed/2/200/200');background-size:cover"></div>
            <div>
              <div style="font-weight:700">Sample Film 2</div>
              <div style="color:var(--muted);font-size:13px">PG-13 • 2h 4m</div>
            </div>
          </div>

          <div style="margin-top:12px;color:var(--muted);font-size:13px">Server time: {{ now }} </div>
        </div>
      </aside>
    </section>

    {% for row_title, seeds in rows %}
      <div class="row">
        <h3>{{ row_title }}</h3>
        <div class="thumbnails">
          {% for s in seeds %}
            <div class="thumb" style="background-image:url('https://picsum.photos/seed/{{ s }}/400/240')">
              <div class="label">Sample {{ loop.index }}</div>
            </div>
          {% endfor %}
        </div>
      </div>
    {% endfor %}

    <footer>
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>StreamMock — demo streaming UI inspired layout</div>
        <div style="color:var(--muted)">Hostname: <strong>{{ hostname }}</strong></div>
      </div>
    </footer>
  </main>
</body>
</html>
"""

@app.route("/")
def index():
    hostname = socket.gethostname()
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    # Create a few sample rows with unique seeds for images
    rows = [
        ("Top picks for you", list(range(101, 110))),
        ("Trending now", list(range(201, 210))),
        ("Watch it again", list(range(301, 309))),
    ]
    return render_template_string(TEMPLATE, hostname=hostname, rows=rows, now=now)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
