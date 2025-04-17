document.getElementById("send").addEventListener("click", async () => {
  const res = await fetch("http://127.0.0.1:5000/api/hello");
  const data = await res.json();
  document.getElementById("response").innerText = data.message;
});
