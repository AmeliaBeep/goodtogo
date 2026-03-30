// document.addEventListener("DOMContentLoaded", function() {
//     const commentForm = document.getElementById("comment-form");
//     const commentList = document.getElementById("comment-list");
//     const formErrors = document.getElementById("form-errors");
 
//     commentForm.addEventListener("submit", async function(e) {
//         e.preventDefault();  // Prevent default form submission (no page reload)
 
//         // Get form data (including CSRF token)
//         const formData = new FormData(commentForm);
 
//         try {
//             // Send AJAX POST request
//             const response = await fetch(commentForm.action, {
//                 method: "POST",
//                 body: formData,
//                 headers: {
//                     "X-Requested-With": "XMLHttpRequest",  // Indicate AJAX request
//                 },
//             });
 
//             const data = await response.json();
 
//             if (data.success) {
//                 // Update comment list with new HTML
//                 commentList.innerHTML = data.html;
//                 // Clear form fields
//                 commentForm.reset();
//                 // Clear errors
//                 formErrors.textContent = "";
//             } else {
//                 // Display form errors
//                 let errors = "";
//                 for (const [field, messages] of Object.entries(data.errors)) {
//                     errors += `${field}: ${messages.join(", ")}\n`;
//                 }
//                 formErrors.textContent = errors;
//             }
//         } catch (error) {
//             formErrors.textContent = "An error occurred. Please try again.";
//             console.error("AJAX Error:", error);
//         }
//     });
// });
document.addEventListener("DOMContentLoaded", function() {
    const calendarViewButton = document.getElementById("calendar-view");
    const listViewButton = document.getElementById("list-view");
    const contentContainer = document.getElementById("content-container");

    async function getListView() {
        try {
            // Send AJAX POST request
            const response = await fetch("api/get-list-view", {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",  // Indicate AJAX request
                },
            });
 
            const data = await response.json();
 
            if (data.success) {
                // Update comment list with new HTML
                contentContainer.innerHTML = data.html;
            } else {
                // Display form errors
                console.log("oops")
            }
        } catch (error) {
            console.error("AJAX Error:", error);
        }
    }
    
    listViewButton.addEventListener("click", getListView)
});