# 应用场景

## 样例

[Mer-car-i](https://www.reddit.com/r/Mercari/comments/8o1p14/how_do_you_guys_pronounce_mercari_mercari_or/) 

Mercari Price Suggestion Challenge



## 数据

[Porto Seguro’s Safe Driver Prediction](https://www.kaggle.com/competitions/porto-seguro-safe-driver-prediction/overview/evaluation)




> id,target,ps_ind_01,ps_ind_02_cat,ps_ind_03,ps_ind_04_cat,ps_ind_05_cat,ps_ind_06_bin,ps_ind_07_bin,ps_ind_08_bin,ps_ind_09_bin,ps_ind_10_bin,ps_ind_11_bin,ps_ind_12_bin,ps_ind_13_bin,ps_ind_14,ps_ind_15,ps_ind_16_bin,ps_ind_17_bin,ps_ind_18_bin,ps_reg_01,ps_reg_02,ps_reg_03,ps_car_01_cat,ps_car_02_cat,ps_car_03_cat,ps_car_04_cat,ps_car_05_cat,ps_car_06_cat,ps_car_07_cat,ps_car_08_cat,ps_car_09_cat,ps_car_10_cat,ps_car_11_cat,ps_car_11,ps_car_12,ps_car_13,ps_car_14,ps_car_15,ps_calc_01,ps_calc_02,ps_calc_03,ps_calc_04,ps_calc_05,ps_calc_06,ps_calc_07,ps_calc_08,ps_calc_09,ps_calc_10,ps_calc_11,ps_calc_12,ps_calc_13,ps_calc_14,ps_calc_15_bin,ps_calc_16_bin,ps_calc_17_bin,ps_calc_18_bin,ps_calc_19_bin,ps_calc_20_bin
> 7,0,2,2,5,1,0,0,1,0,0,0,0,0,0,0,11,0,1,0,0.7,0.2,0.7180703307999999,10,1,-1,0,1,4,1,0,0,1,12,2,0.4,0.8836789178,0.3708099244,3.6055512755000003,0.6,0.5,0.2,3,1,10,1,10,1,5,9,1,5,8,0,1,1,0,0,1
> 9,0,1,1,7,0,0,0,0,1,0,0,0,0,0,0,3,0,0,1,0.8,0.4,0.7660776723,11,1,-1,0,-1,11,1,1,2,1,19,3,0.316227766,0.6188165191,0.3887158345,2.4494897428,0.3,0.1,0.3,2,1,9,5,8,1,7,3,1,1,9,0,1,1,0,1,0
> 13,0,5,4,9,1,0,0,0,1,0,0,0,0,0,0,12,1,0,0,0.0,0.0,-1.0,7,1,-1,0,-1,14,1,1,2,1,60,1,0.316227766,0.6415857163,0.34727510710000004,3.3166247904,0.5,0.7,0.1,2,2,9,1,8,2,7,4,2,7,7,0,1,1,0,1,0
> 16,0,0,1,2,0,0,1,0,0,0,0,0,0,0,0,8,1,0,0,0.9,0.2,0.5809475019,7,1,0,0,1,11,1,1,3,1,104,1,0.3741657387,0.5429487899000001,0.2949576241,2.0,0.6,0.9,0.1,2,4,7,1,8,4,2,2,2,4,9,0,0,0,0,0,0
> 17,0,0,2,0,1,0,1,0,0,0,0,0,0,0,0,9,1,0,0,0.7,0.6,0.840758586,11,1,-1,0,-1,14,1,1,2,1,82,3,0.3160696126,0.5658315025,0.3651027253,2.0,0.4,0.6,0.0,2,2,6,3,10,2,12,3,1,1,3,0,0,0,1,1,0
> 19,0,5,1,4,0,0,0,0,0,1,0,0,0,0,0,6,1,0,0,0.9,1.8,2.3326487091,10,0,-1,0,0,14,1,1,0,1,104,2,0.44598206240000005,0.879049073,0.4062019202,3.0,0.7,0.8,0.4,3,1,8,2,11,3,8,4,2,0,9,0,1,0,1,1,1





## metrics

Normalized Gini Coefficient



​		









## 训练

https://github.com/smallapes/tensorflow-DeepFM



```
$ conda create -n tensorflow python==3.6.4
$ pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```



训练日志见附录







## 结果



|        | Normalized Gini Coefficient mean | Normalized Gini Coefficient std |
| ------ | -------------------------------- | ------------------------------- |
| deepFM | 0.26699                          | 0.00064                         |
| DNN    | 0.25884                          | 0.00248                         |
| FM     | 0.26695                          | 0.00274                         |



## 总结 md



​	





# 附录







## 训练日志



```
2022-08-07 22:47:47.759234: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
#params: 13483
[1] train-result=0.1240, valid-result=0.1381 [13.7 s]
[2] train-result=0.2430, valid-result=0.2355 [13.3 s]
[3] train-result=0.2636, valid-result=0.2516 [14.6 s]
[4] train-result=0.2705, valid-result=0.2577 [13.2 s]
[5] train-result=0.2737, valid-result=0.2594 [13.4 s]
[6] train-result=0.2758, valid-result=0.2614 [13.3 s]
[7] train-result=0.2774, valid-result=0.2620 [14.7 s]
[8] train-result=0.2786, valid-result=0.2629 [15.4 s]
[9] train-result=0.2796, valid-result=0.2634 [14.6 s]
[10] train-result=0.2802, valid-result=0.2639 [14.8 s]
[11] train-result=0.2807, valid-result=0.2647 [14.8 s]
[12] train-result=0.2815, valid-result=0.2650 [15.0 s]
[13] train-result=0.2817, valid-result=0.2648 [14.5 s]
[14] train-result=0.2820, valid-result=0.2646 [16.1 s]
[15] train-result=0.2821, valid-result=0.2651 [14.9 s]
[16] train-result=0.2826, valid-result=0.2657 [13.5 s]
[17] train-result=0.2826, valid-result=0.2652 [13.6 s]
[18] train-result=0.2827, valid-result=0.2652 [13.5 s]
[19] train-result=0.2828, valid-result=0.2656 [14.6 s]
[20] train-result=0.2831, valid-result=0.2659 [13.3 s]
[21] train-result=0.2833, valid-result=0.2659 [13.3 s]
[22] train-result=0.2831, valid-result=0.2654 [13.4 s]
[23] train-result=0.2835, valid-result=0.2657 [13.4 s]
[24] train-result=0.2831, valid-result=0.2657 [13.3 s]
[25] train-result=0.2834, valid-result=0.2662 [14.6 s]
[26] train-result=0.2836, valid-result=0.2659 [13.4 s]
[27] train-result=0.2837, valid-result=0.2657 [13.3 s]
[28] train-result=0.2839, valid-result=0.2663 [13.4 s]
[29] train-result=0.2839, valid-result=0.2660 [13.2 s]
[30] train-result=0.2839, valid-result=0.2662 [14.7 s]
#params: 13483
[1] train-result=-0.0874, valid-result=-0.0047 [13.6 s]
[2] train-result=0.1869, valid-result=0.2092 [13.3 s]
[3] train-result=0.2356, valid-result=0.2257 [13.3 s]
[4] train-result=0.2599, valid-result=0.2437 [14.6 s]
[5] train-result=0.2599, valid-result=0.2496 [13.3 s]
[6] train-result=0.2592, valid-result=0.2480 [13.3 s]
[7] train-result=0.2633, valid-result=0.2499 [13.3 s]
[8] train-result=0.2663, valid-result=0.2479 [13.3 s]
[9] train-result=0.2607, valid-result=0.2504 [13.3 s]
[10] train-result=0.2636, valid-result=0.2484 [14.5 s]
[11] train-result=0.2674, valid-result=0.2555 [13.3 s]
[12] train-result=0.2623, valid-result=0.2519 [13.7 s]
[13] train-result=0.2639, valid-result=0.2510 [13.2 s]
[14] train-result=0.2683, valid-result=0.2539 [13.2 s]
[15] train-result=0.2629, valid-result=0.2520 [14.4 s]
[16] train-result=0.2707, valid-result=0.2572 [13.2 s]
[17] train-result=0.2707, valid-result=0.2553 [13.3 s]
[18] train-result=0.2706, valid-result=0.2557 [13.3 s]
[19] train-result=0.2722, valid-result=0.2575 [13.3 s]
[20] train-result=0.2691, valid-result=0.2566 [13.2 s]
[21] train-result=0.2688, valid-result=0.2555 [14.5 s]
[22] train-result=0.2731, valid-result=0.2592 [13.3 s]
[23] train-result=0.2715, valid-result=0.2569 [13.3 s]
[24] train-result=0.2748, valid-result=0.2624 [13.3 s]
[25] train-result=0.2717, valid-result=0.2611 [13.1 s]
[26] train-result=0.2742, valid-result=0.2628 [14.5 s]
[27] train-result=0.2755, valid-result=0.2645 [13.2 s]
[28] train-result=0.2760, valid-result=0.2637 [13.2 s]
[29] train-result=0.2759, valid-result=0.2626 [13.2 s]
[30] train-result=0.2764, valid-result=0.2678 [13.2 s]
#params: 13483
[1] train-result=0.1502, valid-result=0.1767 [13.8 s]
[2] train-result=0.2468, valid-result=0.2493 [13.5 s]
[3] train-result=0.2621, valid-result=0.2579 [13.5 s]
[4] train-result=0.2675, valid-result=0.2609 [13.5 s]
[5] train-result=0.2708, valid-result=0.2623 [13.3 s]
[6] train-result=0.2737, valid-result=0.2634 [14.6 s]
[7] train-result=0.2760, valid-result=0.2648 [13.3 s]
[8] train-result=0.2773, valid-result=0.2653 [13.4 s]
[9] train-result=0.2780, valid-result=0.2651 [13.3 s]
[10] train-result=0.2791, valid-result=0.2655 [13.4 s]
[11] train-result=0.2796, valid-result=0.2663 [14.6 s]
[12] train-result=0.2803, valid-result=0.2663 [13.3 s]
[13] train-result=0.2805, valid-result=0.2661 [13.4 s]
[14] train-result=0.2808, valid-result=0.2664 [13.4 s]
[15] train-result=0.2808, valid-result=0.2665 [13.3 s]
[16] train-result=0.2814, valid-result=0.2667 [13.3 s]
[17] train-result=0.2816, valid-result=0.2666 [14.6 s]
[18] train-result=0.2815, valid-result=0.2661 [13.3 s]
[19] train-result=0.2814, valid-result=0.2668 [13.5 s]
[20] train-result=0.2816, valid-result=0.2670 [13.3 s]
[21] train-result=0.2820, valid-result=0.2671 [13.3 s]
[22] train-result=0.2820, valid-result=0.2674 [14.5 s]
[23] train-result=0.2821, valid-result=0.2673 [13.4 s]
[24] train-result=0.2822, valid-result=0.2668 [13.4 s]
[25] train-result=0.2821, valid-result=0.2674 [13.3 s]
[26] train-result=0.2821, valid-result=0.2667 [13.3 s]
[27] train-result=0.2823, valid-result=0.2680 [13.3 s]
[28] train-result=0.2823, valid-result=0.2677 [14.6 s]
[29] train-result=0.2823, valid-result=0.2673 [13.3 s]
[30] train-result=0.2823, valid-result=0.2669 [13.3 s]
DeepFM: 0.26699 (0.00064)


#params: 13451
[1] train-result=0.2629, valid-result=0.2499 [10.0 s]
[2] train-result=0.2735, valid-result=0.2579 [10.9 s]
[3] train-result=0.2757, valid-result=0.2593 [9.7 s]
[4] train-result=0.2771, valid-result=0.2610 [9.7 s]
[5] train-result=0.2791, valid-result=0.2628 [9.8 s]
[6] train-result=0.2800, valid-result=0.2637 [9.7 s]
[7] train-result=0.2808, valid-result=0.2642 [10.9 s]
[8] train-result=0.2810, valid-result=0.2645 [9.7 s]
[9] train-result=0.2818, valid-result=0.2652 [9.7 s]
[10] train-result=0.2827, valid-result=0.2651 [9.8 s]
[11] train-result=0.2827, valid-result=0.2647 [9.8 s]
[12] train-result=0.2832, valid-result=0.2649 [9.7 s]
[13] train-result=0.2829, valid-result=0.2656 [10.9 s]
[14] train-result=0.2837, valid-result=0.2657 [9.8 s]
[15] train-result=0.2862, valid-result=0.2662 [9.8 s]
[16] train-result=0.2876, valid-result=0.2658 [9.8 s]
[17] train-result=0.2894, valid-result=0.2664 [9.7 s]
[18] train-result=0.2906, valid-result=0.2653 [11.0 s]
[19] train-result=0.2903, valid-result=0.2656 [9.7 s]
[20] train-result=0.2911, valid-result=0.2657 [9.8 s]
[21] train-result=0.2913, valid-result=0.2645 [9.7 s]
[22] train-result=0.2916, valid-result=0.2629 [9.8 s]
[23] train-result=0.2929, valid-result=0.2649 [9.8 s]
[24] train-result=0.2927, valid-result=0.2650 [11.1 s]
[25] train-result=0.2932, valid-result=0.2646 [9.7 s]
[26] train-result=0.2934, valid-result=0.2651 [9.8 s]
[27] train-result=0.2949, valid-result=0.2639 [9.8 s]
[28] train-result=0.2958, valid-result=0.2638 [9.8 s]
[29] train-result=0.2960, valid-result=0.2638 [11.0 s]
[30] train-result=0.2971, valid-result=0.2632 [9.8 s]
#params: 13451
[1] train-result=0.2516, valid-result=0.2450 [10.0 s]
[2] train-result=0.2670, valid-result=0.2572 [10.4 s]
[3] train-result=0.2713, valid-result=0.2609 [11.1 s]
[4] train-result=0.2742, valid-result=0.2625 [10.3 s]
[5] train-result=0.2766, valid-result=0.2648 [9.9 s]
[6] train-result=0.2769, valid-result=0.2638 [9.8 s]
[7] train-result=0.2784, valid-result=0.2653 [9.8 s]
[8] train-result=0.2799, valid-result=0.2664 [9.8 s]
[9] train-result=0.2825, valid-result=0.2684 [11.1 s]
[10] train-result=0.2843, valid-result=0.2681 [9.8 s]
[11] train-result=0.2847, valid-result=0.2685 [9.8 s]
[12] train-result=0.2861, valid-result=0.2676 [9.8 s]
[13] train-result=0.2866, valid-result=0.2690 [9.7 s]
[14] train-result=0.2872, valid-result=0.2686 [11.0 s]
[15] train-result=0.2879, valid-result=0.2698 [9.8 s]
[16] train-result=0.2878, valid-result=0.2674 [9.8 s]
[17] train-result=0.2889, valid-result=0.2681 [9.8 s]
[18] train-result=0.2892, valid-result=0.2678 [9.8 s]
[19] train-result=0.2899, valid-result=0.2690 [9.9 s]
[20] train-result=0.2898, valid-result=0.2701 [11.0 s]
[21] train-result=0.2906, valid-result=0.2694 [9.9 s]
[22] train-result=0.2911, valid-result=0.2695 [9.8 s]
[23] train-result=0.2918, valid-result=0.2684 [9.8 s]
[24] train-result=0.2919, valid-result=0.2700 [9.8 s]
[25] train-result=0.2923, valid-result=0.2690 [11.0 s]
[26] train-result=0.2930, valid-result=0.2681 [9.8 s]
[27] train-result=0.2933, valid-result=0.2695 [9.9 s]
[28] train-result=0.2945, valid-result=0.2687 [9.8 s]
[29] train-result=0.2954, valid-result=0.2698 [9.8 s]
[30] train-result=0.2978, valid-result=0.2697 [9.8 s]
#params: 13451
[1] train-result=0.2359, valid-result=0.2326 [10.0 s]
[2] train-result=0.2625, valid-result=0.2536 [9.9 s]
[3] train-result=0.2693, valid-result=0.2587 [10.4 s]
[4] train-result=0.2723, valid-result=0.2608 [10.7 s]
[5] train-result=0.2749, valid-result=0.2624 [11.6 s]
[6] train-result=0.2766, valid-result=0.2628 [10.3 s]
[7] train-result=0.2779, valid-result=0.2650 [10.3 s]
[8] train-result=0.2792, valid-result=0.2648 [10.3 s]
[9] train-result=0.2799, valid-result=0.2659 [10.2 s]
[10] train-result=0.2829, valid-result=0.2665 [11.6 s]
[11] train-result=0.2861, valid-result=0.2682 [10.4 s]
[12] train-result=0.2855, valid-result=0.2680 [10.3 s]
[13] train-result=0.2876, valid-result=0.2685 [10.4 s]
[14] train-result=0.2884, valid-result=0.2701 [10.3 s]
[15] train-result=0.2892, valid-result=0.2682 [9.9 s]
[16] train-result=0.2904, valid-result=0.2691 [11.0 s]
[17] train-result=0.2910, valid-result=0.2697 [9.8 s]
[18] train-result=0.2923, valid-result=0.2697 [9.8 s]
[19] train-result=0.2924, valid-result=0.2689 [9.8 s]
[20] train-result=0.2943, valid-result=0.2693 [9.8 s]
[21] train-result=0.2960, valid-result=0.2692 [11.0 s]
[22] train-result=0.2977, valid-result=0.2690 [9.8 s]
[23] train-result=0.2974, valid-result=0.2686 [9.8 s]
[24] train-result=0.2992, valid-result=0.2683 [9.7 s]
[25] train-result=0.2997, valid-result=0.2688 [9.8 s]
[26] train-result=0.3002, valid-result=0.2688 [9.8 s]
[27] train-result=0.3018, valid-result=0.2679 [11.2 s]
[28] train-result=0.3018, valid-result=0.2688 [10.4 s]
[29] train-result=0.3008, valid-result=0.2671 [10.3 s]
[30] train-result=0.3035, valid-result=0.2679 [10.6 s]
FM: 0.26695 (0.00274)


#params: 13436
[1] train-result=-0.0524, valid-result=-0.1344 [12.5 s]
[2] train-result=-0.1246, valid-result=-0.0441 [12.3 s]
[3] train-result=0.1076, valid-result=0.0744 [12.3 s]
[4] train-result=0.0122, valid-result=0.0458 [12.3 s]
[5] train-result=-0.0504, valid-result=0.0093 [14.3 s]
[6] train-result=0.0866, valid-result=0.0571 [13.2 s]
[7] train-result=-0.0317, valid-result=0.0632 [12.9 s]
[8] train-result=0.0264, valid-result=0.0180 [12.6 s]
[9] train-result=0.1865, valid-result=0.1793 [12.9 s]
[10] train-result=0.2362, valid-result=0.2137 [14.0 s]
[11] train-result=0.2224, valid-result=0.2103 [12.7 s]
[12] train-result=0.2494, valid-result=0.2233 [12.9 s]
[13] train-result=0.2038, valid-result=0.1606 [12.9 s]
[14] train-result=0.2529, valid-result=0.2337 [12.7 s]
[15] train-result=0.2453, valid-result=0.2163 [12.7 s]
[16] train-result=0.2608, valid-result=0.2422 [13.9 s]
[17] train-result=0.2672, valid-result=0.2522 [13.0 s]
[18] train-result=0.2684, valid-result=0.2547 [12.9 s]
[19] train-result=0.2747, valid-result=0.2578 [12.7 s]
[20] train-result=0.2756, valid-result=0.2589 [12.8 s]
[21] train-result=0.2753, valid-result=0.2592 [14.1 s]
[22] train-result=0.2721, valid-result=0.2549 [12.8 s]
[23] train-result=0.2775, valid-result=0.2602 [12.8 s]
[24] train-result=0.2739, valid-result=0.2588 [12.7 s]
[25] train-result=0.2738, valid-result=0.2571 [12.9 s]
[26] train-result=0.2737, valid-result=0.2575 [12.8 s]
[27] train-result=0.2711, valid-result=0.2543 [13.8 s]
[28] train-result=0.2750, valid-result=0.2605 [12.5 s]
[29] train-result=0.2707, valid-result=0.2546 [12.5 s]
[30] train-result=0.2785, valid-result=0.2619 [12.5 s]
#params: 13436
[1] train-result=-0.1027, valid-result=-0.1811 [14.0 s]
[2] train-result=-0.1726, valid-result=-0.0924 [12.5 s]
[3] train-result=-0.0669, valid-result=-0.0396 [12.5 s]
[4] train-result=-0.1001, valid-result=-0.0533 [12.5 s]
[5] train-result=0.0319, valid-result=0.1088 [12.5 s]
[6] train-result=0.2046, valid-result=0.1979 [13.7 s]
[7] train-result=0.1420, valid-result=0.1233 [12.5 s]
[8] train-result=0.0925, valid-result=0.0726 [12.5 s]
[9] train-result=0.2030, valid-result=0.1954 [12.5 s]
[10] train-result=0.1864, valid-result=0.1846 [12.5 s]
[11] train-result=0.1518, valid-result=0.1573 [12.6 s]
[12] train-result=0.2322, valid-result=0.2256 [13.7 s]
[13] train-result=0.2377, valid-result=0.2091 [12.6 s]
[14] train-result=0.2589, valid-result=0.2411 [12.5 s]
[15] train-result=0.2499, valid-result=0.2387 [12.6 s]
[16] train-result=0.2584, valid-result=0.2397 [12.5 s]
[17] train-result=0.2516, valid-result=0.2310 [13.8 s]
[18] train-result=0.2383, valid-result=0.2164 [12.5 s]
[19] train-result=0.2622, valid-result=0.2542 [12.5 s]
[20] train-result=0.2739, valid-result=0.2645 [12.5 s]
[21] train-result=0.2731, valid-result=0.2622 [12.5 s]
[22] train-result=0.2744, valid-result=0.2594 [12.5 s]
[23] train-result=0.2729, valid-result=0.2612 [13.8 s]
[24] train-result=0.2692, valid-result=0.2582 [12.5 s]
[25] train-result=0.2722, valid-result=0.2619 [12.5 s]
[26] train-result=0.2749, valid-result=0.2625 [12.5 s]
[27] train-result=0.2753, valid-result=0.2613 [12.5 s]
[28] train-result=0.2662, valid-result=0.2462 [13.7 s]
[29] train-result=0.2720, valid-result=0.2596 [12.5 s]
[30] train-result=0.2667, valid-result=0.2588 [12.6 s]
#params: 13436
[1] train-result=-0.0201, valid-result=-0.0177 [12.8 s]
[2] train-result=0.0243, valid-result=0.0337 [13.8 s]
[3] train-result=0.0987, valid-result=0.0835 [12.6 s]
[4] train-result=0.0727, valid-result=0.0445 [12.5 s]
[5] train-result=0.1716, valid-result=0.1248 [12.5 s]
[6] train-result=0.1773, valid-result=0.1108 [12.5 s]
[7] train-result=0.2073, valid-result=0.1684 [12.5 s]
[8] train-result=0.1973, valid-result=0.1625 [13.8 s]
[9] train-result=0.2376, valid-result=0.1921 [13.2 s]
[10] train-result=0.2514, valid-result=0.2240 [12.6 s]
[11] train-result=0.2537, valid-result=0.2259 [12.6 s]
[12] train-result=0.2485, valid-result=0.2176 [12.6 s]
[13] train-result=0.2395, valid-result=0.2262 [14.1 s]
[14] train-result=0.2649, valid-result=0.2478 [12.6 s]
[15] train-result=0.2632, valid-result=0.2559 [12.6 s]
[16] train-result=0.2643, valid-result=0.2543 [12.6 s]
[17] train-result=0.2640, valid-result=0.2514 [12.6 s]
[18] train-result=0.2710, valid-result=0.2564 [12.6 s]
[19] train-result=0.2746, valid-result=0.2600 [13.8 s]
[20] train-result=0.2764, valid-result=0.2586 [12.5 s]
[21] train-result=0.2715, valid-result=0.2536 [12.5 s]
[22] train-result=0.2728, valid-result=0.2574 [12.6 s]
[23] train-result=0.2744, valid-result=0.2561 [12.5 s]
[24] train-result=0.2722, valid-result=0.2555 [13.8 s]
[25] train-result=0.2764, valid-result=0.2586 [12.5 s]
[26] train-result=0.2760, valid-result=0.2612 [12.6 s]
[27] train-result=0.2714, valid-result=0.2559 [12.6 s]
[28] train-result=0.2736, valid-result=0.2597 [12.5 s]
[29] train-result=0.2737, valid-result=0.2626 [12.6 s]
[30] train-result=0.2705, valid-result=0.2559 [13.9 s]
DNN: 0.25884 (0.00248)
```





# 其他

// 清华镜像

https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

// 环境导出

https://blog.csdn.net/chekongfu/article/details/83187591

pip freeze >> requirements.txt



## // gini coefficient

https://zhuanlan.zhihu.com/p/76667156

![img](../images/v2-3e63b7fc4766512cd595c4139c9fbfdb_1440w.jpg)

gini coefficient = A/(A+B)



gini coefficient = 2*AUC -1

https://www.kaggle.com/competitions/porto-seguro-safe-driver-prediction/discussion/40706







# debug



```
(python37) lls@changlian example % which python
/Users/changlian.tan/opt/anaconda3/envs/python37/bin/python
(python37) lls@changlian example % conda deactivate
(base) lls@changlian example % which python
/Users/changlian.tan/opt/anaconda3/bin/python
(base) lls@changlian example % conda activate tensorflow1
(tensorflow1) lls@changlian example % which python
/Users/changlian.tan/opt/anaconda3/envs/tensorflow1/bin/python
```





