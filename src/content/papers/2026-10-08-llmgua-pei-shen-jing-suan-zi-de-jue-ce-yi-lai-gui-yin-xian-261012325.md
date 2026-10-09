---
title: Prior or Feedback? What an LLM Uses When Adapting Neural Operators
title_zh: LLM适配神经算子的决策依赖归因：先验知识还是实验反馈
authors:
- Julian Chan
- Javier Mora Jimenez
affiliations:
- University of Surrey
- Compare the Market
arxiv_id: '2610.12325'
url: https://arxiv.org/abs/2610.12325
pdf_url: https://arxiv.org/pdf/2610.12325
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent决策归因 · 可控干预验证
tags:
- LLM Agent
- Hyperparameter Optimization
- Controlled Intervention
- Decision Attribution
- Scientific Agent
one_liner: 通过受控干预验证LLM小预算超参搜索时同时依赖任务先验与实验反馈，性能优于传统方法
practical_value: '- 小预算调参场景（比如推荐模型小流量实验、广告出价策略迭代）可直接用LLM替代传统贝叶斯优化，20次试错即可获得优于TPE、随机搜索的结果，大幅降低调参成本

  - 黑盒LLM Agent的可信性校验可复用单变量干预+动作距离的方案：仅需控制输入变量、度量输出动作的差异，无需访问模型权重即可验证Agent是否真实用到了给定输入

  - LLM序列决策冷启动可通过清晰的任务描述注入领域先验，比如电商新类目推荐策略、大促新场景活动规则冷启动，仅靠任务描述即可获得远超随机试错的初始方案'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM驱动的自动调优、科学实验Agent已广泛用于序列决策任务，但仅靠最终性能指标无法判断决策是来源于预训练先验还是真实响应了实验反馈，Agent决策的可信性难以验证，尤其在试错成本高、预算有限的场景下该问题更加突出。
### 方法关键点
- 实验设定为固定20次试错预算的超参搜索任务：为预训练FNO神经算子选择微调配置，对比随机搜索、TPE贝叶斯优化、DeepSeek-V4-Pro LLM三类策略的性能
- 设计两类受控干预验证决策依赖：冷启动阶段替换输入的任务描述，反馈阶段打乱历史配置与得分的对应关系，通过自定义动作距离度量输出配置的变化幅度
- 动作距离融合数值型超参的归一化差值和类别型超参的匹配度，单类别维度变动对应得分约0.083
### 关键结果
- 基于PDEBench的两类PDE方程的12个同域、跨域迁移场景，每个场景重复3次种子实验
- LLM在36组对比中35组优于TPE，全部优于随机搜索；冷启动首个配置就超过同场景91.7%的随机搜索结果
- 冷启动替换PDE描述会让初始学习率中位数从0.0005翻倍到0.001；打乱反馈得分对应关系会让输出配置的动作距离提升0.085，接近单类别维度的变动幅度
### 核心结论
小预算下LLM超参搜索的优势同时来自任务相关先验和对实验反馈的感知，单变量干预法可低成本验证黑盒LLM Agent的决策可信性
