#ifndef BINARY_SEARCH_H
#define BINARY_SEARCH_H

#ifdef _WIN32
  #include <windows.h>
  #define DLL_EXPORT __declspec(dllexport)
#else
  #define DLL_EXPORT
#endif


extern "C" {

    int DLL_EXPORT binary_search(const int *arr, const int len, const int search);

}

#endif /* BINARY_SEARCH_H */
