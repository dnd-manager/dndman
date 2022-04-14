document.querySelectorAll(".dice").forEach(dice => {
    let max = dice.getAttribute("dice_count");
    let label = dice.getElementsByTagName("h2")[0];

    label.textContent = max;

    dice.getElementsByTagName("button")[0].addEventListener("click", async event => {
        event.preventDefault();
        let num = 0;

        for (let i = 0; i < 20; i++) {
            num = getRand(max);
            label.textContent = num;
            await sleep(i*10);
        }
        
        httpGet("/discord_compat/send_message/Rolled " + num)
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