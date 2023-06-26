window.onload = async () => {
    let ipData = await (await fetch("https://wtfismyip.com/json").catch()).json().catch();
    document.getElementById("main-content-loc").innerText = ipData.YourFuckingCity
    document.getElementById("sidebar-filter-loc").innerText = ipData.YourFuckingCity
}