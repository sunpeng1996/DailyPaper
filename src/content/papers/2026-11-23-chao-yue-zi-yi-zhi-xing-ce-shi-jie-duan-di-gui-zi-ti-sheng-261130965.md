---
title: 'Beyond Self-Consistency: Recursive Self-Improvement at Test Time'
title_zh: 超越自一致性：测试阶段递归自提升框架TT-RSI
authors:
- Jianyu Wu
- Yizhou Wang
- Encheng Su
- Jinouwen Zhang
- Pengze Li
- Lintao Wang
- Chen Tang
- Aoran Wang
- Wanli Ouyang
- Shixiang Tang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- The Chinese University of Hong Kong
- University of Science and Technology of China
- Fudan University
arxiv_id: '2611.30965'
url: https://arxiv.org/abs/2611.30965
pdf_url: https://arxiv.org/pdf/2611.30965
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM 测试时无监督自提升
tags:
- Test-Time-Training
- Recursive-Self-Improvement
- Self-Consistency
- Self-Distillation
- LLM-Reasoning
one_liner: 提出无标签测试阶段递归自提升框架，较最强自一致性基线准确率高4.79%
practical_value: '- 电商query理解、智能客服应答、商品文案生成等推理任务，可复用In-Context RSI的「全推理链路+自主参考」设计，替代传统自一致性投票，相同token预算下准确率更高，同时减少68%左右的生成token成本。

  - 推荐/Agent系统的在线自适应场景，可借鉴In-Weight RSI的「相邻迭代结果蒸馏」思路，用无标注流量的自迭代结果做LoRA小参数更新，无需外部标注即可持续提升模型效果。

  - 部署LLM服务的业务可复用TT-RSI的流水线采样调度方案，重叠生成与更新过程，降低自迭代训练的时间与token消耗。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM测试时自提升方法普遍依赖自一致性（SC）的多数投票机制，存在两个核心缺陷：一是推理效率低，每次采样从头生成，完全浪费之前的推理结果；二是监督信号不可靠，当初始多数答案错误时，训练会强化错误，导致自提升无法持续累积收益，无法满足无标注场景下模型持续优化的需求。

### 方法关键点
- **In-Context RSI**：训练无关的测试时扩缩策略，每次迭代将上一次完整推理结果（含中间推导步骤）作为中性参考输入，不强制要求修正，让模型自主决定复用、修改或重开思路，避免正确结果被误改的问题。
- **In-Weight RSI**：无标注测试时训练方法，取相邻两次迭代的结果作为参考，通过递归蒸馏将迭代收益固化到模型权重，同时引入加速蒸馏让首次推理直接对齐后续迭代的效果，实现收益跨轮累积。
- 两者形成正循环：推理层生成的迭代结果作为训练层的监督信号，训练后模型的推理迭代效果更好，进一步生成更高质量的监督信号。

### 关键实验
用Qwen3 1.7B/4B/8B三个尺寸在5个数学竞赛基准上测试，对比TTPO+SC等5个无标注基线：1）全TT-RSI较基线模型平均准确率提升13.89%；2）相同测试时计算预算下，较最强自一致性基线TTPO+SC平均准确率高4.79%；3）In-Context RSI较自一致性方法减少68.6%的生成token即可达到相同准确率。

**最值得记住的一句话**：无标注测试时自提升无需依赖多数投票，通过相邻迭代结果的蒸馏即可实现持续效果累积，同时兼顾推理效率与收益天花板。
