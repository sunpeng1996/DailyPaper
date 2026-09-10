---
title: 'SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability
  Research?'
title_zh: SAEScientist-Bench：AI Agent能否自主开展SAE可解释性研究
authors:
- Yuqiao Tan
- Shizhu He
- Jun Zhao
- Kang Liu
affiliations:
- The Key Laboratory of Cognitive Intelligence, Institute of Automation, CAS
- School of Artificial Intelligence, University of Chinese Academy of Sciences
arxiv_id: '2609.09113'
url: https://arxiv.org/abs/2609.09113
pdf_url: https://arxiv.org/pdf/2609.09113
published: '2026-09-08'
collected: '2026-09-10'
category: Agent
direction: Agent 大模型可解释性能力评估
tags:
- AI Agent
- SAE
- Mechanistic Interpretability
- Benchmark
- Autonomous R&D
one_liner: 推出SAEScientist-Bench基准，评估AI Agent利用SAE工具自主开展大模型可解释性研究的能力
practical_value: '- 可迁移Agent自主实验评估框架到推荐/广告系统特征可解释性任务，自动挖掘用户行为、物料特征的语义含义，替代人工标注降低成本

  - 基准中的对照探针设计方法可复用在LLM4Rec的特征筛选流程，过滤召回、排序阶段的虚假相关特征，提升推荐稳定性

  - 多维度加权（Rank/Activation/Steering）的Agent能力量化方法可借鉴用于内部业务Agent的效果评估，减少主观判断偏差'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
递归自提升（RSI）领域已基本实现模型训练流程自动化，但可靠的自主研发仍缺少关键环节：事后监控审计以理解模型学习内容、保障安全对齐。SAE是机制可解释性的核心工具，可分离可解释特征用于模型检查与调控，但此前缺乏对Agent利用SAE开展自主机制发现的能力评估基准。
### 方法关键点
推出SAEScientist-Bench，要求Agent给定目标概念后设计对照探针，在Gemma-2-9B-IT的131K+ SAE特征库中定位最优匹配特征，从激活排名、对照文本概念选择性、因果调控三个维度，与Neuronpedia上的专家标注参考特征做对比评估。
### 关键结果数字
测试10种Agent配置、20项任务，前沿Agent在目标概念与对照样本区分能力上接近专家水平，但因果生成调控能力大幅落后；最高Agent综合得分65.8，仅为专家基线（85.6）的76.9%，核心瓶颈为实验测量结果解读错误率高。
