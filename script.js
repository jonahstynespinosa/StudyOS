const btn = document.getElementById("load-assignment")
const showCompletedBtn = document.getElementById("showCompleted")
const showAllBtn = document.getElementById("showAll")
const dataSet = document.getElementById("dataSet")

let assignments = []


async function loadAssignments() {
  try {
  dataSet.innerHTML = "<p>Loading...</p>"

  const res = await fetch("https://jsonplaceholder.typicode.com/todos?_limit=10")

    if(!res.ok) {
      throw new Error("Failed to fetch assignments")
    }

    assignments = await res.json()
    displayAssignments(assignments)
  } catch (error) {
    dataSet.innerHTML = `<p class="error">${error.message}</p>`
  }
}

btn.addEventListener("click", loadAssignments) 

showAllBtn.addEventListener("click", () => displayAssignments(assignments))

showCompletedBtn.addEventListener("click", () => {
  const completedAssignments = assignments.filter(assignment => assignment.completed)
  displayAssignments(completedAssignments)
})

function displayAssignments(assignments) {
  dataSet.innerHTML = ""
  
  assignments.forEach(assignment => {
    const assignmentDiv = document.createElement("div")
    assignmentDiv.classList.add("data-item")

    assignmentDiv.innerHTML = `
      <h3>${assignment.title}</h3>
      <p>${assignment.completed ? "Completed" : "Not completed"}</p>
    `
    dataSet.appendChild(assignmentDiv)
  })
}
