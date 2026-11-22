---
title: 'Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated
  Manipulation Benchmarks'
title_zh: 仿真操作基准成功检验器漏洞审计：虚成功与隐失败
authors:
- Zirui Song
- Jiadong Zhang
- Zheng Lu
- Xiaosong Ma
- Xiaojun Chang
- Xiuying Chen
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Peking University
arxiv_id: '2611.25179'
url: https://arxiv.org/abs/2611.25179
pdf_url: https://arxiv.org/pdf/2611.25179
published: '2026-11-17'
collected: '2026-11-22'
category: Eval
direction: 评估方法 · LLM驱动基准审计
tags:
- LLM-audit
- benchmark-validation
- success-checker
- simulation-evaluation
- error-detection
one_liner: 提出基于LLM的SimAudit流水线，自动审计仿真操作基准手写成功检验器的两类判别缺陷
practical_value: '- 可复用「规则-指令对齐校验」逻辑：针对推荐/Agent业务的手写规则类指标（如转化判定、任务成功判定），用LLM比对规则逻辑与业务目标的一致性，提前识别规则漏判、误判的边界case，避免业务指标失真

  - 构造离线评测基准时，需同时覆盖「部分完成的负例」和「非专家路径的合规正例」两类边界样本，避免仅用单一专家样本校验导致的评测结果偏差

  - 复杂任务的成功判定可借鉴多视图交叉验证思路：例如电商导购Agent的任务完成度判定，可结合用户行为反馈、语义匹配度、任务目标完成度多维度交叉校验，降低单规则判定误差'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
仿真操作基准依赖手写成功检验器判别任务完成状态，仅覆盖专家演示路径，易出现两类缺陷：接受未完成执行的「虚成功」、拒绝合规非专家路径执行的「隐失败」，直接导致策略评估结果失真。
### 方法关键点
提出LLM驱动的SimAudit审计流水线：1. 解析任务指令与检验器代码，自动识别二者判定逻辑不一致的候选场景；2. 仿真复现候选场景，运行原检验器得到判定结果；3. 采用多视角渲染交叉验证实际行为是否匹配指令要求。
### 关键结果数字
在RoboTwin 2.0、RoboCasa365、RoboDojo三个基准测试，183个仿真用例匹配预测的检验器判定结果，共检出49个任务的61个 distinct缺陷，含40个虚成功、21个隐失败，不同基准的缺陷类型分布差异显著。
