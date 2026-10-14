const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const d of fs.readdirSync('.').filter(x=>x.startsWith('ep')&&!x.endsWith('.json')&&!x.endsWith('.py'))){for(let i=1;i<=5;i++){await p.goto('file://'+process.cwd()+`/${d}/${i}.html`);await p.waitForTimeout(150);await p.screenshot({path:`${d}/safe-and-sound-${d.slice(0,4)}-${i}.png`});}}
await b.close();})();
