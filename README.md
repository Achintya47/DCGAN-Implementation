<p align="center">
  <img src="https://pytorch.org/assets/images/pytorch-logo.png" alt="PyTorch Logo" width="160"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.kaggle.com/static/images/site-logo.svg" alt="Kaggle Logo" width="160"/>
</p>

<h1 align="center">DCGAN from Scratch - PyTorch</h1>

<p align="center">
  Implementation of Deep Convolutional GAN (DCGAN) using PyTorch<br>
  Trained on <strong>Kaggle Notebooks</strong> using <strong>anime faces</strong> and <strong>CelebA</strong> datasets.
</p>

---

## ✨ Project Highlights

- ✅ **DCGAN** built from scratch based on the [original paper (arXiv:1511.06434v2)](https://arxiv.org/abs/1511.06434).
- 🧱 Uses `ConvTranspose2d`, `BatchNorm2d`, and correct weight initialization.
- 🎯 Focused training on two datasets — *Anime Faces* and *CelebA Facecards*.
- 📊 Training tracked and visualized with **TensorBoard**.
- 🚀 Implemented and trained on **Kaggle Notebooks**.

---

## 🖼️ Dataset Overview

| Anime Faces Dataset | CelebA Faces Dataset |
|---------------------|----------------------|
|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/real_faces.png" width="400"/>|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/real_anime.png" width="400"/>|

- **Anime Faces Dataset**  
  [Kaggle Link](https://www.kaggle.com/datasets/diraizel/anime-images-dataset)  
  > Diverse set with various artistic styles. Contains full-body characters, posters, and inconsistent framing.

- **CelebA Face Dataset**  
  [Kaggle Link](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset)  
  > High-quality, consistent, and aligned facial images—ideal for DCGAN convergence.

---

## 🚀 Training Progress - TensorBoard Visuals

### 🎨 Anime Faces — First 10 Epochs

| Step 0 to Epoch 10 | |
|--------------------|------------------|
|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/anime_1.png" width="400"/>|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/anime_2.png" width="400"/>|

---

### 🔁 Continued Training to 35 Epochs (Degraded Quality)

| Epoch 10 to 35 | |
|----------------|----------------|
|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/anime_3.png" width="400"/>|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/anime_4.png" width="400"/>|

> ⚠️ **Observation**: Mode collapse and reduced diversity as training continued. The anime dataset has noise and non-face images which led to instability.

---

### 🧑‍🎤 CelebA Faces — First 10 Epochs

| Step 0 to Epoch 10 | |
|--------------------|------------------|
|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/faces_1.png" width="400"/>|<img src="https://raw.githubusercontent.com/Achintya47/Achintya47/main/faces_2.png" width="400"/>|

---

### 🔥 CelebA Faces — Continued to 35 Epochs

| Epoch 10 to 35 | |
|----------------|----------------|
|<img src="./config/face_3.png" width="400"/>|<img src="./config/face_4.png" width="400"/>|

> ✅ **Insight**: CelebA dataset yielded **clearer**, more **consistent** face generations even after prolonged training—thanks to higher quality and alignment.

---

## 📈 Visualizations

Launch TensorBoard locally:

```bash
tensorboard --logdir logs
```




