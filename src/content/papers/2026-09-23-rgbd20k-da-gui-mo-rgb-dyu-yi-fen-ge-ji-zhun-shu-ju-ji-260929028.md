---
title: 'RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation'
title_zh: RGBD20K：大规模RGB-D语义分割基准数据集
authors:
- Shaohua Dong
- Zexuan Meng
- Haiyan Sun
- Bing Fan
- Cuicui Zhang
- Dylan Joseph
- Kewei Sha
- Yunhe Feng
- Heng Fan
arxiv_id: '2609.29028'
url: https://arxiv.org/abs/2609.29028
pdf_url: https://arxiv.org/pdf/2609.29028
published: '2026-09-23'
collected: '2026-09-26'
category: Multimodal
direction: 多模态语义分割 · 基准数据集
tags:
- RGB-D
- Semantic Segmentation
- Dataset Benchmark
- Multimodal Fusion
one_liner: 发布含160细分类2万对高质量标注的RGB-D语义分割数据集，提出SPF融合方法达SOTA
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有RGB-D语义分割基准数据集普遍存在类别覆盖少、样本规模小、标注噪声大的缺陷，严重限制了分割模型的泛化能力与性能上限，无法支撑复杂场景下的稠密感知需求。
### 方法关键点
1. 构建RGBD20K大规模基准数据集，覆盖160个细粒度语义类别，包含20000对高质量RGB-D图像对，类别规模远超现有NYUv2（40类）、SUN RGB-D（37类）等主流基准；
2. 对所有标注执行严格的重评估与修正，消除长期存在的标注噪声，保证标注的高保真度；
3. 提出score-purified fusion（SPF）多模态融合方法，高效对齐融合RGB与深度模态的语义信息。
### 关键结果
SPF方法在所有参与评估的RGB-D语义分割基准上达到SOTA性能，数据集已开源至GitHub。
