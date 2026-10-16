---
title: 'FDE-Gym: The Last Mile of AI Delivery'
title_zh: FDE-Gym：面向AI落地最后一公里的Agent交付能力基准
authors:
- Dongxu Yang
- Hongda Yan
- Renxin Wang
- Baoli Zhang
- Haojia Zuo
- Ying Zhao
- Youmin Chen
- Xiaojian Liao
- Congming Gao
- Tianyang Jiang
affiliations:
- DeepLethe
- Tsinghua University
- Shanghai Jiao Tong University
- Beihang University
- Harvard University
arxiv_id: '2610.22350'
url: https://arxiv.org/abs/2610.22350
pdf_url: https://arxiv.org/pdf/2610.22350
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 真实场景交付能力评估
tags:
- Agent
- Benchmark
- LLM Agent
- Deployment
- Evaluation
- Real-world Task
one_liner: 基于18个行业真实交付项目构建95个端到端任务，评估Agent的真实客户场景交付能力
practical_value: '- 企业级Agent落地可复用其评估逻辑：将业务KPI提升归一化后扣减 stakeholder 沟通/试错成本，替代单纯功能完成率指标，更贴合实际业务价值

  - 电商/推荐类Agent开发可参考其分层测试设计：从L0（全明确需求）到L3（模糊/错误初始需求）的分层测试，可精准定位需求挖掘、约束识别、方案落地各环节瓶颈

  - 落地前需警惕弱模型负收益：当前中小模型在真实交付场景下60%以上任务表现劣于无改动基线，必须经过严格场景适配测试才能上线

  - 构建Agent评估基准可复用其反作弊设计：设置do-nothing基线、字面需求实现得分上限、捷径方案得分上限，避免Agent靠训练数据记忆投机拿分'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准大多基于明确给定的标准化任务，完全不匹配真实企业交付场景：需求模糊、存在大量未声明约束、客户初始需求甚至可能指向错误问题，最终交付效果要以客户实际业务KPI提升为核心判断标准，行业缺少能端到端评估交付全流程能力的基准。

### 方法关键点
- 由行业专家从18个行业的20个真实交付项目改编，生成95个独立任务，每个任务包含模拟客户生产系统、脚本化 stakeholder、真实业务目标，可复现交付全流程；
- 设计4层任务指令梯度：L0（明确问题、约束、评分规则）、L1（明确问题，约束需自行挖掘）、L2（模糊需求）、L3（客户原始请求，可能指向错误问题），仅变更指令其余条件完全一致，可精准定位Agent能力瓶颈；
- 评分规则：先计算归一化业务提升U（0为无改动基线，1为专家参考方案效果），扣减 stakeholder 沟通/等待/试错成本C，加上事故扣减后得到最终得分S，任务完成要求S≥0.8且无生产事故。

### 关键结果
测试13种主流模型配置，最贴近真实场景的L3级别下，最优模型Claude Opus 5.5平均得分仅0.56，仅能完成14/95个任务；约束挖掘是最大瓶颈，从L0到L1（约束从明确给出到需自行挖掘），头部模型得分平均下降0.28；弱模型表现极差，Claude Haiku 4.5在79/95个任务中得分低于无改动基线，交付反而带来负收益。

**最值得记住的结论**：模型在标准化明确任务上的表现完全不能代表其真实业务交付能力，从需求挖掘到落地的最后一公里差距远大于行业预期。
