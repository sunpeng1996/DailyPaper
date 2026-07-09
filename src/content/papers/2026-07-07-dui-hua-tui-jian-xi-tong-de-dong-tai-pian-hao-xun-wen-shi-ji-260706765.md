---
title: 'When and How to Ask: Dynamic Preference Elicitation Strategies for Conversational
  Recommendation'
title_zh: 对话推荐系统的动态偏好询问时机与策略选择方法
authors:
- Feng Xia
- Shuo Zhang
- Xi Wang
affiliations:
- University of Sheffield
- Bloomberg
arxiv_id: '2607.06765'
url: https://arxiv.org/abs/2607.06765
pdf_url: https://arxiv.org/pdf/2607.06765
published: '2026-07-07'
collected: '2026-07-09'
category: RecSys
direction: 对话推荐·动态偏好询问策略
tags:
- Conversational Recommendation
- Preference Elicitation
- Mixture of Experts
- CRS
- Dataset
one_liner: 提出分阶段动态偏好询问策略、标注数据集InPE及MoE驱动的COPE对话推荐框架
practical_value: '- 电商导购Agent/对话式推荐可直接复用分阶段询问规则：用户需求模糊的对话早期用属性类提问缩小范围，需求明确的中后期用商品选项类提问确认偏好，可提升用户交互意愿与推荐准确率

  - 多任务对话推荐系统可复用COPE的MoE+硬路由架构：用LoRA训练轻量专家分别处理闲聊、偏好询问、推荐子任务，分层路由根据上下文动态激活专家，兼顾效果与推理成本

  - 缺乏对话策略标注数据时，可参考LLM初筛+人工校验的标注流程，快速构造业务场景的对话策略标注数据集，标注成本比纯人工低50%以上'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统对话推荐系统偏好询问策略多为静态，要么全程询问属性，要么全程推荐商品，未适配对话不同阶段用户偏好从模糊到明确的演变规律，导致交互效率低、用户体验差，且当前缺乏细粒度标注的数据集支撑动态策略建模。

### 方法关键点
- 328人用户实验验证分阶段策略有效性：对话早期属性类询问用户接受度达63%，中后期商品类询问接受度超过65%，不存在全局最优的单一询问策略
- 构建InPE数据集：在INSPIRED对话推荐数据集基础上，用LLM初筛+人工校验补充每轮对话的询问必要性、策略类型（属性/商品/混合）标注，共包含2063条有效询问标注
- 提出COPE架构：基于共享LLM backbone+LoRA轻量专家的MoE设计，3类专家分别处理偏好询问、商品推荐、闲聊场景，分层路由先判断当前轮次任务类型，若是偏好询问再进一步选择属性/商品/混合策略，训练时用硬路由避免专家参数干扰

### 关键实验结果
在InPE数据集上对比多个SOTA基线，COPE的Recall@10达0.314，比次优的ReFICR高14.6%；人类偏好成对评估胜率达60.4%，比基线高5.3个百分点；当路由完全准确时Recall@10可进一步提升到0.342，证明路由准确率是当前主要性能瓶颈。

最值得记住的结论：对话推荐中没有全局最优的偏好询问策略，最优策略严格依赖对话阶段，从属性询问转向商品询问的时机和用户偏好从抽象到具体的演变完全对齐。
