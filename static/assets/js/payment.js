document.addEventListener('DOMContentLoaded', () => {
    for (const el of document.querySelectorAll("[placeholder][data-slots]")) {
    const pattern = el.getAttribute("placeholder"),
    slots = new Set(el.dataset.slots || "_"),
    prev = (j => Array.from(pattern, (c,i) => slots.has(c)? j=i+1: j))(0),
    first = [...pattern].findIndex(c => slots.has(c)),
    accept = new RegExp(el.dataset.accept || "\\d", "g"),
    clean = input => {
    input = input.match(accept) || [];
    return Array.from(pattern, c =>
    input[0] === c || slots.has(c) ? input.shift() || c : c
    );
    },
    format = () => {
    const [i, j] = [el.selectionStart, el.selectionEnd].map(i => {
    i = clean(el.value.slice(0, i)).findIndex(c => slots.has(c));
    return i<0? prev[prev.length-1]: back? prev[i-1] || first: i; }); el.value=clean(el.value).join``; el.setSelectionRange(i, j); back=false; }; let back=false; el.addEventListener("keydown", (e)=> back = e.key === "Backspace");
        el.addEventListener("input", format);
        el.addEventListener("focus", format);
        el.addEventListener("blur", () => el.value === pattern && (el.value=""));
        }
        });   
     
        var bills_price_h3=document.querySelector(".bill-price h3");
        var bills_price_p=document.querySelector(".bill-price p");
    
        var slider=document.querySelector(".slider");
        var blue_color=document.querySelector(".slider_button");
        slider.addEventListener('click',function(){
        blue_color.classList.toggle('active');
      
        if(blue_color.classList.contains('active')){
            blue_color.innerHTML = "Monthly";
            bills_price_h3.innerHTML="$49/month";
            bills_price_p.innerHTML="$49 billed annually after 14-day free trial."
        }else{
            blue_color.innerHTML = "Yearly";
            bills_price_h3.innerHTML="$549/yearly";
            bills_price_p.innerHTML="$549 billed yearly after 14-day free trial."
        }
        
        });
        
         
        
        
    
        var card_details=document.querySelectorAll(".card-details input");
    
        function Nextitem(values,nextInput){
         
        if(values.value.length>=values.getAttribute('size')){
        card_details[nextInput].focus();
        }
        }