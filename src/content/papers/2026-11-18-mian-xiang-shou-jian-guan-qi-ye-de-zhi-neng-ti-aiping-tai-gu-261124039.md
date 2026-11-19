---
title: A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises
title_zh: 面向受监管企业的智能体AI平台评估能力框架
authors:
- Abbas Raza Ali
- Muhammad Ajmal Siddiqui
- Moona Zahid
affiliations:
- Citigroup Inc.
- Ernst & Young LLP
- NVIDIA Corporation
arxiv_id: '2611.24039'
url: https://arxiv.org/abs/2611.24039
pdf_url: https://arxiv.org/pdf/2611.24039
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 企业级平台评估
tags:
- Agent
- EnterpriseAI
- EvaluationFramework
- RegulatedIndustry
- Benchmark
one_liner: 基于全球银行10款Agent平台实测数据，提出先过审后评分的可复现企业级Agent评估框架
practical_value: '- 企业Agent选型可直接复用9维能力评估框架，针对电商/广告场景的合规要求（比如营销内容合规、用户数据保护）设为非补偿性硬门槛，未达标直接淘汰，避免演示光环效应误导决策

  - 评估Agent执行可靠性时，可复用论文提出的trace级指标：多次重复运行的任务成功率、pass@k一致性、单次成功成本（CoP），不要仅参考单轮最优演示效果

  - 部署状态改变类Agent（比如自动调整广告出价、自动发送营销触达消息）时，可参考分层评估逻辑，先过安全/合规硬门槛，再评估功能性能，避免错误操作带来业务损失

  - 内部Agent选型bakeoff可落地「实据优先」评分规则：按维度分专业小组打分，要求厂商提交执行trace、日志等实据，不要仅依赖现场演示'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前企业Agent平台采购速度远快于评估体系建设速度，公开Agent基准仅测模型能力，不覆盖完整平台的编排、治理、工具层表现，受监管行业缺乏符合合规要求的可落地产级评估方案，现有基于厂商演示的评估模式容易将演示效果误判为平台实际能力。
### 方法关键点
- 设计9维能力评估 taxonomy，覆盖反射、工具调用、记忆、规划、多Agent协作、易用性、协议兼容、量化性能、可解释性/可审计9个维度，每个维度直接对应Agent架构的具体组件
- 提出多阶段评估流程：先做厂商资质筛选（成立时间、部署模式、开源状态等），再开展能力评估+3类典型业务场景（信用风险、RAG、流程自动化）实测，最后优化为「先过审后评分」的4层评估模型，合规/安全等硬门槛为非补偿性要求，未达标直接淘汰
- 提出trace级可靠性指标体系，通过多次重复运行计算任务成功率、pass@k一致性、单次成功成本（CoP），避免单轮运行随机性干扰评估结果
### 关键结果
基于全球银行创新实验室的实测数据，对10款主流Agent平台（覆盖开源框架、商业产品、云厂商生态）的评估显示：
- 平台得分明确分为3个稳定层级，Tier1得分61.7~69.2，Tier2得分41.4~43.0，Tier3得分32.0~37.0，层级划分不受指标权重调整影响
- 9个评估维度的Cronbach's α达0.98，8个维度与总分的相关系数≥0.93，证明现有演示-based评估存在严重光环效应，演示观感对评分的影响远大于实际能力差异
### 核心结论
当前企业Agent评估大多测量的是演示效果而非实际能力，通过买方受控环境测试、按维度收集实据打分、量化执行可靠性是成本可控的优化方向
