---
title: 'INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event
  Sequences'
title_zh: INTENT：面向用户事件序列的跨时跨域冷启动评估基准
authors:
- Mattias Kvist
- Erik Lidman Hillbom
- Edoardo de Cal
- Davis Siemens
- Adam Fredriksson
- Rickard Brüel-Gabrielsson
affiliations:
- KTH AI Society
- Unbox AI
- MIT
arxiv_id: '2611.13069'
url: https://arxiv.org/abs/2611.13069
pdf_url: https://arxiv.org/pdf/2611.13069
published: '2026-11-09'
collected: '2026-11-11'
category: Eval
direction: 推荐系统 · 离线评估基准构建
tags:
- Evaluation
- Sequential Recommendation
- Cold Start
- Time-based Split
- Benchmark
one_liner: 提出覆盖7类真实场景的用户事件序列评估基准，解决传统推荐评估的时间泄露与冷启动场景缺失问题
practical_value: '- 离线评估替换按用户留最后交互的拆分方式，改用全局时间戳拆分+10%用户完全冷启的规则，避免未来信息泄露，评测结果更贴近线上真实表现

  - 新增行为漂移校准逻辑：用无参数的repeat-last基线在时间cutoff前后的得分差，量化用户行为本身的漂移幅度，分离模型性能衰退和行为漂移的影响

  - 冷启动场景评估优先引入item metadata embedding替代纯ID embedding，在item内容丰富的场景下可保留50%以上的新item预测效果

  - 评测基线必加无参数的repeat-last和popularity，避免过度拟合训练分布的模型在离线评测中得分虚高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统序列推荐评估普遍采用按用户留最后交互的拆分方式，存在训练集包含测试事件之后数据的泄露问题，也未覆盖线上真实的新用户、新item、未来时间三类冷启动场景，不同模型评测结果不可比，无法真实反映上线后的实际效果。

### 方法关键点
1. 设计7个测试cell，从「用户是否在训练集中出现」「时间是否在训练cutoff之后」「target item是否在训练集中出现」三个二元维度划分，覆盖所有线上可能的部署场景
2. 制定5条数据集筛选规则，从59个公开数据集家族中筛选出5个覆盖不同场景的数据集，每个数据集采用固定的80%训练数据占比的时间cutoff规则，避免人为调整切分带来的偏差
3. 要求每个测试cell至少1000个用户才参与模型排名，保证统计显著性
4. 配套无参数基线repeat-last、popularity，和SASRec、带metadata的SASRec-F作为参考模型

### 关键实验结果
在5个公开数据集上的测试显示：SASRec在见过item的未来时间场景下NDCG@10比popularity高100%，但在新item场景下得分为0；跨时间cutoff带来的模型性能损失为25%~68%，远高于新用户带来的4%以内的损失；repeat-last基线的跨时间得分损失为21%~64%，说明大部分性能下降来自用户行为漂移而非模型本身；带metadata的SASRec-F仅在内容丰富的MicroLens数据集上的新item场景得分优于其他模型，其余数据集收益极低。

最值得记住的结论：推荐系统离线评估的最大偏差不是来自模型选型，而是来自不符合线上真实流程的数据集拆分规则
