---
title: 'Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format
  Proofs'
title_zh: 拉马努金挑战赛结果：面向多格式证明的AI辅助评估流水线
authors:
- Alan Sorani
- Ashvni Narayanan
- Michael Shalyt
- Tali Monderer
- Rotem Kalisch
- Hila Barkan
- Elyasheev Leibtag
- Shachar Weinbaum
- Carsten Schneider
- John Campbell
affiliations:
- Ramanujan Machine Group, Technion, Haifa, Israel
- Department of Mathematics, Computer Science and Statistics, Ghent University, Ghent,
  Belgium
- Research Institute for Symbolic Computation, Johannes Kepler Universität Linz, Linz,
  Austria
- Department of Mathematics and Statistics, Toronto Metropolitan University, Toronto,
  Canada
arxiv_id: '2610.40551'
url: https://arxiv.org/abs/2610.40551
pdf_url: https://arxiv.org/pdf/2610.40551
published: '2026-10-29'
collected: '2026-11-01'
category: Eval
direction: LLM评估 · 多格式复杂内容评估
tags:
- Evaluation
- LLM Evaluation
- Mathematical Reasoning
- Automated Assessment
- Multi-format Evaluation
one_liner: 提出面向多格式数学证明的AI辅助评估流水线，大幅降低复杂证明评估假阳性率
practical_value: '- 电商商品文案、推荐生成理由的合规性/正确性评估可参考该分层校验思路，替代one-shot LLM评估，大幅降低假阳性

  - Agent决策链路、推理过程的正确性校验可引入「语义校验+逻辑验证+工具执行校验」的框架，替代纯LLM打分，提升评估准确率

  - 多格式（文本、代码、结构化数据）内容的规模化评估可借鉴该方案的分格式适配思路，针对不同类型内容设计针对性校验逻辑'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有研究级数学问题缺少可靠的规模化评估方案，传统one-shot LLM评估自然语言、CAS代码、Lean形式化证明等多格式复杂证明时，假阳性率高、准确率低，无法支撑大规模submission校验。
### 方法关键点
1. 构建面向研究级数论问题的Ramanujan Challenge基准，包含未公开结果与开放猜想，公式正确性可通过数值验证，证明过程需复杂数学推理；
2. 提出多格式证明AI辅助评估流水线，针对三类证明分别做语义逻辑校验、运行验证、编译校验，分层判断正确性。
### 关键结果数字
相比传统one-shot LLM评估，自然语言证明假阳性率从23%降至6%，配套代码评估准确率从46%提升至58%，同时识别出1个开放猜想的有效证明与多份思路异于官方解的正确提交。
