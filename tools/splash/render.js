const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();
for(const [f,w,h] of [['land',2400,1100],['port',1100,2400]]){
 const p=await b.newPage({viewport:{width:w,height:h}});
 await p.setContent('<html><head><link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&display=block" rel="stylesheet"></head><body style="margin:0;background:#000">'+fs.readFileSync(f+'.svg','utf8')+'</body></html>');
 await p.waitForTimeout(2500);await p.screenshot({path:f+'.png'});await p.close();}
await b.close();})();
