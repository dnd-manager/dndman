document.querySelectorAll(".dice").forEach(dice => {
    let max = dice.getAttribute("dice_count");
    let label = dice.getElementsByTagName("h2")[0];

    label.textContent = max;

    dice.getElementsByTagName("button")[0].addEventListener("click", async event => {
        event.preventDefault();
        for (let i = 0; i < 20; i++) {
            label.textContent = getRand(max);
            await sleep(i*10);
        }
        
        httpGet("/discord_compat/send_message/Rolled " + label.textContent)
    });
});

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function getRand(max) {
    return Math.floor(Math.random() * max) + 1;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}