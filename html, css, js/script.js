let valueBox = document.getElementById("value-box");
let lastInputBox = document.getElementById("previous-input");
let lastOperation = "";
let currentOperation = "";
let lastInput = "";
let currentInput = "";

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
    addToHistory(first, currentOperation, scnd, result);
    currentInput = result.toString();
    currentOperation = "";
    lastInput = "";
    valueBox.textContent = `${currentInput}`
    lastInputBox.textContent = ""
}


function backOne() {
    let lastElement = valueBox.textContent.slice(-1)
    if (!"+-/*".includes(lastElement)) {
        currentInput = currentInput.slice(0, -1)
        valueBox.textContent = valueBox.textContent.slice(0, -1);
    }
}

function clearDisplay() {
    currentInput = '';
    lastInput = '';
    currentOperation = '';
    valueBox.textContent = "0";
    lastInputBox.textContent = "";
}

function clearEntry() {
    currentInput = '';
    valueBox.textContent = "0";
}

function equals() {
    calculate()
}

function charChange() {
    let inputValue = parseFloat(currentInput)
    let result = inputValue * (-1)
    currentInput = result
    valueBox.textContent = result
}

function addToHistory(first, operator, scnd, result) {
    const clearHistoryBtn = document.getElementById("clearHistory-btn")
    const historyTab = document.getElementById("history-tab");

    const button = document.createElement("button");
    button.classList.add("equation-btn");

    button.innerHTML = `
        <div class="equation">${first} ${operator} ${scnd} =</div>
        <div class="result">${result}</div>
    `;

    button.addEventListener("click", historyBtnClick);

    historyTab.appendChild(button);
    clearHistoryBtn.style.display = "block";
}

function historyBtnClick(event) {
    const button = event.currentTarget;

    const equationText = button.querySelector(".equation").textContent;
    const resultText = button.querySelector(".result").textContent;

    const parts = equationText.replace("=", "").trim().split(" ");

    const first = parts[0];
    const operator = parts[1];
    const second = parts[2];
    const result = resultText;

    currentInput = result;
    currentOperation = "";
    lastInputBox.textContent = `${first} ${operator} ${second}=`;
    valueBox.textContent = result;
}

function showHistory() {
    const historyTab = document.getElementById("history-container");
    historyTab.classList.toggle("historyTab-active");
}

function clearHistory() {
    const historyTab = document.getElementById("history-tab");

    while (historyTab.firstChild) {
        historyTab.removeChild(historyTab.firstChild);
    }
    const clearHistoryBtn = document.getElementById("clearHistory-btn");
    clearHistoryBtn.style.display = "none";
}

function percent() {
    let result;

    if (currentOperation === '+' || currentOperation === '-') {
        result = (currentInput / 100) * lastInput;
    } else if (currentOperation === '*' || currentOperation === '/') {
        result = currentInput / 100;
    } else {
        result = currentInput / 100;
    }

    currentInput = result;
    valueBox.textContent = result;
}

document.getElementById("history-btn").addEventListener("click", showHistory);