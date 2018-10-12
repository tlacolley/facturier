$(document).ready(function(){

const picker = datepicker('#datePickerInput',{
    startDay: 1,
    customMonths: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
});

//  function filter by date, Ne fonctionne pas, recuperation de la date

$('#datePickerInput').change( function() {
        var selectDate = $(this).val();
        $('.formDate').submit();
        $('input[name=dateInputHide]').val(selectDate)
        console.log(selectDate);
     })

//  function filter by Quotation status

$('#selectStatus').change( function(){
    var selectStatus = $(this).find(":selected").val();
    $('.formStatus').submit();
    // $('#selectStatus').val(selectStatus)
    console.log(selectStatus);

})

//  function filter by Name or date
$('input[name=orderByFilter]').click( function(){
    var selectRadio = $(this).val();

    $('.formOrder').submit();
    console.log(selectRadio);
})

// function pour deplier le form


$(".FilterSide").click(function () {

    $FilterSide = $(this);
    //getting the next element
    filterBox = $FilterSide.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    filterBox.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
        $FilterSide.text(function () {
            //change text based on condition
            return filterBox.is(":visible") ? "Reduce" : "Filter";
        });
    });

});

})
