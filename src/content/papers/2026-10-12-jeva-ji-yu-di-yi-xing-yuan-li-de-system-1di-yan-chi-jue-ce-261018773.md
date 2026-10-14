---
title: 'Jeva: System One Models from First Principles'
title_zh: 《Jeva：基于第一性原理的System 1低延迟决策模型》
authors:
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.18773'
url: https://arxiv.org/abs/2610.18773
pdf_url: https://arxiv.org/pdf/2610.18773
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: Agent 低延迟决策架构设计
tags:
- System1 Model
- Permutation Invariance
- Cacheable Decision
- Null-Aware
- Low-Latency Inference
one_liner: 提出请求与候选分离编码的决策原生架构，同时满足空值感知、排列不变、可扩展、可缓存四大特性
practical_value: '- 电商推荐/搜索排序场景可复用请求-候选分离编码设计，提前预计算全量item的特征存入内存缓存，每次请求仅需编码用户query/上下文，配合轻量决策模块完成候选打分，大幅降低千级以上长尾候选集的排序延迟

  - Agent工具调用/用户意图识别场景可复用显式空值门设计，单独建模「无合适匹配项」的概率，无需额外引入"None of above"候选参与训练即可避免强制选择导致的bad
  case

  - 多候选排序任务可直接复用排列不变的决策模块，无需做候选顺序的增广训练，即可保证候选重排不会改变最终决策结果，减少线上召回结果顺序变化导致的排序抖动'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有System 1低延迟决策模型大多将请求与候选拼接后联合编码，存在四大核心缺陷：候选顺序会影响决策结果、候选规模扩展需要重新定义输出空间、无法区分「无合适候选」与「候选间不确定」、候选计算无法跨请求复用，在候选集规模大、请求量高的推荐/Agent场景下，推理延迟和决策稳定性都无法满足业务要求。
### 方法关键点
- 采用共享编码器独立编码请求与每个候选，候选编码不含任何请求、其他候选相关信息，支持跨请求缓存
- 轻量决策模块仅更新请求状态，通过对称聚合与共享打分实现排列等变的候选概率，候选规模扩展无需修改模型参数
- 单独设计coverage门，基于候选最大打分单独建模「存在有效候选」的概率，将空值概率与候选间的竞争分布解耦
- 支持Choice（候选选择）、Noul（二分类判断）、Score（数值打分）三类决策输出复用同一套架构
### 关键实验
数据集覆盖Typed Decisions、BANKING77、MASSIVE、Mind2Web，对比JevK5、Intern-Decision、KEV等10+基线模型：空值检测AUROC达98.66%，比最优基线高5.05个百分点；候选重排下决策翻转率为0，概率分布平均总偏差仅3.17e-8；2048个候选场景下准确率达69.88%，比递归基线高2.41个百分点，延迟降低2倍以上；候选全缓存时p50延迟降低27倍，决策结果无变化。
**最值得记住的一句话**：决策原生架构的核心是将可复用的候选语义编码、集合依赖的请求状态更新、候选可用性判断三个模块完全解耦，在不损失决策精度的前提下同时满足稳定性、扩展性与低延迟要求。
