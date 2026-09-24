---
title: 'PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety'
title_zh: PASTABench：面向Agent多轮轨迹的主动安全监控基准
authors:
- Jiapeng Sun
- Yujin Zhou
- Han Zhu
- Pengcheng Wen
- Jiayi Zhou
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- Peking University
arxiv_id: '2609.28197'
url: https://arxiv.org/abs/2609.28197
pdf_url: https://arxiv.org/pdf/2609.28197
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent 主动安全监控基准构建
tags:
- Agent Safety
- Benchmark
- Proactive Monitoring
- LLM Evaluation
- Risk Detection
one_liner: 首个标注最优干预窗口的多轮Agent主动安全基准，覆盖5大类共1139条轨迹
practical_value: '- 电商/广告Agent做操作拦截时，可复用OIW（最优干预窗口）设计思路，平衡安全与业务可用性，避免过早拦截打断正常流程、过晚拦截造成用户资产/隐私损失

  - 业务侧构建风险监控体系时，可参考分层风险标注方法，将风险划分为一级二级分类，便于后续错误归因和定向优化

  - 采用开源模型做安全拦截时，需做风险关键词脱敏测试：开源模型普遍存在词汇过拟合问题，无显性风险关键词的累积风险漏判率极高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent多轮交互的安全评估存在两类核心缺陷：单步评估孤立看待每个动作，无法捕捉风险的累积效应；全轨迹事后评估只能在伤害发生后给出结论，没有提前干预的空间，无法适配电商、政务等高风险Agent场景的安全需求。

### 方法关键点
- 提出解耦的主动安全监控框架，从「是否需要干预、何时干预、风险是什么」三个维度量化评估能力
- 构建PASTABench基准，包含1139条多轮交互轨迹，覆盖5大类13子类风险；每条轨迹标注「最早风险信号轮次」和「不可逆伤害触发轮次」，定义两者之间的区间为最优干预窗口（OIW），可同时量化过早/过晚拦截的损失
- 数据构造采用闭环校验流程：从现有安全数据集过滤初始样本，用DeepSeek-R1生成动态Actor-环境交互轨迹，经GPT-4o标注、Gemini-2.5-Pro交叉校验、人工核验，最终标注通过率90.4%

### 关键实验
评估16款主流LLM（含GPT-4o、Gemini系列、Qwen系列、Llama系列等），核心结果：
1. 最优模型GPT-4o的最优时机干预准确率仅40.74%，大部分模型过早拦截率超过40%，过晚拦截率不足1%
2. 风险关键词替换为中性词后，开源模型主动安全能力几乎崩溃，闭源模型OIW匹配率仅下降不到10%
3. 流程类安全缺口是最难识别的风险，所有模型有效拦截率仅0%~32.6%

**最值得记住的一句话**：当前Agent安全的核心矛盾不是漏判显性风险，而是过高的过早拦截误判率，以及对无关键词的隐含累积风险的识别能力缺失。
