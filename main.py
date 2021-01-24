from server import setup_server

app = setup_server()

def main() -> None:
  port = 8080
  # host = '127.0.0.1'
  host = '0.0.0.0'

  app.run(host=host, port=port, debug=False)

if __name__ == '__main__':
  main()
