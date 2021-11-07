class Products {

   render() {
      let htmlCatalog = '';

      catalog.forEach(({ id, name, prise, Image }) => {
           
         htmlCatalog += `
            <div class="line_1">
               <img class="content_img" src="${Image}" />
               <div>${name}</div>
               <div>${prise}</div> 
               <button class="content_btn">Добавить в корзину</button>           
            </div>
              `;

        });

        const html = `
            <div class="cards">
               ${htmlCatalog}
            </div>
            <div class="cards">
               ${htmlCatalog}
            </div>
            <div class="cards">
               ${htmlCatalog}
            </div>
           

        `;

        root_products.innerHTML = html;

   }

}

const productsPage = new Products();
productsPage.render();