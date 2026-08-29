---
title: Using profiles of cognitive capability to assess AI suitability for workplace
  tasks
title_zh: 基于认知能力画像的工作场景AI任务适配性评估
authors:
- Jonathan Prunty
- Marko Tešić
- Patrick Quinn
- José Hernández-Orallo
- Lucy Cheke
affiliations:
- University of Cambridge
- Department for Science, Innovation and Technology
- Universitat Politècnica de València
arxiv_id: '2608.25623'
url: https://arxiv.org/abs/2608.25623
pdf_url: https://arxiv.org/pdf/2608.25623
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: AI能力评估 · 人-机任务分配
tags:
- AI Evaluation
- Cognitive Capability
- Task Allocation
- Agent Profiling
- Human-AI Collaboration
one_liner: 提出基于统一认知维度的Agent与任务画像匹配框架，可量化评估AI对不同工作任务的适配性
practical_value: '- 落地Agent任务分配体系时，可借鉴统一认知维度锚定思路，避免每次迭代都重新制定Agent与任务的适配规则

  - 评估LLM/Agent业务适配性时，可抛弃单一总分评估逻辑，按业务实际需要的认知维度加权打分，预判落地效果更准确

  - 电商客服、内容审核、运营等场景AI落地时，可复用该框架快速筛选适合自动化的任务，降低试错成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
企业部署AI时普遍存在任务适配决策难题：总benchmark分数无法预判模型实际落地表现，人工对模型能力的判断极易随技术迭代过时，缺乏可动态更新的适配评估方案。
### 方法关键点
构建统一的核心认知维度集，分别做Agent能力画像与任务需求画像：Agent侧通过带认知需求标注的benchmark集推断各维度能力得分；任务侧由领域专家标注各认知维度的权重，两者可独立更新，匹配后输出从领域到单个任务多粒度的AI适配度。
### 关键结果
在合成Agent上验证了能力还原有效性，完成6个AI系统的认知画像，采集6个职业领域410名员工的任务需求数据；发现AI系统的认知维度差异远大于模型家族差异，工作场景任务存在共通核心认知需求。
