# flask app to run on a server
# hardcode server name at the top to differentiate each server
# how to run
# 1 create virtualenv optional
# 2 pip install flask
# 3 python onepage_flask_server_app.py

from flask import Flask, render_template_string

# hardcode this value to differentiate servers
SERVER_NAME = "Server 1"

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Netflix - Demo</title>
  <style>
    :root{--bg:#0b0b0b;--accent:#e50914;--muted:#b3b3b3}
    *{box-sizing:border-box}
    body {margin:0;font-family:Inter, Arial,Helvetica,sans-serif;background-color:var(--bg);color:#fff}
    header{display:flex;align-items:center;justify-content:space-between;padding:18px 32px;background:linear-gradient(90deg,rgba(0,0,0,0.6),transparent)}
    .brand{display:flex;align-items:center;gap:18px}
    .logo{color:var(--accent);font-weight:800;font-size:26px;letter-spacing:2px}
    .server-name{color:var(--muted);font-size:14px}
    nav a{color:#fff;margin-left:18px;text-decoration:none;font-weight:600;opacity:0.9}
    nav a:hover{opacity:1}

    .hero{position:relative;height:66vh;display:flex;align-items:flex-end;padding:48px;background-size:cover;background-position:center;border-bottom:6px solid rgba(0,0,0,0.6)}
    .hero::after{content:'';position:absolute;left:0;right:0;top:0;bottom:0;background:linear-gradient(180deg,rgba(0,0,0,0.25),rgba(0,0,0,0.75));}
    .hero-content{position:relative;max-width:1100px;z-index:2}
    .hero h2{font-size:56px;margin:0 0 12px}
    .hero p{max-width:700px;color:var(--muted);margin:0 0 18px}
    .hero .cta{display:flex;gap:12px}
    .btn{background:var(--accent);padding:12px 20px;border-radius:6px;border:none;color:white;font-weight:700;cursor:pointer}
    .btn.ghost{background:rgba(255,255,255,0.12)}

    .container{padding:28px 32px}
    .section{margin-bottom:28px}
    .section h3{margin:0 0 12px;font-size:20px}
    .row{display:flex;gap:16px;overflow-x:auto;padding-bottom:8px}
    .card{flex:0 0 180px;border-radius:8px;overflow:hidden;background:#111;min-height:270px;box-shadow:0 10px 30px rgba(0,0,0,0.6);transition:transform .18s ease;cursor:pointer}
    .card:hover{transform:translateY(-8px)}
    .card img{width:100%;height:270px;object-fit:cover;display:block}
    .card .meta{padding:8px 10px;background:linear-gradient(180deg,transparent,rgba(0,0,0,0.6));font-size:13px;color:var(--muted)}

    /* modal */
    .modal{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.75);visibility:hidden;opacity:0;transition:opacity .18s ease,visibility .18s}
    .modal.open{visibility:visible;opacity:1}
    .modal-card{background:#0f0f0f;width:min(920px,96%);border-radius:10px;overflow:hidden;display:flex;gap:20px}
    .modal-card img{width:360px;height:520px;object-fit:cover}
    .modal-body{padding:20px;color:#ddd}
    .meta-row{display:flex;gap:12px;color:var(--muted);margin:8px 0}
    .close{position:absolute;top:18px;right:24px;font-size:28px;color:#fff;cursor:pointer}

    footer{padding:18px 32px;color:var(--muted);font-size:14px;border-top:1px solid rgba(255,255,255,0.02)}

    @media(max-width:900px){.modal-card{flex-direction:column}.modal-card img{width:100%;height:320px}}
  </style>
</head>
<body>
  <header>
    <div class="brand">
      <div class="logo">NETFLIX</div>
      <div style="display:flex;flex-direction:column">
        <div style="font-weight:700">Home</div>
        <div class="server-name">Server: {{ server_name }}</div>
      </div>
    </div>
    <nav>
      <a href="#">TV Shows</a>
      <a href="#">Movies</a>
      <a href="#">Latest</a>
      <a href="#">My List</a>
    </nav>
  </header>

  <!-- hero with cover image - replace URL if you want a custom cover -->
  <div class="hero" style="background-image:url('https://images.unsplash.com/photo-1517602302552-471fe67acf66?auto=format&fit=crop&w=1400&q=80')">
    <div class="hero-content">
      <h2>Unlimited movies, TV shows and more</h2>
      <p>Watch anywhere. Cancel anytime. This is a demo homepage to run on each server. Click any poster to see details.</p>
      <div class="cta">
        <button class="btn">Play</button>
        <button class="btn ghost">More Info</button>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="section">
      <h3>Popular on Netflix</h3>
      <div class="row" id="popular">
        <!-- each card has data attributes for modal -->
        <div class="card" tabindex="0" data-title="Inception" data-year="2010" data-rating="8.8" data-desc="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO." data-img="https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=101'" alt="Inception"><div class="meta">Inception · 2010</div></div>

        <div class="card" tabindex="0" data-title="The Dark Knight" data-year="2008" data-rating="9.0" data-desc="When the menace known as the Joker emerges, he wreaks havoc and chaos on the people of Gotham." data-img="https://m.media-amazon.com/images/I/81aA7hEEykL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81aA7hEEykL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=102'" alt="Dark Knight"><div class="meta">The Dark Knight · 2008</div></div>

        <div class="card" tabindex="0" data-title="Interstellar" data-year="2014" data-rating="8.6" data-desc="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival." data-img="https://m.media-amazon.com/images/I/91KkWf50SoL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/91KkWf50SoL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=103'" alt="Interstellar"><div class="meta">Interstellar · 2014</div></div>

        <div class="card" tabindex="0" data-title="Joker" data-year="2019" data-rating="8.5" data-desc="In Gotham City, mentally troubled comedian Arthur Fleck embarks on a downward spiral that leads to the birth of an iconic villain." data-img="https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=104'" alt="Joker"><div class="meta">Joker · 2019</div></div>

        <div class="card" tabindex="0" data-title="The Matrix" data-year="1999" data-rating="8.7" data-desc="A computer hacker learns about the true nature of his reality and his role in the war against its controllers." data-img="https://m.media-amazon.com/images/I/81Y3VY6T8LL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81Y3VY6T8LL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=105'" alt="Matrix"><div class="meta">The Matrix · 1999</div></div>

        <div class="card" tabindex="0" data-title="Fight Club" data-year="1999" data-rating="8.8" data-desc="An insomniac office worker and a devil-may-care soap maker form an underground fight club." data-img="https://m.media-amazon.com/images/I/81Zt42ioCgL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81Zt42ioCgL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=106'" alt="Fight Club"><div class="meta">Fight Club · 1999</div></div>
      </div>
    </div>

    <div class="section">
      <h3>Trending Now</h3>
      <div class="row" id="trending">
        <div class="card" tabindex="0" data-title="Spider-Man: No Way Home" data-year="2021" data-rating="8.3" data-desc="Peter Parker seeks help from Doctor Strange after his identity is revealed, accidentally breaking the multiverse." data-img="https://m.media-amazon.com/images/I/81GkA2e8F-L._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81GkA2e8F-L._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=107'" alt="Spider-Man"><div class="meta">Spider-Man · 2021</div></div>

        <div class="card" tabindex="0" data-title="Black Panther" data-year="2018" data-rating="7.3" data-desc="T'Challa returns home to the African nation of Wakanda to take his rightful place as king." data-img="https://m.media-amazon.com/images/I/91vr9wL1pZL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/91vr9wL1pZL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=108'" alt="Black Panther"><div class="meta">Black Panther · 2018</div></div>

        <div class="card" tabindex="0" data-title="Doctor Strange" data-year="2016" data-rating="7.5" data-desc="A surgeon learns the mystic arts and defends the world from magical threats." data-img="https://m.media-amazon.com/images/I/91vKejH5uDL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/91vKejH5uDL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=109'" alt="Doctor Strange"><div class="meta">Doctor Strange · 2016</div></div>

        <div class="card" tabindex="0" data-title="Thor: Ragnarok" data-year="2017" data-rating="7.9" data-desc="Thor must escape the alien planet Sakaar and return to Asgard to stop Ragnarok." data-img="https://m.media-amazon.com/images/I/81AIq9f0a2L._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81AIq9f0a2L._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=110'" alt="Thor"><div class="meta">Thor: Ragnarok · 2017</div></div>

        <div class="card" tabindex="0" data-title="Iron Man" data-year="2008" data-rating="7.9" data-desc="After being held captive, Tony Stark builds a high-tech suit to escape and becomes Iron Man." data-img="https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=111'" alt="Iron Man"><div class="meta">Iron Man · 2008</div></div>
      </div>
    </div>

    <div class="section">
      <h3>TV Shows You Might Like</h3>
      <div class="row" id="tvshows">
        <div class="card" tabindex="0" data-title="Stranger Things" data-year="2016" data-rating="8.7" data-desc="When a young boy disappears, his mother and friends encounter secret experiments and supernatural forces." data-img="https://m.media-amazon.com/images/I/81v+o5u9H9L._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81v+o5u9H9L._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=112'" alt="Stranger Things"><div class="meta">Stranger Things · 2016</div></div>

        <div class="card" tabindex="0" data-title="Breaking Bad" data-year="2008" data-rating="9.5" data-desc="A chemistry teacher diagnosed with cancer turns to manufacturing meth to secure his family's future." data-img="https://m.media-amazon.com/images/I/81dQwQlmAXL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81dQwQlmAXL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=113'" alt="Breaking Bad"><div class="meta">Breaking Bad · 2008</div></div>

        <div class="card" tabindex="0" data-title="Money Heist" data-year="2017" data-rating="8.3" data-desc="A criminal mastermind assembles a group to carry out the biggest heist in Spain's history." data-img="https://m.media-amazon.com/images/I/81+Z8i0N6vL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81+Z8i0N6vL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=114'" alt="Money Heist"><div class="meta">Money Heist · 2017</div></div>

        <div class="card" tabindex="0" data-title="The Crown" data-year="2016" data-rating="8.7" data-desc="Chronicles the life of Queen Elizabeth II from the 1940s to modern times." data-img="https://m.media-amazon.com/images/I/81b0D6x5Y9L._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81b0D6x5Y9L._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=115'" alt="The Crown"><div class="meta">The Crown · 2016</div></div>

        <div class="card" tabindex="0" data-title="The Witcher" data-year="2019" data-rating="8.2" data-desc="A mutated monster-hunter struggles to find his place in a world where people often prove more wicked than beasts." data-img="https://m.media-amazon.com/images/I/81YF1pE0OtL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/81YF1pE0OtL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=116'" alt="The Witcher"><div class="meta">The Witcher · 2019</div></div>

        <div class="card" tabindex="0" data-title="House of Cards" data-year="2013" data-rating="8.7" data-desc="A Congressman works with his equally conniving wife to exact revenge on those who betrayed him." data-img="https://m.media-amazon.com/images/I/91uwocAMtSL._AC_SY679_.jpg"><img loading="lazy" src="https://m.media-amazon.com/images/I/91uwocAMtSL._AC_SY679_.jpg" onerror="this.onerror=null;this.src='https://picsum.photos/360/520?random=117'" alt="House of Cards"><div class="meta">House of Cards · 2013</div></div>
      </div>
    </div>

  </div>

  <footer>
    Netflix demo homepage | Server: {{ server_name }}
  </footer>

  <!-- modal for details -->
  <div id="modal" class="modal" role="dialog" aria-hidden="true">
    <div class="close" id="modalClose">×</div>
    <div class="modal-card" role="document">
      <img id="modalImg" src="" alt="poster">
      <div class="modal-body">
        <h2 id="modalTitle">Title</h2>
        <div class="meta-row"><div id="modalYear"></div><div id="modalRating"></div></div>
        <p id="modalDesc" style="line-height:1.4;color:#ddd"></p>
      </div>
    </div>
  </div>

  <script>
    // attach click handler to cards
    document.addEventListener('click', function(e){
      const card = e.target.closest('.card')
      if(card){ openModalFromCard(card) }
    })

    // keyboard and close
    const modal = document.getElementById('modal')
    const modalClose = document.getElementById('modalClose')
    modalClose.addEventListener('click', closeModal)
    modal.addEventListener('click', function(e){ if(e.target === modal) closeModal() })
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeModal() })

    function openModalFromCard(card){
      const title = card.getAttribute('data-title')
      const year = card.getAttribute('data-year')
      const rating = card.getAttribute('data-rating')
      const desc = card.getAttribute('data-desc')
      const img = card.getAttribute('data-img')
      document.getElementById('modalTitle').textContent = title
      document.getElementById('modalYear').textContent = year
      document.getElementById('modalRating').textContent = 'Rating: ' + rating
      document.getElementById('modalDesc').textContent = desc
      const modalImg = document.getElementById('modalImg')
      modalImg.src = img
      modalImg.onerror = function(){ this.onerror=null; this.src='https://picsum.photos/360/520?random=999' }
      modal.classList.add('open')
      modal.setAttribute('aria-hidden','false')
    }

    function closeModal(){
      modal.classList.remove('open')
      modal.setAttribute('aria-hidden','true')
    }

    // lazy load images attribute
    document.addEventListener('DOMContentLoaded', function(){
      document.querySelectorAll('img').forEach(img => img.loading = 'lazy')
    })
  </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE, server_name=SERVER_NAME)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
