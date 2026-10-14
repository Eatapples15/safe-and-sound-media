const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const d of process.argv.slice(2)){for(const f of fs.readdirSync('fissi/'+d).filter(x=>x.endsWith('.html')).sort()){await p.goto('file://'+process.cwd()+`/fissi/${d}/${f}`);await p.waitForTimeout(150);await p.screenshot({path:`fissi/${d}/safe-and-sound-${d}-${f.replace('.html','')}.png`});}}
await b.close();})();
