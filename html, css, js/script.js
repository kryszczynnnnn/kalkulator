let rownanie = "";
let wynik = "";
let valueBox = document.getElementById("value-box")

function addnumber(numberToAdd) {
    if (numberToAdd != 0) {
        rownanie += numberToAdd
    }
    else if (rownanie.length > 0) {
        rownanie += numberToAdd
    }
    valueBox.textContent = rownanie
    console.log(rownanie)
}

function operation(type) {
    if ("+-/*".includes(type)) {
        if (rownanie.length > 0) {
            let lastChar = rownanie.slice(-1);

            if (!"+-/*".includes(lastChar)) {
                rownanie += type;
                valueBox.textContent += type
            }
        }
    }
}