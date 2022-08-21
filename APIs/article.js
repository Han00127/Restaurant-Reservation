var count = 0;
async function mycur2 (){
    document.querySelector("#links").innerHTML = "";
    document.querySelector("#country").innerHTML = "";
    var country = document.querySelector('#ok').value;
    country = country.toLowerCase();
    const res01 = await fetch("https://api.myjson.com/bins/17q5jg");
    const data02 = await res01.json(); 
    let keys01 = Object.keys(data02);
    let vals01 =  Object.values(data02);
     for(var i = 0; i < vals01.length; i++){
         if(country==keys01[i]){
             country = vals01[i];
          }
     }
    const res1 = await fetch("https://api.myjson.com/bins/17mzvs");
    const data2 = await res1.json(); 
    let keys = Object.keys(data2);
    let vals = Object.values(data2);
    is_valid = false;
    for(var i = 0; i < vals.length; i++){
        if (vals[i].toLowerCase() == country.toLowerCase()){
            code_name = keys[i];
            is_valid = true;
        }
    }
    if(is_valid == false){
        alert("Invalid input. Please type full name of the country e.g United States, South Korea, India");
        return;
    }
    var hr = document.createElement('hr');
    document.querySelector("#links").appendChild(hr);
    document.querySelector("#country").textContent = "Article from NewYork Time about " +country;
    document.querySelector("#country").style = "color:#feda6a;"
    const api_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+country+"&api-key=u90tCI6gAA6EYHImKyUt9YyJ6FFrsHja";
    const res = await fetch(api_url);
    const data = await res.json();
    for (var i = 0; i < data.response.docs.length; i++){
        var url = data.response.docs[i].web_url;
        // console.log(data.response.docs[i].headline.main);
        var link_text = document.createTextNode(data.response.docs[i].headline.main);
        var a = document.createElement('a');
        a.appendChild(link_text);
        a.href = url;
        document.querySelector("#links").appendChild(a);
        document.querySelector("#links").appendChild(document.createElement("br"));
     
    }
    if(count == 0){
       document.body.appendChild(document.createElement("hr"));
        var myh = document.createElement("h4");
        myh.textContent = "CSCI 4131 Fall 2019";
        myh.style = "text-align: center;color:#d4d4dc;";
        document.body.appendChild(myh);
        count++;
    }
}
