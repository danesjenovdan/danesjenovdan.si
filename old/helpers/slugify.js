import standardSlugify from 'standard-slugify';

function slugify(string, options) {
  return standardSlugify(string, options).replace(/-+/g, '-');
}

export { slugify };
