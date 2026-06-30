---
title: Regime-Aware Peer Specialization for Robust RAG under Heterogeneous Knowledge
  Conflicts
title_zh: 异质知识冲突下鲁棒RAG的制度感知对等专精训练框架
authors:
- Bo Wang
- Heyan Huang
- Yaolin Li
- Yanghao Zhou
- Jiahao Teng
- Ziyi Yang
- Ge Shi
- Chong Feng
affiliations:
- Beijing Institute of Technology
arxiv_id: '2606.30518'
url: https://arxiv.org/abs/2606.30518
pdf_url: https://arxiv.org/pdf/2606.30518
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: 鲁棒RAG · 知识冲突处理
tags:
- RAG
- Knowledge Conflict
- On-policy Distillation
- Token Selection
- Peer Specialization
one_liner: 提出分制度对等专精训练框架，解决RAG异质知识冲突，推理无额外开销
practical_value: '- 电商/搜索RAG场景中，不同来源的商品/知识内容天然存在可靠性异质性，可按可信度将冲突分类做分制度训练，避免单模型的梯度干扰

  - 可复用三信号（教师间冲突、师生gap、学生熵）双层token选择机制，聚焦高价值矫正信号，提升训练效率

  - 训练阶段用同规模对等教师做专精，推理仅需单个学生模型，不增加推理时延，符合工业部署要求

  - 对抗性冲突场景（错误商品信息、篡改检索结果）收益最大，适合需要可靠性校验的RAG系统'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG引入外部检索知识后，常出现外部上下文与模型参数知识冲突的问题，而冲突可靠性是连续谱，覆盖完全可靠、部分可靠到对抗性不可靠三类场景。现有方法采用不分制度的统一监督，会引入跨制度的梯度冲突，导致模型要么过度信任错误上下文，要么误拒正确上下文，性能缺陷明显，该问题在工业级RAG中普遍存在，亟待解决。

### 方法关键点
- 样本级路由：将冲突按可靠性分为Grounding（整合可靠知识）、Arbitration（选择性信任混合知识）、Resistance（拒绝对抗知识）三类，每个制度从共享base微调一个同规模peer specialist，训练时样本硬路由到对应教师做on-policy reverse-KL蒸馏，base做隐式KL锚点，消除跨制度干扰
- Token级选择：用三个互补信号（教师间JS散度衡量冲突、师生reverse-KL衡量gap、归一化学生熵衡量不确定度）做双层选择：硬掩码过滤无信息和不稳定token，软权重上调学生自信但错配token的权重
- 难度退火调度：训练初期覆盖全token，逐步将监督聚焦到高难度高冲突token，避免过早聚焦难token导致训练不稳定，推理仅保留单个学生模型，无需制度标签，无额外推理开销

### 关键结果
在5个知识冲突场景、2个OOD基准测试，对比多类SOTA基线，Qwen2.5-7B上相比SOTA Knowledgeable-R1，三个制度的EM分别提升7.4、6.6、11.2个百分点；OOD的ConflictQA上EM达到42.7%，优于所有基线，同时不损害原模型的参数知识保留，在3B/7B/14B不同规模均有一致提升，对抗性冲突场景收益最大。

最值得记住的一句话：鲁棒冲突解决本质上是一个专精问题，而非缩放问题，不要强迫单一策略调和不相容的优化目标
