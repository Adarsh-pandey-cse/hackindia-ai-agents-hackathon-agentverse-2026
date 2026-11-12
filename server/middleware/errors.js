/**
 * Centralized Error Handling Middleware Alias
 * Re-exports errorHandler and ApiError from server/errors/errorHandler.js
 */
import { errorHandler, ApiError } from '../errors/errorHandler.js';

export { errorHandler, ApiError };
export default errorHandler;
