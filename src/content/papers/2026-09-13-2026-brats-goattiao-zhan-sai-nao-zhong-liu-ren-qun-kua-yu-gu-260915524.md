---
title: Assessing nnU-Net Generalization across Brain Tumor Populations in BraTS-GoAT
  2026
title_zh: 2026 BraTS-GoAT挑战赛脑肿瘤人群跨域nnU-Net泛化性能评估
authors:
- Tristan Kirscher
- Vivian Metzger
- Philippe Meyer
- Xavier Coubez
affiliations:
- ICube Laboratory, CNRS UMR 7357, University of Strasbourg
- CLCC Institut Strauss, Strasbourg, France
arxiv_id: '2609.15524'
url: https://arxiv.org/abs/2609.15524
pdf_url: https://arxiv.org/pdf/2609.15524
published: '2026-09-13'
collected: '2026-09-20'
category: Other
direction: 医学影像分割 · 模型泛化性评估
tags:
- nnU-Net
- medical-image-segmentation
- generalization
- test-time-augmentation
- failure-analysis
one_liner: 在BraTS-GoAT异质脑肿瘤数据集上评估3D nnU-Net跨人群泛化能力并分析失效原因
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
跨人群、跨采集协议的脑肿瘤MRI分割泛化性是临床落地核心难点，BraTS-GoAT任务面向多类型异质脑肿瘤数据集评估算法鲁棒性，现有nnU-Net在异质人群下的泛化表现尚未被系统验证。

### 方法关键点
基于1351例标注数据训练常规3D nnU-Net，采用5折交叉验证每折训练1000轮，最终预测器集成所有折输出并添加测试时镜像增强，同时对比残差编码器版本的效果，系统分析失效样本特征。

### 关键结果数字
官方 pooled 验证集上，增强肿瘤（ET）、肿瘤核心（TC）、全肿瘤（WT）的全局DSC分别为0.7805、0.8288、0.8854；异质人群验证较源域OOF集平均DSC下降0.0747；测试时镜像仅单折有小幅收益，无明显集成增益；失效样本多对应ET体积小、ET组件分散的场景。
