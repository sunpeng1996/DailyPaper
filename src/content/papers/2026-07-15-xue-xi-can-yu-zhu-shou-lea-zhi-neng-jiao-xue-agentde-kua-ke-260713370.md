---
title: 'Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom
  Evaluation of an Agentic AI Tutoring System'
title_zh: 学习参与助手(LEA)：智能教学Agent的跨课程可扩展性与课堂评估
authors:
- Teri Rumble
- Javad Zarrin
- P. George Lovell
- Ruth Falconer
affiliations:
- Faculty of Design, Informatics and Business, Abertay University
arxiv_id: '2607.13370'
url: https://arxiv.org/abs/2607.13370
pdf_url: https://arxiv.org/pdf/2607.13370
published: '2026-07-15'
collected: '2026-07-17'
category: Agent
direction: Agent 跨场景可扩展性评估
tags:
- RAG
- Agent
- RAGAS
- Evaluation
- Scalability
- Knowledge Modeling
one_liner: 通过真实课堂部署与跨课程测试，验证AI教学Agent的RAG效果稳定性与跨域适配局限
practical_value: '- Agent跨业务场景迁移时，编排层可直接复用，仅优化下游生成逻辑即可降低适配成本

  - RAG跨场景评估可复用RAGAS指标体系，重点监控Faithfulness随领域距离的衰减，提前做领域适配

  - 系统上线前的仿真评估无法完全替代真实用户测试，需加入小流量真实用户验证避免效果偏差'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
此前提出的AI教学Agent LEA仅在单门STEM课程完成仿真验证，未经过真实用户检验，也未验证跨课程可扩展性。
### 方法关键点
1. 首次在真实课堂部署LEA，覆盖8名修读CMP511课程的学生；
2. 选取3门分属不同学段、不同学科的课程做可扩展性测试，基于660个问题用RAGAS指标体系做量化评估；
3. 对比仿真预测结果与真实部署的效果差异。
### 关键结果
仿真与真实部署效果存在明显偏差，单一仿真评估无法覆盖真实落地的所有问题；跨课程场景下Answer Relevancy（0.88-0.94）、Context Precision（0.88-0.90）表现稳定，Faithfulness随与原课程的内容距离增加从0.69降至0.50；Agent编排层无需修改即可跨课程复用，仅下游生成组件需做领域适配。
