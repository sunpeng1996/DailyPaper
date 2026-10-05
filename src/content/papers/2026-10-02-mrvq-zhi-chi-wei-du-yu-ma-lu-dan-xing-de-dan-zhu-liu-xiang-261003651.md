---
title: 'MRVQ: One Resident Index for Dimension- and Rate-Elastic Vector Search'
title_zh: MRVQ：支持维度与码率弹性的单驻留向量搜索索引
authors:
- Sean Culatana
- Shang-En Huang
- Kang Li
affiliations:
- Atlassian
- National Taiwan University
arxiv_id: '2610.03651'
url: https://arxiv.org/abs/2610.03651
pdf_url: https://arxiv.org/pdf/2610.03651
published: '2026-10-02'
collected: '2026-10-05'
category: RAG
direction: RAG向量检索 · 弹性量化索引优化
tags:
- Vector Search
- Residual Quantization
- Dense Retrieval
- Memory Optimization
- Elastic Index
one_liner: 提出嵌套残差量化MRVQ，单索引适配多维度多码率，大幅降低检索层内存开销
practical_value: '- 多租户/多业务线向量检索场景可复用MRVQ设计：仅维护1份量化索引即可支撑不同延迟/质量/内存预算的业务需求，省去多套索引的存储和维护成本，尤其适合千万级以下语料的Agent/RAG系统

  - 快速迭代的实时检索场景可直接复用PCA-scalar量化方案：构建速度比OPQ快420倍以上，检索质量与RaBitQ相当，适合需要频繁重建索引的电商商品/内容检索场景

  - 资源约束场景选型参考：内存敏感场景优先选MRVQ，质量优先场景仍用QINCo2；千万级以上超大语料下MRVQ相对共享模型QINCo2的内存优势缩小到10%以内，可按需选型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Dense retrieval是RAG、Agent系统的核心组件，现有部署为适配不同的延迟、质量、内存预算，需同时维护多套不同维度、不同压缩码率的量化索引，检索层内存开销极高；中小规模/多租户场景下量化模型参数甚至占内存的90%以上，亟需单索引同时支持多维度、多码率的弹性量化方案。

### 方法关键点
- 提出MRVQ，针对冻结embedding做后训练残差量化，训练时同时优化所有目标前缀维度的重建误差，生成的最大码率编码支持双向截断：丢弃残差阶段降低码率，丢弃embedding坐标后缀降低维度，无需重编码即可适配任意（维度，码率）组合
- 额外提供轻量PCA-scalar量化方案：先做PCA旋转，按坐标方差分配比特位做标量量化，无需迭代训练码本，构建成本极低

### 关键实验
在BEIR的FiQA、NFCorpus数据集上，覆盖MPNet、BGE等4种主流embedding，对比PQ、OPQ、AdANNS-OPQ、QINCo2等基线：
1. 内存开销：单MRVQ索引比3套独立训练的QINCo2索引内存低17.8~22.0×，比最精简的共享模型QINCo2低1.89~2.02×，千万级语料下相对独立QINCo2的内存优势仍保持1.75×的渐近值
2. 检索质量：相同码率下比OPQ高0.06~0.07 nDCG@10，比PQ高0.10~0.12 nDCG@10，仅比独立训练的QINCo2低0.026~0.107 nDCG@10；PCA-scalar质量与RaBitQ相当，构建速度中位数快420×

### 核心结论
MRVQ是内存约束下弹性向量检索的最优选型，和专用量化方案形成质量-内存的帕累托边界，没有通用最优方案，选型完全取决于业务的核心约束
