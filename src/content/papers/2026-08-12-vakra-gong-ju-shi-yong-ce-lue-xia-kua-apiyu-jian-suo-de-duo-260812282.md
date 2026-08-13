---
title: 'VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use
  Policies'
title_zh: VAKRA：工具使用策略下跨API与检索的多跳推理评估基准
authors:
- Ankita Rajaram Naik
- Anupama Murthi
- Benjamin Elder
- Siyu Huo
- Raavi Gupta
- Abhinav Jain
- Praveen Venkateswaran
- Abdulhamid Adebayo
- Danish Contractor
affiliations:
- IBM
arxiv_id: '2608.12282'
url: https://arxiv.org/abs/2608.12282
pdf_url: https://arxiv.org/pdf/2608.12282
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: 工具调用Agent · 多源推理能力评估
tags:
- Agent
- Tool-Calling
- Benchmark
- Multi-hop Reasoning
- RAG
- Policy Adherence
one_liner: 首个整合API调用、多跳推理、RAG、策略约束的可执行Agent评估基准
practical_value: '- 评估业务Agent（如电商客服、工单处理Agent）时，可复用轨迹级重执行验证逻辑，无需硬匹配工具调用序列，支持多有效路径，评估结果更贴近真实业务场景

  - 优化业务Agent性能优先攻坚实体消歧、跨源（如订单API与客服知识库）信息对齐、schema匹配等语言推理环节，而非仅优化工具调用格式，论文验证80%+失败集中在前者

  - 企业级Agent需新增工具使用策略识别分支，专门处理策略下不可回答的场景，避免幻觉输出，现有最优模型在这类任务上准确率仅2.4%，是落地核心坑点

  - 封装内部业务API时优先做Dashboard风格的高抽象端点，比需多步组合的SLOT/SEL接口可提升Agent调用成功率约40%'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
企业落地的Agent需要同时调用结构化API、检索非结构化文档、遵守自然语言工具使用策略，但现有基准均孤立评估单一项能力，75%的Agent部署团队无正式评估体系，导致多跳组合场景下性能远低于预期。

### 方法关键点
- 构建覆盖62个领域的8000+可执行本地API，配套对齐的领域文档RAG库，所有API对接真实SQL数据库，执行结果可复现，无第三方API波动问题
- 任务分三级难度梯度：不同交互风格API调用、纯API 2~5跳推理、跨API+RAG多源推理+自然语言工具使用策略约束
- 采用固定ReAct框架隔离模型能力与Agent架构差异，评估时重执行工具调用序列验证正确性，支持多条有效解决路径，无需严格匹配步骤

### 关键结果
- 最强模型GPT-5.5在单跳Dashboard API任务准确率70.4%，组合式BI API仅50~51%；推理深度增加后，多数模型准确率下降超50%
- 带工具策略约束的不可回答问题上，最优模型准确率仅2.4%
- 失败案例90%集中在实体消歧、跨源信息对齐、schema匹配等语言推理环节，而非工具调用格式错误

**最值得记住的结论**：企业级工具调用Agent的核心瓶颈不是工具调用能力，而是跨异构数据源的组合式语言推理与约束合规理解能力
