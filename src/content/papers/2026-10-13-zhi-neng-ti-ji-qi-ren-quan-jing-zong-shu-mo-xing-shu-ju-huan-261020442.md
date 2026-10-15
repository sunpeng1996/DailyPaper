---
title: 'Towards Agentic Robots: Model, Data, Environment, and Harness'
title_zh: 智能体机器人全景综述：模型、数据、环境与管控体系
authors:
- Chonghan Qin
- Dongming Wu
- Kaituo Feng
- Jiaxu Wang
- Xinlei Yu
- Peiwen Sun
- Yijia Fan
- Xilin He
- Bingao Chen
- Weitong Lian
affiliations:
- MMLab, The Chinese University of Hong Kong
- Fudan University
- Tsinghua University
- Zhejiang University
- Sun Yat-sen University
arxiv_id: '2610.20442'
url: https://arxiv.org/abs/2610.20442
pdf_url: https://arxiv.org/pdf/2610.20442
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 具身机器人体系分类综述
tags:
- Agentic Robot
- Embodied AI
- VLA
- World Model
- Taxonomy
one_liner: 提出智能体机器人统一分类框架，梳理四大领域17个方向的研究进展与落地路线
practical_value: '- 可复用Agent系统四域划分思路：将智能体系统拆解为模型能力、数据闭环、环境仿真、运行管控四大模块，可直接迁移到电商导购Agent、推荐系统自主调优Agent的架构设计

  - 分层决策设计方法：参考大模型做任务规划、专用模型执行具体动作的高低阶分离模式，落地时可降低大模型调用成本，提升业务系统稳定性

  - 执行反馈闭环优化技巧：借鉴机器人的执行监控、失败重试、动态调优机制，可用于优化搜索推荐冷启动流程、Agent多工具调用的容错逻辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型推动机器人智能从低阶动作预测向目标导向的全流程自主决策演进，智能体机器人成为具身AI的核心方向，但当前研究分散在模型训练、数据采集、仿真构建、系统设计等多个独立领域，缺乏统一框架指导完整系统搭建，概念边界模糊也阻碍了技术落地。
### 方法关键点
- 梳理机器人智能四代演进路径：任务专属策略→视觉-语言-动作（VLA）模型→世界/世界动作模型→智能体机器人，明确各阶段的核心能力与局限
- 提出四大领域17个细分方向的统一分类体系：Model覆盖训练、感知、规划、控制、适配5类能力；Data覆盖采集、标注、提纯3类数据闭环流程；Environment覆盖场景重建、任务生成、基准评测3类仿真与评估能力；Harness覆盖编排、记忆、故障恢复、技能管理、基础设施、分层系统6类运行管控能力
- 厘清智能体机器人与具身AI、自主机器人、机器人基座模型的核心差异：其本质是基于环境反馈的自主规划、动态调优决策闭环，而非单一模型能力
### 关键结果
GPT-6 Astra作为通用智能体核心，在RoboDojo 42个仿真机器人任务上平均成功率达22.48%，超越专用训练的机器人策略DM0.5（19.34%），验证了通用大模型结合Agent闭环框架的性能优势。
### 核心结论
智能体系统的核心竞争力不是单一模型的参数规模，而是多模块协同的决策闭环能力和从环境反馈中持续迭代的机制。
