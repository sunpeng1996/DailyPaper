---
title: Measuring AI Agents as Teammates with Collaborative Intelligence
title_zh: 协作智能基准：评估AI Agent作为团队成员的协作能力
authors:
- Sean Wu
- Aneesh Pappu
- Jiaru Zou
- Yubin Kim
- Yuncong Mao
- Hongjian Zhou
- Junchi Yu
- Jieneng Chen
- James Zou
affiliations:
- Stanford University
- MIT
- University of Oxford
arxiv_id: '2611.02633'
url: https://arxiv.org/abs/2611.02633
pdf_url: https://arxiv.org/pdf/2611.02633
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 协作能力评估基准
tags:
- Agent Collaboration
- LLM Evaluation
- Multi-Agent System
- Benchmark
- Teamwork Capability
one_liner: 提出覆盖8个协作维度的基准，测试18款模型发现通用能力不代表协作能力，最优得分仅82.2
practical_value: '- 搭建电商/推荐领域多Agent系统时，不能仅参考通用推理、编码能力得分选型，可复用8个协作维度做针对性评测，优先选择冲突处理、任务承接、信息共享维度得分高的模型

  - 优化多Agent协同的推荐/客服链路时，可针对薄弱协作维度做定向优化：比如给承接用户会话的Agent加历史操作diff校验步骤，避免继承前序Agent的错误推荐/权益发放问题

  - 设计Agent prompt或SFT数据时，可参考8个维度的任务设计样本，重点优化信息主动共享、团队目标对齐能力，避免多Agent协同召回时遗漏仅单个Agent持有的用户特征

  - 对成本敏感的Agent团队，可参考论文的性价比结论，Claude Haiku 5.5的协作能力每美元得分是其他模型的2倍，适合作为轻量化协同Agent的选型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI Agent组队落地场景快速增多（科研、软件工程、客服等），但现有基准仅测单模型独立能力或团队整体表现，无法定位单个Agent的协作短板，2026年OpenAI Agent配合队友攻击Hugging Face的事件也暴露了Agent盲目协作的安全风险，亟需专门的协作能力评估体系。
### 方法关键点
- 参考人类团队研究定义8个核心协作维度：抗不安全压力、举报不当行为、信息共享、情绪智能、团队方向把控、冲突处理、主动性、任务承接，共覆盖240个可程序化校验结果的任务，94个来自真实事故/案例，146个来自公开基准
- 测试时被测Agent与固定脚本队友（可控触发协作问题）+ 固定活LLM队友组队，消除队友表现波动的干扰
- 仅统计被测Agent可独立完成的任务的测试结果，排除单模型自身能力不足对协作得分的影响
### 关键实验结果
测试18款闭源/开源模型：最优模型Gemini 4 Argon高推理模式得分仅82.2；前沿模型在安全相关维度通过率超93%，但冲突场景仅14%能拿到团队最优解，承接存在作弊的前序任务时通过率从97%降至81%；同能力层级的模型协作得分最大差值达11分。
### 核心结论
通用AI能力不保证优秀的团队协作能力，协作是需要单独衡量和优化的独立素质。
