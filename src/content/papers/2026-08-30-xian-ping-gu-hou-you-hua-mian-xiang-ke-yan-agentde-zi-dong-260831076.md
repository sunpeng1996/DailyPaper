---
title: 'Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic
  Research Agents'
title_zh: 先评估后优化：面向科研Agent的自动评分规则归纳框架
authors:
- Xuehai Wang
- Haowei Qin
- Tongxin Liu
- Junkai Li
- Buqiang Xu
- Jintian Zhang
- Yijun Chen
- Zirui Xue
- Shumin Deng
affiliations:
- Zhejiang University
- University of Electronic Science and Technology of China
- Beijing University of Posts and Telecommunications
- Zhejiang University of Technology
arxiv_id: '2608.31076'
url: https://arxiv.org/abs/2608.31076
pdf_url: https://arxiv.org/pdf/2608.31076
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 评分规则引导的迭代优化
tags:
- LLM Agent
- Automatic Rubric
- Iterative Refinement
- Autonomous Research
- Evaluation First
one_liner: 提出先自动归纳可执行科研评分规则、再指导Agent执行迭代的AutoSciRub框架，跨多模型多Agent架构均有效
practical_value: '- 可将「先评估后执行」范式迁移到电商内容/广告生成Agent：先基于业务规则、历史优质案例、可用物料生成可执行校验规则（如卖点完整性、合规性、素材匹配度），再指导Agent生成，减少无效输出

  - 迭代修订流程可直接复用：按生成规则逐维度校验，仅针对未达标项给出精准反馈再修订，比通用自修订效率高2.7倍，适合推荐文案生成、商品卖点提炼等场景降低冗余计算

  - 规则归纳四步流程（骨架生成→业务知识grounding→可用物料探查→规则合成）可复用在业务Agent的prompt工程中，降低人工编写复杂规则的成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前自主科研Agent处理开放任务时，指令通常仅给出高层目标，隐含的分析要求、方法规范、证据标准均不明确，容易出现遗漏关键分析、方法适配性差、结论无证据支撑等问题；传统人工编写评分规则成本极高无法规模化，且仅用于事后评估，不能反向指导Agent执行过程。

### 方法关键点
- 自动评分规则归纳：先将模糊指令拆解为原子科研目标生成规则骨架，再通过检索相关文献、行业标准补充方法/指标/基线要求，接着探查任务可用数据资源筛选可行方案，最终合成可执行、可验证的任务专属评分规则，明确数据源、实验要求、评估指标、产出物、达标条件
- 规则引导的迭代修订：Agent先按规则产出初始结果，再逐规则校验未达标项，针对具体缺口定向修订，所有规则达标或修订预算耗尽时停止

### 关键结果
在ResearchClawBench 40个跨领域科研任务上，固定Codex Agent框架时跨3个backbone LLM平均得分提升2.08分，固定DeepSeek-V4-Flash backbone时跨3个Agent框架平均提升2.95分；在AstaBench 20个端到端科研任务上跨3个Agent平均得分提升16.8分，任务完成率最高从18/20提升到20/20；规则引导的修订效率是无规则通用自修订的2.7倍。

**最值得记住的一句话**：对于模糊开放的Agent任务，先把隐含要求显性化为可验证的执行规则，再指导执行和定向修订，比直接生成+通用自修订的效果和效率都高得多。
