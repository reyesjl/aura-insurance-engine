/** Generic normal response type for API endpoints. */
export interface NormalResponse<T> {
    status: string;
    message: string;
    data: T;
}