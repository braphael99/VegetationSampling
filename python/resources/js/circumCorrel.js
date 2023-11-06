//fetching the circumference correlation, r-squared, and linear equation data
fetch('/circumCorrel')
.then(response => response.json())
.then(data => {
    //storing the data locally to use
    const correlation = data.correlation;
    const rSquared = data.rSquared;
    const slope = data.slope;
    const intercept = data.intercept;

    // Manipulate the HTML to display the JSON data
    document.getElementById('circumHolder').innerText = `The Correlation Coefficient is: ${correlation.toFixed(3)}`
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

    document.getElementById("circumRSquared").innerText = `The r-squared (coefficient of determination) value: ${rSquared.toFixed(3)}.`;
    document.getElementById("circumEquation").innerText = `The slope-intercept form equation is: y = ${slope.toFixed(3)}x + ${intercept.toFixed(3)}.`;

})
.catch(error => {
    //error handling
    console.error('Error fetching data:', error);
});