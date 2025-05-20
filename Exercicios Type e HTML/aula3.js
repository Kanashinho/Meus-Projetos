const numero = Number(prompt("Escolha seu numero:"));
const tilte = document.getElementById("title");
const texto = document.getElementById("text");

title.innerHTML= numero;
texto.innerHTML = ``;
texto.innerHTML += `<p>A raiz quadrada do seu número é: ${numero ** 0.5}</p>`;
texto.innerHTML += `<p>${numero} é inteiro: ${Number.isInteger(numero)}</p>`;
texto.innerHTML += `<p>:Arredondando para cima ${Math.ceil(numero)}</p>`;
texto.innerHTML += `<p>:Arredondando para baixo ${Math.floor(numero)}</p>`;
texto.innerHTML += `<p>A raiz quadrada do seu número é: ${numero.toFixed(2)}</p>`;
