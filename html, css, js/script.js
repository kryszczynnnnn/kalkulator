let rownanie = "";
let lastOperation = null;
let currentOperation = null;
let lastInput = "";
let currentInput = "";
let wynik = "";
let valueBox = document.getElementById("value-box")

function addnumber(numberToAdd) {
    if (numberToAdd != 0) {
        rownanie += numberToAdd
        lastInput += numberToAdd
    }
    else if (rownanie.length > 0) {
        rownanie += numberToAdd
    }
    valueBox.textContent = rownanie
    console.log(rownanie)
}

function operation(type) {
    // if (lastOperation == null) {
    //     if ("+-/*".includes(type)) {
    //         if (rownanie.length > 0) {
    //             let lastChar = rownanie.slice(-1);
    //             if (!"+-/*".includes(lastChar)) {
    //                 rownanie += type;
    //                 valueBox.textContent += type
    //             }
    //         }
    //     }
    // } else {

    // }

    if (lastOperation == "") {
        if (("+-/*").includes(type)) {
            if (rownanie.length > 0 ) {
                let lastChar = rownanie.slice(-1);
                if (!"+-/*".includes(lastChar)) {
                    rownanie += type;
                    valueBox.textContent += type
                    lastOperation = type
                }
            }
        }
    } else {
        calculate()
    }
}

function calculate() {
    wynik = lastInput + currentInput
    
}

function backOne() {
    let newValue = valueBox.textContent.slice(0, -1);
    valueBox.textContent = newValue
    rownanie = newValue
}