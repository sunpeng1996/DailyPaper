---
title: 'EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic
  Reinforcement Learning'
title_zh: EnvACE：基于世界推演内化环境动态的智能体强化学习方法
authors:
- Zishan Xu
- Zhiyuan Yao
- Yuxin Chen
- Yifu Guo
- Zhengxi Lu
- Yuquan Lu
- Jinyang Huang
- Yan Xu
- Yasheng Wang
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
- National University of Singapore
- Sun Yat-sen University
- Tencent Inc.
arxiv_id: '2608.06197'
url: https://arxiv.org/abs/2608.06197
pdf_url: https://arxiv.org/pdf/2608.06197
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: Agent强化训练 · 世界推演
tags:
- LLM Agent
- Reinforcement Learning
- World Model
- Tool Use
- GRPO
one_liner: 提出单模型双角色的世界推演Agent RL训练范式，无需外部环境即可内化动态，测试时可预推演提效
practical_value: '- 训练端降本：业务场景训练工具调用Agent（如电商售后查单、改地址，金融合规工具调用）时，可复用世界推演范式，无需搭建复杂的真实/合成可执行环境，仅通过单模型双角色联合优化即可完成RL训练，大幅降低环境搭建与验证成本

  - 测试端提效：上线时增加1-2次并行私有推演步骤，提前模拟工具调用结果，自动修正参数错误、拦截高危操作（如误取消订单、违规改价），无需额外外部交互即可降低实际执行错误率，减少用户投诉

  - 训练trick复用：优化时采用角色分离的GRPO基线计算，避免ACT和REHEARSE两个角色的reward分布差异干扰训练，且共享参数比分开训练两个模型效果更优，参数利用率更高

  - 小模型适配：该方法对小模型收益显著，1.7B规模即可超过同参数基础模型，适合算力受限的端侧/低时延业务场景落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent训练要么依赖真实交互环境，搭建、验证成本随复杂度指数上升，要么用外部独立模拟器，存在响应不稳定、接地性差的问题，且环境建模与决策策略分离，无法让策略内化动作与反馈的关联，训练效率低。

### 方法关键点
- 世界推演机制：单个共享Policy同时承担ACT（生成工具调用动作）和REHEARSE（模拟环境返回结果）两个角色，交替生成动作和反馈，自主展开完整交互轨迹，全程无需外部环境输入
- 角色感知GRPO优化：按角色分组计算reward baseline，相同角色的输出共用基线计算优势，两个角色的loss联合更新同一套模型参数，让环境动态直接内化到策略参数中
- 测试时推演增强：推理阶段可选择并行/串行模式做多轮私有推演，模拟不同动作的执行结果，聚合为推演记忆后指导真实执行，整个过程完全不改动外部环境状态

### 关键实验
在BFCL-v4、τ2-Bench、VitaBench、FinMCP-Bench四个跨领域工具Agent基准上测试，对比EnvScaler、AWM等主流环境缩放基线，8B版本整体得分32.91%，超过EnvScaler-8B 0.99%、AWM-14B 0.37%；测试时加2次并行推演，整体得分进一步提升4.2%，1.7B小模型也较同规模基础模型获得明确收益。

最值得记住的结论：让Agent自己预判动作后果，比依赖外部环境反馈再修正的成本更低、执行效率更高
