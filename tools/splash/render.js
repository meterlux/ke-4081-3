const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2000,height:2000}});
await p.setContent('<html><body style="margin:0;background:#000">'+fs.readFileSync('scene.svg','utf8')+'</body></html>');
await p.waitForTimeout(500);await p.screenshot({path:'scene.png'});await b.close();})();
