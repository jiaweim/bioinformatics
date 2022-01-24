# 颜色设置

- [颜色设置](#颜色设置)
  - [bg_color](#bg_color)
  - [color](#color)
  - [set_color](#set_color)

## bg_color

https://pymolwiki.org/index.php/Bg_Color

```sh
bg_color [color]
```

设置背景颜色。

## color

```sh
color color-name
color color-name, object-name
color color-name, (selection)
```

`color` 设置对象和选择的原子颜色，支持的颜色：

- 预定义颜色
- 颜色名称
- RGB hex
- color ramp

预定义颜色，可以参考 [颜色值](https://pymolwiki.org/index.php/Color_Values)。在脚本中可以使用 [List Colors](https://pymolwiki.org/index.php/List_Colors) 查看颜色列表。

- `color-name`

指定颜色名称。

- `object-name`

待设置颜色的对象名称。如果没有指定任何对象，默认为 all。

- `selection`

选择的原子。

- **例 1**，将所有碳原子设置为黄色：

```sh
color yellow, (name C*)
```

- **例 2**，将除碳以外的所有元素着色

```sh
color atomic, (not elem C)
```

- **例 3**，使用自动 RGB 颜色

```sh
color 0x006600
```

- **例 4**，将 320-376 的氨基酸设置为 limon

```sh
color limon, resi 320-376
```

- **例 5**，设置单个氨基酸的颜色

```sh
color deepteal, resi 333
```

这里将第 333 个残基设置为 deepteal 颜色。

## set_color

https://pymolwiki.org/index.php/Set_Color

自定义颜色。