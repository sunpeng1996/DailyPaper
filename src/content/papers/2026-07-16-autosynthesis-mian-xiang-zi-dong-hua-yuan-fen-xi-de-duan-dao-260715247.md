---
title: 'AutoSynthesis: An agentic system for automated meta-analysis'
title_zh: AutoSynthesis：面向自动化元分析的端到端多智能体系统
authors:
- Moein Taherinezhad
- Sebastian Maier
- Gerardo Vitagliano
- Francesco Pierri
- Stefan Feuerriegel
affiliations:
- Politecnico di Milano
- LMU Munich
- Munich Center for Machine Learning
- MIT CSAIL
arxiv_id: '2607.15247'
url: https://arxiv.org/abs/2607.15247
pdf_url: https://arxiv.org/pdf/2607.15247
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: 多智能体协作 · 科研工作流自动化
tags:
- MultiAgent
- WorkflowAutomation
- MetaAnalysis
- LLM
- ScientificAgent
one_liner: 端到端多智能体系统自动完成元分析全流程，输出结果与专家手动元分析高度一致
practical_value: '- 长链路Agent任务可复用「细分专业智能体+确定性计算模块」的混合架构：LLM仅负责推理类任务，统计、业务规则类逻辑用硬代码实现，大幅降低幻觉，适合电商大促复盘、用户反馈分析等场景

  - 结构化提取场景可复用「两阶段抽取+二次校验」流程：先构建源文本的结构化关联映射，再定向抽取目标值，之后用验证Agent核对源文本，可直接用于电商评论结构化、商品属性提取等任务，错误率可降低30%以上

  - 多源内容采集链路可复用「降级解析」设计：PDF/网页解析采用优先级从高到低的工具链，失败自动切换下一级解析方案，可用于竞品情报抓取、多模态商品信息采集的工程实现

  - 报告自动化需求可直接复用全流程框架：从检索→提取→分析→生成符合规范的报告，适配行业标准模板，可大幅降低运营、行业研究类报告的人工成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统元分析需手动完成文献检索、筛选、统计提取、效应量计算、报告生成全流程，平均耗时超1000人时、周期长达1年，现有LLM辅助工具仅覆盖文献筛选、信息提取环节，无法完成端到端的标准化统计合成与合规报告输出，难以满足快速证据合成的需求。
### 方法关键点
- 基于LangGraph构建混合架构多智能体工作流，拆分11个细分专业智能体分别负责协议规划、多源检索、全文解析、eligibility校验、统计提取、验证、效应量计算、偏误评估、报告生成等环节；LLM仅承担推理类任务，统计计算、可视化全部用确定性硬代码实现，避免幻觉保证严谨性
- 统计提取采用两阶段设计：先构建论文结构化JSON映射（关联实验设计、变量、结果位置），再定向抽取对应统计值，避免无关结果干扰；抽取后新增验证Agent二次核对源文本，过滤错误/幻觉数据
- 多源检索+降级解析链路：对接5个开源文献库，PDF解析优先用MinerU，失败后依次降级到LlamaParse、Mistral OCR、传统文本提取，提升解析成功率
- 全流程留痕，所有决策均存储审计日志，最终自动生成符合PRISMA规范的完整元分析报告
### 关键结果
以已发表的LLM说服力专家元分析为基准：
- 文献筛选原始召回71.4%，修正后召回85.7%、精度87.5%
- 最终合并效应量Hedges' g与专家结果偏差仅0.123，处于±0.2的行业可接受误差区间，匹配的研究级效应量Pearson相关系数r=0.69
- 单轮端到端运行仅需0.5小时，成本约1.5美元，消耗1M输入token、100K输出token

复杂长链路任务的Agent落地，最优架构是细分专业智能体+确定性计算模块的混合架构，而非单一大模型端到端输出。
