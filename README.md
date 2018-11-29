# Plasticc - Version 2

<span class="notice">
The classes are mapped to an integer. We are using the convention [real_class -> mapped_integer] in our graphics. If
some of the two values is missing (ex: class[xx -> 11]) please refer you to the following mapping.
</span>

# Class Mapping
- 92 -> 0
- 88 -> 1
- 42 -> 2
- 90 -> 3
- 65 -> 4
- 16 -> 5
- 67 -> 6
- 95 -> 7
- 62 -> 8
- 15 -> 9
- 52 -> 10
- 6 -> 11
- 64 -> 12
- 53 -> 13
- unknown_class -> 14

## Data analysis
### Intra galactic
#### Class 6 -> 11
Non periodic but symmetric light curves

![./graphics/light_curves_cls11_object0.png](graphics/light_curves_cls11_object0.png)
![./graphics/light_curves_cls11_object1.png](graphics/light_curves_cls11_object1.png)
![./graphics/light_curves_cls11_object2.png](graphics/light_curves_cls11_object2.png)
![./graphics/light_curves_cls11_object3.png](graphics/light_curves_cls11_object3.png)
![./graphics/light_curves_cls11_object4.png](graphics/light_curves_cls11_object4.png)
![./graphics/light_curves_cls11_object5.png](graphics/light_curves_cls11_object5.png)

#### Class 92 -> 0
Periodic bands (need periodogram): looks like a sinusoid

![./graphics/light_curves_cls0_object0.png](graphics/light_curves_cls0_object0.png)
![./graphics/light_curves_cls0_object1.png](graphics/light_curves_cls0_object1.png)
![./graphics/light_curves_cls0_object2.png](graphics/light_curves_cls0_object2.png)
![./graphics/light_curves_cls0_object3.png](graphics/light_curves_cls0_object3.png)
![./graphics/light_curves_cls0_object4.png](graphics/light_curves_cls0_object4.png)
![./graphics/light_curves_cls0_object5.png](graphics/light_curves_cls0_object5.png)

#### Class 16 -> 5
A lot of points are near 0, some of them are below zero. All the light bands move at the same time

![./graphics/light_curves_cls5_object0.png](graphics/light_curves_cls5_object0.png)
![./graphics/light_curves_cls5_object1.png](graphics/light_curves_cls5_object1.png)
![./graphics/light_curves_cls5_object2.png](graphics/light_curves_cls5_object2.png)
![./graphics/light_curves_cls5_object3.png](graphics/light_curves_cls5_object3.png)
![./graphics/light_curves_cls5_object4.png](graphics/light_curves_cls5_object4.png)
![./graphics/light_curves_cls5_object5.png](graphics/light_curves_cls5_object5.png)


#### Class 53 -> 13
Periodic bands (but not regular as class 92 -> 0)

![./graphics/light_curves_cls13_object0.png](graphics/light_curves_cls13_object0.png)
![./graphics/light_curves_cls13_object1.png](graphics/light_curves_cls13_object1.png)
![./graphics/light_curves_cls13_object2.png](graphics/light_curves_cls13_object2.png)
![./graphics/light_curves_cls13_object3.png](graphics/light_curves_cls13_object3.png)
![./graphics/light_curves_cls13_object4.png](graphics/light_curves_cls13_object4.png)
![./graphics/light_curves_cls13_object5.png](graphics/light_curves_cls13_object5.png)


#### Class 65 -> 4
Very stable bands with very high points (use median absolute deviation to detect outliers)

![./graphics/light_curves_cls4_object0.png](graphics/light_curves_cls4_object0.png)
![./graphics/light_curves_cls4_object1.png](graphics/light_curves_cls4_object1.png)
![./graphics/light_curves_cls4_object2.png](graphics/light_curves_cls4_object2.png)
![./graphics/light_curves_cls4_object3.png](graphics/light_curves_cls4_object3.png)
![./graphics/light_curves_cls4_object4.png](graphics/light_curves_cls4_object4.png)
![./graphics/light_curves_cls4_object5.png](graphics/light_curves_cls4_object5.png)


### Extra galactic
#### Class 64 -> 12
Looks like class 64 -> 4 but it's extra galactic

![./graphics/light_curves_cls12_object0.png](graphics/light_curves_cls12_object0.png)
![./graphics/light_curves_cls12_object1.png](graphics/light_curves_cls12_object1.png)
![./graphics/light_curves_cls12_object2.png](graphics/light_curves_cls12_object2.png)
![./graphics/light_curves_cls12_object3.png](graphics/light_curves_cls12_object3.png)
![./graphics/light_curves_cls12_object4.png](graphics/light_curves_cls12_object4.png)
![./graphics/light_curves_cls12_object5.png](graphics/light_curves_cls12_object5.png)


#### Class 88 -> 1
No periodic, very noisy. Almost all points are not at zero.

![./graphics/light_curves_cls1_object0.png](graphics/light_curves_cls1_object0.png)
![./graphics/light_curves_cls1_object1.png](graphics/light_curves_cls1_object1.png)
![./graphics/light_curves_cls1_object2.png](graphics/light_curves_cls1_object2.png)
![./graphics/light_curves_cls1_object3.png](graphics/light_curves_cls1_object3.png)
![./graphics/light_curves_cls1_object4.png](graphics/light_curves_cls1_object4.png)
![./graphics/light_curves_cls1_object5.png](graphics/light_curves_cls1_object5.png)


#### Class 15 -> 9
A lot of points are near 0 but they are rise/descent
Use the ratio between the light bands.

