---
title: Enhancing Rubric-based RL via Self-Distillation
title_zh: 通过自蒸馏增强基于评分规则的强化学习
authors:
- Mingxuan Xia
- Yuhang Yang
- Chao Ye
- Shuai Zhu
- Shenzhi Yang
- Guangcheng Zhu
- Yuhang Zhang
- Cheng Peng
- Haobo Wang
- Siqing Wang
affiliations:
- Zhejiang University
- ByteDance
arxiv_id: '2607.18082'
url: https://arxiv.org/abs/2607.18082
pdf_url: https://arxiv.org/pdf/2607.18082
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: LLM训练 · 评分规则RL优化
tags:
- RLHF
- GRPO
- Self-Distillation
- Rubric-based RL
- LLM Alignment
one_liner: 提出CriPO自蒸馏RL框架，同时解决评分规则RL两类失效问题，收敛速度提升2倍
practical_value: '- 做多维度评分的LLM对齐（如商品文案生成、Agent回复优化）时，可复用CriPO的双失效模式检测逻辑，避免未覆盖评分项无优化信号、局部达标但整体负分的有用特征被抑制

  - 自蒸馏辅助GRPO的混合架构可直接迁移：保留GRPO作为稳定训练主骨架，用基于特权信息的自蒸馏做局部token级修正，既避免训练推理偏差，又比纯OPSD训练更稳定

  - 做多目标奖励聚合优化（如推荐多目标排序、多维度转化目标建模）时，可借鉴优势翻转思路，对局部满足某目标的负优势样本的相关特征做局部增益，避免全局负分覆盖局部有效信号'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
基于评分规则（Rubric）的RL是对齐LLM开放任务能力的核心范式，但存在两类普遍且长期被忽视的失效问题：一是**未探索准则**：当前采样rollout均未满足的评分项无任何优化信号；二是**抑制准则**：部分rollout满足某评分项，但全局多维度聚合后优势为负，导致有效达标行为被惩罚。现有探索增强方法依赖训练时的外部评分规则引导，会引入训练-推理分布偏差，且完全未覆盖抑制准则问题，同时纯on-policy自蒸馏（OPSD）训练不稳定易出现性能退化。

### 方法关键点
- 保留GRPO作为稳定的奖励对齐主骨架，引入OPSD作为辅助模块做局部修正，全程on-policy完全避免训练-推理分布偏差
- 针对未探索准则：构造准则注入自教师，仅在组内最优rollout上计算前向KL，筛选累计贡献占95%KL的token做局部蒸馏，注入缺失行为的同时过滤噪声
- 针对抑制准则：构造反事实自教师定位负优势rollout中与达标准则相关的token，局部翻转其优势为正，保留有用特征不被全局负分覆盖

### 关键实验
在医疗、科学QA数据集上对比GRPO、HeRL等基线，Qwen3-1.7B平均得分相对GRPO提升3.2，Qwen3-4B提升1.4；收敛效率提升2倍，仅需GRPO一半的训练步数即可达到其收敛性能，额外单步计算开销不影响整体落地性价比。

> 最值得记住：多维度奖励优化中全局聚合损失会掩盖局部有效信号，基于自蒸馏的token级局部修正可无偏差地同时解决探索不足和信号抑制问题
