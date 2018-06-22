function(modal) {
    modal.respond('colourChosen', '{{ feature }}', ['{{ all_features|join:"','" }}']);
    modal.close();
}