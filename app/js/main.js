function processRequest() {
    let subject = document.getElementById("subject").value;
    let description = document.getElementById("description").value;
    let attachments = document.getElementById("attachments").files;
    let numOfAttachments = document.getElementById("attachments").files.length;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "http://0.0.0.0:8081/requests/new", true);
    xmlHttp.onload = function() {
        document.getElementById("displayRequest").innerHTML = this.responseText;
    };

    let form = new FormData();

    form.append("subject", subject);
    form.append("description", description);

    form.append("attachments", []);
    for (let i = 0; i < numOfAttachments; i++) {
        const file = attachments[i];
        form.append("attachments", file);
    }

    xmlHttp.send(form);
}