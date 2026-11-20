---
title: Sequential Anytime Valid Tests for Efficient Inference-Time Alignment
title_zh: 面向高效推理时对齐的序列随时有效测试方法
authors:
- Vishesh Kumar Singh
- Sayak Ray Chowdhury
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2611.26413'
url: https://arxiv.org/abs/2611.26413
pdf_url: https://arxiv.org/pdf/2611.26413
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理对齐 · 自适应停止
tags:
- InferenceAlignment
- EarlyStopping
- BestOfN
- EProcess
- RewardModel
one_liner: 提出带严格Type-I错误控制的推理对齐自适应停止规则，大幅降低token成本同时保持或提升精度
practical_value: '- 做Agent/生成式推荐的BoN采样对齐时，可直接复用RWSC聚合规则，平衡自洽性和Reward Model得分，避免Reward
  Hacking导致的结果劣化，比纯BoN/纯投票效果更稳定

  - 推理时多候选采样的停止逻辑可参考E-RWSC框架，通过逐答案的e-process统计检验实现自适应停止，不用全局固定N，能降低30%-60%的token成本，同时保证错误率可控

  - Reward Model质量不高的场景也可使用该框架，RWSC的正则效应能抵消RM校准误差的影响，且有效性不受RM质量波动破坏，仅影响停止速度不影响正确性

  - 工程上该框架的CPU计算开销仅为GPU生成耗时的0.0002%，几乎无额外latency，可直接嵌入现有LLM推理pipeline无需改造底层架构'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
推理时对齐（如Best-of-N、自洽性投票）是无需微调即可提升LLM输出质量的常用手段，但固定采样数N的方式存在明显缺陷：对简单prompt浪费算力、对高难度prompt采样不足；现有自适应停止方法均为启发式阈值调优，没有严格的统计错误控制，容易提前停止选出非最优答案，且需要针对不同模型、任务反复调参，落地成本高。

### 方法关键点
- 提出Reward-Weighted Self-Consistency（RWSC）聚合规则：将生成结果按最终答案聚类，用Reward得分的softmax加权计算每类的得分，温度τ可调，τ→∞退化为自洽性投票，τ→0退化为纯BoN，同时兼顾答案出现频率和质量
- 先提出SPRT-RWSC用Wald序列概率比检验做停止，但因待检验的领先答案随采样动态变化，不满足SPRT的固定假设，无严格错误保证
- 提出E-RWSC：为每个首次出现的答案单独维护一个赌博上鞅（e-process），用可预测的Kelly投注规则累积证据，通过Ville不等式保证Type-I错误（将非主导答案判定为有效）严格低于用户指定的α，不受采样次数、领先答案切换的影响
- 主导答案的采样时间复杂度为O(log(1/α)/dKL(θa||1/2))，算力自动匹配prompt难度，简单prompt少量采样即可停止，难prompt自动增加采样量

### 关键实验
在GSM8K、MATH500、MMLU、CruxEval 4个基准，5个不同参数的LLM、4个不同Reward Model上测试：E-RWSC在MATH500上比Vanilla BoN高8.2%绝对精度，同时采样预算降低61.7%；提前停止的认证答案准确率达94.5%，比同类方法MMC高5.6个百分点；每步统计检验的CPU开销仅0.014ms，占GPU推理耗时的0.0002%，几乎无额外延迟。

### 最值得记住的一句话
任何用多候选采样做LLM推理对齐的场景，都可以用E-RWSC替代固定N的BoN，在严格错误控制下实现算力成本的大幅降低。
