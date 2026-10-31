from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


PASTA_PAINEL = Path(__file__).resolve().parent
ENDERECO_LOCAL = "127.0.0.1"
PORTA_LOCAL = int(os.environ.get("PORTA", "8765"))


class ManipuladorPainel(SimpleHTTPRequestHandler):
    def __init__(self, *argumentos, **opcoes):
        super().__init__(*argumentos, directory=str(PASTA_PAINEL), **opcoes)

    def log_message(self, formato, *argumentos):
        print(f"Acesso local: {self.command} {self.path}")


manipulador = ManipuladorPainel
servidor = ThreadingHTTPServer((ENDERECO_LOCAL, PORTA_LOCAL), manipulador)

print(f"Painel disponível em http://{ENDERECO_LOCAL}:{PORTA_LOCAL}")
print("Pressione Ctrl+C para encerrar o servidor.")

try:
    servidor.serve_forever()
except KeyboardInterrupt:
    print("\nServidor local encerrado.")
finally:
    servidor.server_close()
