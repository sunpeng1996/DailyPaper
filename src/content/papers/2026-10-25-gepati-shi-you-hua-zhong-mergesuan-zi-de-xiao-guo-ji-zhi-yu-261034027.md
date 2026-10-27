---
title: When Does GEPA Merge Help? A Mechanism-Level Diagnostic
title_zh: GEPA提示优化中Merge算子的效果机制与配置诊断
authors:
- Chong Zhao
- Ruyi Yang
- Changming Liu
- Alice Zhao
affiliations:
- Harvard University
arxiv_id: '2610.34027'
url: https://arxiv.org/abs/2610.34027
pdf_url: https://arxiv.org/pdf/2610.34027
published: '2026-10-25'
collected: '2026-10-27'
category: LLM
direction: LLM提示优化 · 进化算子配置诊断
tags:
- Prompt Optimization
- GEPA
- Evolutionary Search
- LLM Pipeline
- Merge Operator
one_liner: 诊断GEPA Merge跨模型不稳定机制，提出行为门控规避灾难性性能下降
practical_value: '- 落地Agent/LLM工作流的进化式Prompt优化时，不要直接使用默认Merge配置，优先在反射迭代进入性能平台期后再触发Merge，可降低早期不成熟Prompt合并的性能下降风险

  - 小参数部署模型（如7B/14B级）慎用concat式Merge算子，避免Prompt冗余导致的格式解析错误、推理准确率下降，优先选摘要重写式Merge或原生选优Merge

  - 判断Merge质量不要依赖静态Prompt特征（如长度、语义相似度），必须用验证集行为信号（如子样本准确率、错误互补性）做Merge准入判断，可大幅降低20pp以上的灾难性下降概率

  - 若任务的验证/测试集相关性低（如电商文案优化的离线指标和线上转化率相关性差），不要盲目使用Merge算子，优先靠反射突变拿收益更稳定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
GEPA是当前性能最强的反射式Prompt进化优化器之一，效果可匹配甚至超过RL微调且rollout成本低35倍，但其自带的Merge算子存在跨模型不稳定问题：相同配置下对gpt-4.1-mini平均提分1.14pp，却会导致Qwen3-8B平均降分2.45pp，原有研究未解释该现象，也没有明确Merge算子的适用条件，工业界落地时存在不可控的性能波动风险。

### 方法关键点
- 覆盖3×3配置空间扫描：3种Merge触发时机（立即触发、得分平台期触发、33%预算消耗后触发）、3种Merge算子（原生选优、全内容拼接、摘要重写），跨2种模型、5类多跳QA/指令跟随数据集测试
- 开展3项机制诊断：验证静态Prompt特征对Merge接受度的预测能力、对比反射突变与Merge的单步收益贡献、统计不同任务的验证/测试集相关性
- 设计4层行为门控探针：基于平台期启动、父节点强度/成熟度校验、错误互补性配对、算子动态路由4个规则控制Merge触发

### 关键结果
对比NoMerge基线，所有（模型+任务）组合下至少存在1种Merge配置可超过基线，最优配置最高提分6.34pp；默认的立即触发+原生算子配置极少成为最优解，且存在最高35.67pp的灾难性下降风险；设计的行为探针可将所有多种子运行的性能下降控制在10pp以内，无超过20pp的灾难性下降，在gpt-4.1-mini上5类任务平均提分1.44pp。

### 核心结论
GEPA Merge算子不是天生无效而是配置敏感，其质量由行为信号而非文本特征决定，核心价值是优化搜索轨迹而非直接带来单步收益，优先用于控制长尾风险而非追求全局提分。
