
function mostrar_ocultar(elemento) {
    let hijo = elemento.children[0];
    let padre_padre = elemento.parentNode.parentNode.parentNode;
    let hijoConClase = padre_padre.querySelector(".subs");

    if (hijoConClase.classList.contains("d-none")) {
        hijo.style.color = "#fe6d20";
        hijoConClase.classList.remove("d-none");
        hijoConClase.style.opacity = 0;
        hijoConClase.style.transform = "translateY(-10px)";
        hijoConClase.offsetHeight;
        hijoConClase.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        hijoConClase.style.opacity = 1;
        hijoConClase.style.transform = "translateY(0)";
    } else {
        hijo.style.color = "#878787";
        hijoConClase.style.transition = "opacity 0.5s ease, transform 0.5s ease";
        hijoConClase.style.opacity = 0;
        hijoConClase.style.transform = "translateY(-10px)";
        setTimeout(() => {
            hijoConClase.classList.add("d-none");
        }, 500);
    }
}

