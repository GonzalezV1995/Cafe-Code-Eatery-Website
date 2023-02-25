// website source: https://html.form.guide/calculation-forms/simple-html-calculation-form/

function calculateTotal()
{
    let unit_price={
    small: 22,
    medium: 12,
    large: 2,
    espresso: 2,
    bubbletea: 2,
    poke: 2,
    ramen: 2,
    bahnmi: 2,
};
let item_price={}

item_price.small = $("#qty_small").val() * parseInt(document.getElementById("unit_price_small").value);

document.getElementById("unit_price_small").value= item_price.small





item_price.medium = ($("#qty_medium").val() * unit_price.medium )
$("#price_medium").val(item_price.medium);

item_price.large = ($("#qty_large").val() * unit_price.large )
$("#price_large").val(item_price.large);  

item_price.latte = ($("#qty_steampunk").val() * unit_price.steampunk )
$("#price_steampunk").val(item_price.steampunk);    

item_price.espresso = ($("#qty_espresso").val() * unit_price.espresso )
$("#price_espresso").val(item_price.espresso);   

item_price.bubbletea = ($("#qty_bubbletea").val() * unit_price.bubbletea )
$("#price_bubbletea").val(item_price.bubbletea);   

item_price.poke = ($("#qty_poke").val() * unit_price.poke )
$("#price_poke").val(item_price.poke);   

item_price.ramen = ($("#qty_ramen").val() * unit_price.ramen )
$("#price_ramen").val(item_price.ramen); 

item_price.bahnmi = ($("#qty_bahnmi").val() * unit_price.bahnmi )
$("#price_bahnmi").val(item_price.bahnmi); 


let total = item_price.small + item_price.medium + item_price.large + item_price.espresso + item_price.bubble+ item_price.poke+ item_price.ramen+ item_price.bubble+ item_price.bahnmi;


$("#total_value").text(total);

}

$(function()
 {
    $(".qty").on("change keyup",calculateTotal)
})

