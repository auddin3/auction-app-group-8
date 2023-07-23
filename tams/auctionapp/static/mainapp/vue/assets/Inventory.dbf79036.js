import{_ as m,c as r,a as e,F as _,r as f,b as g,e as v,w as c,v as a,d as p,o as u,t as d}from"./index.18052401.js";const b={data(){let o=new Date;const t=new Date(o.getFullYear(),o.getMonth(),o.getDate(),o.getHours(),o.getMinutes(),o.getSeconds());return{items:[],user_id:0,product_id:0,product_name:"",product_image:"/media/product-images/stock-image.png",description:"",start_price:0,end_of_bid:t.toISOString().slice(0,10),owner:"",edit:!1,new_product_image:"/product-images/stock-image.png"}},computed:{filteredItems(){return JSON.parse(JSON.stringify(this.items))}},methods:{async fetchItems(){let t=await(await fetch("http://localhost:8000/auctionapp/api/ownedProducts/items/"+this.user_id,{credentials:"include",mode:"cors",referrerPolicy:"no-referrer",method:"GET"})).json();this.items=t.items},async saveNewItem(){await(await fetch("http://localhost:8000/auctionapp/api/ownedProducts/items/"+ +this.user_id,{headers:{"Content-Type":"application/json"},method:"POST",body:JSON.stringify({product_name:this.product_name,product_image:this.new_product_image,description:this.description,start_price:this.start_price,end_of_bid:this.end_of_bid})})).json(),this.fetchItems()},async onFileSelected(o){const t=o.target.files[0],i=new FormData;i.append("image",t),i.append("name",t.name);let l=await(await fetch("http://localhost:8000/auctionapp/api/productPic/",{method:"POST",body:i})).json();this.new_product_image=l.path},async deleteItem(o){let i=await(await fetch("http://localhost:8000/auctionapp/api/product/"+o,{method:"DELETE",body:JSON.stringify({id:o})})).json();this.items=i.items,this.fetchItems()}},async mounted(){try{let t=await(await fetch("http://localhost:8000/auctionapp/user",{credentials:"include",mode:"cors",referrerPolicy:"no-referrer",method:"GET"})).json();this.user_id=t.user_id,this.fetchItems()}catch{window.location.href="http://localhost:8000/auctionapp"}}};const w=e("div",{class:"inventory"},[e("h1",{class:""},"My Inventory")],-1),y=e("div",{class:"Saved Items"},null,-1),I={key:0},x=e("br",null,null,-1),S=e("div",null,[e("h3",{class:"items_title"},"My Saved Items")],-1),C={class:"card-group"},M={class:"card mt-4",style:{width:"10rem"}},N=["src"],V={class:"card mt-4",style:{width:"60rem"}},k={class:"card-title"},D={class:"card-title"},F={class:"card-title"},O={class:"card-text price-colour"},P=e("strong",null,"Start Price:",-1),T={class:"card-title"},E={class:"card-text"},j=e("strong",null,"End of Bid:",-1),A={class:"owner"},B=e("strong",null,"Owner: ",-1),z=["onClick"],L=e("b",null,"Delete",-1),J=[L],U=e("br",null,null,-1),H=e("br",null,null,-1),G={class:"card formCard",style:{width:"65rem"}},Y=e("h3",{class:"items_title"},"Add your item!",-1),q=e("br",null,null,-1),K={class:"item-photo-container"},Q=e("label",{type:"button",for:"upload-file",refs:"upload-file",class:"profile-pic-button btn-lg"},[e("svg",{xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink","enable-background":"new 0 0 32 32",height:"20px",id:"Layer_1",version:"1.1",viewBox:"0 0 32 32",width:"20px","xml:space":"preserve",class:"btn-icon"},[e("g",{id:"camera"},[e("path",{"clip-rule":"evenodd",d:"M16,10.001c-4.419,0-8,3.581-8,8c0,4.418,3.581,8,8,8   c4.418,0,8-3.582,8-8C24,13.583,20.418,10.001,16,10.001z M20.555,21.906c-2.156,2.516-5.943,2.807-8.459,0.65   c-2.517-2.156-2.807-5.944-0.65-8.459c2.155-2.517,5.943-2.807,8.459-0.65C22.42,15.602,22.711,19.391,20.555,21.906z",fill:"#ffffff","fill-rule":"evenodd"}),e("path",{"clip-rule":"evenodd",d:"M16,14.001c-2.209,0-3.999,1.791-4,3.999v0.002   c0,0.275,0.224,0.5,0.5,0.5s0.5-0.225,0.5-0.5V18c0.001-1.656,1.343-2.999,3-2.999c0.276,0,0.5-0.224,0.5-0.5   S16.276,14.001,16,14.001z",fill:"#ffffff","fill-rule":"evenodd"}),e("path",{"clip-rule":"evenodd",d:"M29.492,9.042l-4.334-0.723l-1.373-3.434   C23.326,3.74,22.232,3,21,3H11C9.768,3,8.674,3.74,8.214,4.886L6.842,8.319L2.509,9.042C1.055,9.283,0,10.527,0,12v15   c0,1.654,1.346,3,3,3h26c1.654,0,3-1.346,3-3V12C32,10.527,30.945,9.283,29.492,9.042z M30,27c0,0.553-0.447,1-1,1H3   c-0.553,0-1-0.447-1-1V12c0-0.489,0.354-0.906,0.836-0.986l5.444-0.907l1.791-4.478C10.224,5.25,10.591,5,11,5h10   c0.408,0,0.775,0.249,0.928,0.629l1.791,4.478l5.445,0.907C29.646,11.094,30,11.511,30,12V27z",fill:"#ffffff","fill-rule":"evenodd"})])]),e("div",null,[e("p",{class:"d-inline btn-text"},[p(" \xA0 "),e("strong",null,"Add item's picture")])])],-1),R=e("br",null,null,-1),W=e("label",{for:"product_name"},[e("b",null,"Item Name")],-1),X=e("br",null,null,-1),Z=e("label",{for:"description"},[e("b",null,"Item Description")],-1),$=e("br",null,null,-1),ee=e("label",{for:"start_price"},[e("b",null,"Starting Price")],-1),te=e("br",null,null,-1),se=e("label",{for:"end_of_bid"},[e("b",null,"End of Bid")],-1),oe=e("br",null,null,-1),le=e("div",null,[e("button",{type:"submit"},[e("b",null,"Submit")])],-1);function ne(o,t,i,h,l,n){return u(),r(_,null,[w,y,e("div",null,[n.filteredItems.length>0?(u(),r("div",I,[x,S,(u(!0),r(_,null,f(n.filteredItems,s=>(u(),r("div",null,[e("div",C,[e("div",M,[e("div",null,[e("img",{class:"card-img-top product-image",src:`http://localhost:8000${s.product_image}`,alt:"MyItems"},null,8,N)])]),e("div",V,[e("h4",k,d(s.product_name),1),e("div",D,d(s.description),1),e("div",F,[e("p",O,[P,p(" \xA3"+d(s.start_price),1)])]),e("div",T,[e("p",E,[j,p(" "+d(s.end_of_bid.substring(0,10))+" \xA0 "+d(s.end_of_bid.substring(11,19)),1)])]),e("div",A,[e("p",null,[B,p(d(s.owner),1)])]),e("button",{onClick:ie=>n.deleteItem(s.id),type:"button",class:"btn btn-outline-danger"},J,8,z),U])])]))),256))])):g("",!0)]),H,e("div",G,[Y,q,e("div",null,[e("form",{onSubmit:t[5]||(t[5]=v((...s)=>n.saveNewItem&&n.saveNewItem(...s),["prevent"]))},[e("fieldset",null,[e("div",K,[e("div",null,[e("input",{onChange:t[0]||(t[0]=(...s)=>n.onFileSelected&&n.onFileSelected(...s)),type:"file",id:"upload-file",name:"upload-file",ref:"myFileInput",accept:"image/gif, image/jpeg, image/png",hidden:""},null,544),Q])]),R,e("div",null,[W,c(e("input",{type:"text",id:"product_name",class:"form-control","onUpdate:modelValue":t[1]||(t[1]=s=>l.product_name=s)},null,512),[[a,l.product_name]])]),X,e("div",null,[Z,c(e("input",{type:"text",id:"description",class:"form-control","onUpdate:modelValue":t[2]||(t[2]=s=>l.description=s)},null,512),[[a,l.description]])]),$,e("div",null,[ee,c(e("input",{type:"number",step:"0.01",id:"start_price",class:"form-control","onUpdate:modelValue":t[3]||(t[3]=s=>l.start_price=s)},null,512),[[a,l.start_price]])]),te,e("div",null,[se,c(e("input",{type:"datetime-local",id:"end_of_bid",class:"form-control","onUpdate:modelValue":t[4]||(t[4]=s=>l.end_of_bid=s)},null,512),[[a,l.end_of_bid]])]),oe,le])],32)])])],64)}const re=m(b,[["render",ne]]);export{re as default};