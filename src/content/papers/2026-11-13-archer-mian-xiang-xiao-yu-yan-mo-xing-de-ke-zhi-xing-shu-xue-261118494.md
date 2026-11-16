---
title: 'ARCHER: From Rationale Imitation to Executable Reasoning in Small Language
  Models'
title_zh: ARCHER：面向小语言模型的可执行数学推理训练框架
authors:
- Dhruv Dixit
- Khushi Patel
- Congcong Xu
- Min Song
affiliations:
- Stevens Institute of Technology
arxiv_id: '2611.18494'
url: https://arxiv.org/abs/2611.18494
pdf_url: https://arxiv.org/pdf/2611.18494
published: '2026-11-13'
collected: '2026-11-16'
category: Reasoning
direction: 小语言模型 · 可执行推理训练
tags:
- SLM
- Mathematical Reasoning
- Tool Use
- RL
- Trace Compilation
one_liner: 提出两阶段训练框架赋能小语言模型生成可执行推理轨迹，数学推理精度领先基线5.51pp
practical_value: '- 做Agent工具调用训练时可复用两阶段范式：先通过规则把现有业务场景的CoT数据转成结构化工具调用轨迹做SFT，再用分层门控RL优化，无需从零构造新标注数据

  - 多维度RL奖励设计可直接迁移：按优先级（结果正确性>工具调用合规>流程规范>轨迹对齐）给奖励加权重和条件门控，避免辅助奖励干扰主优化目标，大幅提升训练稳定性

  - 业务落地轻量化推理Agent（比如电商智能客服算优惠、营销活动预算预估、广告投放效果测算）时，可基于该框架训10B以下SLM，降低部署成本同时提升计算类请求的准确率

  - 工具调用轨迹标准化设计可复用：将工具调用、返回结果、校验、回答都定义成明确的动作类型，大幅降低推理过程的不可控性，方便事后排查问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
小语言模型（SLM）具备本地部署、成本低、隐私友好的优势，但传统CoT训练仅模仿自由格式解释文本，容易出现「伪推理」问题；工具增强方法仅开放工具调用权限，无法教会模型合理选择调用时机、构造合法请求、正确使用返回结果，数学推理场景的准确性和可审计性远达不到落地要求。
### 方法关键点
- 两阶段训练范式：第一阶段TRACE编译器将现有CoT数据集自动转换为结构化可执行轨迹，定义6类标准化动作，将算术运算统一映射为「计算器调用+确定性返回结果」对，基于编译轨迹做SFT，让模型首先掌握可执行推理的动作规范
- 第二阶段HiGRA分层门控RL优化：按优先级设置4类奖励（结果正确>工具接地>流程规范>轨迹对齐），辅助奖励仅在相关场景下激活，避免奖励冲突；采用GRPO做策略优化，无需额外训练价值模型，降低训练成本
### 关键结果
在7个10B以下backbone、8个数学推理benchmark上验证：5个通用SLM平均精度较最强工具增强基线高5.51pp，其中MATH-500提升8.95pp，AIME2024/2025分别提升5.33/5.34pp；对已经过RL优化的推理专用模型（DeepSeek-R1、MiMo等），仍能在所有benchmark上取得稳定精度提升。
> 最值得记住的结论：将推理监督信号与可执行的中间计算对齐，是低成本训练高可靠、可审计小推理模型的核心路径
