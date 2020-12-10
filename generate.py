import json

data = {
    "name": "IBM",
    "globals": {
        "background": "#161616",
        "foreground": "#ffffff",
        "selection": "#262626",
        "selection_border": "#ffffff",
        "caret": "#0f62fe",
    },
    "rules": [
        {
            "name": "Red 40",
            "foreground": "#ff8389",
            "scope": ", ".join([
                "constant.numeric",
                "constant.other.color"
            ])
        },
        {
            "name": "Magenta 40",
            "foreground": "#ff7eb6",
            "scope": ", ".join([
                "keyword",
                "punctuation.definition.numeric",
                "punctuation.separator.combinator",
                "entity.other.pseudo-class",
                "entity.other.pseudo-element",
                "storage.type.function.arrow"
            ])
        },
        {
            "name": "Purple 40",
            "foreground": "#be95ff",
            "scope": ", ".join([
                "constant.language",
                "support.type",
                "support.class",
                "support.other.namespace",
                "entity.name.class",
                "entity.other.inherited-class",
                "entity.name.interface",
                "entity.name.trait",
                "entity.name.namespace",
                "entity.name.struct",
                "entity.name.enum",
                "entity.name.type",
                "variable.type"
            ])
        },
        {
            "name": "Blue 50",
            "foreground": "#4589ff",
            "scope": ", ".join([
                "storage.type",
                "storage.modifier",
                "variable.language",
                "entity.name.tag",
                "support.type.primitive"
            ])
        },
        {
            "name": "Teal 30",
            "foreground": "#3ddbd9",
            "scope": ", ".join([
                "variable.function",
                "variable.annotation",
                "entity.name.function",
                "entity.other.attribute-name",
                "support.function"
            ])
        },
        {
            "name": "Green 30",
            "foreground": "#6fdc8c",
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
                "punctuation",
                "keyword.operator.type.annotation"
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
                "storage.type",
                "storage.modifier",
                "variable.language",
                "entity.name.tag",
                "entity.other.pseudo-class",
                "entity.other.pseudo-element",
                "support.type.primitive"
            ]),
            "font_style": "italic"
        },
        {
            "name": "None",
            "scope": ", ".join([
                "keyword.operator.arithmetic",
                "keyword.operator.comparison",
                "keyword.operator.assignment",
                "keyword.operator.unpacking",
                "keyword.operator.relational",
                "keyword.operator.optional",
                "keyword.operator.type.annotation",
                "storage.type.function.arrow",
                "entity.name.tag.html",
                "entity.name.tag."
            ]),
            "font_style": ""
        }
    ]
}

with open('ibm.sublime-color-scheme', 'w') as outfile:
    json.dump(data, outfile, indent=4)
