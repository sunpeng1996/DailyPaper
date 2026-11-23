---
title: Efficient Natural Language to Temporal Logic Translation for Real-Time Physical
  AI
title_zh: 面向实时物理AI的高效自然语言到时序逻辑翻译
authors:
- Oliver Schön
- Adrien Banse
- John Lygeros
- Lars Lindemann
affiliations:
- Automatic Control Laboratory, ETH Zürich, Switzerland
arxiv_id: '2611.27489'
url: https://arxiv.org/abs/2611.27489
pdf_url: https://arxiv.org/pdf/2611.27489
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM高效推理 · 形式化语言翻译
tags:
- LLM
- Formal Language Translation
- System-One
- Low-latency Inference
- Temporal Logic
- Edge Deployment
one_liner: 用NL分类器替代生成式LLM实现低耗时低能耗的自然语言到线性时序逻辑翻译
practical_value: '- 固定语法输出的生成类任务可拆解为预定义答案的分类子任务，替代端到端大模型生成，大幅降低推理延迟与能耗，可复用到电商query意图识别、规范话术生成等场景

  - 边缘/端侧Agent部署时，针对规则明确的结构化输出需求，用轻量NL分类器即可达到甚至超过同体量生成式LLM的精度，显著降低资源消耗

  - 时序类规则的自然语言转结构化指令可复用该拆解思路，比如电商大促活动规则转可执行的推荐触发逻辑'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有自然语言转线性时序逻辑（LTL）方案依赖生成式LLM，在边缘设备（如实体机器人）部署时受限于算力、能耗约束，云侧卸载存在延迟高、数据敏感等问题，且生成式方案未利用固定形式语言的明确语法规则，冗余度高。
### 方法关键点
摒弃端到端生成思路，将NL转LTL任务拆解为多个带预定义答案的分类子问题，采用轻量NL分类器System-One逐一回答子问题，拼接结果得到合规LTL公式，全程无开放生成过程。
### 关键结果
在3个基准数据集上精度匹配或超过当前最优本地LLM方案，运行耗时、能耗最高降低1个数量级，可泛化到未见过的原子命题与时序模式。
