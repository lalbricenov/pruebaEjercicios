let sols = document.querySelectorAll(".imgSol");
let solButtons = document.querySelectorAll(".butSol");

const N = solButtons.length;

let show = function (e) {
  let numQ = parseInt(e.srcElement.id.slice(-1));
  console.log(`Mostrar solución de pregunta numero ${numQ}`);
  sols[numQ - 1].style.display = "block";
  e.srcElement.innerHTML = "Ocultar solución";
  e.srcElement.onclick = hide;
};

let hide = function (e) {
  let numQ = parseInt(e.srcElement.id.slice(-1));
  console.log(`Ocultar solución de pregunta numero ${numQ}`);
  //   console.log(sols);
  sols[numQ - 1].style.display = "none";
  e.srcElement.innerHTML = "Ver solución";
  e.srcElement.onclick = show;
};

for (let i = 0; i < N; i++) {
  solButtons[i].onclick = show;
}
