let toolbox = {
  "kind": "flyoutToolbox",
  "contents": []
};

let customGen = new Blockly.Generator("Custom Python")

function make(name, json, func) {
  Blockly.Blocks["c::" + name] = {
    init: function() { this.jsonInit(json); }
  };
  toolbox.contents.push({
    "kind": "block",
    "type": "c::" + name
  });
  customGen["c::" + name] = func;
}

let newBlockGen = console.log;

let workspace = null;

window.addEventListener("load", () => {
  workspace = Blockly.inject("blocklyDiv", { "toolbox": toolbox });
})
