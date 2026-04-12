let valueBox = document.getElementById("value-box");
let lastInputBox = document.getElementById("previous-input");
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
    valueBox.textContent = `${currentInput}`
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
    lastInputBox.textContent = `${lastInput}${currentOperation}`;
    valueBox.textContent = "0"
}

function instantOperation(type) {
    let result;
    switch (type) {
        case "1/x":
            result = 1/currentInput;
            break;
        case "x2":
            result = currentInput * currentInput;
            break;
        case "sqrt":
            result = Math.sqrt(currentInput)
            break;
        default:
            return;
    }
    if (result) {
        currentInput = result
        valueBox.textContent = `${currentInput}`
    }
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
    lastInputBox.textContent = ""
}


function backOne() {
    let lastElement = valueBox.textContent.slice(-1)
    console.log(typeof lastElement)
    if (!"+-/*".includes(lastElement)) {
        currentInput = currentInput.slice(0, -1)
        console.log(currentInput)
        valueBox.textContent = valueBox.textContent.slice(0, -1);
    }
    console.log(lastElement)
}

function clearDisplay() {
    currentInput = '';
    lastInput = '';
    currentOperation = '';
    valueBox.textContent = "0";
    lastInputBox.textContent = "";
}

function equals() {
    calculate()
}