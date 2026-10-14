const { chromium } = require('playwright');
(async()=>{const [f,dur,out]=process.argv.slice(2);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/'+f);await p.waitForTimeout(400);const n=Math.round(dur*30);require('fs').mkdirSync(out,{recursive:true});
for(let i=0;i<n;i++){await p.evaluate(t=>draw(t),i/30);await p.screenshot({path:`${out}/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
