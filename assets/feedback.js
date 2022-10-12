function toggleFeedback() {
    toggle('feedback');
    toggle('feedback-closed');

    localStorage.setItem("zowe-feedback-open", getCurrentDate());
}

function toggle(id) {
    const x = document.getElementById(id);
    if (x.className.indexOf("feedback-hide") == -1) {
        x.className += " feedback-hide";
    } else {
        x.className = x.className.replace(" feedback-hide", "");
    }
}

function getCurrentDate() {
    const currentDate = new Date();
    return currentDate.getFullYear() + "-" + currentDate.getMonth();
}

const feedbackOpen = localStorage.getItem("zowe-feedback-open");
// For more friendly first-time user UX, always leave feedback box closed on default
toggleFeedback();

const dateObj = new Date();
const monthNameLong = dateObj.toLocaleString("en-US", { month: "long" });
const elementsToTransform = document.getElementsByClassName("question-name ");
for (var i = 0; i < elementsToTransform.length; i++) {
    elementsToTransform[i].innerHTML = "Question for " + monthNameLong;
}