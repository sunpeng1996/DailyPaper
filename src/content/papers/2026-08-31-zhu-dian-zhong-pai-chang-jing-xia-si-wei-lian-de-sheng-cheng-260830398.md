---
title: 'Beyond Polarization: The Generative Constraint of Chain-of-Thought in Pointwise
  Reranking'
title_zh: 逐点重排场景下思维链的生成约束：极化现象之外的性能瓶颈
authors:
- Xiaoyang Chen
- Jie Liu
- Haijin Liang
- Haibo Shi
- Jin Ma
- Ben He
- Yingfei Sun
- Dezhi Ye
affiliations:
- 中国科学院大学
- 中国科学院软件研究所
- 腾讯
arxiv_id: '2608.30398'
url: https://arxiv.org/abs/2608.30398
pdf_url: https://arxiv.org/pdf/2608.30398
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: LLM 重排 · 思维链性能瓶颈分析
tags:
- CoT
- Pointwise Reranking
- LLM4Rec
- NDCG
- GRPO
one_liner: 实证证实逐点重排中思维链落后于直接打分的核心是离散文本的排序信号分辨率瓶颈
practical_value: '- 电商搜索/广告逐点重排场景优先选直接打分方案，避免盲目引入CoT损失效果；仅小模型零样本冷启动阶段可尝试CoT，其性能可能优于直接打分

  - 若需保留CoT的可解释性，可采用两阶段架构：先由LLM生成CoT，再输入独立打分模型输出得分，可部分缓解端到端CoT的性能损失

  - 重排训练时新增0-4级细粒度相关性标签，可同时提升直接打分和CoT方案的性能上限，缩小两者的相对差距'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
逐点重排是搜索、推荐、广告系统的核心环节，近期将Chain-of-Thought（CoT）引入大语言模型（LLM）重排的方案普遍出现性能落后于直接打分的问题，过往研究将其归因于分类精度低、分数极化、概率校准失效，但针对性优化能否完全消除性能差距尚不明确，需定位核心瓶颈以指导工业落地。
### 方法关键点
- 覆盖Qwen2.5/Qwen3全系列0.6B-32B参数规模，同时采用Llama-3.1-8B做跨模型家族验证，排除模型偏置
- 第一阶段验证差距稳定性：对比零样本、SFT（含DeepSeek-R1、Gemini-3-Pro蒸馏的CoT监督信号）、不同训练数据量下CoT与直接打分的性能差
- 第二阶段压力测试：分别用GRPO强化学习对齐分类边界、0-4级细粒度标签监督缓解分数极化、CoT生成与打分两阶段解耦三个方案，针对性修复过往提出的问题
- 设计Label-CoT-Label探针实验，隔离离散文本对排序信号的衰减效应
### 关键结果
在TREC DL19、DL20、BRIGHT三个基准数据集上测试，对比baseline为直接打分（noCoT）：1）0.6B到32B全参数规模下，CoT方案NDCG@10始终落后直接打分1~12个点，差距不受模型、数据规模、CoT监督质量影响；2）三类压力测试可提升CoT绝对性能，但仍与直接打分存在0.3~11.3的NDCG@10差距；3）探针实验显示排序信号经过CoT离散文本后，DL19数据集NDCG@10从72.7下降到68.2，验证离散文本的瓶颈效应。

**最值得记住的结论**：逐点重排范式下，连续的相关性语义经过离散文本路由时会损失排序信号分辨率，这是现有标准方法难以克服的稳定瓶颈。
