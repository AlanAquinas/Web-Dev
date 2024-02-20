import { Component } from '@angular/core';
import { Product, products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})
export class ProductListComponent {
  products: Product[] = products;
  searchInput: string = '';

  get filteredProducts(): Product[] {
    const searchTerm = this.searchInput.toLowerCase();
    return this.products.filter(product => product.name.toLowerCase().includes(searchTerm));
  }

  shareWA(productName: string, productLink: string) {
    const shareMessage = `Check out this product: ${productName} - ${productLink}`;
    const whatsappLink = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareMessage)}`;
    window.location.href = whatsappLink;
  }

  shareTG(productName: string, productLink: string) {
    const shareMessage = `Check out this product: ${productName} - ${productLink}`;
    const whatsappLink = `https://t.me/share/url?url=${encodeURIComponent(shareMessage)}`;
    window.location.href = whatsappLink;
  }
}
