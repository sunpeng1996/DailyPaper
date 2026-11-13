---
title: 'Cortex-FL: Agent-Mediated Collaboration for Federated Learning'
title_zh: Cortex-FL：基于Agent中介的联邦学习协作框架
authors:
- Rui Sun
- Jinfeng Peng
- Zehua Cheng
- Jiahao Sun
- Zhipeng Wang
affiliations:
- Newcastle University
- FLock.io
- University of Oxford
- Korea University
- The University of Manchester
arxiv_id: '2611.17186'
url: https://arxiv.org/abs/2611.17186
pdf_url: https://arxiv.org/pdf/2611.17186
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 联邦学习协作流程自动化
tags:
- Federated Learning
- Multi-Agent
- Decentralized Learning
- Natural Language Delegation
- Incentive Mechanism
one_liner: 构建Agent原生联邦学习系统，支持自然语言发起任务，自动完成协作组队、训练与激励结算
practical_value: '- 可复用「Agent协调+本地权限隔离」架构设计，将Agent作为协作者而非决策者，所有核心操作（数据授权、支付、训练启动）需经过用户校验，适合对数据安全敏感的跨机构推荐模型联合训练场景

  - 可迁移「任务签名链+双轨激励」机制：用可验证的签名artifacts绑定任务定义、参与协议、训练准入规则，同时分离协议奖励与服务付费，解决跨主体协作的信任与激励问题

  - 自然语言任务转可执行模板的设计思路可复用：将用户自然语言需求映射到预定义的模型训练模板，降低无FL专业能力的业务方使用联邦学习的门槛，适合电商跨商家联合建模场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
联邦学习（FL）支持多数据方无需集中原始数据即可联合训练模型，但跨机构部署时存在协作方匹配难、任务配置门槛高、激励与执行协调复杂等问题，缺乏FL专业能力的组织很难落地，现有Agent协作框架未打通任务定义、组队、训练、结算的全链路，且难以保障数据方对本地资源的控制权。

### 方法关键点
- 架构分为交互层、可信主机、隔离训练runtime三层，Agent仅通过受限工具调用执行协调动作，无核心权限，所有关键操作（发布任务、加入训练、支付等）需用户授权或主机校验
- 全链路签名artifact链绑定任务清单、双边参与协议、训练准入规则与链上注册任务，所有节点可验证执行内容的合法性
- 激励双轨设计：FL智能合约管控训练参与的奖励与惩罚，服务付费单独通过x402协议在买方验证模型交付后结算，两类交易相互隔离
- 支持自然语言任务转可执行模板，内置图像分类、时序预测、LLM微调等多种训练模板，自动完成数据兼容性校验、本地试跑、协作方发现与协议协商

### 关键实验
在4节点异构设备部署（1台MacBook Pro+3台Mac mini），用CIFAR-10数据集做5分类任务，发起方仅持有猫狗两类数据，其余3类数据由合作方持有；10轮训练后验证损失从1.52降到0.96，4节点最终checkpoint完全一致，总结算成本0.006 test USDC，符合用户低于0.01 USDC的预算要求，全流程从自然语言发起到模型交付无需人工介入协调。

### 最值得记住的一句话
Agent协作系统的核心设计原则是将协调权交给Agent，控制权留给用户，才能在提升效率的同时解决跨主体协作的信任与安全问题。
