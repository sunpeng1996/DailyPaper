---
title: How Much Were You Told? Measuring External Information in Peer Reviews
title_zh: 如何测量审稿中的外部信息：区分LLM润色与全委托审稿
authors:
- Matthieu Dubois
- Pablo Piantanida
- François Yvon
affiliations:
- Sorbonne Université
- CNRS
- MILA
- Université Paris-Saclay
- International Laboratory on Learning Systems (ILLS)
arxiv_id: '2609.28041'
url: https://arxiv.org/abs/2609.28041
pdf_url: https://arxiv.org/pdf/2609.28041
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM生成文本检测 · 信息论估计
tags:
- LLM
- Artificial Text Detection
- Information Theory
- Unsupervised Learning
- Peer Review
one_liner: 提出无监督自条件信息估计器，可区分审稿场景下LLM润色与全委托生成行为
practical_value: '- 可复用Self-Conditioning思路检测电商UGC、商家营销文案是否为LLM全量生成，区分人工创作+LLM润色的合规场景，降低内容管控误判率

  - 无监督信息熵对比方案无需标注数据，可快速落地到广告文案原创性校验、内容风控场景，落地成本远低于有监督ATD方案

  - 高temperature采样可规避检测但降低内容质量的结论，可用于指导UGC质量规则设计，新增内容一致性、流畅度维度加权降低规避概率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有人工文本检测（ATD）方法仅识别文本表面特征，无法区分LLM用于审稿润色与全委托生成的行为，无法匹配学术会议的审稿监管需求。
### 方法关键点
提出无监督Self-Conditioning信息论估计器，对比审稿文本在原始上下文（仅论文+通用审稿指令）下的生成概率，与上下文叠加从审稿文本提取的提示后的生成概率，差值越大说明外部信息含量越高，越可能为全委托生成。
### 关键结果
在IntelLabs审稿基准上，区分全委托生成与机器润色文本的AUC最高达1.0，且对表面改写鲁棒；生成器输入外部信息越多，得分越接近人类区间，呈单调变化，性能远超传统ATD基线；高温度采样可绕过检测，但会显著降低输出质量。
