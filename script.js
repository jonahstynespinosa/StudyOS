let assignments = []


const btn = document.getElementById("load-assignment")
const showCompletedBtn = document.getElementById("showCompleted")
const showAllBtn = document.getElementById("showAll")
const clearBtn = document.getElementById("clearData")
const dataSet = document.getElementById("dataSet")
const searchInput = document.getElementById("searchInput")
const searchBtn = document.getElementById("searchBtn")
const completed = assignments.filter(a => a.completed).length
const total = assignments.length
const remaining = total - completed


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

clearBtn.addEventListener("click", () => {
  assignments = []
  dataSet.innerHTML = ""
})

searchBtn.addEventListener("click", () => {
  const query = searchInput.value.toLowerCase()
  const filteredAssignments = assignments.filter(assignment => assignment.title.toLowerCase().includes(query))
  displayAssignments(filteredAssignments)
})

searchInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    searchBtn.click()
  }
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

function displayStats() {
  let statsDiv = document.getElementById("dataSet")
  statsDiv.innerHTML = `
    <p>Total Assignments: ${total}</p>
    <p>Completed: ${completed}</p>
    <p>Remaining: ${remaining}</p>
  `
}
