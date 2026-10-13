---
title: Structural Automata for Neural Semantic Parsing
title_zh: 面向神经语义解析的结构自动机方法
authors:
- Xiao Zhang
affiliations:
- University of Groningen
arxiv_id: '2610.13896'
url: https://arxiv.org/abs/2610.13896
pdf_url: https://arxiv.org/pdf/2610.13896
published: '2026-10-09'
collected: '2026-10-13'
category: Reasoning
direction: 神经语义解析 · 约束解码优化
tags:
- Semantic Parsing
- Constrained Decoding
- Structural Automaton
- APD
- DRS
- AMR
one_liner: 在语义解析三阶段引入结构自动机约束，提出无需回滚的APD解码保证输出合法性
practical_value: '- 电商搜索Query语义解析、可执行SQL生成场景可复用APD解码思路，在固定输出长度限制下无需回滚即可保证生成结果合法，降低推理耗时

  - 冷启动小样本训练场景下，可引入结构自动机惩罚非法输出token，训练早期即可快速提升效果，减少标注数据需求

  - 生成式推荐、Agent工具调用的结构化输出场景，可参考三阶段约束方案，结合解码限制、后处理过滤、训练惩罚多环节对齐业务格式要求'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有神经语义解析的约束解码仅能拦截局部非法token，无法保证合法前缀可在固定输出长度限制下生成完整合规结果，不同阶段结构约束的落地价值边界不明确。
### 方法关键点
针对DRS、AMR两类语义解析任务，在解码、后处理、训练三个阶段引入结构自动机约束：解码阶段提出接受路径解码（APD），每步仅选择可在剩余长度内完成合法输出的模型偏好token，无需回滚即可保证输出合法；后处理阶段针对非法输出做批量过滤；训练阶段对自动机拒绝的token增加损失惩罚。
### 关键结果
紧长度限制下，APD相比局部掩码在DRS、AMR任务上Smatch++分别提升5.1/2.4、6.4/3.2个点，效果与带回滚的解码方案相当；小样本下8次无约束采样有10.2%输入无合法输出，全量数据下该比例降至0.4%，过滤后效果与APD仅差0.2 Smatch++；训练早期加非法token惩罚可提升Smatch++ 3.6~11.0个点，训练到1/6轮后该优势消失。
