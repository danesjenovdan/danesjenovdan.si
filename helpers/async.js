function catchError(asyncData) {
  return async (...args) => {
    const error = args[0].error;
    try {
      return await asyncData(...args);
    } catch (err) {
      if (err.response) {
        error({
          statusCode: err.response.status,
          message: err.response.data,
        });
        return;
      }
      error({ statusCode: 500, message: err.message });
    }
  };
}

export { catchError };
