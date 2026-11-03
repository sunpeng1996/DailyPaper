---
title: Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery
  for Enterprise Text-to-SQL
title_zh: LLM Agent 作为前置部署工程师的可行性：企业Text-to-SQL需求发现与交付
authors:
- Marianne Menglin Liu
- Rongguang Wang
- Zheng Wang
- Yewen Wang
- Leonid Boytsov
- Tao Sheng
- Sujith Ravi
- Dan Roth
affiliations:
- Oracle AI
arxiv_id: '2611.03551'
url: https://arxiv.org/abs/2611.03551
pdf_url: https://arxiv.org/pdf/2611.03551
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 企业级场景落地能力评测
tags:
- LLM Agent
- Text-to-SQL
- Requirement Elicitation
- Model Deployment
- Enterprise AI
one_liner: 在真实企业Text-to-SQL场景验证LLM前置部署工程师Agent的能力，定位瓶颈并给出优化方案
practical_value: '- 做企业级Agent需求采集场景时，可借鉴「事实表驱动的用户模拟器」设计，基于真实业务历史标注的事实库自动回复Agent的澄清问题，降低真人标注成本

  - 算法/模型上线前不能只看benchmark指标，必须加入生产环境（如线上真实query、目标部署硬件）的校验，避免benchmark达标但生产不可用的问题

  - 落地自主规划执行的Agent时，优先采用「规划-执行解耦」的工作流，在规划完成后加入人工校验环节，可大幅降低执行失败率，提升资源利用率

  - 需求采集阶段要求Agent明确标记未澄清的模糊点，禁止自行填充默认值，可减少后续交付阶段的需求 mismatch 问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM编码Agent已可自动化完成模型post-training，但能否替代前置部署工程师（FDE），从客户模糊需求出发完成需求澄清到落地交付的全流程，尚无实证支撑。而企业级AI落地中，需求对齐差、部署适配难是导致项目失败的核心原因，研究针对落地成本极高的企业Text-to-SQL场景，验证FDE Agent的可行性。
### 方法关键点
- 基于真实落地的Oracle企业Text-to-SQL项目，标注17项核心需求、6项客户未明确决策点，构建事实表驱动的模拟客户，可自动响应Agent的澄清请求
- 拆分为两个核心阶段：①需求发现：Agent从模糊初始请求出发，通过多轮对话输出结构化需求清单，明确标记未澄清的模糊点；②交付：支持规划-执行解耦（计划经校验冻结后执行）、端到端自主两种工作流，完成模型选型、LoRA微调、量化、部署校验全流程
- 验收指标覆盖benchmark准确率、生产SQL编译失败率、目标CPU环境p90延迟三类，对齐真实企业交付标准
### 关键结果
- 需求发现阶段测试15款模型：前沿闭源模型需求召回率最高达81.7%，开源模型仅为41.8%~49.4%
- 交付阶段测试8组Agent配置：仅25%的运行完全满足所有验收要求，且所有Agent交付的模型效果均弱于人类FDE的交付结果
- 共定位4个核心瓶颈：40%的需求漏采或错采、执行可靠性低、算力预算利用率不足、benchmark指标无法保证生产可用性
### 核心结论
企业级AI落地中，需求对齐的重要性远高于模型本身的benchmark表现，未经过生产环境校验的算法效果不具备业务价值
