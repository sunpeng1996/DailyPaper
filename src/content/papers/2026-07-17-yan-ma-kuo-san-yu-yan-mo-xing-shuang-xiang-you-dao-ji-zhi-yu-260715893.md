---
title: 'Induction in Both Directions: A Mechanistic Analysis of In-Context Learning
  in Masked Diffusion Language Models'
title_zh: 掩码扩散语言模型双向诱导机制与上下文学习机理分析
authors:
- Andy Catruna
- Emilian Radoi
affiliations:
- National University of Science and Technology POLITEHNICA Bucharest
arxiv_id: '2607.15893'
url: https://arxiv.org/abs/2607.15893
pdf_url: https://arxiv.org/pdf/2607.15893
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 扩散大语言模型 · 机制可解释性
tags:
- Diffusion LLM
- Mechanistic Interpretability
- In-Context Learning
- Induction Heads
- Bidirectional Context
one_liner: 揭示掩码扩散语言模型双向诱导电路，证明其上下文学习优势来自双向上下文访问并存在隐式时间步编码
practical_value: '- 做电商商品标题改写、评论补全、Query补全等有前后文约束的填空类生成任务时，可优先选用DLM架构，利用其双向上下文能力获得比同规模AR模型更好的效果

  - 训练轻量化扩散语言模型时可复用论文结论：DLM会自动编码全局掩码率作为隐式时间步，无需额外设计显式时间步嵌入，降低模型复杂度与训练成本

  - 优化DLM的少样本上下文学习能力时，可参考双向诱导电路结构，针对性强化相邻token注意力头与后续诱导头的连接权重，提升少样本任务推理性能

  - 团队做模型可解释性排查、核心功能电路定位时，可复用论文的均值消融、QK/OV分解、路径补丁等分析方法'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自回归（AR）大模型的内部机制研究已非常充分，但扩散语言模型（DLM）作为支持并行解码的新兴架构，其上下文学习的实现机理尚不明确，明确DLM与AR模型的能力差异、核心电路结构对DLM的落地优化有重要指导意义。

### 方法关键点
- 控制变量训练结构完全匹配的仅注意力AR模型与吸收掩码DLM，仅调整注意力掩码和训练目标，其余架构、训练流程完全一致
- 用随机token构造重复序列作为测试集，排除语义与词频干扰，以重复序列与非重复对照序列的正确token对数概率差作为诱导能力得分
- 结合均值消融、QK/OV权重分解、线性探针、路径补丁等方法，定位核心电路并验证因果关系

### 关键结果
- DLM诱导能力近似方向对称，L2层DLM正向诱导得分4.13±0.17nats，反向诱导得分4.07±0.25nats，两者几乎持平
- 仅开放左上下文（匹配AR模型的信息访问权限）时，L2层DLM诱导得分2.23nats，低于同结构AR模型的3.46nats；开放双向上下文时DLM得分升至4.39nats，超过AR模型
- 线性探针在L0注意力层之后即可从残差流中预测全局掩码率，R²达0.82-0.91，补丁隐式时间步方向可恢复13%-88%的预测熵变差距

### 核心结论
DLM的上下文学习优势并非来自更强的单侧诱导能力，而是来自对掩码位置双向上下文的访问能力。
