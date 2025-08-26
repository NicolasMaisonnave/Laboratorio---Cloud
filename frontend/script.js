// ====== CONFIG ======
const API_BASE = "http://localhost:7071/api"; // ← cambia esto

// ====== HELPERS ======
function $(id) { return document.getElementById(id); }
function setStatusOp(id) { $("opId").textContent = `op: ${id}`; }

async function callGetNews(country, q) {
const url = new URL(`${API_BASE}/GetNews`);
if (country) url.searchParams.set("country", country);
if (q) url.searchParams.set("q", q);


const res = await fetch(url.toString(), {
method: "GET",
headers: { "Accept": "application/json" },
// Importante: habilita CORS en la Function App para el dominio de tu Static Website
});
if (!res.ok) throw new Error(`GetNews falló (${res.status})`);
return res.json();
}


async function callLogAccess(operationId, extra = {}) {
const res = await fetch(`${API_BASE}/LogAccess`, {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ operationId, ...extra }),
});
if (!res.ok) throw new Error(`LogAccess falló (${res.status})`);
return res.json();
}

function renderHeadlines(headlines) {
const ul = $("newsList");
ul.innerHTML = "";
for (const h of headlines) {
const li = document.createElement("li");
const title = h.title || "(sin título)";
const source = h.source?.name ? ` — ${h.source.name}` : "";
const link = h.url ? `<a href="${h.url}" target="_blank" rel="noopener">ver</a>` : "";
li.innerHTML = `<strong>${title}</strong>${source}<br>${link}`;
ul.appendChild(li);
}
}

// ====== MAIN ======
$("btnLoad").addEventListener("click", async () => {
const operationId = crypto.randomUUID();
setStatusOp(operationId);


const country = $("country").value;
const q = $("q").value.trim();


try {
const data = await callGetNews(country, q);
const headlines = data?.articles || [];
renderHeadlines(headlines);


// Registrar acceso (no bloqueante)
callLogAccess(operationId, { count: headlines.length, country, q }).catch(console.warn);
} catch (err) {
alert(err.message);
}
});