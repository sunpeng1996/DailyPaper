---
title: 'K2-Horizon: A Frontier Fleet of Open Source Language Models'
title_zh: K2-Horizon：全链路开源的多规格推理/Agent专用大模型家族
authors:
- K2 Team
- Zhengzhong Liu
- Haonan Li
- Xuezhe Ma
- Alexander Moreno
- Subham Sekhar Sahoo
- Rupesh Kumar Srivastava
- Mikhail Yurochkin
- Hadi Abdine
- Yash Akhauri
affiliations:
- Institute of Foundation Models
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.21003'
url: https://arxiv.org/abs/2611.21003
pdf_url: https://arxiv.org/pdf/2611.21003
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: LLM开发 · 开源推理/Agent专用模型家族
tags:
- MoE
- LLM
- Agent LLM
- MoVA
- Inference Acceleration
- Open Source
one_liner: 开源覆盖0.9B到375B的6款大模型，全量开放训练数据、checkpoint、全流程代码与工具链
practical_value: '- 低资源Agent推理部署可选36B-A4B MoVA模型：仅1/7 32B稠密模型的激活参数量，性能差距不足3.7个百分点，可大幅降低自托管Agent的推理成本

  - 推理加速可复用Uno无损失扩散适配器技术：无需额外Draft模型即可实现最高2.2倍解码提速，适配电商客服、商品文案生成等低延迟场景

  - Agent训练可借鉴「早引入Agent轨迹数据」方案：在长上下文扩展阶段（而非仅SFT阶段）注入Agent交互数据，可提升工具调用、任务规划的稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型普遍仅开放最终权重，训练全链路数据、中间checkpoint、流水线代码缺失，难以支撑可复现的模型迭代与场景化定制；同时针对Agent、推理场景优化的开源多规格模型梯队不足，不同部署场景（端侧/自托管/服务端）难以找到匹配的高性价比基座。

### 方法关键点
- 模型架构：覆盖0.9B稠密到375B-A23B MoE共6款模型，新增Grouped RMSNorm提升训练稳定性、MoVA（值混合注意力）将MoE稀疏化引入注意力值投影，搭配softplus注意力门实现更高表达力
- 训练链路：全量开放22T预训练语料（含10T合成数据）、各阶段中间checkpoint、xLLM训练框架、RL360强化学习栈、Eval360评测工具链；长上下文扩展阶段提前注入Agent轨迹数据，提升Agent性能
- 推理优化：推出Uno无损失扩散适配器，无需额外Draft模型即可实现解码加速

### 关键结果数字
- 375B-A23B MoE模型在Toolathlon-Verified基准得分65.3，超过GPT-5.6 Terra，接近GPT-5.6 Luna；SWE-Atlas-QnA代码理解得分48.4，领先同期开源模型
- 36B-A4B MoVA模型仅激活4.6B参数，性能与同训练数据的32B稠密模型差距在1.2~3.7个百分点之间，推理成本降低85%+
- Uno适配器实现无精度损失的最高2.2倍解码提速

大模型的可复现性不仅需要开放最终权重，全链路训练数据、中间状态、流水线代码的开源是支撑场景化定制与技术迭代的核心基础
