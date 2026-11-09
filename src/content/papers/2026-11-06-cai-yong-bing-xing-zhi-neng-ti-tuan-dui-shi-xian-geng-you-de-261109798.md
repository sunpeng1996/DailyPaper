---
title: Test-Time Compute Scales Better with Parallel Agent Teams
title_zh: 采用并行智能体团队实现更优的测试时计算扩展
authors:
- Junlin Wang
- Haozhe Chen
- Ang Li
- Rahul Chalamala
- Zhuang Liu
affiliations:
- Duke University
- Modal Labs
- Princeton University
- New York University
arxiv_id: '2611.09798'
url: https://arxiv.org/abs/2611.09798
pdf_url: https://arxiv.org/pdf/2611.09798
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: 多智能体 · 测试时计算优化
tags:
- MultiAgent
- Test-Time Scaling
- Best-of-N
- LLM Agents
- Team Collaboration
one_liner: 提出并行小智能体团队方案，结合协作提效与best-of-N选优，实现更高效的测试时计算扩展
practical_value: '- 电商/广告场景的多Agent文案生成、投放策略优化任务可直接复用架构：将总预算拆为多个5-10人规模的无角色flat小团队，每个团队内部共享信息协作产出方案，再以点击率、转化率等业务指标作为verifier选最优，比独立跑N个单Agent或单一大团队ROI更高

  - Agent架构选型trick：优先采用无管理者的flat团队，成员仅通过公共论坛共享进度，比带编排器的分层团队同成本下效果高14%-37%，避免管理者瓶颈

  - 测试时预算分配参考：对于难度高、单Agent输出质量差的任务，优先把预算分给多个小团队，而非延长单个Agent的运行时长，相同agent-hour成本下2人6小时团队比单人12小时效果高10%以上

  - 降本方案参考：对于有自动验证指标的任务，用小参数模型跑并行小团队，同等成本下可超越大模型效果，适合预算有限的业务场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有测试时计算扩展的两类主流方案均存在瓶颈：Best-of-N独立采样的单样本质量低，效果很快饱和；单一大协作团队易收敛、多样性丢失，规模扩大后效果不升反降，无法稳定将测试时算力转化为效果提升。

### 方法关键点
- 提出并行智能体团队架构：把总算力预算拆分为N个独立小协作团队，每个团队内部成员通过公共论坛共享信息，无分层角色，再用verifier选择所有团队的最优结果，天然覆盖了独立采样（团队规模k=1）和单一大团队（k=总预算）两种极端情况
- 推导统计模型证明最优性：最优期望得分=单样本均值+标准差×√(2lnN)，小团队比单Agent有更高的单样本均值，比单一大团队保留了多采样的方差增益，平衡两者实现最优效果

### 关键实验
在12个长周期优化任务（覆盖GPU内核优化、数学证明、广告投放优化等9个领域）上验证：总预算100个Agent时，10个10人小团队在10/12任务上优于独立Agent采样，平均提升27%；在所有支持大团队的4个任务上优于100人单一大团队，提升8%-30%；同等成本下27B模型的并行小团队在4/8任务上优于前沿大模型GPT-5.6-sol。

### 核心结论
对于有自动验证能力的任务，通过协作提升单样本质量，比单纯增加采样数量的测试时扩展效率更高。
