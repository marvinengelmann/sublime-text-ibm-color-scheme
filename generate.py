import json

data = {
    "name": "IBM",
    "globals": {
        "background": "#161616",
        "foreground": "#ffffff",
        "selection": "#262626",
        "selection_border": "#78a9ff",
        "caret": "#0f62fe",
    },
    "rules": [
        {
            "name": "Red 50",
            "foreground": "#fa4d56",
            "scope": ", ".join([
                "constant.numeric"
            ])
        },
        {
            "name": "Magenta 50",
            "foreground": "#ee5396",
            "scope": ", ".join([
                "keyword",
                "punctuation.definition.numeric"
            ])
        },
        {
            "name": "Purple 50",
            "foreground": "#a56eff",
            "scope": ", ".join([
                "constant.language",
                "support.type",
                "support.class",
                "support.other.namespace",
                "entity.name.class",
                "entity.other.inherited-class",
                "entity.name.interface",
                "entity.name.trait",
                "entity.name.namespace"
            ])
        },
        {
            "name": "Blue 50",
            "foreground": "#4589ff",
            "scope": ", ".join([
                "storage.type",
                "storage.modifier",
                "variable.language",
            ])
        },
        {
            "name": "Teal 40",
            "foreground": "#08bdba",
            "scope": ", ".join([
                "variable.function",
                "variable.annotation",
                "entity.name.function",
                "support.function"
            ])
        },
        {
            "name": "Green 40",
            "foreground": "#42be65",
            "scope": ", ".join([
                "string"
            ])
        },
        {
            "name": "Gray 70",
            "foreground": "#525252",
            "scope": ", ".join([
                "comment",
                "punctuation.definition.comment"
            ])
        },
        {
            "name": "Gray 30",
            "foreground": "#c6c6c6",
            "scope": ", ".join([
                "punctuation"
            ])
        },
        {
            "name": "White",
            "foreground": "#ffffff",
            "scope": ", ".join([
            ])
        },
        {
            "name": "Italic",
            "scope": ", ".join([
                "constant.language",
                "keyword",
                "keyword.operator.logical",
                "storage.type",
                "storage.modifier",
                "variable.language"
            ]),
            "font_style": "italic"
        },
        {
            "name": "None",
            "scope": ", ".join([
                "keyword.operator"
            ]),
            "font_style": ""
        }
    ]
}

with open('ibm.sublime-color-scheme', 'w') as outfile:
    json.dump(data, outfile, indent=4)
