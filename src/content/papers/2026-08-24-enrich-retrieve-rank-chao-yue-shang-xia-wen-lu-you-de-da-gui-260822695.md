---
title: 'Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing'
title_zh: Enrich-Retrieve-Rank：超越上下文路由的大规模能力发现框架
authors:
- Nazib Sorathiya
- Daniel Zhang
- Bardiya Akhbari
affiliations:
- Amazon AGI
arxiv_id: '2608.22695'
url: https://arxiv.org/abs/2608.22695
pdf_url: https://arxiv.org/pdf/2608.22695
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent能力发现 · 检索排序优化
tags:
- Agent Routing
- Tool Retrieval
- Retrieve Rerank
- LLM Agent
- Scalable Agent
one_liner: 提出三段式能力发现pipeline，千级规模下效果成本均优于现有上下文路由方案
practical_value: '- 当业务侧Agent/工具/服务注册量超过500时，直接放弃全上下文路由方案，切换为检索-重排架构，成本和准确率收益明确

  - 元数据稀疏场景（比如商家自主提交的工具/服务描述不规范、过短）可加离线LLM富集步骤，仅在注册时执行一次生成结构化摘要、关键词、使用例，元数据越差收益越高

  - 能力发现的性能瓶颈70%来自召回阶段，优先优化混合召回（BM25+通用稠密向量）即可，无需一开始投入资源做领域微调的召回器，实验显示通用编码器效果优于工具领域微调模型

  - 重排阶段采用多信号加权融合策略，权重固定无需按能力类型调参，可同时支持工具、Agent、技能三类能力的发现，降低运维成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent生态的模型、Agent、工具、技能（MATS）组件已达数千级规模，传统能力发现依赖上下文路由：将能力元数据塞入prompt让LLM直接选择，规模扩大后准确率暴跌，调用成本、延迟飙升，还存在调用未信任端点的安全风险，现有方案未解决千级规模下的能力发现痛点。
### 方法关键点
- 三段式pipeline：离线Enrich阶段仅在能力注册时执行一次，LLM将稀疏元数据转换为结构化profile（摘要、动词开头的描述、关键词、正反使用例、信任分、类型标签），同时供召回和重排使用
- 在线Retrieve阶段：采用BM25+通用稠密向量（BGE/Titan）混合召回Top15/25候选
- 在线Rank阶段：多信号固定权重融合，LLM重排分（0.5）+ BM25分（0.05）+ 离线质量分（0.3）+ 意图匹配分（0.15），无对应字段自动归一化权重，跨能力类型无需调参
### 关键结果
- 覆盖7278个工具、5885个Agent、859个技能的公开/生产数据集，对比4种主流基线：正则匹配、全上下文路由Full-Ctx、带搜索工具的Search&Pick、试错调用Trial&Err
- 规模从10涨到7278时，Full-Ctx的Match@1从0.85跌至0.12，本方案仅从0.81跌至0.39，交叉点在N=500，即能力数超过500后本方案全面优于全上下文路由
- 7278工具规模下，本方案Match@1达0.397，比Search&Pick高6.5pp，成本为后者的1/2、Full-Ctx的1/70；大规模场景下70%的错误来自召回阶段，重排条件准确率稳定在0.7-0.87不受规模影响
### 核心结论
Agent能力库规模超过500后，全上下文路由的收益会被检索排序架构全面反超，后者的性能瓶颈在召回而非重排
