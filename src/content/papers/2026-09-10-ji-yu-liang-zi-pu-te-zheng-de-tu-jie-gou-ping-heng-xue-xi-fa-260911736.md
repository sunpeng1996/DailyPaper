---
title: Learning structural balance of graphs from quantum spectral features
title_zh: 基于量子谱特征的图结构平衡学习方法
authors:
- Stefano Scali
- Oleksandr Kyriienko
affiliations:
- University of Exeter, UK
- University of Sheffield, UK
arxiv_id: '2609.11736'
url: https://arxiv.org/abs/2609.11736
pdf_url: https://arxiv.org/pdf/2609.11736
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 量子机器学习 · 符号图特征提取
tags:
- Graph Learning
- Quantum ML
- Spectral Feature
- Signed Graph
- Feature Extraction
one_liner: 提出基于量子哈密顿量态密度矩的符号图特征，高效学习NP难的图结构平衡指标
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
符号图结构平衡核心度量挫折指数求解为NP难问题，传统图谱特征提取依赖经典矩阵对角化，大尺度场景效率极低，缺乏量子可实现的高效提取方案。
### 方法关键点
1. 将符号图映射为含正负交互的Ising模型，以Ising态密度（DOS）的标准化矩作为学习特征，具备切换不变、尺寸无关特性；
2. 提出DOS-QPE量子相位估计方案，相较基于Hadamard测试的迹采样，采样shot数降低数个量级，提取的特征可直接输入经典训练模型。
### 关键结果
在1.4×10^5个标注图数据集上，精确DOS可完全确定挫折指数，仅用5个矩即可实现平均误差0.4，远低于1次符号翻转的误差水平；零场场景下可经典采样验证量子提取结果，非零场下可提取无经典高效采样方案的谱特征。
