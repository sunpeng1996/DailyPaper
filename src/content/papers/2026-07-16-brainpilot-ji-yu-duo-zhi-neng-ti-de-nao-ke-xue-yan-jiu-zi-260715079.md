---
title: 'BrainPilot: Automating Brain Discovery with Agentic Research'
title_zh: BrainPilot：基于多智能体的脑科学研究自动化框架
authors:
- Haoxuan Li
- Tianci Gao
- Jianhe Li
- Yang Fan
- Runze Shi
- Weiran Wang
- Tianxiang Zhao
- Zezhao Wu
- Xiaoyang Jiang
- Qihui Zhang
affiliations:
- College of AI, Tsinghua University
- Shanghai Qizhi Institute
- Business School, Renmin University of China
- School of Physics, Beihang University
- School of Information and Software Engineering, University of Electronic Science
  and Technology of China
arxiv_id: '2607.15079'
url: https://arxiv.org/abs/2607.15079
pdf_url: https://arxiv.org/pdf/2607.15079
published: '2026-07-16'
collected: '2026-07-19'
category: MultiAgent
direction: 多智能体 · 科研任务自动化
tags:
- Multi-Agent
- Scientific Agent
- Hallucination Checking
- Traceable Workflow
- Open-Source Framework
one_liner: 开源多智能体脑科学研究框架，支持可追溯流程与幻觉校验，低本能效对标SOTA智能体框架
practical_value: '- 多智能体分层架构（PI调度Agent+领域专家Agent+审计Agent）可直接复用，适配电商大促运营、广告素材合规审核等多步骤复杂业务场景

  - Graph of Trace全链路可追溯设计可迁移到推荐系统A/B实验归因、LLM生成内容溯源场景，大幅降低问题排查成本

  - 垂直领域知识库+可复用技能库的Agent grounding方案，可用于电商客服、搜索query语义理解的领域适配，减少幻觉

  - 内置审计Agent做幻觉校验的流程可嵌入生成式推荐文案、商品标题生成管线，降低内容违规风险'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有垂直领域AI Agent缺乏专属领域知识，易生成幻觉、多步推理漂移，且缺少可审计的专家干预节点，在脑科学这类高容错成本领域难以落地。
### 方法关键点
1. 采用PI Agent调度多领域专家Agent的分层架构，所有Agent基于含7233条索引的脑科学知识库、覆盖7个领域的72个可复用方法技能库做grounding
2. 设计Graph of Trace记录子目标、工具调用、证据、结论的全链路映射关系，支持流程审计与人工介入
3. 内置Auditor Agent将幻觉校验嵌入全工作流，保障输出结果可靠性
### 关键结果
在3个脑科学标准任务、自研BrainPilotBench-v0基准及端到端案例测试中，基于开源基座的BrainPilot性能对标SOTA智能体框架，且成本更低
