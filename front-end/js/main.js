const slidesContainer = document.querySelector('.slides-container');
const dotsContainer = document.querySelector('.dots');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

let slides = [];
let dots = [];
let index = 0;

// 🏠 URL da sua API local
const API_URL = "http://localhost:5000/pets"; // ajuste conforme o seu endpoint

async function carregarDados() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Erro ao buscar dados");
    const data = await response.json();
    criarSlides(data);
  } catch (error) {
    console.error("Erro ao carregar API:", error);
    slidesContainer.innerHTML = `<p style="text-align:center;">Erro ao carregar dados da API.</p>`;
  }
}

function criarSlides(data) {
  slidesContainer.innerHTML = "";
  dotsContainer.innerHTML = "";

  data.forEach((pet, i) => {
    const slide = document.createElement("div");
    slide.classList.add("slide");
    if (i === 0) slide.classList.add("active");

    slide.innerHTML = `
      <h2>${pet.nome}</h2>
      <p><strong>Espécie:</strong> ${pet.especie}</p>
      <p><strong>Idade:</strong> ${pet.idade} anos</p>
      <p><strong>Localização:</strong> ${pet.localizacao.toUpperCase()}</p>
    `;

    slidesContainer.appendChild(slide);

    const dot = document.createElement("span");
    dot.classList.add("dot");
    if (i === 0) dot.classList.add("active");
    dot.addEventListener("click", () => mostrarSlide(i));
    dotsContainer.appendChild(dot);
  });

  slides = document.querySelectorAll(".slide");
  dots = document.querySelectorAll(".dot");

  iniciarCarrossel();
}

function mostrarSlide(n) {
  slides.forEach(slide => slide.classList.remove("active"));
  dots.forEach(dot => dot.classList.remove("active"));

  slides[n].classList.add("active");
  dots[n].classList.add("active");
  index = n;
}

function proximoSlide() {
  index = (index + 1) % slides.length;
  mostrarSlide(index);
}

function anteriorSlide() {
  index = (index - 1 + slides.length) % slides.length;
  mostrarSlide(index);
}

function iniciarCarrossel() {
  nextBtn.addEventListener("click", proximoSlide);
  prevBtn.addEventListener("click", anteriorSlide);
  setInterval(proximoSlide, 4000);
}

carregarDados();
