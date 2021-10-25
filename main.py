from quart import Quart, render_template

app = Quart(__name__, static_folder="static")

@app.route('/')
async def main():
    return await render_template('index.html')

app.run(host='0.0.0.0', port=8080)