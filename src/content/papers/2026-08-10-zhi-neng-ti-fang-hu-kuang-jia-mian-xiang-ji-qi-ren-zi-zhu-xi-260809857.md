---
title: 'Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy'
title_zh: 智能体防护框架：面向机器人自主系统的LLM驱动验证层
authors:
- Rohan Bhagra
- Mahantesh Halapannavar
- Uddhav Bhattarai
affiliations:
- Pacific Northwest National Laboratory
- Carnegie Mellon University
arxiv_id: '2608.09857'
url: https://arxiv.org/abs/2608.09857
pdf_url: https://arxiv.org/pdf/2608.09857
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent系统安全 · 动作合规校验
tags:
- LLM-as-a-Judge
- Agent Safety
- Verification Layer
- Knowledge Graph
- Prompt Injection Guard
one_liner: 提出双层LLM裁判架构的验证中间层，阻断机器人自主系统的不安全、违规、受攻击计划
practical_value: '- 做Agent动作/输出合规校验可复用「前置规则过滤+多LLM裁判ensemble+首席裁判聚合」架构，避免单模型偏差，大幅降低致命错误率

  - LLM上层裁判无需接触原始输入，仅聚合下层裁判的推理结论，可降低校验成本、规避prompt泄露风险

  - 结合领域知识图谱RAG给裁判提供事实依据，再加历史bad case召回，能大幅提升复杂场景下的判断准确率

  - 多LLM异步调用的方式，可在增加ensemble规模的同时几乎不抬升总延迟，平衡效果与性能'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前机器人自主系统研发重点集中在规划执行，缺失统一的计划校验层，存在LLM规划器为达成目标生成不安全、违背伦理动作的问题，同时系统易受对抗攻击、prompt注入等风险，现有校验方案多零散独立，未融合低级别安全约束、高层语义伦理校验与持续能力感知能力。

### 方法关键点
- 校验层作为中间件部署在规划模块与执行控制模块之间，输出accept/reject/escalate三类决策
- 双层LLM裁判架构：第一层为多模型异步ensemble裁判，搭配RAG检索领域知识图谱（硬件参数、安全规则、攻击知识库、历史bad case等）完成推理；第二层为首席裁判，仅基于下层裁判的推理结果聚合输出最终决策，不接触原始计划
- 前置规则校验层，做代码路径沙箱检查、prompt注入检测、技能白名单校验，提前拦截明确违规请求

### 关键实验结果
实验覆盖安全、伦理对齐、对抗攻击三类共58条标注计划，加权精度达85%，无accept与reject的交叉致命错误；对抗攻击专项测试中，97%的恶意计划被成功拦截，致命错误率为0；3个模型的ensemble在成本、延迟、效果上达到最优平衡点，单轮校验平均延迟约29s。

### 核心结论
Agent系统的校验层要严格分离规划与治理职责，优先保证无致命错误，边界模糊的请求统一走人工escalation，比追求整体准确率更重要。
