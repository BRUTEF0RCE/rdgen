import re
from pathlib import Path


PATCH_NAME = "aom-nasm-3.diff"
PATCH = """diff --git a/build/cmake/aom_optimization.cmake b/build/cmake/aom_optimization.cmake
--- a/build/cmake/aom_optimization.cmake
+++ b/build/cmake/aom_optimization.cmake
@@ -214,3 +214,3 @@
 function(test_nasm)
-  execute_process(COMMAND ${CMAKE_ASM_NASM_COMPILER} -hf
+  execute_process(COMMAND ${CMAKE_ASM_NASM_COMPILER} -hO
                   OUTPUT_VARIABLE nasm_helptext)
@@ -220,5 +220,7 @@
       FATAL_ERROR "Unsupported nasm: multipass optimization not supported.")
   endif()
 
+  execute_process(COMMAND ${CMAKE_ASM_NASM_COMPILER} -hf
+                  OUTPUT_VARIABLE nasm_helptext)
   if("${AOM_TARGET_CPU}" STREQUAL "x86")
     if("${AOM_TARGET_SYSTEM}" STREQUAL "Darwin")
"""


def main():
    port = Path("res/vcpkg/aom")
    portfile = port / "portfile.cmake"
    if not portfile.exists():
        print("No aom overlay port; skipping NASM compatibility patch.")
        return

    source = portfile.read_text(encoding="utf-8")
    if PATCH_NAME in source:
        print("aom NASM compatibility patch already registered.")
        return

    patched, count = re.subn(
        r"(REF\s+(?:8ad484f8a18ed1853c094e7d3a4e023b2a92df28|"
        r"10aece4157eb79315da205f39e19bf6ab3ee30d0)\b[^)]*?\bPATCHES)\b",
        rf"\1\n            {PATCH_NAME}",
        source,
    )
    if not count:
        print("No affected aom source revisions; skipping NASM compatibility patch.")
        return

    (port / PATCH_NAME).write_text(PATCH, encoding="utf-8")
    portfile.write_text(patched, encoding="utf-8")
    print(f"Registered upstream NASM compatibility patch for {count} aom revisions.")


if __name__ == "__main__":
    main()