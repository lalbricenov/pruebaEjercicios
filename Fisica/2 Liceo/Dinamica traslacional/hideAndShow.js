let sols = document.querySelectorAll(".imgSol");
let solButtons = document.querySelectorAll(".butSol");

const N = solButtons.length;

let show = function (e) {
  let numQ = parseInt(e.srcElement.id.slice(-1));
  console.log(`Pregunta numero ${numQ}`);
  console.log(sols);
  sols[numQ - 1].style.display = "block";
};

for (let i = 0; i < N; i++) {
  solButtons[i].onclick = show;
}
