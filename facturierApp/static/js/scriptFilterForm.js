$(document).ready(function(){

const picker = datepicker('#datePickerInput',{
    startDay: 1,
    customMonths: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
});


$('#datePickerInput').change( function() {
        var selectDate = $(this).val();
        $('.formDate').submit();
        $('input[name=dateInputHide]').val(selectDate)
        console.log(selectDate);
     })


$('#selectStatus').change( function(){
    var selectStatus = $(this).find(":selected").val();
    $('.formStatus').submit();
    // $('#selectStatus').val(selectStatus)
    console.log(selectStatus);

})


$('input[name=orderByFilter]').click( function(){
    var selectRadio = $(this).val();

    $('.formOrder').submit();
    console.log(selectRadio);
})






})
