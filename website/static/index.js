function deleteNote(note, date) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ note: note, date: date }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
