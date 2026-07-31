---
title: 'Beacon: Knowing When and How to Perform Agentic Visual Reasoning'
title_zh: Beacon：支持自适应工具调用的智能体视觉推理框架
authors:
- Qixun Wang
- Yang Shi
- Letian Cheng
- Zhuoran Zhang
- Yan He
- Yuqi Tang
- Qi Zhang
- Xinlei Yu
- Ruizhe Chen
- Tianrun Xu
affiliations:
- Peking University
- Kling Team
- HKUST(GZ)
- CUHK
- THU
arxiv_id: '2607.28595'
url: https://arxiv.org/abs/2607.28595
pdf_url: https://arxiv.org/pdf/2607.28595
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: 多模态Agent · 自适应工具调用优化
tags:
- Agentic Reasoning
- MLLM
- Reinforcement Learning
- Tool Call
- Multimodal
one_liner: 基于必要性感知奖励和提示引导RL，实现多模态视觉推理自适应工具调用，兼顾效率与效果
practical_value: '- 自适应工具调用的Necessity-Aware Adaptive Reward可直接复用在多模态商品理解/审核Agent上：易解问题直接输出结果降推理延迟，难问题自动调用OCR/目标检测工具提准确率，平衡业务效率与效果

  - Hint-Guided Capability Expansion思路可迁移到推荐系统复杂query理解的RL训练：对模型无法解决的难样本，注入专家生成的无答案提示辅助生成有效正轨迹，解决难样本无有效梯度的问题

  - 论文提出的Tool-Gain/Tool-Harm/Mode Adaptiveness指标可直接用于业务Agent的工具调用能力评估，替代单一准确率，量化工具调用的真实价值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态智能体视觉推理普遍存在工具调用适配性差的问题：要么盲目调用工具产生冗余计算开销，还会在简单问题上引入额外错误；要么不调用工具无法解决复杂推理问题，工具带来的增益基本被简单场景的损失抵消，净收益极低。

### 方法关键点
- 提出两类核心评估维度：Mode Adaptiveness（模型是否能根据任务难度选择是否调用工具）、Tool Effect（工具是否能带来真实能力增益），量化工具调用的必要性和实际价值
- 训练采用SFT+RL两阶段范式：SFT阶段用Gemini 3.1 Pro生成高质量代码辅助推理轨迹，完成基础工具使用能力的冷启动
- RL阶段设计Necessity-Aware Adaptive Reward：对纯文本可解的简单问题，正确纯文本回答给满奖励，正确工具调用仅给0.25倍奖励，避免冗余调用；对纯文本无解的难问题，正确工具调用给满奖励，鼓励工具使用
- 新增Hint-Guided Capability Expansion机制：对RL rollout全错的难样本，用专家模型生成不含最终答案的推理提示，辅助模型探索有效工具调用轨迹，回收难样本的梯度信号

### 关键结果
在13个多模态推理基准上对比7个开源SOTA模型，Beacon平均准确率达58.98%，比基线Qwen3-VL-8B高6.07个点，在11个基准上排名第一；工具调用净增益（Tool-Gain - Tool-Harm）达3.14%，远高于其他模型接近0的水平，工具调用的真实价值大幅提升。

> 最值得记住的结论：Agent的工具调用能力进步不能只看工具调用频率，更要关注「什么时候需要调用」和「调用后有没有带来真实能力增益」
