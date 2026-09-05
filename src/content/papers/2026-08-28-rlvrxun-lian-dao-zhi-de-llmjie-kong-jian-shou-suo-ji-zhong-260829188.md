---
title: 'Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space'
title_zh: RLVR训练导致的LLM解空间收缩集中于推理路径入口阶段
authors:
- Qiancheng Zhou
- Ruizhe Li
affiliations:
- School of Future Technology, Shanghai University
- School of Computer Science, University of Birmingham
arxiv_id: '2608.29188'
url: https://arxiv.org/abs/2608.29188
pdf_url: https://arxiv.org/pdf/2608.29188
published: '2026-08-28'
collected: '2026-09-05'
category: Training
direction: 大模型推理训练 · RLVR多样性优化
tags:
- RLVR
- LLM Reasoning
- PPO
- GRPO
- Solution Diversity
- Training Optimization
one_liner: 定位RLVR导致的LLM推理多样性损失位置，提出入口导向干预方案，无精度损失提升解覆盖率
practical_value: '- 做电商/广告Agent的RL优化（如推荐话术生成、query改写）时，不要仅关注单次准确率，需额外监测初始决策分支（如首句话术、首个改写方向）的覆盖率，提前识别多样性坍塌

  - 遇到RL优化后多样性下降问题时，可优先做入口阶段干预：将训练早期checkpoint的Transformer高层（如最后8层）参数与最终模型插值，或按可行入口分支分配推理采样预算，无需损失准确率即可提升多样性

  - 多步对齐优先采用SFT→DPO→RLVR的分步训练pipeline，比直接RLVR保留至少2倍的初始决策多样性，更适合需要多路径输出的场景（如多样推荐理由、多风格营销文案生成）

  - 若业务对输出多样性要求高，可在SFT阶段给同一输入喂多套不同入口的示范数据，从根源避免后续RL训练的多样性坍塌，效果远优于后期调温度、改prompt'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR是当前LLM推理优化的主流范式，可大幅提升单样本准确率pass@1，但会导致解空间严重收缩，大幅削弱测试时多采样、树搜索等方法的增益。此前研究未明确多样性损失的具体发生阶段，混淆了「无法进入有效解分支」和「进入后无法完成下游推理」两种错误模式，导致优化方向不明确。

### 方法关键点
- 基于可穷举所有有效解的Countdown算术任务，将解空间按首个操作数+运算符划分为独立入口族，解耦「入口访问」和「下游执行」两个阶段
- 覆盖PPO（训练Qwen2.5-3B）、GRPO（训练Qwen2.5-3B-Instruct）两种主流RLVR范式，对比训练各阶段的解覆盖率、分阶段token似然偏移
- 测试prompt调优、温度调整、高层参数插值、checkpoint混合等多种干预方案的效果
- 扩展到6个通用数学基准、7B/14B参数规模验证现象的通用性

### 关键结果
- RLVR训练后，PPO设置下pass@1提升50倍，解覆盖率下降67%；GRPO设置下pass@1提升3倍，解覆盖率下降43%
- 入口阶段的token似然偏移是下游执行阶段的11~16倍，给低访问入口族补充前缀可让完成率提升1个数量级（PPO下0.018→0.212），证明下游执行能力未损失，仅不再进入其他入口分支
- 用训练早期checkpoint的高层（20~28层）参数插值，可在无pass@1损失的前提下提升37%的解覆盖率；SFT→DPO→RLVR分步训练可保留2倍以上的解覆盖率

### 最值得记住的结论
RLVR导致的推理多样性损失是「进门难」不是「走路难」，优化要优先瞄准初始决策阶段，而非下游执行过程
