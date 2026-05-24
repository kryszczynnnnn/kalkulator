/**
 * @jest-environment jsdom
 */

document.body.innerHTML = `
  <div id="value-box"></div>
  <div id="previous-input"></div>
  <button id="history-btn"></button>
  <div id="history-tab"></div>
  <button id="clearHistory-btn"></button>
`;

const { addnumber, operation, calculate, clearDisplay } = require('./src/script');

describe("Calculator tests", () => {

    beforeEach(() => {
        clearDisplay();
    });

    test("dodaje liczby poprawnie (2 + 3 = 5)", () => {
        addnumber(2);
        operation("+");
        addnumber(3);
        calculate();

        expect(global.document.getElementById("value-box").textContent).toBe("5");
    });

    test("nie pozwala dzielić przez 0", () => {
        global.alert = jest.fn();

        addnumber(5);
        operation("/");
        addnumber(0);
        calculate();

        expect(global.alert).toHaveBeenCalled();
    });

    test("clearDisplay resetuje wszystko", () => {
        addnumber(9);
        clearDisplay();

        expect(global.document.getElementById("value-box").textContent).toBe("0");
    });

    test("operation zapisuje poprzednią wartość", () => {
        addnumber(7);
        operation("+");

        expect(global.document.getElementById("value-box").textContent).toBe("0");
    });

});