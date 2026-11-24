---
title: 'From Rewarding What Models Say to How They Think: Attention Process Reward
  Model for LLM Reinforcement Learning'
title_zh: 面向LLM强化学习的注意力过程奖励模型APRM
authors:
- Kairong Han
- Nuanqiao Shan
- Ziyu Zhao
- Xinpeng Dong
- Zijing Hu
- Dian Jin
- Leyan Deng
- Junjian Ye
- Lujia Pan
- Fei Wu
affiliations:
- Zhejiang University
- Noah's Ark Lab, Huawei Technologies
arxiv_id: '2611.30627'
url: https://arxiv.org/abs/2611.30627
pdf_url: https://arxiv.org/pdf/2611.30627
published: '2026-11-22'
collected: '2026-11-24'
category: Training
direction: LLM训练 · 强化学习奖励模型
tags:
- Reinforcement Learning
- Reward Model
- Attention
- Process Supervision
- RLHF
one_liner: 基于LLM内部隐状态与注意力信号构造轻量奖励模型，缓解文本奖励混叠，提升RL推理性能
practical_value: '- 做LLM-based Agent/生成式推荐的RL微调时，可复用APRM思路，除外部输出奖励外，抽取LLM最后几层注意力、隐状态构造内部过程奖励，补充监督信号，避免文本奖励混叠问题

  - 轻量奖励模型架构可直接复用：用注意力融合概念池压缩长序列特征，再接Edge-biased GAT建模推理关联，仅46M参数即可实现有效过程奖励，不会带来过大开销

  - 训练trick可迁移：用正负样本排序损失+注意力扰动反事实损失联合训练奖励模型，仅靠最终输出对错标签即可冷启动，适合业务场景标注成本高的情况

  - RL训练的奖励融合方式可复用：将内部奖励做组内中心化后，用可调系数β与原始任务奖励加权融合，定期更新奖励模型应对分布漂移，平衡过程信号与业务目标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM强化学习的奖励模型仅关注最终输出或文本化思考轨迹，存在文本奖励混叠问题：不同内部推理过程可能生成完全一致的外部文本，导致奖励无法区分真实推理质量，尤其在长链CoT、复杂推理场景下，稀疏外部奖励难以引导模型学到正确推理逻辑。
### 方法关键点
- 提出仅46M参数的轻量奖励模型APRM，直接基于LLM生成过程中最后K层平均注意力图、最后一层隐状态计算内部过程奖励
- 架构上先通过注意力融合概念池将长序列token特征压缩为少量隐式推理概念，构造稀疏概念关联图，再用Edge-biased GAT建模概念间依赖关系输出质量得分
- 冷启动阶段仅需最终输出对错标签，用配对排序损失（正确轨迹得分高于错误轨迹）+ 反事实损失（原始注意力得分高于扰动后注意力得分）联合优化，无需额外过程标注
- RL训练阶段将APRM得分组内中心化后，与原始任务奖励加权融合作为最终优势信号，定期更新APRM应对策略漂移
### 关键实验
在AIME2025、AMC、MATH500、OlympiadBench四个数学推理数据集上测试，基于Qwen3-1.7B/4B底座，对接GRPO、GPG、GSPO等主流RL算法，平均pass@8提升2.88%，推理轨迹长度最高缩短17.08%；跨任务迁移到代码生成场景，平均pass@8提升2.96%。
### 核心结论
强化学习不仅可以奖励LLM输出了什么，更可以奖励其内部是如何思考的，内部注意力、隐状态信号可以提供文本之外的高价值监督信息
