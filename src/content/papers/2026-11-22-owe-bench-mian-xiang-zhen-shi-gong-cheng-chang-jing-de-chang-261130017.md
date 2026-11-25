---
title: 'OWE-Bench: A long-horizon benchmark for measuring real-world engineering'
title_zh: OWE-Bench：面向真实工程场景的长周期Agent评测基准
authors:
- Jacob Cole
- Martin Dimakis
- Victor Barres
- Bertie Vidgen
- Edward Hu
- Jason Wei
affiliations:
- Mercor
arxiv_id: '2611.30017'
url: https://arxiv.org/abs/2611.30017
pdf_url: https://arxiv.org/pdf/2611.30017
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: Agent长周期工程任务评测
tags:
- Agent Benchmark
- Long-horizon Reasoning
- Deployment Gap
- Autonomous Engineering
- LLM Evaluation
one_liner: 开源26个多领域长周期工程任务Agent基准，可测量部署性能差与时间利用效率
practical_value: '- 做业务Agent评测时可借鉴开发/隐藏测试集分离的设计，量化模型上线后的真实效果gap，避免过拟合现有测试用例

  - 调度工程类Agent时可按模型特性分配资源：GPT类适合短周期高优先级任务，Claude类适合长周期高复杂度任务

  - 业务迭代调优优先给单轮更长的迭代预算，而非拆成多轮短迭代选最优，可拿到更好的最终效果

  - 做Agent自校验时需新增分布外校验case，不要仅依赖现有测试用例通过率，避免高估线上性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准要么仅评估最终制品质量，要么允许Agent直接查询评测器，无法衡量Agent对自身方案泛化性的判断能力，也无法匹配真实工程中开放世界、长周期、无明确完成标准的任务特性，亟需更贴近实际场景的评测体系。

### 方法关键点
- 包含26个领域专家编写的长周期工程任务，覆盖软件工程、物理工程、机器学习、科学计算4个领域，单任务耗时4-18小时，无明确及格线，按速度、成本、精度等实际指标连续打分
- 严格分离开发与评测环境：Agent仅能使用提供的工具与开发测试集迭代，最终方案在不可访问的隐藏测试集上打分，量化开发分数与隐藏分数的差值（部署gap）
- 测试不同时间预算下的模型表现，同时采集Agent对自身方案的性能预测，评估其自我判断能力

### 关键结果
14个前沿模型参与评测，每个任务跑8次独立尝试：
- 最优模型Claude Fable 5.2得分54.6%，单任务平均消耗2.11亿token
- 所有模型的开发集得分平均比隐藏集高18分（部署gap），同时对隐藏集得分的预测平均高估21分
- 相同token用量下GPT-6 Astra得分更高，Claude Fable 5.2通过消耗更多token拿到全局最优；单长轮次迭代比拆成2个短轮次选最优的效果高5.7分

**最值得记住的一句话**：Agent的开发测试表现远不能代表上线后的真实性能，当前前沿Agent普遍严重高估自身方案的泛化能力，且任务给定的时间预算会直接影响Agent的工作节奏与最终效果，哪怕预算从未被用尽
