---
title: 'IACM-RL: Intent-Aware Context Management and Reinforcement Learning for Complex
  Tool Invocation under Dynamic Intent Fluctuations'
title_zh: 面向动态意图波动下复杂工具调用的意图感知上下文管理RL框架
authors:
- Dingwei Zhu
- Jiahan Li
- Chengjun Pan
- Yunxian Yang
- Yunbin Zhao
- Yunke Zhang
- Zhonghang Lu
- Zhuohui Sheng
- Chenhao Huang
- Jiahang Lin
affiliations:
- Fudan University
- Honor Device Co., Ltd.
- Peking University
arxiv_id: '2608.02110'
url: https://arxiv.org/abs/2608.02110
pdf_url: https://arxiv.org/pdf/2608.02110
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 动态意图感知工具调用优化
tags:
- Tool Calling
- Reinforcement Learning
- Context Management
- Intent Tracking
- PPO
one_liner: 通过显式信念状态上下文管理与分层RL优化，提升动态意图下工具调用稳定性与泛化性
practical_value: '- 电商导购Agent/智能客服可直接复用BeliefState的stale flag机制，标记用户已修改的需求参数（如预算、品类偏好），避免重复推荐过时商品/服务，降低意图偏差

  - 多轮对话推荐的RL优化可借鉴分层意图驱动奖励设计，从认知（槽位识别）、行为（交互逻辑）、结果（任务完成）三层分配奖励权重，提升奖励信号密度，降低训练难度

  - 长会话推荐场景可引入CM状态蒸馏思路：训练阶段用显式上下文管理模块辅助状态追踪，推理阶段蒸馏为隐式能力，既降低推理开销，又提升长对话下的意图稳定性

  - 低资源场景下工具调用训练可复用DynamicIntent的LLM模拟轨迹生成流程，无需真实后端即可批量生成带意图波动的多轮训练数据，降低数据采集成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
真实场景下用户意图动态波动（中途改需求、插入闲聊、歧义表达），现有工具调用方案依赖隐式历史扫描，易受过时约束干扰，导致意图偏移、无限API循环等严重问题；现有数据集多假设静态指令，缺乏动态意图场景的训练和评估支撑。

### 方法关键点
- 构建DynamicIntent数据集，覆盖13种细粒度意图波动场景（修改、中断、澄清、累加、链式5大类），配套5维诊断指标（JGA、SCRR、RIR、DTCR、ISSR），支持ID/OOD泛化评估
- 设计基于BeliefState的自生成上下文管理器，显式追踪当前目标、参数槽位、待澄清问题、最近工具调用等状态，为已覆盖的旧参数添加stale flag，从结构上隔离过时信息
- 采用分层意图驱动的RL优化，奖励分认知、行为、结果三层，匹配BeliefState各字段实现细粒度credit assignment；新增3个辅助损失：动作校准损失绑定响应与工具调用准确率，CM提取损失直接优化上下文块生成，状态蒸馏损失把显式CM能力蒸馏为模型隐式能力，降低推理开销

### 关键实验
在DynamicIntent、BFCL-V3、τ2-Bench上测试，对比7种基线方案，IACM-RL整体平均分64.0，比基线最高提升1.4分；OOD场景认知分36.3，比基线高2.5分；长对话（>16k token）下准确率比PPO-noCM高34.8%；L3级对抗干扰下准确率比基线高11.2%。

最值得记住的一句话：动态意图场景下，把状态追踪和动作生成显式解耦，搭配分层RL优化，是提升长horizon Agent稳定性的性价比极高的方案
