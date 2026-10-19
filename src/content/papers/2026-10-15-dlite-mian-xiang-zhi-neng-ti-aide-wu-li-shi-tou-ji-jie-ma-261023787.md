---
title: 'DLite: History-free Speculative Decoding for Agentic AI'
title_zh: DLite：面向智能体AI的无历史投机解码框架
authors:
- Jiaming Xu
- Hanzhen Wang
- Tianlang Zhao
- Jiewen Xiao
- Chengze Yuan
- Jiayi Pan
- Yongkang Zhou
- Jiancai Ye
- Yu Wang
- Guohao Dai
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Tsinghua University
- Infinigence-AI
arxiv_id: '2610.23787'
url: https://arxiv.org/abs/2610.23787
pdf_url: https://arxiv.org/pdf/2610.23787
published: '2026-10-15'
collected: '2026-10-19'
category: LLM
direction: LLM推理优化 · 投机解码
tags:
- Speculative Decoding
- LLM Inference
- Agentic AI
- KV Cache
- Long Context
one_liner: 无需维护draft模型KV缓存的无历史投机解码框架，智能体场景性能超SOTA达70%
practical_value: '- 电商导购/客服类多轮Agent服务可直接落地DLite方案，完全省去draft模型KV缓存维护开销，可降低10%~20%的多轮推理延迟，长上下文场景下速度提升更明显

  - 生成式推荐场景可复用跨模块特征复用思路：生成推荐文案、商品Semantic ID时直接复用召回/排序阶段已经计算好的用户/商品隐状态，避免生成侧重复计算长上下文特征，降低推理成本

  - 异构小模型蒸馏可复用两阶段训练策略：先用同构教师模型做中间蒸馏解决结构不匹配问题，再直接对齐目标大模型，适合训练小尺寸的推荐生成类draft模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有投机解码在智能体长上下文、多轮交互场景下存在两大痛点：一是draft模型接受长度较通用场景下降80%，仅能达到1~2个token；二是draft模型KV缓存更新、维护操作占端到端推理延迟的10%~20%。根源在于draft模型需要独立编码维护不断增长的历史上下文，而目标模型已经完成了相同上下文的计算，存在严重的冗余。
### 方法关键点
- 架构采用无历史并行骨干，直接复用目标模型的多层上下文隐状态，搭配可学习深度embedding区分不同层隐状态来源，仅针对当前解码位置做局部预测，完全无需维护draft模型的历史KV缓存
- 新增轻量级低秩RNN风格序列头，仅恢复投机块内部的因果依赖，直接在隐空间计算避免中间全词表投影开销，进一步降低推理延迟
- 采用两阶段训练策略：第一阶段用同构有历史的教师模型做KL蒸馏，解决异构结构不匹配导致的训练不稳定问题；第二阶段直接对齐目标模型，用CE+TV损失优化分布对齐
### 关键结果
在Qwen3-4B、Qwen3-8B上验证，对比EAGLE3、DSpark等SOTA方案，覆盖通用、长上下文、智能体三类 workload：通用场景接受长度达2~6，略超DSpark；长上下文场景端到端加速比DSpark高20%~30%；智能体场景接受长度较DSpark最高提升70%，端到端加速最高达2.74x，高并发下吞吐量较DSpark高5%~10%。

**最值得记住的一句话**：小模型长上下文建模能力天然有限，避免冗余重复计算、直接复用大模型已生成的高质量隐特征，是兼顾推理效率与效果的核心思路。
