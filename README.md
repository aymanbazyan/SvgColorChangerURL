# Simple SVG Color Replacer Web App

This is a simple Flask-based web application that allows you to upload SVG files and replace specific colors via a GET request.

## How It Works

- Place your SVG files in the `svgs/` directory.
- Send a GET request in the following format:

  ```
  /svgs/<filename>.svg?old=<old_color>&new=<new_color>
  ```

- The application will return the modified SVG file with all instances of `old_color` replaced by `new_color`.

### Example Request

```
http://127.0.0.1:5000/svgs/dog-and-cat-1.svg?old=2596BE&new=542532
```

This request loads `dog-and-cat-1.svg` and replaces all occurrences of `#2596BE` with `#542532`.
