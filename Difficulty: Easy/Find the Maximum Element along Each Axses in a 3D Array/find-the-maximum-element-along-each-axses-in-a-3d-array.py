def max_along_axes(arr, n):
    # Find the maximum element along each axis in the 3D array
    arr = np.max(arr, axis=n)
    return arr