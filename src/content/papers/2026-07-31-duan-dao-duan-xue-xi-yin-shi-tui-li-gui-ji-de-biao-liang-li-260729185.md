---
title: Learning Latent Reasoning Traces for Scalar Reward Models End-to-End
title_zh: 端到端学习隐式推理轨迹的标量奖励模型
authors:
- Sanwoo Lee
- Clive Bai
- Hsiu-Yuan Huang
- Kun Liang
- Weijie Liu
- Yunfang Wu
affiliations:
- 北京大学
- 腾讯
arxiv_id: '2607.29185'
url: https://arxiv.org/abs/2607.29185
pdf_url: https://arxiv.org/pdf/2607.29185
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: LLM对齐 · 奖励模型训练
tags:
- Reward Model
- RLHF
- Latent Variable
- Chain-of-Thought
- On-Policy Training
one_liner: 将推理作为离散隐变量端到端联合优化生成器与标量奖励模型，兼顾鲁棒性与评分灵活性
practical_value: '- 电商/推荐排序场景可复用该架构思路：将排序特征的选择/推理过程作为隐变量，端到端对齐最终排序目标，避免人工设计特征规则带来的偏差，提升冷启动/OOD场景的排序效果

  - Agent的自动评价模块可直接适配LatentRM框架：用生成的结构化推理过程辅助标量质量打分，无需依赖外部大模型蒸馏，同时提升多轮对话、复杂任务等OOD场景的评价鲁棒性

  - RLHF对齐流程中可替换原有奖励模型：采用该on-policy联合训练方法，无需额外的推理蒸馏步骤，即可同时提升RM的泛化性和评分稳定性，缓解奖励过优化、回复冗长等问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
传统标量奖励模型（RM）效率高、具备概率可解释性，但易过拟合训练数据表面特征，分布外（OOD）泛化性差；生成式RM依赖深度推理，鲁棒性更强，但输出的自然语言评分缺乏数值灵活性，无法直接适配RLHF等下游流程。现有混合方案采用多任务并行优化生成器与标量RM，推理轨迹的优化目标与下游标量预测目标不匹配，无法充分发挥两者优势。

**方法关键点**
- 将链式思考（CoT）推理轨迹作为离散隐变量，构建生成器-标量RM联合架构，推理z作为输入x与偏好标签y的中间桥接
- 基于证据下界（ELBO）推导端到端优化目标，生成器采用REINFORCE算法更新，以标量RM的偏好似然作为奖励信号，实现全on-policy训练，消除训推不一致问题
- 生成器输出结构化推理结果（含任务专属评分规则、逐响应评价、粗打分），标量RM抽取粗打分前的隐藏态映射为最终标量奖励，采用Plackett-Luce模型建模排序似然

**关键结果数字**
以Qwen3-4B-Instruct为基座，在覆盖通用、数学、代码、安全、对抗5个域的4.3万训练样本上训练，对比3类基线：
- 分布内测试集平均Kendall's τ达0.759，较MultitaskRM高0.003，较传统ScalarRM高0.041
- OOD测试集RM-Bench平均准确率82.8%，PPE Correctness平均72.1%，均为所有方法最优，优于27B-70B参数的外部基线RM
- 用于RLHF训练后，生成响应平均长度最短（1289 tokens），长度控制胜率对ScalarRM达58.5%，对MultitaskRM达52.0%

最值得记住的结论：将中间推理过程作为隐变量直接对齐下游任务目标，比单独优化推理自身的正确性更能提升整体任务性能
