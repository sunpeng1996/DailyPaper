---
title: 'From Rollouts to Recipes: Self-Contained Post-Training for LLMs'
title_zh: 基于自生成Rollout的自适应路由LLM后训练框架
authors:
- Yifei Li
- Lingling Zhang
- Muye Huang
- Zihan Ma
- Jiashuai Liu
- Jun Liu
affiliations:
- 西安交通大学计算机科学与技术学院
- 国家视觉信息与应用工程研究中心
- 陕西省大数据知识工程重点实验室
- 中关村学院
arxiv_id: '2609.01422'
url: https://arxiv.org/abs/2609.01422
pdf_url: https://arxiv.org/pdf/2609.01422
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: LLM后训练 · 自适应策略路由
tags:
- Post-training
- GRPO
- Self-distillation
- Behavior Routing
- Reasoning LLM
one_liner: 利用模型自身Rollout信号为每个样本自适应分配训练策略，无额外标注提升推理性能
practical_value: '- 做电商导购Agent、营销文案生成LLM的RLHF/微调时，可复用样本级路由逻辑，无需全局统一用GRPO/SFT，根据样本当前学习状态分配训练目标，减少无效梯度，提升训练效率和最终效果

  - 可直接复用轻量行为信号计算方案：用rollout正确率+token熵归一化得到的置信度做路由，不需要额外标注或外部模型，适配所有可自动化校验结果的业务场景（如文案通过率、query改写相关性、商品推荐理由合理性校验）

  - 训练阶段动态调整策略的思路可直接复用：早期多分配自蒸馏目标打基础，中期用GRPO优化不确定性样本，后期加大正则占比防止能力漂移，可有效缓解专项训练后的通用能力下降问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM后训练（尤其是数学、代码等可验证推理任务的RL类训练）普遍对全量样本采用统一的全局训练策略，忽略了模型自身生成的rollout已经暴露的样本级学习状态差异，要么浪费算力在已经完全掌握的样本上，要么优化目标与样本当前状态不匹配，导致训练效率低、最终效果差，甚至出现通用能力漂移。
### 方法关键点
- 每个训练迭代为当前batch的每个样本生成G个on-policy rollout，通过验证器得到每个rollout的正确性，计算样本级正确率ax；再通过token级预测熵归一化得到样本级置信度cx，二者共同构成样本的行为状态bx
- 设计可解释的路由打分规则，根据bx将样本路由到4个分支：不确定可解样本走GRPO做奖励驱动优化，失败但可恢复样本走OPSD on-policy自蒸馏做稠密指导，稳定掌握样本走正则约束防止漂移，低信号/高置信失败样本跳过本次更新
- 仅聚合活跃分支的损失更新模型，无需额外标注、外部教师或额外采样开销
### 关键结果
在DAPO-Math-17K数据集训练，跨Qwen3/Qwen3.5共6个不同规模底座测试，对比统一GRPO、统一OPSD、固定比例混合、简单阈值路由等基线：Qwen3.5-4B上6个评估基准平均得分达86.6，比统一GRPO高6.8，比统一OPSD高3.6；训练成本仅为全量GRPO的54%，同时OOD泛化能力下降幅度是所有后训练方法中最小的。
**最值得记住的一句话**：Rollout行为信号不仅可以用来筛选样本，更应该用来决定每个样本的优化方式。
