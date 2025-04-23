//1. convertir la siguiente funcion a una funcion flecha  ennuna solo linea sin llaves(1p)
function esPar(numero) {
    if (numero % 2 === 0) {
      return true;
    } else {
      return false;
    }
  }

const esPar = (numero)=>numero%2===0; //Resuelto
console.log(esPar(1)) ;


//2. Crear unha funcion callback que acepte un arreglo de numeros y una funcion callback donde duplique cada elemento del arreglo 

function duplicarArreglo(arreglo, callback) //Resuelto
{
  for (let i = 0; i < arreglo.length; i++) 
  {
      callback(arreglo[i]);
  }
}
duplicarArreglo([1, 2, 3, 4],(numero)=>console.log("Elemento duplicado:", numero * 2));


//3. Usando los metodos setTimeOut y setInterval crear un contador que disminuya del 5 al 0 

let contador = 5; //Resuelto

let idIntervalo = setInterval(function () 
{
  console.log("Contador:", contador);
  contador --;

    if (contador < 0) 
      {
        clearInterval(idIntervalo);
        console.log("¡Se lllego al numero 0!");
      }
}, 1000);


// Dado el siguiente arreglo:
const libros = [
    { id: 1, titulo: "Cien años de soledad", autor: "Gabriel García Márquez", año: 1967 },
    { id: 2, titulo: "La casa de lo Espiritus", autor: "Isabel Allende", año: 1982 },
    { id: 3, titulo: "Rayuela", autor: "Julio Cortázar", año: 1963 },
    { id: 4, titulo: "El código Da Vinci", autor: "Dan Brown", año: 2005 }
  ];


//4. Cambiar el nombre del libro con id 3 a Final del juego usando for..of

for (let libro of libros) {
  if (libro.id === 3) {
      libro.titulo = "Final del juego";
  }
}

console.log(libros);


//5. Crear una  funcion que muestre solo los titulos de arreglo libros usando for..of

function mostrarTitulos(libros) {
  for (let libro of libros) {
      console.log("Título:", libro.titulo);
  }
}

mostrarTitulos(libros);

