# Adaptive Text Input
[heading__title]:
  #adaptive-text-input
  "&#x2B06; Top of ReadMe File"


Kivy layout that adapts dimensions based off text volume and active state.


## [![Byte size of adaptive-text-input.py][badge__master__adaptive_grid_layout__source_code]][adaptive_grid_layout__master__source_code] [![Open Issues][badge__issues__adaptive_grid_layout]][issues__adaptive_grid_layout] [![Open Pull Requests][badge__pull_requests__adaptive_grid_layout]][pull_requests__adaptive_grid_layout] [![Latest commits][badge__commits__adaptive_grid_layout__master]][commits__adaptive_grid_layout__master]



------


#### Table of Contents


- [:arrow_up: Top of ReadMe File][heading__title]

- [:zap: Quick Start][heading__quick_start]

  - [:memo: Edit Your ReadMe File][heading__your_readme_file]
  - [:snake: Utilize Adaptive Text Input][heading__utilize]
  - [:floppy_disk: Commit and Push][heading__commit_and_push]

- [&#x1F5D2; Notes][heading__notes]

- [&#x2696; License][heading__license]


------



## Quick Start
[heading__quick_start]:
  #quick-start
  "&#9889; Perhaps as easy as one, 2.0,..."


**Bash Variables**


```Bash
_module_name='adaptive-text-input'
_module_https_url="https://github.com/kivy-utilities/${_module_name}.git"
_module_relative_path="lib/modules/${_module_name//-/_}"
```


**Bash Submodule Commands**


```Bash
cd "<your-git-project-path>"
mkdir -vp "lib/modules"

git submodule add\
 -b master --name "${_module_name}"\
 "${_module_https_url}" "${_module_relative_path}"
```


### Your ReadMe File
[heading__your_readme_file]:
  #your-readme-file
  "&#x1F578; Suggested additions for your ReadMe.md file so everyone has a good time with submodules"


Suggested additions for your _`ReadMe.md`_ file so everyone has a good time with submodules


```MarkDown
Clone with the following to avoid incomplete downloads


    git clone --recurse-submodules <url-for-your-project>


Update/upgrade submodules via


    git submodule update --init --merge --recursive
```


### Utilize Adaptive Text Input
[heading__utilize]:
  #utilize-adaptive-text-input
  "&#x1F40D; How to make use of this submodule within another project"


Incorporate the `adaptive-text-input.kv` file within some layout...


**`kivi/some_screen.kv`**


```Kivy
#:include lib/adaptive_text_input/adaptive-text-input.kv


Some_Screen:
  id: Some_Screen
  name: 'Some Screen'
  group: 'screens'

  ScrollView:
    GridLayout:
      cols: 1
      id: Some_GridLayout

      Adaptive_TextInput:
        synopsis_line_limit: 2
        id: Some_TextInput
```


And/or import and utilize Python class directly...


**`lib/some_screen.py`**


```Python
#!/usr/bin/env python


from kivy.uix.screenmanager import Screen

from lib.modules.adaptive_text_input import Adaptive_TextInput


class Some_Screen(Screen):
  def __init__(self, arg):
    super(Some_Screen, self).__init__()

  def attach_adaptive_text_input(self, input_id, parent, clear = False):
    if clear:
      parent.clear_widgets(children = parent.children)

    new_text_input = Adaptive_TextInput(synopsis_line_limit = 2, id = input_id)
    return parent.add_widget(new_text_input)
```


**Test that things operate as expected** and if it's a bug report it as such, otherwise an adjustment of expectations and/or code may be necessary.


### Commit and Push
[heading__commit_and_push]:
  #commit-and-push
  "&#x1F4BE; It may be just this easy..."


```Bash
git add .gitmodules
git add lib/modules/adaptive-text-input


## Add any changed files too


git commit -F- <<'EOF'
:heavy_plus_sign: Adds `kivy-utilities/adaptive-text-input#1` submodule



**Additions**


- `.gitmodules`, tracks submodules AKA Git within Git _fanciness_

- `README.md`, updates installation and updating guidance

- `lib/modules/adaptive-text-input`, builds list of pages for a named collection
EOF


git push origin master
```


**:tada: Excellent :tada:** your site is now ready to begin unitizing code from this repository!


___


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional resources and things to keep in mind when developing"


To ensure that Kivy honors `height` and/or `width` set `size_hint_y` and/or `size_hint_x` to `None` for each element within layout.


Fonts and Unicode may cause spacing and sizing to become a bit fiddly; or in other words code is **not** fully tested for internationalization.


To make full use of this project consider utilizing the [Adaptive_GridLayout](https://github.com/kivy-utilities/adaptive-grid-layout) source code within projects make use of `Adaptive_TextInput` layouts.


Some portions of logic may seem illogical, please open Pull Requests to correct bugs and/or add features.


Python requires a `__init__.py` within each directory that may be imported...


```Bash
touch lib/__init__.py
touch lib/modules/__init__.py
```


___


## License
[heading__license]:
  #license
  "&#x2696; Legal bits of Open Source software"


Legal bits of Open Source software


```
Adaptive Text Input ReadMe documenting how things like this could be utilized
Copyright (C) 2019  S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```



[badge__commits__adaptive_grid_layout__master]:
  https://img.shields.io/github/last-commit/kivy-utilities/adaptive-text-input/master.svg

[commits__adaptive_grid_layout__master]:
  https://github.com/kivy-utilities/adaptive-text-input/commits/master
  "&#x1F4DD; History of changes on this branch"


[adaptive_grid_layout__community]:
  https://github.com/kivy-utilities/adaptive-text-input/community
  "&#x1F331; Dedicated to functioning code"


[badge__issues__adaptive_grid_layout]:
  https://img.shields.io/github/issues/kivy-utilities/adaptive-text-input.svg

[issues__adaptive_grid_layout]:
  https://github.com/kivy-utilities/adaptive-text-input/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."


[badge__pull_requests__adaptive_grid_layout]:
  https://img.shields.io/github/issues-pr/kivy-utilities/adaptive-text-input.svg

[pull_requests__adaptive_grid_layout]:
  https://github.com/kivy-utilities/adaptive-text-input/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"


[badge__master__adaptive_grid_layout__source_code]:
  https://img.shields.io/github/size/kivy-utilities/adaptive-text-input/__init__.py.svg?label=__init__.py

[adaptive_grid_layout__master__source_code]:
  https://github.com/kivy-utilities/adaptive-text-input/blob/master/__init__.py
  "&#x2328; Project source code!"
