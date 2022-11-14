const data = [
    {
      id: 1,
      name: "Invicta Men's Pro Diver",
      img: "sound.jpg",
      price: 74,
      cat: "Best",
    },
    {
      id: 11,
      name: "Invicta Men's Pro Diver 2",
      img: "sound1.jpg",
      price: 74,
      cat: "Superbass",
    },
    {
      id: 2,
      name: "Alexa  Expedition Scout ",
      img: "sound2.jpg",
      price: 40,
      cat: "Superbass",
    },
    {
      id: 3,
      name: "Breitling Superocean Heritage",
      img: "sound3.jpeg",
      price: 200,
      cat: "Luxury",
    },
    {
      id: 4,
      name: "Casio Classic  ",
      img: "sound4.jpeg",
      price: 16,
      cat: "Sport",
    },
    {
      id: 5,
      name: "Smartlistener ",
      img: "sound5.jpg",
      price: 74,
      cat: "Sport",
    },
  ];
  
  const productsContainer = document.querySelector(".products");
  const searchInput = document.querySelector(".search");
  const categoriesContainer = document.querySelector(".cats");
  const priceRange = document.querySelector(".priceRange");
  const priceValue = document.querySelector(".priceValue");
  
  const displayProducts = (filteredProducts) => {
    productsContainer.innerHTML = filteredProducts
      .map(
        (product) =>
          `
         <div class="product">
            <img
            src=${product.img}
            alt=""
            />
            <span class="name">${product.name}</span>
            <span class="priceText">$${product.price}</span>
          </div>
      `
      )
      .join("");
  };
  
  displayProducts(data);
  
  searchInput.addEventListener("keyup", (e) => {
    const value = e.target.value.toLowerCase();
  
    if (value) {
      displayProducts(
        data.filter((item) => item.name.toLowerCase().indexOf(value) !== -1)
      );
    } else {
      displayProducts(data);
    }
  });
  
  const setCategories = () => {
    const allCats = data.map((item) => item.cat);
    const categories = [
      "All",
      ...allCats.filter((item, i) => {
        return allCats.indexOf(item) === i;
      }),
    ];
  
    categoriesContainer.innerHTML = categories
      .map(
        (cat) =>
          `
        <span class="cat">${cat}</span>
      `
      )
      .join("");
  
    categoriesContainer.addEventListener("click", (e) => {
      const selectedCat = e.target.textContent;
  
      selectedCat === "All"
        ? displayProducts(data)
        : displayProducts(data.filter((item) => item.cat === selectedCat));
    });
  };
  
  const setPrices = () => {
    const priceList = data.map((item) => item.price);
    const minPrice = Math.min(...priceList);
    const maxPrice = Math.max(...priceList);
  
    priceRange.min = minPrice;
    priceRange.max = maxPrice;
    priceRange.value = maxPrice;
    priceValue.textContent = "$" + maxPrice;
  
    priceRange.addEventListener("input", (e) => {
      priceValue.textContent = "$" + e.target.value;
      displayProducts(data.filter((item) => item.price <= e.target.value));
    });
  };
  
  setCategories();
  setPrices();