---
title: 'Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving'
title_zh: 聚类、路由、升级：感知成本的LLM推理服务级联框架
authors:
- Yasmin Moslem
- Magdalena Kacmajor
- Vasudevan Nedumpozhimana
- Ammar Abbas
- Solmaz Panahi
- David Lynch
- Zhuangzhuang Nie
- Alexandros Agapitos
- Aleksandar Milenovic
- Hongmeng Song
affiliations:
- ADAPT Centre, Trinity College Dublin
- Huawei Research
arxiv_id: '2606.27457'
url: https://arxiv.org/abs/2606.27457
pdf_url: https://arxiv.org/pdf/2606.27457
published: '2026-06-24'
collected: '2026-06-30'
category: LLM
direction: LLM推理优化 · 多模型路由
tags:
- LLM Serving
- Model Routing
- Cascaded Inference
- Cost Efficiency
- Inference Optimization
one_liner: 提出两级级联框架，保留最强模型97%以上精度同时降低LLM推理平均TPOT
practical_value: '- 电商搜索/多Agent对话场景，可复用这套两级架构：将用户query/Agent子任务按语义聚类预路由，简单问题给小模型，难问题提前分给大模型，再用QE兜底升级小模型的错输出，比纯后验级联节省大量不必要的小模型推理消耗

  - λ超参数可直接解释为「使用最贵模型可接受的最大错误率惩罚」，业务上可直接对齐QPS/latency预算，不需要手动写路由规则，调参成本低

  - 模型池迭代时，新模型接入可自动通过Pareto剪枝淘汰无效模型，不需要重新训练整个路由模块，适配推荐/Agent场景频繁迭代模型的需求

  - 多Agent系统拆分的不同复杂度子任务，可直接用这套框架分配模型，在保效果的前提下降低整体推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
生产环境部署LLM时，单模型部署存在精度与成本的固有矛盾：全用大模型会在简单查询上浪费推理资源，全用小模型会在难查询上精度不足；现有路由方法大多需要额外标注，无法显式对齐给定的推理成本预算，也缺乏预路由+后验纠错的组合设计，仍然存在不必要的推理消耗。

### 方法关键点
1. 第一级聚类路由：对训练query用all-MiniLM做embedding后k-means语义聚类，自动选择聚类数；每个聚类下每个模型按`Score(m,c) = Error(m,c) + λ·Costnorm(m)`打分，选分数最低的模型路由；λ为可解释超参数，表示使用最贵模型可接受的最大错误率惩罚，自动在训练集上调参选满足用户给定TPOT预算的最优λ，同时自动Pareto剪枝淘汰占优模型，新模型接入仅需重跑Pareto分析即可更新路由，无需额外标注重训。
2. 第二级QE升级：轻量ModernBERT二分类器仅对小模型输出做质量判断，低质量输出升级到大模型，大模型输出直接绕过，不增加额外消耗；分类器仅用任务正确性标签训练，不需要额外标注。

### 关键结果
在AIME 2024数学推理、TeleQnA电信QA两个数据集测试，模型池覆盖不同规格Qwen、Gemma系列模型：
- AIME：两级框架仅比全用最强Qwen3-30B模型低0.7%精度，TPOT降低18%
- TeleQnA：保留最强Gemma4-26B模型97%的精度，平均TPOT低于全用最强模型

最值得记住的结论：预路由提前把确定难的查询分给大模型，后验QE兜底救小模型的错输出，组合后比纯级联或纯路由都更省成本