![./graphics/light_curves_cls9_object0.png](graphics/light_curves_cls9_object0.png)
![./graphics/light_curves_cls9_object1.png](graphics/light_curves_cls9_object1.png)
![./graphics/light_curves_cls9_object2.png](graphics/light_curves_cls9_object2.png)
![./graphics/light_curves_cls9_object3.png](graphics/light_curves_cls9_object3.png)
![./graphics/light_curves_cls9_object4.png](graphics/light_curves_cls9_object4.png)
![./graphics/light_curves_cls9_object5.png](graphics/light_curves_cls9_object5.png)


#### Class 42 -> 2
Same as 15 -> 9.

![./graphics/light_curves_cls2_object0.png](graphics/light_curves_cls2_object0.png)
![./graphics/light_curves_cls2_object1.png](graphics/light_curves_cls2_object1.png)
![./graphics/light_curves_cls2_object2.png](graphics/light_curves_cls2_object2.png)
![./graphics/light_curves_cls2_object3.png](graphics/light_curves_cls2_object3.png)
![./graphics/light_curves_cls2_object4.png](graphics/light_curves_cls2_object4.png)
![./graphics/light_curves_cls2_object5.png](graphics/light_curves_cls2_object5.png)


#### Class 52 -> 10
Same as 15 -> 9.
Red bands seems to be lower (check the real bands mapping)

![./graphics/light_curves_cls10_object0.png](graphics/light_curves_cls10_object0.png)
![./graphics/light_curves_cls10_object1.png](graphics/light_curves_cls10_object1.png)
![./graphics/light_curves_cls10_object2.png](graphics/light_curves_cls10_object2.png)
![./graphics/light_curves_cls10_object3.png](graphics/light_curves_cls10_object3.png)
![./graphics/light_curves_cls10_object4.png](graphics/light_curves_cls10_object4.png)
![./graphics/light_curves_cls10_object5.png](graphics/light_curves_cls10_object5.png)


#### Class 62 -> 8
Fast rise/descent

![./graphics/light_curves_cls8_object0.png](graphics/light_curves_cls8_object0.png)
![./graphics/light_curves_cls8_object1.png](graphics/light_curves_cls8_object1.png)
![./graphics/light_curves_cls8_object2.png](graphics/light_curves_cls8_object2.png)
![./graphics/light_curves_cls8_object3.png](graphics/light_curves_cls8_object3.png)
![./graphics/light_curves_cls8_object4.png](graphics/light_curves_cls8_object4.png)
![./graphics/light_curves_cls8_object5.png](graphics/light_curves_cls8_object5.png)


#### Class 67 -> 6
Fast rise/descent

![./graphics/light_curves_cls6_object0.png](graphics/light_curves_cls6_object0.png)
![./graphics/light_curves_cls6_object1.png](graphics/light_curves_cls6_object1.png)
![./graphics/light_curves_cls6_object2.png](graphics/light_curves_cls6_object2.png)
![./graphics/light_curves_cls6_object3.png](graphics/light_curves_cls6_object3.png)
![./graphics/light_curves_cls6_object4.png](graphics/light_curves_cls6_object4.png)
![./graphics/light_curves_cls6_object5.png](graphics/light_curves_cls6_object5.png)


#### Class 90 -> 3
Looks more bright than the others (confirm this hypothesis)

![./graphics/light_curves_cls3_object0.png](graphics/light_curves_cls3_object0.png)
![./graphics/light_curves_cls3_object1.png](graphics/light_curves_cls3_object1.png)
![./graphics/light_curves_cls3_object2.png](graphics/light_curves_cls3_object2.png)
![./graphics/light_curves_cls3_object3.png](graphics/light_curves_cls3_object3.png)
![./graphics/light_curves_cls3_object4.png](graphics/light_curves_cls3_object4.png)
![./graphics/light_curves_cls3_object5.png](graphics/light_curves_cls3_object5.png)

#### Class 95 -> 7
Strong rise (more triangular shape)
The light bands don't reach their max at the same time.

![./graphics/light_curves_cls7_object0.png](graphics/light_curves_cls7_object0.png)
![./graphics/light_curves_cls7_object1.png](graphics/light_curves_cls7_object1.png)
![./graphics/light_curves_cls7_object2.png](graphics/light_curves_cls7_object2.png)
![./graphics/light_curves_cls7_object3.png](graphics/light_curves_cls7_object3.png)
![./graphics/light_curves_cls7_object4.png](graphics/light_curves_cls7_object4.png)
![./graphics/light_curves_cls7_object5.png](graphics/light_curves_cls7_object5.png)

## Features
1. [Intra galactic](#Intra galactic)
2. [Deep survey](#Deep survey)
3. [Periodogram](#Periodogram)
4. [Outliers (using MAD)](#MAD Outliers)
5. [Light bands ratios](#Light bands ratios)
6. [Rises detection](#Rises detection)
7. [Descents detection](#Descents detection)

**Achievements** :
- [x] Intra galactic
- [x] Deep survey
- [ ] Periodogram
- [ ] MAD Outliers
- [ ] Light bands ratios
- [ ] Rises detection
- [ ] Descents detection
 
### Intra galactic
#### Property computation
```python
PHOTOZ = Property('photoz', lambda meta: meta.photoz)
```

#### Selected features
```python
intra_galactic = PHOTOZ == 0.0
# extra_galactic == intra_galactic is False
```

### Deep survey
#### Property computation
```python
DDF = Property('DDF', lambda meta: meta.ddf)
```

#### Selected features
```python
deep_survey = DDF == True
# Wide survey == deep_survey is False
```

### Periodogram
#### Property computation
#### Selected features


### MAD Outliers
#### Property computation
#### Selected features

### Light bands ratios
#### Property computation
#### Selected features

### Rises detection
#### Property computation
#### Selected features

### Descents detection
#### Property computation
#### Selected features