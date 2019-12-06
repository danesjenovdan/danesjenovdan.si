const fs = require('fs');
const path = require('path');
const sass = require('node-sass');

module.exports = {
  'fs-readFile($filePath)': (filePath) => {
    const resolvedPath = path.resolve(path.join('./', filePath.getValue()));
    try {
      return sass.types.String(fs.readFileSync(resolvedPath, 'utf-8'));
    } catch (error) {
      return sass.types.String(String(error));
    }
  },
  'encode-svg($svg)': (svg) => {
    return sass.types.String(
      `"data:image/svg+xml,${encodeURIComponent(svg.getValue())}"`,
    );
  },
  'string-replace($str, $find, $replace: "")': (str, find, replace) => {
    return sass.types.String(
      str
        .getValue()
        .split(find.getValue())
        .join(replace.getValue()),
    );
  },
};
