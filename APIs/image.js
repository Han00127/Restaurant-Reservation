 async function mycur1 (){
                document.querySelector("#images").innerHTML = "";
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
                    return;
                }
                const image_api_url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&safe_search=3&api_key=2e7d941570fb9c6591c1cfbe37d2d521&format=json&nojsoncallback=1&per_page=05&text="+country+"flag &page=1";
                const res = await fetch(image_api_url);
                var n = await res.json();
                var _s = n.photos.photo;
                var divd = document.getElementById("#images");
                for(var z = 0 ; z < n.photos.photo.length ; z++)
                {
                    var CurrentPhotoUrl = 'https://farm'+_s[z]['farm']+'.staticflickr.com/'+_s[z]['server']+'/'+_s[z]['id']+'_'+_s[z]['secret']+'_n.jpg'
                    $("<img />").attr({"src": CurrentPhotoUrl,"style":"margin:40px","class":"img-thumbnail"}).appendTo("#images");
                }
                var br = document.createElement('br');
                document.querySelector("#images").appendChild(br);
                var hr = document.createElement('hr');
                document.querySelector("#images").appendChild(hr);
}
