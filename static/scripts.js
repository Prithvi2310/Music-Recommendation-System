document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('input_song');
    const suggestionsDiv = document.getElementById('suggestions');

    locationInput.addEventListener('input', function() {
        const inputText = this.value.toLowerCase();
        const suggestions = getFilteredSuggestions(inputText);

        // Clear previous suggestions
        suggestionsDiv.innerHTML = '';

        // Add new suggestions
        suggestions.forEach(function(suggestion) {
            const option = document.createElement('div');
            option.textContent = suggestion;
            option.addEventListener('click', function() {
                locationInput.value = this.textContent;
                suggestionsDiv.innerHTML = '';
            });
            suggestionsDiv.appendChild(option);
        });
    });


    function getFilteredSuggestions(inputText) {
        
        // Example: Fetch suggestions from a server based on inputText
        const allSuggestions = ["Danny Boy", "Get Busy", "Stand Up", "I'm A Ding Dong Daddy", "Chicago Breakdown", 
        "Everybody Loves My Baby", "Holidae In", "Right Thurr", "In Those Jeans", "Po' Folks", "Running", 
        "Midnight Rider", "Get Something", "21 Questions", "Inside Your Heaven", "Almost Home", 
        "Get Off The Corner - Amended Version", "Be Mine - Live", "A Few Questions", "Forever And For Always", 
        "Sing For The Moment", "I Love This Bar", "Raining On Sunday", "Lonely Road Of Faith", "Bump_ Bump_ Bump", 
        "Snake - Remix - feat. Big Tigger", "My Heart", "Hotter Than That", "Blue Yodel No. 9", "A Monday Date", 
        "Heebie Jeebies", "Naughty Man", "Stardust", "Lifestyles of the Rich & Famous", "Fighter", "Landslide", 
        "Walk A Little Straighter", "Speechless", "It's Five O'Clock Somewhere", "Top of the World", "Stacy's Mom", 
        "A Few Questions - Single Version", "She Was The Prize", "Underneath It All", "Tiny Dancer", "Real Good Man", 
        "Boom", "Stuck", "More to Life", "From The Inside", "Forever And For Always - Red Version", "Godspeed (Sweet Dreams)", 
        "Low", "Let's Fall In Love", "Here Without You", "Me", "Johnny Tarr", "Swing_ Swing", "The Night I Punched Russell Crowe", 
        "Without Me", "Where Are You Going", "Soldier", "In The Shadows", "Chicks Dig It", "She Got Soul", "Girl All The Bad Guys Want", 
        "A Lot Of Things Different", "Wild West Show", "Personal Jesus", "Don't Stop Dancing", "Somewhere I Belong", "Frantic", 
        "Stillborn", "Times Like These", "La Tortura", "The Way You Look Tonight", "Crimen", "Walked Outta Heaven", 
        "My Boo - Non-Album Version", "Texas Moaner Blues - 78rpm Version"];
        return allSuggestions.filter(function(suggestion) {
            return suggestion.toLowerCase().startsWith(inputText);
        });
    }
});
