---
title: 'AdaSpark: Adaptive DSpark with Online Learning for Tree Verification and N-gram
  Fill'
title_zh: AdaSpark：面向树验证与N-gram补全的在线学习自适应DSpark调度器
authors:
- Liquan Liu
- Yifan Zhang
- Bowei Xu
affiliations:
- Zeraix
arxiv_id: '2610.05774'
url: https://arxiv.org/abs/2610.05774
pdf_url: https://arxiv.org/pdf/2610.05774
published: '2026-10-05'
collected: '2026-10-06'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- speculative_decoding
- online_learning
- DSpark
- tree_verification
- inference_acceleration
one_liner: 提出无需预校准的在线自适应DSpark调度器，比llama.cpp原生DSpark提速1.5-3.1倍
practical_value: '- 推理侧可复用在线latency建模思路：用低分位数损失拟合不同上下文下的验证耗时，无需预校准即可适配稠密/MoE模型、不同硬件的特性，可直接用于Agent、电商大模型服务的低延迟优化

  - 多来源候选排序方法可迁移：将生成候选、检索候选统一按期望收益做best-first排序，无需固定分配配额，可用于推荐多路召回融合、RAG检索结果与生成结果的动态排序场景

  - 动态资源调度思路可复用：基于长期吞吐率而非单轮收益比选择最优并行度，适合推荐系统多队列调度、Agent多工具调用的资源分配，平衡吞吐与延迟'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有DSpark投机解码调度器依赖离线预校准的验证耗时、草稿模型置信度选择树宽度，无法适配不同模型（稠密/MoE）、硬件、上下文长度的差异，固定宽度或简单校正策略远达不到最优吞吐，额外的预校准步骤也增加部署成本。

### 方法关键点
- 在线验证成本模型：自动学习可选宽度集合，用低分位数损失拟合不同宽度的耗时与上下文长度的关系，规避GPU干扰的影响，无需预校准；
- 在线接受概率模型：以草稿模型置信度、候选占比为特征，在线拟合每个候选的验证通过率，同时支持n-gram补全候选打分，将两类候选统一按路径期望接受概率做best-first排序，自动分配树节点配额；
- 自适应宽度选择：基于上下文的长期解码速率而非单轮吞吐比选择最优树宽度，加入迟滞避免频繁切换，适配非单调的耗时曲线。

### 关键结果
在3个稠密LLM、1个MoE LLM、6个公开对话数据集上测试：比llama.cpp默认DSpark提速1.5~3.1倍；对比相同引擎下的3-token链默认配置，仅调度器优化就带来1.17~1.52倍提速；无需预扫宽度，性能始终不低于最优固定宽度的99.7%。

最值得记住的：在线学习的调度策略可在无预校准的前提下逼近甚至超过离线调优的最优固定配置，大幅降低LLM推理服务的部署适配成本
