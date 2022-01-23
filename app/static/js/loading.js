class ImageWrapper extends HTMLElement {

    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <div class="image_wrapper">         
                <img class=${this.getAttribute("image_class")} src=${this.getAttribute("image_source_path")} alt="No Img Available">
                <h1 class="live-counter text-blue-dark font-weight-bolder m-0 text-break">${this.getAttribute("value")}</h1>
                <p class="live-counter-subtitle text-blue-dark font-weight-light text-uppercase mb-0">${this.getAttribute("description")}</p>
            </div>  
    `;
    }
}

customElements.define('image_wrapper-component', ImageWrapper);
