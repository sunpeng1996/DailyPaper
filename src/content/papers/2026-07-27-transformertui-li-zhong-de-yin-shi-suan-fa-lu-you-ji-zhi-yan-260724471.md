---
title: Grounding latent algorithm routing in transformer reasoning
title_zh: Transformer推理中的隐式算法路由机制验证
authors:
- Xiangbo Zhang
- Xiaoxu Ma
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.24471'
url: https://arxiv.org/abs/2607.24471
pdf_url: https://arxiv.org/pdf/2607.24471
published: '2026-07-27'
collected: '2026-07-28'
category: Reasoning
direction: LLM推理 · 隐式算法路由
tags:
- Latent Routing
- In-Context Learning
- Mechanistic Interpretability
- Transformer
- Benchmark
one_liner: 提出ROUTEBENCH诊断基准，验证大参数量稠密Transformer可自发形成鲁棒隐式算法路由能力
practical_value: '- 多场景自适应推荐/搜索路由设计可参考本文逻辑，无需显式路由标签，仅靠混合场景训练即可让模型自发学习最优策略选择

  - Agent任务调度模块验证可复用三大路由判据（结构必要性、扰动鲁棒性、因果可编辑性），避免仅靠输出准确率误判调度逻辑有效性

  - 大模型业务优化可借鉴中间层激活探针+定向编辑方法，无需重训即可 steering 模型适配业务场景的推理策略，降低场景适配成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往上下文学习研究无法区分Transformer的输出是依赖表面prompt匹配，还是真能根据数据潜在模式自动选择匹配归纳偏置的求解器，仅靠输出准确率无法验证隐式路由的真实存在，也缺乏统一的诊断基准。
### 方法关键点
- 提出三大隐式路由有效性判据：结构必要性（prompt格式固定时，数据模式切换触发求解器选择变化）、扰动鲁棒性（语义不变的prompt改写不改变求解器选择）、因果可编辑性（定向修改激活可切换求解器且不显著降低答案质量）
- 构建ROUTEBENCH诊断基准，覆盖稀疏/稠密线性结构、干净/重尾噪声、全局/局部规律三类数据模式，对应ridge、lasso、Huber、kNN四类经典求解器
- 训练44M~612M参数量的稠密Decoder-only Transformer，全程不提供路由标签，对比固定求解器、全局软混合、输入条件软混合、无监督Gumbel路由等基线方案
### 关键结果
- 306M模型可填补80.9%的oracle路由性能gap，路由F1达84.1；612M模型gap填补率达86.5%，OOD性能、扰动鲁棒性均优于输入条件混合、无监督Gumbel路由等显式路由方案
- 中间层可线性解码路由信号，峰值AUC达0.91，定向修改中间层激活可实现73.8%的路由切换成功率，同时保留96.7%的答案质量
- 路由能力随模型规模提升同步增强，对自然语言改写、样本顺序打乱等扰动保持鲁棒

**最值得记住的结论**：稠密Transformer不需要显式路由模块，仅靠混合场景训练就能自发学习隐式的策略选择能力，效果优于多数人工设计的显式路由方案
