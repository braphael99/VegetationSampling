fetch('/diamCorrel')
.then(response => response.json())
.then(data => {
    const correlation = data.correlation;
// Manipulate the HTML to display the JSON data
    document.getElementById('diamHolder').innerText = `The Correlation Coefficient is: ${correlation}`
    if (correlation >= -1.0 && correlation < -0.6){
        document.getElementById("correlationInterp").innerText = "The correlation is a very strongly negative correlation.";
    }
    else if (correlation >= -0.6 && correlation < -0.3){
        document.getElementById("correlationInterp").innerText = "The correlation is a negative correlation.";
    }
    else if (correlation >= -0.3 && correlation < 0){
        document.getElementById("correlationInterp").innerText = "The correlation is a very weak negative correlation.";
    }
    else if (correlation >= 0 && correlation < 0.3){
        document.getElementById("correlationInterp").innerText = "The correlation is a very weak positive correlation.";
    }
    else if (correlation >= 0.3 && correlation < 0.6){
        document.getElementById("correlationInterp").innerText = "The correlation is a positive correlation.";
    }
    else{
        document.getElementById("correlationInterp").innerText = "The correlation is a very strong postitive correlation.";
    }

})
.catch(error => {
    console.error('Error fetching data:', error);
});