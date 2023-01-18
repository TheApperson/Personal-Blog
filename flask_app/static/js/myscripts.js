function myFunction(id) {
    var dots = document.getElementById("dots-"+id);
    var moreText = document.getElementById("more-"+id);
    var btnText = document.getElementById("myBtn-"+id);

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more"; 
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "Read less"; 
        moreText.style.display = "inline";
    }
}


const grid = document.querySelector(".gridContainer");
const userInput = document.getElementById("quantity");
const resetButton = document.querySelector(".reset");

createGrid = () => {
for (let i = 0; i < 256; i++) {
    const div = document.createElement("div");
    div.classList.add("square");
    grid.appendChild(div);
}
};

updateGrid = () => {
grid.innerHTML = "";
grid.style.setProperty(
    "grid-template-columns",
    `repeat(${userInput.value}, 2fr)`
);
grid.style.setProperty(
    "grid-template-rows",
    `repeat(${userInput.value}, 2fr)`
);
for (let i = 0; i < userInput.value * userInput.value; i++) {
    const div = document.createElement("div");
    div.classList.add("square");
    grid.appendChild(div);
}
console.log(userInput.value);
};

const square = document.querySelector("div");
square.addEventListener("mouseover", function(event) {
event.target.classList.replace("square", "color");
});
const square2 = document.querySelector("div");
square.addEventListener("click", function(event) {
event.target.classList.replace("color", "square");
});
const square3= document.querySelector("div");
square.addEventListener("mouseout", function(event) {
event.target.classList.replace("color", "square2");
});


userInput.addEventListener("change", updateGrid);

resetButton.addEventListener("click", function() {
grid.innerHTML = "";
userInput.value = "";
grid.style.setProperty("grid-template-columns", `repeat(16, 2fr)`);
grid.style.setProperty("grid-template-rows", `repeat(16, 2fr)`);
createGrid();
});

createGrid();