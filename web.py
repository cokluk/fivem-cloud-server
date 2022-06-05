from http import server
import os, asyncio, base64, random, multiprocessing, signal, psutil, jinja2, aiohttp_jinja2, aiohttp_session
from threading import Thread
from cryptography import fernet
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage

routes = web.RouteTableDef()

ports = [1]
servers = {}
min_port = 30000
max_port = 30010
server_ip = "185.243.182.225"

def get_port(sv_licenseKey):
    r = random.randrange(min_port, max_port)
    i = 1
    for x in range(min_port, max_port):
        if int(x) in ports:
           i=i+1
    if i >= (max_port - min_port):
        return "Slot not available!"    
    servers[int(r)] = multiprocessing.Process(target=create_server, args=(r,sv_licenseKey,))
    servers[int(r)].start()
    return r

def create_server(port, sv_licenseKey):
    ports.append(port)
    os.system(f"""/home/rare/fivem/run.sh +exec /home/rare/fivem/server.cfg +endpoint_add_tcp "0.0.0.0:{port}" +endpoint_add_udp "0.0.0.0:{port}" +set onesync_enableInfinity 1 +set sv_enforceGameBuild 2189 +sv_licenseKey "{sv_licenseKey}" >/dev/null 2>&1 """)
    return "Pending..."

@routes.get("/requestSlot")
async def requestSlot(request):
    if "sv_licenseKey" not in request.query:
        raise web.HTTPClientError()
    try:
        sv_licenseKey = request.query["sv_licenseKey"]
    except ValueError:
        raise web.HTTPClientError()
    return web.json_response({"slot": get_port(sv_licenseKey), "ip": server_ip, "thread": 1, "sv_licenseKey": sv_licenseKey })

@routes.post("/stopServer")
async def stopServer(request):
    data = await request.post()
    for proc in psutil.process_iter():
     for conns in proc.connections(kind='inet'):
        if conns.laddr.port == int(data["port"]):
            print("Task Terminated!")
            proc.send_signal(signal.SIGTERM)
    return web.json_response({ "status": True })

@routes.get("/")
async def index(request):
    return aiohttp_jinja2.render_template("index.html", request, context = {})

@routes.get("/stop")
async def index(request):
    return aiohttp_jinja2.render_template("stop.html", request, context={})
 

async def main():
    global app
    app = web.Application()
    app.add_routes(routes)
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("www"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 80)
    await site.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()