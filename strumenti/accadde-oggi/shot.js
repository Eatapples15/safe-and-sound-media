const { chromium } = require('playwright');
(async()=>{const [dir,...ids]=process.argv.slice(2);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const id of ids){await p.goto('file://'+dir+'/'+id+'.html');await p.waitForTimeout(300);await p.screenshot({path:dir+'/'+id+'.png'});}
await b.close();})();
