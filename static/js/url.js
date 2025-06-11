const urlInput = document.getElementById("urlInput");
const scanBtn  = document.getElementById("scanUrlBtn");

// enable button when something is typed
urlInput.oninput = () => scanBtn.disabled = urlInput.value.trim() === "";

// helper from app.js (already defined there)
function showResult(id, verdict, conf) {
  const el = document.getElementById(id);
  const colour = verdict === "Phishing" ? "danger" : "success";
  el.className = `alert alert-${colour}`;
  el.innerHTML = `
     <h5>${verdict}</h5>
     <div class="progress my-2" style="height:8px">
       <div class="progress-bar bg-${colour}" style="width:${conf*100}%"></div>
     </div>
     <small>Confidence ${(conf*100).toFixed(1)}%</small>`;
  el.classList.remove("d-none");
}

scanBtn.onclick = async () => {
  const url = urlInput.value.trim();
  const res  = await fetch("/api/url", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({url})
  });
  const data = await res.json();
  showResult("urlResult", data.verdict, data.confidence);
};
