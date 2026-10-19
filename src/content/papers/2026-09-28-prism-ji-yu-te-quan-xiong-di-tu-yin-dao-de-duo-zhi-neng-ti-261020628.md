---
title: 'PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design'
title_zh: PRISM：基于特权兄弟图引导的多智能体协作拓扑设计方法
authors:
- Phuong Tuan Dat
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.20628'
url: https://arxiv.org/abs/2610.20628
pdf_url: https://arxiv.org/pdf/2610.20628
published: '2026-09-28'
collected: '2026-10-19'
category: Agent
direction: 多智能体系统 · 协作拓扑自动设计
tags:
- Multi-Agent
- Topology Design
- Knowledge Distillation
- Privileged Information
- On-Policy Training
one_liner: 利用训练时特权兄弟拓扑做自蒸馏，无额外推理开销提升多智能体拓扑生成效果
practical_value: '- 业务多Agent工作流（电商选品、文案生成、客诉处理等）的拓扑生成场景，可复用PRISM训练范式：用历史同任务成功拓扑作为训练时特权输入，无需额外执行成本即可提升拓扑适配性，避免纯SFT偏向高频通用拓扑导致的细分任务掉点问题

  - on-policy自蒸馏+anchor loss的训练技巧可直接迁移到所有生成式工作流、路由策略生成场景，解决训练推理分布不一致的exposure bias问题

  - 对部署成本敏感的生产环境，PRISM仅增加1% LLM调用量即可获得2.5%+准确率提升，性价比极高，适合大促等流量高峰场景的Agent服务优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体拓扑生成器依赖执行验证后的成功拓扑语料做SFT训练，但语料仅记录有效拓扑不对其做优劣排序，导致SFT后模型偏向高频通用拓扑，跨任务表现波动大，同时还存在训练推理分布不一致的exposure bias问题：训练时用标注的固定拓扑轨迹，推理时要基于自己生成的部分拓扑做决策，分布不匹配影响效果。
### 方法关键点
- 两阶段训练：第一阶段从学生模型初始化教师，新增低秩FiLM分支读取仅训练时可用的同query成功兄弟拓扑作为特权信息，训练教师模型；
- 第二阶段on-policy自蒸馏：学生自行采样拓扑轨迹，用教师为轨迹每一步决策输出软标签，结合anchor loss保留已验证的有效拓扑模式做优化，训练完成后丢弃教师，推理无额外开销；
- 部署模型与原拓扑生成器架构完全一致，无需改动现有推理链路。
### 关键结果
基于Qwen2.5-7B-Instruct底座，在GSM8K、AQuA、HumanEval等6个推理/代码基准上对比ARG-DESIGNER、SFT等基线：PRISM平均准确率提升2.56%-3.24%，仅增加1%的LLM调用量；在SFT掉点最严重的AQuA数据集上，PRISM准确率比SFT高13.78%，完全解决了SFT的跨任务波动问题。
> 最值得记住的一句话：利用已有的历史成功样本作为训练时特权信息做自蒸馏，无需额外标注或执行成本，就能大幅提升生成式策略的跨任务适配性，是性价比极高的生产级优化方案。
