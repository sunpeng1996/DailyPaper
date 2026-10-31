---
title: 'rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment'
title_zh: rTaste：研究Agent是否具备研究品味？早期研究判断能力评估
authors:
- Art Kanke
affiliations:
- University of Minnesota
arxiv_id: '2610.40488'
url: https://arxiv.org/abs/2610.40488
pdf_url: https://arxiv.org/pdf/2610.40488
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: Agent 研究判断能力量化评估
tags:
- Research Agent
- LLM Evaluation
- Experiment Judgment
- Multi-Agent
- Minimum Viable Experiment
one_liner: 构建rTaste评估框架，量化研究Agent的实验提议、预测与排序能力
practical_value: '- 业务策略迭代场景选型：如果是做常规AB实验设计、现有推荐/广告策略调优，小模型搭配多Agent团队的ROI接近大模型；若需探索突破性新方向，优先选GPT-6
  Astra/Sol类大模型，非显而易见的创新方案产出率比其他模型高48pct

  - Agent优先级排序优化：不需要让消耗大量token做文献检索、代码阅读的提出Agent做排序，用无上下文的同模型实例仅基于实验描述排序即可达到相同效果，可降低50%以上的推理成本

  - 多Agent架构选型参考：算力预算有限时不建议盲目上多Agent团队，本实验中团队比单Agent成本高56%，但实验提议质量无统计显著提升，仅小模型用团队架构有较明显增益

  - 业务实验范式借鉴：可复用MVEs（最小可行实验）范式，每个策略方向先做低成本小范围验证，再推全量，降低无效实验的资源浪费'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent已能承担文献检索、代码实现、实验执行等大部分科研流程工作，但核心的「研究品味」——即对未知实验价值的判断能力，尚未被系统评估。现有评估要么仅测执行能力，要么仅对未执行的想法做主观打分，无法验证Agent的判断与实际实验结果的匹配度。

### 方法关键点
- 选取7篇2026年8-9月最新发布、带公开代码的NLP论文作为种子材料，无预设研究方向
- 评估6款前沿LLM在2种模式下的能力：单Agent/同模型3角色多Agent团队，先提出5个最小可行实验（MVEs），再预测每个实验结果、做优先级排序
- 全流程隔离设计：独立Executor执行所有MVEs，3款LLM做审计评估实际价值，对比有研发上下文的提出Agent、无上下文的同模型Judge的预测/排序效果

### 关键结果
共产出415个MVEs，其中194个被判定为合理、有价值、新颖，仅73个超出原论文且非显而易见；Agent排序的top1和审计最优匹配率38%，比随机（20%）高18pct，但和无上下文同模型Judge的效果无显著差异；Agent的实验结果预测准确率仅比基线高，但和无上下文同模型Judge的预测准确率无显著差异；多Agent团队比单Agent成本高56%，但MVEs质量没有统计显著提升。

### 最值得记住的一句话
当前Agent更擅长执行现有研究的常规跟进优化，额外的上下文检索与思考并未显著提升其研究判断的准确率。
