/** Generic paginated response type for API endpoints that use pagination.
 * Use as: PaginatedResponse<Question>, PaginatedResponse<User>, etc.
 * 
 * Note: based on Django REST Framework's pagination structure.
 */
export interface PaginatedResponse<T> {
    count: number;
    next?: string;
    previous?: string;
    results: T[];
}