coconut_sources = $(wildcard coconut/**.coco)

coconut_generated: coconut/
	coconut -k --no-tco --target 35 coconut omni_converter/coconut
