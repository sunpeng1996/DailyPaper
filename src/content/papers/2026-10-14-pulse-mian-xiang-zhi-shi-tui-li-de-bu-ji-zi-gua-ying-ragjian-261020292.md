---
title: 'Taking the PULSE of Medical Reasoning: Step-Level Retrieval Timing for Knowledge-Grounded
  Inference'
title_zh: PULSE：面向知识推理的步级自适应RAG检索触发方法
authors:
- Danyang Zhao
- Sendong Zhao
- Yanrui Du
- Haochun Wang
- Ming Ma
- Wenhao Li
- Jingbo Wang
- Jiatong Liu
- Bing Qin
affiliations:
- Harbin Institute of Technology
arxiv_id: '2610.20292'
url: https://arxiv.org/abs/2610.20292
pdf_url: https://arxiv.org/pdf/2610.20292
published: '2026-10-14'
collected: '2026-10-15'
category: RAG
direction: RAG自适应检索 · 隐层特征探测
tags:
- RAG
- Retrieval Timing
- Factuality Detection
- Hidden State Probing
- Multi-step Reasoning
one_liner: 利用LLM隐层跨层波动特征检测步级事实错误，实现RAG检索量降72%且精度持平全量检索
practical_value: '- 多步推理Agent/电商客服RAG系统可直接复用步级粒度的检索触发思路，替代固定query/每步全检索策略，在不掉精度的前提下将检索调用成本降低60%以上，同时减少无关检索结果带来的幻觉

  - 事实性检测场景可直接复用中间层隐层特征提取方案：仅用中间层的角度+幅度变化特征训练轻量MLP探针，不需要大量标注数据，工程实现成本极低，可无缝集成进现有LLM推理链路

  - 跨业务域的RAG系统可复用其域泛化结论：中间层隐层波动是事实错误的通用特征，不需要针对每个业务域（比如不同品类的商品咨询）重新训练探针，大幅降低落地成本

  - 注意适用限制：仅支持可访问中间隐层的开源LLM，闭源API无法直接使用；对于非结构化推理输出，可结合语义分块方法替代强制步骤分割，拓展适用场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多步推理场景下现有RAG方案存在明显缺陷：粗粒度query级检索无法覆盖推理中间步骤的事实错误，全量步级检索则带来大量无效调用、引入噪声还显著提升 latency。传统基于输出 perplexity、熵、最大概率等表面信号的检索触发策略，无法准确区分语言不确定性和真实知识缺失，跨域泛化性极差，无法平衡精度和检索成本。
### 方法关键点
- 后验轨迹分析发现：存在事实错误的推理步骤，隐层状态跨层波动幅度显著高于正确步骤，且该特征与推理复杂度无关，是稳定的内在事实性信号
- 抽取Transformer中间层（避免浅层语法噪声、深层输出分布噪声）的相邻层角度变化、幅度变化两个互补几何特征，拼接后训练2层轻量MLP探针，参数量仅几十k，推理 overhead 可忽略
- 探针判定步骤出错时触发检索，支持两种知识注入策略：检索结果前置到query前、或插入到出错步骤前再生错误步骤，适配不同推理场景
### 关键实验
在4个医疗QA基准上测试，和全量每步检索（IRCoT）相比，PULSE触发的检索精度持平甚至部分场景超出，检索调用量减少72%；零样本迁移到未见过的法律推理数据集，精度比全量检索高2.27%，检索量减少47%；比基于输出信号、拼接隐层的现有 baseline 检测AUROC高5~8个百分点，OOD场景优势更明显。
### 最值得记住的结论
对于需要RAG的多步推理场景，砍掉70%的无效检索不会降低精度，反而可能因为减少噪声引入提升效果。
