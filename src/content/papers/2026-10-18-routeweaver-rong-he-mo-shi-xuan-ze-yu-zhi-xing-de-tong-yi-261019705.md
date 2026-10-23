---
title: 'RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing'
title_zh: RouteWeaver：融合模式选择与执行的统一LLM路由框架
authors:
- Xiaohan Wang
- Haozhen Zhang
- Qingyuan Liu
- Tao Feng
- Wenya Wang
affiliations:
- Nanyang Technological University
- Huazhong University of Science and Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2610.19705'
url: https://arxiv.org/abs/2610.19705
pdf_url: https://arxiv.org/pdf/2610.19705
published: '2026-10-18'
collected: '2026-10-23'
category: LLM
direction: LLM路由 · 多模式联合优化
tags:
- LLM Routing
- GRPO
- Reinforcement Learning
- Mode Adaptation
- Multi-Model Collaboration
one_liner: 提出统一LLM路由框架，联合学习三类路由模式选择与内部执行策略
practical_value: '- 电商多模型服务（客服、文案生成、多Agent导购）可借鉴统一路由范式，无需预先固定单/多轮/协作模式，让模型根据query复杂度自适应选择，平衡效果与推理成本

  - 多决策层RL任务可复用COMET-GRPO分层credit分配思路，例如推荐系统召回+排序两层决策，分别计算优势信号避免梯度混淆，提升训练稳定性

  - 训练分层决策模型可复用渐进式探索策略，先固定上层决策让下层学好执行逻辑，再逐步放开上层选择，避免冷启动时策略塌陷到单一模式

  - 可复用α权重调参思路，无需重训即可在效果-成本间切换：大促期优先效果设α=0，日常流量优先成本设α=0.1~0.3，适配不同业务阶段需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM路由方法均预先固定执行范式：单轮路由选1个模型一次性执行、多轮路由迭代选模型、Agent路由组织多模型协作，无法根据query需求灵活调整调用组织方式，导致复杂query用单轮效果差、简单query用多轮/Agent模式成本高；同时联合优化模式选择和内部执行存在credit分配模糊、训练早期策略塌陷的问题。

### 方法关键点
- 统一路由格式：将单轮、多轮、Agent三种路由范式抽象为一套通用动作语法，先选执行模式，再输出对应模式下的模型选择、子任务、角色/依赖（仅Agent模式需要）等动作
- COMET-GRPO训练：把轨迹级优势拆分为跨模式的模式选择优势和同模式的内部执行优势，分别分配给对应决策token，避免不同层级决策的梯度混淆
- 渐进式探索：分三阶段训练，第一阶段强制分配模式让模型先学会每种模式的执行逻辑，第二阶段逐步放开模式选择并加入模式分布正则避免策略塌陷，第三阶段完全自主选择模式

### 关键结果
在数学、代码、知识、逻辑推理、事实召回5个领域9个基准测试上，对比10个固定范式路由基线，平均准确率达61.4%，较最强基线Router-R1相对提升11.03%；α=0.1时Worker推理成本下降23%，仅损失1个点准确率；在3个未见过的域外基准上相对提升18.28%；去掉渐进式探索策略后，路由策略会完全塌陷到单轮执行，准确率下降5.8个点。

### 核心洞察
有效的LLM路由不仅要适配调用哪个模型，还要适配模型计算的组织方式
