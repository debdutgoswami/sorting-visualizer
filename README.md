[![HitCount](http://hits.dwyl.com/debdutgoswami/sorting-visualizer.svg)](http://hits.dwyl.com/debdutgoswami/sorting-visualizer)

<p align="center">
<a href="https://pypi.org/project/sorting-visualizer/" rel="nofollow"><img src="" alt="image" style="max-width:100%;"></a>
<img src="https://img.shields.io/github/license/debdutgoswami/sorting-visualizer" alt="image" style="max-width:100%;">
<img src="https://img.shields.io/github/stars/debdutgoswami/sorting-visualizer" alt="image" style="max-width:100%">
</p>

# Sorting Visualizer

A simple python project which visualizes various sorting algorithms. 

---

## How to setup

Simply open up your terminal and type

```
pip3 install sorting-visualizer
```

---

## Algorithms Implemented

- [x] Bubble Sort (bubblesort)
- [x] Selection Sort (selectionsort)
- [x] Insertion Sort (insertionsort)
- [x] Merge Sort (mergesort)
- [ ] Quick Sort
- [ ] Heap Sort

---

## Prerequisite

1. [ffmpeg](https://www.ffmpeg.org/download.html)

---

## How to use

1. Show the plot

    ```
    from sorting_visualizer import visualizer
    visualizer.visualize('bubblesort')
    ```

2. Show and save the plot

    ```
    from sorting_visualizer import visualizer
    visualizer.visualize('bubblesort', save=True)
    ```

3. Only save the plot and not show it

    ```
    from sorting_visualizer import visualizer
    visualizer.visualize('bubblesort', save=True, show=False)
    ```

4. Saving in a particular location

    ```
    from sorting_visualizer import visualizer
    visualizer.visualize('bubblesort', save=True, path='path/to/directory')
    ```

The default saving location is your current working directory.