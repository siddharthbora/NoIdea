function showDetails(productId) {
  // Get the product details container
  var detailsContainer = document.getElementById('detailsContainer');
  // Get the product details div
  var productDetails = document.getElementById('productDetails');

  // Clear previous details
  productDetails.innerHTML = '';

  // Add new details based on productId
  if (productId === 'product1') {
    productDetails.innerHTML = `
      <h3>Product 1 Details</h3>
      <p>Product 1 description...</p>
      <div id="chartContainer1" style="height: 300px; width: 100%;"></div>
    `;

    // Create and render a sample chart (you can replace this with your actual chart code)
    var chart1 = new CanvasJS.Chart('chartContainer1', {
      animationEnabled: true,
      title: {
        text: 'Sample Chart 1'
      },
      data: [{
        type: 'column',
        dataPoints: [
          { label: 'A', y: 10 },
          { label: 'B', y: 20 },
          { label: 'C', y: 30 },
          { label: 'D', y: 40 },
          { label: 'E', y: 50 }
        ]
      }]
    });
    chart1.render();
  } else if (productId === 'product2') {
    productDetails.innerHTML = `
      <h3>Product 2 Details</h3>
      <p>Product 2 description...</p>
      <div id="chartContainer2" style="height: 300px; width: 100%;"></div>
    `;

    // Create and render a sample chart (you can replace this with your actual chart code)
    var chart2 = new CanvasJS.Chart('chartContainer2', {
      animationEnabled: true,
      title: {
        text: 'Sample Chart 2'
      },
      data: [{
        type: 'column',
        dataPoints: [
          { label: 'A', y: 30 },
          { label: 'B', y: 40 },
          { label: 'C', y: 50 },
          { label: 'D', y: 60 },
          { label: 'E', y: 70 }
        ]
      }]
    });
    chart2.render();
  } else if (productId === 'product3') {
    productDetails.innerHTML = `
      <h3>Product 2 Details</h3>
      <p>Product 2 description...</p>
      <div id="chartContainer2" style="height: 300px; width: 100%;"></div>
    `;

    // Create and render a sample chart (you can replace this with your actual chart code)
    var chart2 = new CanvasJS.Chart('chartContainer2', {
      animationEnabled: true,
      title: {
        text: 'Sample Chart 2'
      },
      data: [{
        type: 'column',
        dataPoints: [
          { label: 'A', y: 30 },
          { label: 'B', y: 40 },
          { label: 'C', y: 50 },
          { label: 'D', y: 60 },
          { label: 'E', y: 70 }
        ]
      }]
    });
    chart2.render();
  } else if (productId === 'product4') {
    productDetails.innerHTML = `
      <h3>Product 2 Details</h3>
      <p>Product 2 description...</p>
      <div id="chartContainer2" style="height: 300px; width: 100%;"></div>
    `;

    // Create and render a sample chart (you can replace this with your actual chart code)
    var chart2 = new CanvasJS.Chart('chartContainer2', {
      animationEnabled: true,
      title: {
        text: 'Sample Chart 2'
      },
      data: [{
        type: 'column',
        dataPoints: [
          { label: 'A', y: 30 },
          { label: 'B', y: 40 },
          { label: 'C', y: 50 },
          { label: 'D', y: 60 },
          { label: 'E', y: 70 }
        ]
      }]
    });
    chart2.render();
  }

  // Show the product details container
  detailsContainer.style.display = 'block';
}
