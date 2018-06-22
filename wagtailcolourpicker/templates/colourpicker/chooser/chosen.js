function(modal) {
    modal.respond('colourChosen', '{{ feature_name }}', ['{{ all_feature_names|join:"','" }}']);
    modal.close();
}