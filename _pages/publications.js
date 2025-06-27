fetch('publications.json')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById("pubs");
    list.innerHTML = '';
    data.forEach(pub => {
      const li = document.createElement("li");
      li.innerHTML = `<strong>${pub.title}</strong> (${pub.year}), <em>${pub.venue}</em> - <a href="${pub.url}" target="_blank">lien</a>`;
      list.appendChild(li);
    });
  })
  .catch(err => {
    document.getElementById("pubs").innerText = "Erreur de chargement des publications.";
    console.error(err);
  });
