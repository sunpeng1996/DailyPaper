---
title: The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model
  and the Net Human-Agent Score (NHAS) in Autonomous Commerce
title_zh: 自主商业动态可验证多智能体人智忠诚环模型与净人智分数
authors:
- Sai Srikanth Madugula
- Peplluis Esteva de la Rosa
- Daya Shankar
affiliations:
- Woxsen University
- Universitat de Girona
arxiv_id: '2607.13998'
url: https://arxiv.org/abs/2607.13998
pdf_url: https://arxiv.org/pdf/2607.13998
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent 自主商业忠诚与对齐评估
tags:
- Multi-Agent
- Autonomous Commerce
- Trust Calibration
- Loyalty Model
- NHAS
one_liner: 提出适配自主商业的多智能体忠诚环框架与可审计人智对齐评估指标NHAS
practical_value: '- 开发自主购物Agent时，可复用DVM-HALL的效用加权逻辑，根据用户当前授权度动态平衡人类情感偏好与Agent执行效率、风险指标，避免过度依赖算法忽略用户品牌偏好

  - 可直接采用NHAS作为Agent商业任务的评估指标与RL微调奖励信号，替代传统仅面向人类的NPS，同时覆盖决策对齐度、执行效率、风险合规三类核心维度，数据来源可直接对接现有用户反馈、系统日志、交易凭证模块

  - 涉及代币化忠诚度、DeFi结算的跨境电商场景，可直接复用论文给出的Agent执行风险特征集（gas成本、滑点、智能合约风险、撤销便利性等），补充到现有排序特征体系中'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统客户忠诚模型仅面向人类消费者，随Agentic AI普及，具备自主采购决策权的机器客户成为新消费主体，原有模型未覆盖算法有限理性、可验证执行风险、人智信任动态变化等核心变量，无法适配自主商业新范式。
### 方法关键点
- 构建DVM-HALL三端忠诚环框架，覆盖人对Agent的信任校准、Agent对品牌的算法偏好、品牌对人/Agent的双轨运营三个交互维度
- 分层计算决策效用：分别建模人类情感类效用（品牌情绪资产、满意度、伦理合规性等）与Agent执行类效用（API可用性、滑点、MEV风险、智能合约风险等可量化可验证指标），再按用户当前授权度、人智信任系数加权得到综合效用，通过softmax输出品牌选择概率
- 设计递归动态更新机制，每次交互后根据决策对齐度、执行质量、解释性、硬规则违规情况自动调整信任值与用户授权度
- 提出NHAS净人智对齐分数，融合人类反馈、执行日志、基准对比、可验证交易凭证四类数据，带风险权重，可审计，适配自主场景替代传统NPS
### 关键结果
- 仿真验证：当Agent幻觉率为5%时，NHAS基准值约为61.5，符合理论边界公式E[NHAS] = 70 - 170h
- 当系统幻觉率上升到45%时，NHAS跌至负值，触发授权系数自动重置为0，系统回退到传统人工搜索模式
- 已提出三类验证计划：受控人类-Agent购物实验、多智能体市场仿真、DeFi/代币化忠诚度测试床验证
### 核心结论
未来品牌竞争需要同时抢占人类情感心智和Agent算法偏好，而非仅关注人类消费者需求
