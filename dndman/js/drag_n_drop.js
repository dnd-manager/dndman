document.querySelectorAll(".drop-area").forEach(daEle => {
    const uploader = daEle.closest(".upload-input");
    const label = daEle.closest(".drop-label");

    daEle.addEventListener("dragover", _event => {
        label.classList.add("drag-over");
    });
});