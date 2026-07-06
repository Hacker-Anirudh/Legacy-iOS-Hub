# Legacy iOS Hub

<https://ios.sudothelinuxwizard.com>

or for iOS 6 and earlier

<http://ios.sudothelinuxwizard.com>

The one-stop shop for older iOS devices!

A simple, extremely lightweight (absolutely no JavaScript) website collecting wallpapers, jailbreaks, certificates, and other legacy iOS resources.

## Known issues

- GitHub Pages uses TLS 1.2. Devices running iOS 6 and earlier will need to use the HTTP website because those devices only support older TLS versions.

## Build guide

There is no build step, as the website is pure HTML and CSS. To contribute, edit the files directly and open a pull request.

### Adding wallpapers

1. Put the image file into the appropriate `wallpapers/<collection>/` folder (create a new folder for a new collection).
2. Add a thumbnail entry to that collection's `index.html`. Use a code block for the HTML example so the tags are preserved:

```html
<a href="[filename]"><img src="[filename]" alt="[alt name]"></a>
```

## Features

- Install updated root certificates (from <tlsroot.litten.ca>)
- Add Cydia repositories with one click
- Links to some of the websites that still work on older iOS versions
- A limited collection of web-based jailbreaks (if you have anymore please contact me at [thenasaplusit@proton.me](mailto:thenasaplusit@proton.me))
- Download a vast collection of modern Apple wallpapers (if you would like to see any more, again: [thenasaplusit@proton.me](mailto:thenasaplusit@proton.me))

## Compatibility

I tested down to iOS 6.1.3. It will likely work on older versions (there is barely anything to be incompatible with, most likely even [Mosaic browser](https://en.wikipedia.org/wiki/NCSA_Mosaic) could load the HTTP page), but I can not confirm those. Please inform me if you find any incompatibility with older versions.
It is meant to be used on iOS 11 and earlier given those have the most difficulty with modern websites, but will work on newer versions (obviously).

## Credits

- Wallpapers: <https://www.idownloadblog.com/>
- Certificate bundles: <https://tlsroot.litten.ca>

## Disclaimers

I did not make the certificate bundles, but it is worth mentioning you should be cautious with any root certificates you find on the internet. That being said, I have verified them and this site uses HTTPS for iOS 7+, so they should, in theory, be good. If you trust me, that is - at the end of the day that is your call to make.

## Licensing

Copyright (C) 2020-2026 Anirudh Menon
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.