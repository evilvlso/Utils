
function formatDate(dateArg){
    const date = new Date(dateArg);
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    const formatMonth = month < 10 ? `0${month}` : month;
    const formatDay = day < 10 ? `0${day}` : day;
    return `${year}-${formatMonth}-${formatDay}`
}

function get_pre_date() {
    var myDate = new Date();
var pre_end_date= myDate.setDate(myDate.getDate()+1);
var end_date = formatDate(pre_end_date);
var pre_start_date =myDate.setDate(myDate.getDate()-8);
var start_date = formatDate(pre_start_date);

return {"start_date":start_date,"end_data":end_date}
}