import ast, json

blocks = []

def block(name: str, layout: dict, num: tuple[int, int, int]):
    def app(fn):
        blocks.append((name, fn, layout, num))
        return fn
    return app

def gen():
    ret = ""
    for n, f, l, (fl, vl, st) in blocks:
        ret += f"newBlockGen('{n}', {json.dumps(l)}, {{ 'fields': {fl}, 'values': {vl}, 'statements': {st} }});\n"
    return ret
