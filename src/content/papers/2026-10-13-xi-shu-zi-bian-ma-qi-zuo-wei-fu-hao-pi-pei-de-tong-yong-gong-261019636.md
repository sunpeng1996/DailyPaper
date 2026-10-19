---
title: Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching
title_zh: 稀疏自编码器作为符号匹配的通用共享坐标系
authors:
- Xiaocong Yang
- Xuanyu Meng
- Yuji Zhang
- Jiawei Han
- ChengXiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.19636'
url: https://arxiv.org/abs/2610.19636
pdf_url: https://arxiv.org/pdf/2610.19636
published: '2026-10-13'
collected: '2026-10-19'
category: LLM
direction: LLM可解释性 · 跨系统符号匹配
tags:
- Sparse Autoencoder
- Symbolic Matching
- Interpretability
- LLM
- TF-IDF
one_liner: 提出无需训练的SAE-IDF方法，基于稀疏自编码器与稀有度权重实现跨异构系统的可解释符号匹配
practical_value: '- 可复用SAE+IDF的权重思路优化召回/语义匹配场景：商品/Query语义编码后，对高频通用特征降权、稀有特征提权，避免通用特征主导相似度计算，提升跨域/跨模态匹配准确率

  - 做可解释匹配链路时可引入SAE稀疏可解释特征，每个匹配结果可拆解为具体概念维度的贡献，满足电商合规、推荐理由生成需求，比如用户搜「露营椅」的匹配理由可拆解为「户外家具」「便携」等明确特征

  - 跨异构系统的实体对齐任务（如不同站点的商品ID对齐、多源知识图谱实体融合）可直接复用SAE-IDF无训练pipeline，无需标注配对数据，冷启动阶段即可拿到优于dense
  embedding的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有神经符号系统的符号体系高度依赖人工构建，普遍局限于特定领域，难以扩展；跨异构符号系统的匹配（如不同知识图谱实体对齐、跨语言代码检索、多语言本体匹配）是构建通用神经符号系统的核心基础。但直接用LLM的dense隐状态做匹配存在固有缺陷：隐空间各向异性，通用无关特征占比过高，易匹配到表面相似但语义无关的结果，且匹配过程完全不可解释。

### 方法关键点
- 提出无训练的SAE-IDF pipeline：将符号连同其原生上下文输入LLM，取指定层对应符号token的残差流输出，输入预训练的SAE得到稀疏编码
- 稀疏编码稀有度加权：统计每个SAE特征在候选集合中的出现频率，用类似IDF的公式对高频通用特征降权、稀有语义特征提权
- 匹配用加权稀疏向量的余弦相似度排序，结果可拆解为每个可解释特征的贡献占比，匹配逻辑完全白盒

### 关键实验
在6类符号系统的12个任务上测试，对比同LLM的dense隐状态、去除第一主成分的dense隐状态、字符串TF-IDF、专用检索模型等baseline：Gemma-2-9B架构下SAE-IDF在所有任务上超越dense baseline，最高提升0.45 MRR（Lean4转Metamath任务）；Llama-3.1-8B架构下在13/14个任务上超越dense baseline；无需训练的SAE-IDF在10/15个任务上优于专门训练的多语言检索模型BGE-M3。

### 核心结论
LLM预训练得到的SAE稀疏特征天然是可解释的共享语义坐标系，结合稀有度加权后可在无标注配对数据的情况下实现跨异构系统的精准符号匹配。
