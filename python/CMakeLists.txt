
add_subdirectory(pybind11)

include_directories(${PYTHON_INCLUDE_DIRS})


pybind11_add_module(pyopengv pyopengv.cpp)
target_link_libraries(pyopengv PRIVATE opengv)

set_target_properties(pyopengv PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/pyopengv"
)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../README.txt
               ${CMAKE_CURRENT_BINARY_DIR}/README.txt
               COPYONLY)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/setup.py
               ${CMAKE_CURRENT_BINARY_DIR}/setup.py
               COPYONLY)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/pyopengv/__init__.py
               ${CMAKE_CURRENT_BINARY_DIR}/pyopengv/__init__.py
               COPYONLY)
