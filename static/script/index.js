function render() {
    const productsStore = localStorageUtil.getProducts();

   
    productsPage.render();
}

let catalog = [];


fetch('setting.json', { mode: 'no-cors'})
    .then(res => res.json())
    .then(body => {
        catalog = body;
        render();
    })
    .catch(error => {
        console.log(error);
    });