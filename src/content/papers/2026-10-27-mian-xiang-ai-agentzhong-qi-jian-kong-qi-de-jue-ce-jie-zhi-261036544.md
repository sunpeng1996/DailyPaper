---
title: 'Monitor Accuracy Isn''t the Answer: A Decision-Value Framework for Evaluating
  AI Agent Restart Monitors'
title_zh: 面向AI Agent重启监控器的决策价值评估框架，替代单纯准确率指标
authors:
- Siddharth Jain
- Venkat N. Vedam
affiliations:
- Intuit
arxiv_id: '2610.36544'
url: https://arxiv.org/abs/2610.36544
pdf_url: https://arxiv.org/pdf/2610.36544
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent 故障监控与重启策略评估
tags:
- Agent
- Restart Policy
- Evaluation Framework
- Decision Value
- Monitor Audit
one_liner: 证明监控准确率无法评估Agent重启策略价值，提出决策导向的评估框架与无模型审计方法
practical_value: '- 评估电商/导购/推荐类Agent的故障恢复策略时，不要仅考核故障检测的准确率、TPR/FPR指标，必须联合计算重启后剩余预算下的任务成功率，避免高准确率监控反而带来业务收益负向

  - 上线Agent重启类动作前，可复用文中的无模型决策审计方法，基于历史trace计算二项分布置信区间，证据不足时直接选择弃权（沿用原有策略），尤其适合对稳定性要求高的电商场景

  - 做Agent对话上下文压缩时，无需追求语义重构的高保真度，只要保留「继续执行/重启」的决策边界信息即可，节省的token成本可直接转化为业务降本收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前AI Agent故障重启监控普遍采用分类准确率、TPR/FPR等指标评估，但这些指标完全无法反映重启决策的核心业务价值：重启是否能提升最终任务成功率。高准确率的故障监控可能因为重启后剩余预算不足、重启成功率低，反而导致整体任务成功率下降，现有评估体系存在明显缺陷。
### 方法关键点
- 推导警报-动作价值恒等式，从理论上证明固定准确率的监控（如90%准确率）的重启收益可在-5pp到+35pp区间波动，完全由重启后剩余预算下的任务成功率决定，与监控准确率无直接关联
- 给出决策充分性准则，为Blackwell实验比较的二元动作特化版本，可直接判断进度表示、上下文压缩方案是否保留了「继续/重启」最优决策所需的全部信息
- 给出有限样本无模型决策审计方法，基于现有Agent历史trace计算同步二项分布置信区间，直接输出「重启/继续/弃权」三种结论，无需额外模型调用，统计置信度可配置
### 关键结果
基于SWE-bench Verified的19个SymPy任务、194次mini-swe-agent执行trace，回溯审计130条轨迹得到核心结果：
1. 同一切换阈值在不同模型上的收益差可达42.29pp，完全无跨模型迁移性
2. 前期观测到的2.29pp重启成功率提升，完全来自单条幸存的失败轨迹，不具备普适性
3. 103次实时决策对比中，无1条达到95%置信度的决策要求，绝大多数看似有效的重启策略实际统计显著性不足

**最值得记住的结论**：Agent故障恢复的业务价值等于故障检测能力乘以重启后的实际任务收益，脱离后者谈检测准确率没有任何实际意义。
