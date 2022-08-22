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
// Hide feedback when already shown in this month
if (feedbackOpen === getCurrentDate()) {
    toggleFeedback();
}