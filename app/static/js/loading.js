class Visuals extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div>         
        <div class="row">
        <div class="page-header">Circle progress bar with image</div>
    </div>

    <div class="row">
        <div class="col-lg-3 col-md-3 col-sm-3">

             <div class="wrapper">
                    
                    <svg class="mi-progressbar">
                        <circle id="circle1" r="25%" cx="50%" cy="50%" stroke-width="20"></circle>
                    </svg>

            </div>

        </div>

    </div>  
    `;
  }
}

customElements.define('visual-component', Visuals);