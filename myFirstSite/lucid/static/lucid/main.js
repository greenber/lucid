var valOfCard1 = "First Card"
var valOfCard2 = "Second Card"
var deck = ["Wizards", "Goblins", "Witch", "Cat"]
var questionDeck = ["Just say yes", "Just say no"]


function myFunction() {

    card(valOfCard1, "card1", 1); 
    card(valOfCard2, "card2", 2);
    
}//myFunction

function card(currentVal, elementId, cardNum) {

	var randomElement = parseInt ((Math.random() * 4), 10);
	
	replaceString = deck[randomElement]; 
	if (cardNum == 1) {
		valOfCard1 = replaceString;

	} else {

		valOfCard2 = replaceString; 

	}//Else 

	document.getElementById(elementId).innerHTML = replaceString; 

}//Card

function dmFun(){

	var randomElement = parseInt ((Math.random() * 2), 10);

	document.getElementById("dialog").innerHTML = questionDeck[randomElement];

	$( "#dialog" ).dialog({ autoOpen: false });
	$( "#opener" ).click(function() {
	  $( "#dialog" ).dialog( "open" );
	});

}///addAtt





