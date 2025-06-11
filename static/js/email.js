// enable button when file selected
const fileInput = document.getElementById("emlInput");
const btn       = document.getElementById("scanEmailBtn");
fileInput.onchange = () => btn.disabled = !fileInput.files.length;

// showResult shared helper (already added in app.js last step)
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

// click handler
btn.onclick = async () => {
  const fd = new FormData();
  fd.append("file", fileInput.files[0]);

  const res = await fetch("/api/email", {method:"POST", body: fd});
  const data = await res.json();          // { verdict, confidence }
  showResult("emailResult", data.verdict, data.confidence);
};
