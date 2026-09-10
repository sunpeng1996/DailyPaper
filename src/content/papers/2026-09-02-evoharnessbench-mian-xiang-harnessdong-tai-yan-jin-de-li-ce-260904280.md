---
title: 'EVOHARNESSBENCH: Can Your Agents Keep Pace with an Evolving Harness?'
title_zh: EVOHARNESSBENCH：面向harness动态演进的Agent能力评测基准
authors:
- Zixuan Ke
- Vaidehi Patil
- Haizhou Shi
- Yang Li
- Ye Liu
- Sarath Shekkizhar
- Anurag Koul
- Jiayu Wang
- Xuan Phi Nguyen
- Semih Yavuz
affiliations:
- Salesforce AI Research
- University of North Carolina at Chapel Hill
- University of Wisconsin–Madison
arxiv_id: '2609.04280'
url: https://arxiv.org/abs/2609.04280
pdf_url: https://arxiv.org/pdf/2609.04280
published: '2026-09-02'
collected: '2026-09-10'
category: Agent
direction: Agent 动态harness演进能力评测
tags:
- Agent_Evaluation
- Harness_Evolution
- Tool_Use
- Skill_Learning
- Multi_Agent_Collaboration
one_liner: 首个聚焦外部harness动态演进的Agent评测基准，覆盖工具、技能、多智体三个维度
practical_value: '- 迭代电商导购/客服/运营Agent的工具、技能库时，可复用基准的部署评测方法：固定模型参数测试harness扩容后旧任务的性能退化，提前规避harness-induced遗忘问题

  - Agent适配演进harness的策略选型可直接参考结论：工具/技能演进场景用任务相关的窄范围训练更高效，多智体池演进场景优先用固定全量池训练，平衡旧能力保留与新能力适配

  - 多智体协同的推荐系统迭代 specialist 智体池时，重点监控核心任务的required-agent召回率而非仅看智体选择准确率，避免稳定任务出现性能掉点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent实际部署中，外部harness（工具集、可复用技能、specialist 智体池）处于持续迭代状态，但现有Agent基准多固定harness或仅变化任务流，未覆盖harness演进场景下的能力评测，甚至存在模型参数不变、仅harness扩容就导致旧任务性能下降的harness-induced forgetting问题，亟需针对性评测体系。
### 方法关键点
- 覆盖三个演进轴：工具（API目录扩容）、技能（可复用流程库扩容）、智体（specialist智体池扩容），能力按高频核心到低频长尾分阶段释放，符合真实迭代规律
- 两种评测模式：部署评测（关闭跨阶段经验迁移，隔离harness扩容本身的性能影响）、自演进适配评测（允许保留记忆/提示/策略，测试历史经验对新harness的适配价值）
- 基准包含17个多阶段harness流，共802个可自动判分的任务、520个可执行工具、42个参考技能、62个specialist智体
### 关键实验结果
对比主流单/多智体框架与三类自演进适配方法：
1. 工具扩容场景：全量工具集比任务专属工具集准确率提升3.9pct，但token消耗上升57%；最优适配方法MemToolAgent可将准确率进一步提升至38.6%
2. 技能扩容场景：harness扩容本身对性能影响极小，最优提示类适配方法GEPA可提升准确率5.2pct
3. 智体池扩容场景：部分场景下harness扩容可导致最高34.7%的性能退化，最优代码类适配方法Meta-Harness可相对提升准确率110.2%
### 核心结论
Agent适配演进harness时，保留旧能力与适配新能力的目标往往存在冲突，不能孤立优化适配策略，必须同时监控跨阶段前向转移（新任务适配）和后向转移（旧任务保留）指标
