# Omni-Converter
> Core of automatic conversion for any data.

Omni-Converter is a tool to automatically compose multiple conversion functions to realize desired conversion.

When we handle image data in python, many different image processing libraries require an image data to be stored in specific format in memory such as numpy, torch, jpg, bytes and so on.

While we can manually convert the format of the image data manually, it is tedeous to compose a conversion function manually.
This library is for automating creation of conversion function from known conversion rules.

These are some examples of what you can do with this library.
```python
from omni_converter import AutoDataFactory
from omni_cv_rules import CV_RULEBOOK
auto = AutoDataFactory(CV_RULEBOOK)
# loading an image
img:"IAutoData" = auto("image_path","path/to/image")
# You can convert it to any format by calling 'to'
# this will automatically search for a composition of functions to convert 'image_path' into numpy array.
ary:np.ndarray = img.to("numpy,uint8,HWC,RGB,0_255")
# CHW means that the tensor shape is (Channel, Height, Widgth).
torch_img:torch.Tensor = img.to("torch,float32,CHW,RGB,0_1")
# BCHW means that the tensor shape is (Batch, Channel, Height, Widgth).
torch_batch:torch.Tensor = img.to("torch,float32,BCHW,RGB,0_1")
# you can start searching from any format
base64_str:str = auto("torch,float32,CHW,RGB,0_1",torch_img).to("base64")
# everything can be changed at once
np_ary:np.ndarray = auto("torch,float32,CHW,RGB,0_1",torch_img).to("numpy,float64,BHWC,BGR,0_1")
# list of format is supported. enclosing any valid format with square bracket means that the data is list of that format. 
paths = ["1.png","2.png"]
auto("[image_path]")(paths).to("torch,float32,BCHW,RGB,0_1")
# and back also
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[torch,float32,CHW,RGB,0_1]") # list of torch array from a batch!
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[image,RGB,RGB]") # list of PIL.Image.Image!
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[base64]") # list of base64
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("[html]") # list of html text
auto("torch,float32,BCHW,RGB,0_1",torch_img).to("widget") # ipywidget for displaying in notebook
```

Since this library is designed as just a core of function composition, no conversion rules are implemented here.
Please take a look at omni-cv-rules library for using conversion rules above.

# Overview
The core components of this library are 'format', Rule, and AstarSolver.

## format
Format is any immutable object that explains the internal data format for planning data conversions.
You can use anything to define your own.
Format needs to be hashable for caching.

Examples: `"numpy,float32,BCHW,RGB,0_1"`, `frozendict(_type=numpy,dtype=np.float32,...)`, `base64_str`

## Rule
Rule is a function that returns a list of possible conversions from a given format.

Examples:
```python
def rule_A_to_AB(format:Any)->List[RuleEdge]:
    if format == "A":
        # you can do any smart handling of a format here.
        return [RuleEdge(
            converter = lambda a:a+["B"],
            new_format = "AB",
            cost=1,#optional
            name="A to AB" # optional name to explain this conversion
        )]
    else:
        return [] # you can also return None.
def rule_AB_to_ABC(format:Any)->List[RuleEdge]:
    if format == "AB":
        return [RuleEdge(
            converter = lambda ab:ab+["C"],
            new_format= "ABC",
            name="AB to ABC"
        )]
    # omit return []
```

## AstarSolver
AstarSolver is a solver that composes multiple functions to find a conversion from given source format and target format.
```python
solver = AstarSolver(
    heuristics=lambda x,y:0,#no heuristics used so it is just a BFS
    neighbors= AutoRuleBook().add_rules(
        rule_A_to_AB,
        rule_AB_to_ABC
    ),
    max_depth=100,
    silent = False # for debugging
)
# lets find a converter from A to ABC
conversion = solver.solve("A","ABC")
# result:
"""
Converter(A => ABC):cost=2
  index  converter    src_format    dst_format
-------  -----------  ------------  ------------
      0  A to AB      A             AB
      1  AB to ABC    AB            ABC
"""
```
