---
title: 'Verify, Don''t Trust: Agentic Model Development for Video Discovery Retrieval
  at Scale'
title_zh: 先验证、勿轻信：面向大规模视频发现检索的Agent化模型开发
authors:
- Hao Fu
- Baiting Zhu
- Minglei Chen
- Yinjie Huang
- Shuai Ding
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.21257'
url: https://arxiv.org/abs/2609.21257
pdf_url: https://arxiv.org/pdf/2609.21257
published: '2026-09-18'
collected: '2026-09-22'
category: Agent
direction: Agent 检索模型实验自动化迭代
tags:
- Agentic ML
- Retrieval System
- Experiment Validation
- EvoPilot
- Online Experimentation
one_liner: Meta推出带人类门控和确定性校验的EvoPilot系统，解决长周期线上检索模型实验的可信度问题
practical_value: '- 实验校验层可复用「对比为最小证据单元」设计：所有A/B实验上线前必须校验对照组与实验组的未声明变量（代码版本、数据快照、召回深度P/K、评估逻辑版本）完全对齐，避免因链路不一致得出无效结论

  - Agent化ML开发架构可复用「角色拆分+版本化领域技能+可执行guard」设计：不要把全流程逻辑塞在prompt里，将固定操作封装为版本化工具集，校验规则转为可执行拦截逻辑，仅将规划、分析类任务交由Agent完成，大幅提升稳定性

  - 长周期实验可直接落地artifact复用机制：按实验维度存储版本化的checkpoint、索引、评估artifact，相同基线的变体复用上游产物，可大幅减少重复训练、建索引的GPU开销'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent化自动ML框架仅能处理分钟级、自包含的小规模实验，而工业级线上检索/推荐模型的实验跨代码、训练、发布、服务、评估多个异步系统，迭代周期长达数小时到数周，仅跑通的实验常因空操作代码、数据泄露、评估语义漂移、实验组对照组链路不一致等问题得出无效结论，甚至误导迭代方向。
### 方法关键点
- 采用人类门控的实验协议：每轮实验的基线、授权变量差异、数据快照、评估指标均需人工审批，仅允许声明范围内的变量差异
- 细粒度Agent角色拆分：分为规划、基线构建、实验执行、结果分析等6个专用角色，每个角色仅持有有限操作权限，避免越权修改
- 对比级证据校验：以「对照组-实验组配对」为最小证据单元，仅当两组所有未授权变量完全对齐时，结果才被纳入有效证据
- 可执行的经验沉淀：故障教训仅在转化为可执行的校验guard后生效，而非仅作为prompt中的文本提示，从流程上避免同类问题复现
### 关键实验
在Meta VDD视频发现检索场景落地37天，覆盖7个研究方向，索引规模数亿视频：修复原始自动实验的配置不一致问题后，测出interaction head带来3.20pp离线hit率提升，线上7天A/B测试GSRR相对提升0.66%；10组重放/突变测试中100%合法对比通过校验、100%故障对比被拦截；artifact复用机制节省约5GPU小时的冗余计算。
### 核心结论
完成的实验不等于有效的证据，所有实验结论的可信度都建立在对照组与实验组除声明变量外完全对齐的基础上。
