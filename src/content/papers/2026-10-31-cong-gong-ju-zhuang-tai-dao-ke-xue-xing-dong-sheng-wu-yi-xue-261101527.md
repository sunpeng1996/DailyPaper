---
title: 'From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical
  Research Agents'
title_zh: 从工具状态到科学行动：生物医学研究Agent决策溯源审计
authors:
- Xingyu Yi
- Xinya Zhang
- Yunshen Zhou
- Haoyu Bao
affiliations:
- INTOSYN AI Labs
- Columbia University
- Microsoft
arxiv_id: '2611.01527'
url: https://arxiv.org/abs/2611.01527
pdf_url: https://arxiv.org/pdf/2611.01527
published: '2026-10-31'
collected: '2026-11-11'
category: Agent
direction: Agent 决策溯源与可解释性审计
tags:
- Agent
- Decision Provenance
- Audit
- Fault Recovery
- Scientific Agent
one_liner: 提出BioAgent-DF框架审计生物医学科研Agent决策来源，定位证据引用与决策不一致的隐性故障
practical_value: '- 可复用Agent状态回溯方案，在电商导购Agent、广告投放Agent的决策归因场景，保存关键计算节点的参考值对，可快速定位决策异常原因，如商品推荐不符合偏好、广告出价异常等问题

  - 可借鉴故障恢复逻辑：当推荐/广告Agent出现隐性数值故障时，优先恢复执行时的原始状态+补全可信特征值，比直接替换输入文件的修复效率高100%，大幅降低故障影响时长

  - 流式算术校验优化方案可直接迁移到大模型推理+工具调用的Agent链路，在不改变输出正确性的前提下降低端到端执行耗时40%+，适合对时延要求高的搜索推荐实时Agent场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
生物医学科研Agent常出现输出结论一致，但引用证据、检索路径完全不同的问题，隐性工具数值故障会导致证据选择异常，现有审计方案仅追踪最终结论，无法定位决策来源的隐性偏差，合规性与可靠性不足。
### 方法关键点
提出BioAgent-DF审计框架，在Agent每个计算节点保存配对的参考值与候选值，在原始坐标下恢复/移植状态后重新执行Agent，区分数值状态恢复、排序列表恢复、可见历史恢复三类故障场景，配套流式算术校验模块降低验证开销。
### 关键结果数字
8组SciFact数据集测试中，Qwen3.5-4B、Gemma3 4B IT共出现7组可复现的证据引用/读取异常，覆盖2类声明；hERG心脏安全检测场景中，恢复早期执行状态+提供可信分值可100%修复39个异常决策，替换预测文件修复率为0；流式算术校验相比原始FP64实现，端到端执行+验证总耗时降低42.4%，输出完全一致。
