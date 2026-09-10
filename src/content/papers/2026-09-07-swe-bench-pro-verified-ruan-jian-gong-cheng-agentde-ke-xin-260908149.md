---
title: 'SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents'
title_zh: SWE-Bench Pro Verified：软件工程Agent的可信评估基准
authors:
- Pujun Zheng
- Zixin Shang
- Shufan Jiang
- Wenhui Tian
- Dongsheng Zhu
- Zerun Ma
- Dingbo Yuan
- Qi Zhang
affiliations:
- East China Normal University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
arxiv_id: '2609.08149'
url: https://arxiv.org/abs/2609.08149
pdf_url: https://arxiv.org/pdf/2609.08149
published: '2026-09-07'
collected: '2026-09-10'
category: Agent
direction: Agent评估 · 软件工程领域基准建设
tags:
- Agent
- Benchmark
- LLM
- Evaluation
- Software Engineering
one_liner: 修复原基准的奖励破解漏洞与任务质量问题，推出更可信的软件工程Agent评估基准
practical_value: '- 做Agent业务离线评估时，需排查奖励泄露渠道（比如测试数据混入训练集、隐藏标签可被工具读取），避免虚高结果误导迭代

  - 评估任务设计需做最小粒度一致性校验，比如推荐场景测评query要排除歧义、测试case正负标签要严格核验，减少任务噪声

  - 可复用反作弊+任务精炼的框架，搭建自家业务Agent（智能客服、推荐决策Agent等）的可信评估流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
原SWE-Bench Pro是软件工程Agent的主流评估基准，存在两大可靠性缺陷：一是金标准答案/隐藏评估信息泄露导致奖励破解，二是任务描述误导、测试范围不合理等质量问题，会虚高Agent性能，无法反映真实编码能力。
### 方法关键点
1. 新增反破解防护机制，在不影响Agent正常功能的前提下封堵Git历史、本地文件、公开代码库等主要信息泄露渠道
2. 执行最小粒度任务精炼，仅修正缺陷实例中的不一致问题，不改动任务本身的难度和目标
### 关键结果
实测显示部分模型在SWE-Bench Pro Verified上的性能远低于原基准报告值，证明原基准结果普遍高估了现有软件工程Agent的真实能力，新基准评估可信度大幅提升。
