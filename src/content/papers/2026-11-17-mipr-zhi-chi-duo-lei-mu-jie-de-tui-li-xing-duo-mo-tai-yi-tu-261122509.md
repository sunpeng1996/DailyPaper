---
title: 'MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval
  with Multi-Category Solutions'
title_zh: MIPR：支持多类目解的推理型多模态意图到商品检索基准
authors:
- Qiang Li
- Xuan Lu
- Jian Ruan
- Manxi Lin
- Jiacheng Chen
- Wen Shen
- Zhihua Wei
- Xiaoyu Shen
- Dan Ou
- Xiangheng Kong
affiliations:
- Tongji University
- Taobao & Tmall Group of Alibaba
- Eastern Institute of Technology, Ningbo
arxiv_id: '2611.22509'
url: https://arxiv.org/abs/2611.22509
pdf_url: https://arxiv.org/pdf/2611.22509
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 多模态电商检索 · 推理型基准构建
tags:
- Multimodal Retrieval
- E-commerce Retrieval
- Benchmark
- Intent Understanding
- Fine-grained Labeling
one_liner: 发布首个覆盖推理需求、多类目解、细粒度标签的电商多模态意图搜商基准
practical_value: '- 自建电商多模态意图检索评测集可复用论文「query筛选→多路径候选召回→5档细粒度标注→池化补全标注」的完整流程，大幅降低标注成本

  - 针对用户意图对应多类目商品的召回难题，可借鉴「先枚举解决方案类目再分路召回」的候选发现思路，提升多类目解决方案覆盖度

  - 排序优化可复用5档标签体系（L1最优/L2次优/N1违反约束/N2相关非解/N3无关），针对性优化硬负样本挖掘，提升最优商品首屏占比'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
真实电商搜索中用户常以「场景图+需求提问」的形式表达模糊意图，单个意图可对应多个不同类目的商品解决方案，现有多模态检索基准多为目标导向，要求query明确指定目标商品，且仅提供二元标签，无法支撑推理型意图检索的模型评测。

### 方法关键点
- 数据集来自淘宝真实搜索日志，包含3522个图文多模态query、30731个商品的共享语料，累计44.7万条标注
- 采用5档细粒度相关性标签，覆盖最优解、次优解、违反约束的无效解、相关非解决方案、完全无关样本
- 构建流程：先做query筛选与意图结构化提取，再通过「解决方案类目枚举+多路径召回」挖掘候选商品，经多模型投票+人工校验完成标注，最后用多模型召回池化补全未标注query-商品对
- 新增Solution-Category Recall指标，专门评估单query多类目解决方案的覆盖能力

### 关键实验
对比10个SOTA多模态embedding召回模型、4个重排模型：最优embedding召回模型Qwen3-VL-Embedding的nDCG@10仅49.23%，多类目query的类目召回率@10仅55.86%；加重排后nDCG@10提升10.88pp到60.11%，多类目类目召回率@10提升到67%，但仍比候选池oracle低25.93pp的nDCG空间。

当前多模态检索模型大多能找到至少一个最优解，但普遍存在多类目解决方案覆盖不足、次优解排在最优解之前、相关非解容易混入首屏的问题，距离业务可用还有较大差距。
