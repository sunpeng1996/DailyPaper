---
title: 'From Trajectories to Evidence: Auditable Experimental Records for Industrial
  Research Agents'
title_zh: 从轨迹到证据：面向工业研究Agent的可审计实验记录框架
authors:
- Zijie Zhuang
- Changxin Lao
- Pengbo Xu
- Hanwen Xu
- Ruochen Yang
- Yingzhi He
- Peng Zhang
- Jiangxia Cao
- Yusheng Huang
- Guohong Mu
affiliations:
- Kuaishou Technology
arxiv_id: '2608.05235'
url: https://arxiv.org/abs/2608.05235
pdf_url: https://arxiv.org/pdf/2608.05235
published: '2026-08-05'
collected: '2026-08-07'
category: Agent
direction: 工业研究Agent 实验可信沉淀与复用
tags:
- Research Agent
- Trajectory Memory
- Auditable Record
- Industrial Recommendation
- LLM Controller
one_liner: 提出将研究Agent实验轨迹转化为带边界可审计证据的框架，解决轨迹结论不可靠问题
practical_value: '- 做推荐系统Agent自动迭代时，不要直接取最后一轮实验结果，实验轨迹是非单调的：22/30的方法最终轮效果劣于之前最优轮，需主动沉淀中间有效干预

  - Agent生成的提案、代码、结果等产物可加入上下文隔离的generate-verify-repair校验流程，3次重试即可将提案通过率从73.3%提升到100%，代码可观测性从67%提升到100%

  - 实验结论沉淀需明确适用边界、归因逻辑、触发条件，不要全量存入记忆库：14个候选claim中仅9个符合可复用要求，其余证据不足的结论需归档不可复用

  - LLM控制器的Apply决策精度仅25%，记忆复用的Apply决策应作为待验证假设而非确定性结论，需先做小流量验证再落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐场景中研究Agent已被用于多轮模型迭代实验，但轨迹天然混杂无效实验、错误归因、非单调效果波动，直接将轨迹作为记忆复用易出现幻觉、结论不可靠、落地负向等问题，现有方案仅用轨迹指导后续动作，未明确筛选可沉淀的可信结论。

### 方法关键点
1. 源适配阶段加上下文隔离的generate-verify-repair校验：分别校验产物是否与现有证据冲突、是否缺失下游必要信息，最多K次修复不通过则回滚到上一有效状态
2. 事后claim qualification：按执行有效性、归因确定性、适用边界清晰度三个维度校验实验结论，分为三类：Repair（可落地的有效干预）、Guard（需规避的明确失败模式）、Withheld（证据不足不予沉淀），仅前两类进入记录库，每条记录附带来源、干预、效果、证据、适用边界5个语义块
3. 下游复用阶段采用混合LLM控制器，基于目标场景特征匹配记录，输出Apply/Defer/Reject三类决策

### 关键实验
基于30篇推荐论文适配工业RankMixer基线，公开数据集采用Amazon Electronics，对比无校验、无记忆的基线：26/30的方法后续轮次优于首轮，但22/30的最终轮次劣于历史最优轮；校验流程将提案通过率从73.3%提升至100%，代码可观测性从67%提升至100%；LLM控制器Apply决策精度仅25%；两个落地案例分别带来直播页时长+0.75%、用户增长净效用+6.34%的在线A/B测试提升。

### 核心洞见
实验轨迹本身不是知识，只有经过校验、归因、明确适用边界的可信结论才是可复用的实验资产。
