---
title: 'Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits'
title_zh: CANOPY：面向多置信度老虎机的分段平滑树先验利用算法
authors:
- Michael Jerge
- Suman Jana
affiliations:
- Amazon
- Columbia University
arxiv_id: '2609.30017'
url: https://arxiv.org/abs/2609.30017
pdf_url: https://arxiv.org/pdf/2609.30017
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: LLM推理优化 · 多保真树老虎机
tags:
- Multi-Fidelity Bandit
- Tree Prior
- LLM Inference
- Online Optimization
- Prefix Caching
one_liner: 无需预设全局平滑性，通过在线局部平滑检测的多保真树老虎机，大幅优化LLM推理效率
practical_value: '- LLM路由场景可直接复用CANOPY的分段平滑检测逻辑，用低精度模型打分作为cheap probe，高精度模型推理作为expensive
  leaf evaluation，相同成本下千模池top10召回可提升2.9倍，适合电商多模型混合调用的降本提效需求。

  - KV cache管理场景可借鉴不连续性导向的采样思路，对prefix共享度高的区域批量缓存，仅对检测到的平滑性失效区域做精细化eviction，实测可比LRU多缓存78%的块，中位数time-to-first-token降低3.6倍，适配大促流量突增场景。

  - Agent测试时搜索（代码生成、推理路径探索等）可迁移其多保真分层探索框架，用partial trace的廉价验证（语法检查、单步执行结果）作为probe，全路径跑测作为leaf
  evaluation，可比best-of-N多解决1.6倍的复杂任务，提升工具Agent的成功率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统分层老虎机优化依赖预设的全局平滑性假设，但LLM推理场景下的树结构优化（模型路由、prefix缓存、prompt裁剪、测试时搜索等）的目标函数通常仅分段平滑，最优值常位于突变边界附近，预设平滑性要么错过优质区域，要么浪费算力，亟需可在线自适应检测局部平滑性的多保真优化方法。

### 方法关键点
- 提出在线局部Lipschitz聚合偏差证书：通过节点廉价随机路径探针的观测值，经log-sum-exp上界、高斯噪声解卷积、经验伯恩斯坦置信界三步，高概率估计当前子树的聚合偏差，无需预设全局平滑参数。
- 设计不连续性引导的自适应采样策略：仅将昂贵的叶子节点评估资源分配给平滑性检测失效的子树区域，平滑区域直接剪枝以节约算力。
- 构建统一的成本预算优化框架，将模型路由、prefix缓存、测试时搜索等LLM推理场景都抽象为同一多保真树优化问题求解。

### 关键实验
在12个开源基准上覆盖5大类任务，对比结构盲搜索、LRU缓存、best-of-N等基线：千模池路由top10召回是基线的2.9倍；SWE-bench Verified问题解决数是best-of-N的1.6倍；prefix缓存下中位数time-to-first-token降低3.6倍，流量偏移后比LRU多省83%的首包时延；prompt裁剪在相同token数下QA F1提升0.045。

### 核心结论
多保真树优化的收益核心来自「廉价探针可信时用结构剪枝节约算力，不可信时仅把资源砸在突变区域」，仅当探针廉价且不连续性稀疏时收益最大。
