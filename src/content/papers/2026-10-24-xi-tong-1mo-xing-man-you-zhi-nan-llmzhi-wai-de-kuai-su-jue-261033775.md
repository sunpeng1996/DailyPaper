---
title: 'The Hitchhiker''s Guide to System 1 Models: Fast Decision-Making Beyond LLMS'
title_zh: 《系统1模型漫游指南：LLM之外的快速决策架构》
authors:
- Haggai Roitman
arxiv_id: '2610.33775'
url: https://arxiv.org/abs/2610.33775
pdf_url: https://arxiv.org/pdf/2610.33775
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 快速决策模型落地指南
tags:
- System1
- Decision Model
- Calibration
- Agent Routing
- Reranking
- LLM
one_liner: 系统梳理5类System1决策模型栈与落地方案，解决LLM在低延迟结构化决策场景的效率痛点
practical_value: '- 电商/广告推荐的排序、召回打分节点可替换LLM轻量级打分方案，采用Encoder分类器、Reward Model等System1模型，单决策延迟可从500ms+降至10~70ms，推理成本降低40~400倍，天然输出校准置信度支撑链路调度

  - Agent工作流的路由、工具选择、内容安全门控环节优先使用System1模型，搭配置信度驱动的System1+System2级联架构：高置信度决策直接返回，低置信度才调用LLM，可在效果基本无损的前提下将整体推理成本降低1~2个数量级

  - 训练业务定制决策模型时，优先采用Brier Score、Log Loss等严格正则得分规则作为训练目标，后处理搭配温度缩放/Platt缩放校准，比仅用交叉熵+准确率训练的模型置信度ECE降低70%以上，减少下游决策偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM的自回归生成范式对应人类慢思考的System2模式，虽擅长复杂推理，但在电商推荐排序、Agent路由、内容审核等结构化决策场景下，存在延迟高（单决策500ms~5s）、成本贵（为专用模型的40~400倍）、置信度校准差三大核心痛点，现有System1相关技术分散在各类论文、开源项目中，缺乏统一的落地指导手册。
### 方法关键点
- 梳理5大类System1决策模型家族：Encoder-based分类器、Reward Model、非自回归决策引擎、对比决策模型、抽取模型，给出各模型的适用场景、优劣势对比与开源选型清单
- 提供全链路训练方案：覆盖SFT、偏好学习训练Reward Model、RLCD校准训练、对比学习、知识蒸馏等，附可直接复用的工业界训练配方
- 给出完整落地方案：包括置信度评估指标、校准方法（温度缩放/Platt缩放/保序回归）、System1+System2级联架构、Agent工作流集成方案、生产部署避坑清单
### 关键实测数据
同等硬件条件下，System1模型决策延迟仅10~70ms，比同效果LLM低1~2个数量级；用严格正则得分规则训练的System1模型ECE仅0.015，远低于LLM的0.12，置信度校准度提升87.5%；采用置信度路由的级联架构可在无损效果的前提下将整体推理成本降低90%以上。
### 核心结论
结构化决策场景下，用原生输出校准概率的System1模型替代LLM做概率估算，效率最高可提升6个数量级
