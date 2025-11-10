import http.server
import socketserver
import base64
import urllib.parse


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Ghi log và decode base64 nếu có
        path = self.path
        if path.startswith('/'):
            encoded_data = path[1:]  # bỏ dấu "/"
            try:
                decoded_bytes = base64.b64decode(encoded_data)
                decoded_str = decoded_bytes.decode('utf-8')
                print(f"\n[+] Decode thành công từ base64:\n{decoded_str}")
            except Exception as e:
                print(f"\n[!] Decode thất bại: {e}")
                print(f"[*] Dữ liệu gốc: {encoded_data}")
        super().log_message(format, *args)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


def main():
    port = 1337
    print(f"[+] Khởi động máy chủ callback trên cổng {port}")
    print("[+] Máy chủ sẽ tự động decode base64 từ URL path")
    with socketserver.TCPServer(("", port), CallbackHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Máy chủ callback đã dừng.")


if __name__ == '__main__':
    main()