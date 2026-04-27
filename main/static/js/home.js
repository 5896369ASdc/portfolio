
document.addEventListener("DOMContentLoaded", function () {

    const nameSearch = document.getElementById("name-search");
    const tags = document.querySelectorAll(".tag");
    const projects = document.querySelectorAll(".project");

    let activeTag = null;

    // SHOW ALL PROJECTS
    function showAll() {
        projects.forEach(project => {
            project.style.display = "";
        });
    }

    // SHOW "NO RESULTS"
    function checkEmptyState() {
        let visibleCount = 0;

        projects.forEach(project => {
            if (project.style.display !== "none") {
                visibleCount++;
            }
        });

        let msg = document.getElementById("no-results");

        if (visibleCount === 0) {
            if (!msg) {
                msg = document.createElement("p");
                msg.id = "no-results";
                msg.innerText = "No projects found 😕";
                msg.style.textAlign = "center";
                msg.style.marginTop = "20px";
                msg.style.color = "#777";
                document.querySelector(".projects-list").appendChild(msg);
            }
        } else {
            if (msg) msg.remove();
        }
    }

    // MAIN FILTER FUNCTION
    function filterProjects() {
        const query = nameSearch.value.toLowerCase().trim();

        projects.forEach(project => {
            const name = project.getAttribute("data-name") || "";
            const projectTags = project.getAttribute("data-tags") || "";

            const matchName = name.includes(query);
            const matchTag = activeTag ? projectTags.includes(activeTag) : true;

            if (matchName && matchTag) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        });

        checkEmptyState();
    }

    // SEARCH INPUT (live filtering)
    nameSearch.addEventListener("input", filterProjects);

    // TAG FILTER
    tags.forEach(tag => {
        tag.addEventListener("click", function () {

            const selected = this.getAttribute("data-tag");

            // toggle same tag (reset)
            if (activeTag === selected) {
                activeTag = null;

                tags.forEach(t => t.style.background = "#007bff");
                showAll();
            } else {
                activeTag = selected;

                // reset all tags
                tags.forEach(t => t.style.background = "#007bff");

                // highlight active tag
                this.style.background = "#28a745";
            }

            filterProjects();
        });
    });

});