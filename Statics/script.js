async function askGemini(){
const q=document.getElementById("question").value.trim();
const a=document.getElementById("answer");
if(!q){a.textContent="Please enter a question.";return;}
a.textContent="EduGenie is thinking...";
try{
const r=await fetch("/ask",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({question:q})});
const d=await r.json(); a.textContent=d.answer||"No answer received.";
}catch(e){a.textContent="Unable to connect to the server.";}
  }
