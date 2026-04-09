let valueBox = document.getElementById("value-box");
let lastOperation = ""
let currentOperation = ""
let lastInput = ""
let currentInput = ""

let boxValue = ""

function addnumber(numberToAdd) {
    if (numberToAdd != 0) {
        boxValue += numberToAdd
        currentInput += numberToAdd
    }
    else if (boxValue.length > 0) {
        boxValue += numberToAdd
        currentInput += numberToAdd
    }
    valueBox.textContent = `${lastInput}${currentOperation}${currentInput}`
    console.log(valueBox)
}

function operation(operationType) {
    if (currentInput === "") return;
    if (lastInput !== "") {
        calculate(); 
    }
    currentOperation = operationType;
    lastInput = currentInput;
    currentInput = "";
    valueBox.textContent = `${lastInput}${currentOperation}`;
}

function calculate() {
    if (lastInput === '' || currentInput === '') return;
    let result = "";
    let first = parseFloat(lastInput);
    let scnd = parseFloat(currentInput);

    switch (currentOperation) {
        case "+":
            result = first + scnd;
            break;
        case "-":
            result = first - scnd;
            break;
        case "*":
            result = first * scnd;
            break;
        case "/":
            if (scnd === 0) {
                alert("Nie można dzielić przez 0!");
                return;
            }
            result = first / scnd;
            break;
        default:
    }

    currentInput = result.toString();
    currentOperation = "";
    lastInput = "";
    valueBox.textContent = `${currentInput}`
}


function backOne() {
    let lastElement = parseInt(valueBox.textContent.slice(-1))
    console.log(typeof lastElement)
    if (typeof lastElement === "number") {
        currentInput = currentInput.slice(0, -1)
        console.log(currentInput)
    } else if (("+-/*").includes(type)) {
        currentOperation = "backed"
    }
    valueBox.textContent = valueBox.textContent.slice(0, -1);
    console.log(lastElement)
}

function clearDisplay() {
    currentInput = '';
    lastInput = '';
    currentOperation = '';
    valueBox.textContent = "0";
}

function equals() {
    calculate()
}