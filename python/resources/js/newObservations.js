//listening for the form submission
document.getElementById("newObservation").addEventListener("click", () => {
    //adding all our values to local variables for easier handling
    const CBH = document.getElementById("CBH").value;
    const height = document.getElementById("height").value;
    const DBH = document.getElementById("DBH").value;
    const BA = document.getElementById("BA").value;
    const dead = document.getElementById("dead").value;

    //setting our variables up in a JSON-like structure
    const newObservation = {
        CBH: CBH,
        height: height,
        DBH: DBH,
        BA: BA,
        dead: dead
    };

    //POSTing the data for storage
    const response = fetch("/newObservations/new", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newObservation) 
    });
    //confirmation pop-up
    confirm("Observation Posted!")
});

