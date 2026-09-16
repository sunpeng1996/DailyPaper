---
title: 'Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer
  Order Its Top Entries, and What to Measure Instead'
title_zh: 编码Agent性能已收敛：SWE-bench头部排名失效原因与评估优化方案
authors:
- Fengshuo Liu
- Ying Liu
- Ruize Sun
- Lie Luo
- Siyuan Guo
affiliations:
- Imperial College London
- The Hong Kong Polytechnic University
- Korea University
- Jinan University
arxiv_id: '2609.17394'
url: https://arxiv.org/abs/2609.17394
pdf_url: https://arxiv.org/pdf/2609.17394
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: Agent评估 · 基准榜单可靠性优化
tags:
- Agent Evaluation
- SWE-bench
- Benchmark Saturation
- Statistical Testing
- Reliable Evaluation
one_liner: 基于254份SWE-bench提交审计证明头部排名无统计显著性，提出5步评估审计协议
practical_value: '- 内部Agent/LLM/推荐系统效果评估时，不要只看总得分排名，需通过McNemar配对检验区分能力层级，避免小分差带来的错误决策

  - 搭建内部基准集时，需同时记录模型与脚手架（Prompt/工具链/排序策略/控制逻辑）版本，二者对效果的影响量级相当，不能直接迁移外部模型排名

  - 评估头部候选时，仅保留所有候选有差异的有效样例（neff），淘汰全部通过/全部失败的冗余样例，可大幅降低评估成本且不损失统计效力

  - 业务A/B测试等对比场景可复用5步审计协议，量化评估结果的统计显著性，避免误判随机波动为有效提升'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前各类Agent、LLM、推荐系统榜单常将头部小分差视为能力差异，用于模型选型、资源投入与科研对比，但此前仅关注任务本身的有效性，未验证排名的统计可靠性，大量资源被投入到无实际意义的榜单刷分中。

### 方法关键点
- 基于2026年7月抓取的4个SWE-bench拆分的254份公开提交的逐实例判决结果，无需重新运行模型即可完成审计
- 定义有效样例数`neff`：仅能区分对比集合内系统的样例才对排名有贡献，其余为不提供信息的退化样例
- 提出嵌套系数量化不同系统解集合的重叠程度，对比分数隐含的随机基线判断性能收敛性
- 采用配对McNemar检验验证相邻排名的统计显著性，输出描述性能力层级而非严格排名
- 提出5步通用审计协议，可复用于所有提供逐实例结果的榜单评估

### 关键结果数字
- SWE-bench Verified拆分头部10个系统共享285个成功样例、51个失败样例，有效样例仅占33%；头部30名的总得分差仅8.8pp，而同一模型搭配不同脚手架的分差可达29.8pp
- 头部16个系统的解集合嵌套系数中位数达0.935，远高于随机基线的0.774，解高度重叠
- Verified拆分头部30名的29对相邻排名，无一对在α=0.05水平下可通过配对检验区分，仅能分为2-3个描述性层级

**最值得记住的一句话**：当基准集头部系统的解高度收敛时，小分差不代表能力差异，报告能力层级而非严格排名才是更严谨的评估方式。
