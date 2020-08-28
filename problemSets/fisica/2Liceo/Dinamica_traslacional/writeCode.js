const code = document.querySelector("#codigo").innerHTML;
// let hideInput = function () {
//   let iframe = document.getElementById("forma");
//   let innerDoc = iframe.contentDocument || iframe.contentWindow.document;
//   console.log(innerDoc.body);
//   //   let inputs = document.querySelectorAll(
//   //     ".freebirdFormviewerViewNumberedItemContainer"
//   //   );
//   //   console.log(inputs[1]);
// };
// forma.onload = hideInput;
forma = document.querySelector("#forma");
forma.src = `https://docs.google.com/forms/d/e/1FAIpQLScuvuS1GZBAbo6jlIs7CYTULXN9oMTftKCQuBQ2-IBf7_GQIg/viewform?embedded=true&entry.19815533=${code}`;
