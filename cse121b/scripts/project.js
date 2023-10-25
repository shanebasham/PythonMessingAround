seen = 1;
total = 1;

function setup(){
plusBtn = document.getElementById("addBtn");
plusBtn.addEventListener("click", addFunction);
deleteBtn = document.getElementById("removeBtn");
deleteBtn.addEventListener("click", removeFunction);
filtBtn = document.getElementById("sortBtn");
filtBtn.addEventListener("click", sortFunction);
input1 = document.getElementById("1");
input1.addEventListener("change", count);

}


function addFunction(){
if(seen < total){
    i=findLatest();
    i2=i+1;
    latest=document.getElementById(i2);
    latest.style.visibility = "visible";
    number=document.getElementById("number"+i2);
    label=document.getElementById("label"+i2);
    number.style.visibility = "visible";
    label.style.visibility = "visible";
    seen++;
}
else{
    temptot= +total+1;
    tab = document.getElementById("data");
    row = data.insertRow(total);
    //cell1 = row.insertAdjacentHTML('beforeend', '<span><label id="label2">2</label></span>');
    //cell2 = row.insertAdjacentHTML('beforeend', '<span><input type="text" id="2" /></span>');
    //cell3= row.insertAdjacentHTML('beforeend','<span id="number2">0</span>');
    cell1 = row.insertCell(0);
    cell2 = row.insertCell(1);
    cell3 = row.insertCell(2);
    var itemLabel = document.createElement("Label");
    itemLabel.setAttribute("id", "label"+temptot);
    itemLabel.style.visibility = "visible";
    itemLabel.innerHTML = total+1;
    cell1.appendChild(itemLabel);
    var input = document.createElement("Input");
    input.id = temptot;
    input.type = "text";
    input.style.visibility = "visible";
    cell2.appendChild(input);
    var spanTxt = document.createElement("Span");
    spanTxt.setAttribute("id", "number"+temptot);
    spanTxt.innerHTML = "0";
    spanTxt.style.visibility = "visible";
    cell3.appendChild(spanTxt);
    input.addEventListener("change", count);
    seen++;
    total++;
}

}

function removeFunction(){
temp=document.getElementById("2");
temp2=document.getElementById("number2");
temp3=document.getElementById("label2");
if(temp.style.visibility != "visible"){
    return;
}
else{
    i=findLatest();
    latest=document.getElementById(i);
    number=document.getElementById("number"+i);
    label=document.getElementById("label"+i);
    latest.style.visibility = "hidden";
    number.style.visibility = "hidden";
    label.style.visibility = "hidden";
    seen--;
}

}

function sortFunction(){
max = findLatest();
var holder = new Array();
for(i=1;i<=max;i++){
    temp=document.getElementById(i);
    temp2=temp.value;
    holder.push(temp2);
}
holder.sort();
for(j=max;j>=1;j--){
    item = holder[j-1];
    check=document.getElementById(j);
    check.value = item;
    holder.pop();
}

}

function count(){
//temp=document.getElementById(this);
temp= this;
temp2=temp.value.length;
lengt=document.getElementById("number"+this.id);
if(lengt.firstChild != null)
    lengt.removeChild(lengt.firstChild);
lengt.appendChild(document.createTextNode(temp2));
}

function findLatest(){
table=document.getElementById("data");
//for(i=2; i<=total; i++){
for(i=1; i<=total; i++){
    temp=document.getElementById(i);
    if(temp.style.visibility == "visible"){
       if(parseInt(i)==parseInt(total)){
        return i;
       }
       else if(i==1 && document.getElementById("2").style.visibility == "hidden"){
           return 1;
       }
       else{

        }
    }
    else if(document.getElementById(i).style.visibility == "hidden" && document.getElementById(i-1).style.visibility == "visible" ) {
        return i-1;
    }

}

}  