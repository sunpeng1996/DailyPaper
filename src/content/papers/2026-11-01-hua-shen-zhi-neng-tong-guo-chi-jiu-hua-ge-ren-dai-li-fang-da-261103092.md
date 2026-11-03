---
title: 'Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents'
title_zh: 化身智能：通过持久化个人代理放大人类主观能动性
authors:
- Zheng Wu
- Xinbei Ma
- Yao Yao
- Zhaoyuan Huang
- Haowen Hu
- Yijie Lu
- Taolei Wang
- Yifei Yang
- Wuyue Xiong
- Pengzhou Cheng
affiliations:
- Shanghai Jiao Tong University
- National University of Singapore
- Shanghai University
arxiv_id: '2611.03092'
url: https://arxiv.org/abs/2611.03092
pdf_url: https://arxiv.org/pdf/2611.03092
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: 个人Agent · 决策授权体系构建
tags:
- PersonalAgent
- DecisionDelegation
- AOI
- RehearsalEngineering
- AgentSafety
one_liner: 提出Avatar Intelligence持久化个人代理范式、成熟度路线图、AOI评估框架及核心研究方向
practical_value: '- 评估层可直接复用AOI指标：搭建电商/广告场景个人助理Agent时，除任务成功率外，将用户干预频率、审核时间、决策负担加权计入评估，避免出现「Agent干活1分钟，用户校验10分钟」的负价值产品

  - 用户建模可参考身份拆分逻辑：将用户画像拆分为稳定决策层（风险偏好、消费习惯、决策风格）和动态上下文层（近期需求、场景约束），跨购物、售后、会员服务等场景复用统一身份，降低用户重复配置成本

  - 上线前验证用Rehearsal Engineering方案：新Agent功能上线前，基于用户历史行为构造仿真场景做沙箱 rehearsal，先验证决策符合用户预期再放量，尤其适用于大额消费、金融导购等高风险场景

  - 高风险操作采用双层安全机制：涉及支付、地址修改等不可逆操作时，技术层做最小权限、二次校验，运营层可配套故障赔付服务，降低用户对授权Agent决策的信任门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个人Agent仅支持单任务响应，用户需投入大量精力明确目标、消除歧义、校验结果，监督负担极重，无法实现长期跨场景的决策授权；行业缺乏统一的个人Agent成熟度划分标准和价值评估体系，无法有效衡量Agent对人类能动性的实际放大效果。
### 方法关键点
- 定义Avatar Intelligence范式：以用户为核心，底层为持续迭代的用户身份模型，拆分稳定人格（价值观、决策风格、风险偏好）和动态知识（事实、经验、领域知识）两层，支持工作、社交、助手等多任务克隆复用同一身份，具备工作连续性、主动服务、能力扩展三大核心特性
- 推出L0-L3四级成熟度路线图：从L0人类主导全流程、L1人类控制关键决策、L2人类仅做少量 checkpoint 校验，到L3授权域内完全自主，同一Avatar可在不同领域处于不同成熟度等级，用户随时可调整授权范围或收回权限
- 设计Agentic Oversight Index（AOI）评估指标：AOI = 归一化净价值U - λ*人工监督负担P，其中净价值扣除Agent侧计算、工具调用成本，人工负担包含干预频率、监督时间、决策复杂度、审计负载四个维度，同时兼顾用户获得的实际价值和使用成本
- 明确三大核心研究方向：身份连续性个性化建模、基于Rehearsal Engineering的用户场景化演化、技术管控+保险赔付双层安全机制
### 关键结果
本研究为范式框架类工作，暂无公开对比实验数据，核心结论基于Meta Muse、OpenAI dots、xAI Grok Bot等现有工业界产品实践总结推导。
### 最值得记住的一句话
个人Agent的进步不应仅以任务执行能力衡量，而应看用户可可靠授权的决策范围，以及获得认可结果所需投入的人力成本。
