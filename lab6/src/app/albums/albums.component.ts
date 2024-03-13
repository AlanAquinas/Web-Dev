import {Component, OnInit, OnDestroy} from '@angular/core';
import {AlbumsService} from "../albums.service";
import {Album} from "../album/album.module";
import {RouterLink} from "@angular/router";
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [
    RouterLink,
    CommonModule
  ],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent implements OnInit{

  albums!: Album[];
  loaded: boolean = false;

  constructor(private albumService: AlbumsService) {
  }
  ngOnInit(): void {
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums;
      this.loaded = true;
    })
  }

  deletePost(id: number) {
    this.albums = this.albums.filter(a => a.id !== id)
    this.albumService.deleteAlbum(id).subscribe(() => {
      console.log("Album deleted successfully!")
    })
  }
}
