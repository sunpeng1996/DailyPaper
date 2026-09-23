---
title: 'ImIR: Image-Instruction Tuning for All-in-One Image Restoration'
title_zh: ImIR：面向一体化图像修复的图像指令微调方法
authors:
- Süleyman Aslan
- Görkay Aydemir
- Mısra Yavuz
- Yunus Bilge Kurt
- Nasrin Rahimi
- Ahmet Rasim Emirdağı
- Burak Can Biner
- M. Akın Yılmaz
affiliations:
- Codeway AI Research
arxiv_id: '2609.25267'
url: https://arxiv.org/abs/2609.25267
pdf_url: https://arxiv.org/pdf/2609.25267
published: '2026-09-20'
collected: '2026-09-23'
category: Other
direction: 图像修复 · 大模型高效微调
tags:
- Image Restoration
- LoRA
- Vision-Language Model
- Instruction Tuning
- Parameter Efficient Fine-tuning
one_liner: 用退化图像自提取的连续指令替代文本prompt，单LoRA适配器支持多类无标签图像修复任务
practical_value: '- 电商商品图劣化（过曝/模糊/低亮）修复场景，可复用「图像自提取指令替代人工文本prompt」的思路，无需人工标注劣化类型，降低落地成本

  - 单GPU 3小时即可训练支持6类修复任务的LoRA适配器，可复用这套低算力适配方案快速迭代垂类场景的图像修复能力

  - 连续指令可缩放的特性，可用于低光增强等非唯一目标的修复场景，支持用户自定义修复程度，适配不同展示需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于文本prompt+LoRA适配预训练图像编辑大模型的修复方案，依赖人工输入劣化类型标签，且文本prompt表征精度有限，无法适配无标签、非唯一目标的修复场景。

### 方法关键点
1. 用退化图像自生成的连续语义指令替代文本prompt，通过轻量token mapper将退化图像的多模态embedding向干净图像embedding空间偏移，生成修复指令；
2. 图像分两路输入：结构信息走VAE路径，语义引导走图像指令路径；
3. 连续指令支持缩放，可生成多档修复结果。

### 关键结果数字
单GPU训练3小时得到的单个LoRA适配器，可支持去噪、去模糊、低光增强等6类修复任务，效果优于同等条件下的文本prompt方案，且支持无劣化标签的任务不可知修复。
