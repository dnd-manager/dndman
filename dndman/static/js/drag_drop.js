document.querySelectorAll(".drop-form").forEach(form => {
    const uploader = form.getElementsByClassName("upload-input")[0];
    const label = form.getElementsByClassName("drop-label")[0];
    const daEle = form.getElementsByClassName("drop-area")[0];

    // when over make text darker
    daEle.addEventListener("dragover", event => {
        event.preventDefault();
        label.classList.add("drag-over");
    });

    // exit
    ["dragleave", "dragend"].forEach(eventType => {
        daEle.addEventListener(eventType, event => {
            label.classList.remove("drag-over");                      
        });
    });
    
    // drop
    daEle.addEventListener("drop", event => {
        event.preventDefault();

        if (event.dataTransfer.files.length > 0) {
            uploader.files = event.dataTransfer.files;
            uploader.dispatchEvent(new Event("change"));
        }

        label.classList.remove("drag-over");
    });

    // click
    daEle.addEventListener("click", event => {
        event.preventDefault();
        uploader.click();
    });

    // update text
    uploader.addEventListener("change", event => {
        let path = event.target.value;
        label.textContent = path.substring(path.lastIndexOf("\\") + 1);
    });
});