// web/script_data.js
function sendDataToGoogleSheet(data) {
    const url = 'https://script.google.com/macros/s/AKfycbwuTAoOTJ-89FVzPbyx5lcFEwAbX2aB7JsauE5X0S-HWCMByTzUhiRcWa9_OrPiDggo/exec'; // Substitua pelo URL ATUALIZADO do seu Apps Script
    const options = {
        method: 'POST',
        mode: 'no-cors', // Essencial para evitar problemas de CORS com itch.io
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Converte o objeto de dados para uma string JSON
    };

    fetch(url, options)
    .then(response => {
        // Com 'no-cors', a resposta real não pode ser acessada.
        // Mas esta parte do código confirma que a requisição foi feita.
        console.log('Requisição de envio de dados para o Google Sheet feita.');
    })
    .catch(error => {
        // Captura erros de rede ou outros problemas antes da requisição.
        console.error('Erro ao fazer a requisição para o Google Sheet:', error);
    });
}
