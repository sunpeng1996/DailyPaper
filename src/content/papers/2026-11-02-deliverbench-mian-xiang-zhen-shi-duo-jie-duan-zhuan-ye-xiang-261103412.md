---
title: 'DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional
  Projects'
title_zh: DeliverBench：面向真实多阶段专业项目交付的AI Agent评测基准
authors:
- Yumou Liu
- Mingju Chen
- Zhoufutu Wen
- Qianyu Yang
- Zijie Wang
- Yeqian Liu
- Chenghao Yang
- Tiliang Duan
- Qiyu Cai
- Yanglihong Xiao
affiliations:
- Humanlaya
- Shanghai Jiao Tong University
- Theseus Labs
arxiv_id: '2611.03412'
url: https://arxiv.org/abs/2611.03412
pdf_url: https://arxiv.org/pdf/2611.03412
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 专业项目交付能力评测
tags:
- Agent Benchmark
- Project Delivery
- LLM Agent
- Multi-stage Task
- Enterprise Agent
one_liner: 构建覆盖7个领域11个真实项目的多阶段专业项目端到端交付Agent评测基准
practical_value: '- 搭建企业级Agent系统时可新增跨阶段依赖校验、变更自动同步模块：比如电商大促全案策划Agent，需确保用户需求变更同步到后续选品、文案、投放所有环节，避免旧参数被下游复用的问题

  - 多阶段Agent评估不能仅看单任务得分，必须补充最终交付一致性、可用性校验：比如推荐全链路调优Agent，不能只看召回、排序单阶段指标，要以端到端GMV、转化率等业务交付结果为核心标准

  - 可复用其过程checkpoint+最终交付双维度评估框架：Agent迭代时既能定位单阶段缺陷，也能发现跨阶段传递的隐性错误，降低线上故障风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent评测大多聚焦单任务独立完成能力，而企业真实场景要求Agent交付完整多阶段项目，上游错误会直接传递到下游环节，单任务得分完全无法反映实际端到端交付能力，存在评测标准与真实需求的显著gap。

### 方法关键点
- 联合13位领域专家重构11个覆盖金融、法律、医疗、审计等7个领域的真实多阶段项目，包含150个相互依赖的子任务、661份输入文件、111项最终交付要求，项目过程中会动态释放新素材、客户反馈
- 采用过程+最终交付双维度评估：过程评估每个子任务提交物质量；最终评估覆盖单文件质量、跨文件一致性、整体交付验收三个维度，从正确性、完整性、一致性、专业性、可用性5个维度打分
- 子任务输入直接复用Agent前序阶段生成的交付物，不注入参考结果，真实还原错误传递的业务场景

### 关键实验
在7个主流模型+工具链系统上测试，最优系统（Claude Opus 5）最终交付得分仅65.0/100，90分阈值下子任务通过率仅50.0%；所有系统最终交付得分比过程得分低11.3~18.5分，69/77的系统-项目对存在该得分gap。

### 核心结论
Agent的单任务能力无法直接累加为项目交付能力，交付质量还取决于项目迭代过程中整体工作的连贯性和一致性
