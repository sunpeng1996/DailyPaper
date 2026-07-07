---
title: Weak-to-Strong Generalization via Direct On-Policy Distillation
title_zh: 基于直接同策略蒸馏的弱到强泛化方法
authors:
- Shiyuan Feng
- Huan-ang Gao
- Haohan Chi
- Hanlin Wu
- Zhilong Zhang
- Zheng Jiang
- Bingxiang He
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- SIA-Lab of Tsinghua AIR and ByteDance Seed
- Institute for AI Industry Research, Tsinghua University
- Department of Computer Science and Technology, Tsinghua University
- Peking University
arxiv_id: '2607.05394'
url: https://arxiv.org/abs/2607.05394
pdf_url: https://arxiv.org/pdf/2607.05394
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: LLM弱到强泛化 · 同策略蒸馏
tags:
- On-Policy Distillation
- Weak-to-Strong Generalization
- RLVR
- Knowledge Distillation
- LLM Post-Training
one_liner: 利用小模型RL前后的策略偏移作为隐式奖励，低成本实现弱模型到强模型的能力迁移
practical_value: '- 垂域LLM（如电商文案生成、客服Agent、商品属性识别）优化时，可先在小参数量模型上跑RLVR获取策略增益，再用Direct-OPD蒸馏到大模型，算力成本可降低90%以上

  - 做跨模型能力迁移时，不要直接蒸馏小模型的最终输出分布，改用模型迭代前后的token级log概率差作为隐式奖励，避免小模型的能力上限拉低大模型原生性能，可直接复用在推荐系统排序模型的蒸馏优化上

  - 训练时采用2k左右的短rollout horizon搭配自适应KL系数，既可以保证策略偏移的泛化性，又能降低长序列带来的训练噪声，适合业务侧快速迭代上线'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前基于可验证奖励的强化学习（RLVR）是提升LLM推理能力的主流后训练方案，但训练成本与模型规模正相关，大模型每轮迭代都要生成大量rollout，算力开销极高；直接将小RL模型蒸馏到大模型会引入小模型的能力缺陷，甚至拉低初始性能更强的大模型效果，亟需低成本的弱到强能力迁移方案。
### 方法关键点
- 提出Direct-OPD范式，提取小模型RL前后的策略偏移（logπ_T - logπ_Tref）作为隐式奖励，而非直接模仿小模型的最终策略，从根源上规避小模型的能力上限限制
- 将序列级策略偏移拆解为逐token的稠密奖励，在大模型自身采样的同策略状态上优化，搭配Rao–Blackwellized的top-k梯度估计降低训练方差
- 设计自适应KL控制器，根据每批次隐式奖励的符号动态调整KL惩罚系数，避免模型漂移到教师分布外的不可靠信号区域
### 关键结果
在AIME 2024/2025数学推理数据集上对比普通同策略蒸馏、直接大模型RL等baseline：
- 仅用8张A100训练4小时，即可将Qwen3-1.7B的AIME2024准确率从48.3%提升至62.4%，效果与直接用32张A100跑一周RL相当
- 1.5B小模型的策略偏移可迁移到4B、7B等更大模型，即使学生初始性能已超过小RL教师，仍能获得稳定增益（如R1-Distill-7B初始准确率56.7%高于教师的51.3%，迁移后提升至63.1%）
- 相同算力预算下，小模型RL+Direct-OPD方案比直接大模型RL准确率高2~5个百分点，总算力成本仅为后者的1/20左右

> 最值得记住的结论：RL的训练成果不应被当做最终模型来模仿，而应被拆解为可跨模型、跨规模复用的改进方向信号。
