---
title: 'Explicit Fuzzy Logic in the Feed-Forward Layer: Self-Forgetting Quantifiers
  Discover Legible Grammatical-Licensing Detectors'
title_zh: 前馈层引入显式模糊逻辑 自遗忘量化器实现可解释语法许可检测
authors:
- Mark Oskin
affiliations:
- University of Washington
arxiv_id: '2606.31845'
url: https://arxiv.org/abs/2606.31845
pdf_url: https://arxiv.org/pdf/2606.31845
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: LLM架构优化 · FFN可解释性改造
tags:
- FFN
- Fuzzy Logic
- Mechanistic Interpretability
- Quantifier
- Transformer
- Grammatical Licensing
one_liner: 将显式模糊逻辑算子引入Transformer前馈层，加入自遗忘量化器在无损语言模型性能的同时大幅提升可解释性
practical_value: '- 做LLM4Rec、Agent等有强可解释性要求的业务场景时，可尝试用NC-FFN替换部分原生GELU FFN模块，参数无额外开销，可在几乎无损性能的前提下获得部分可直接读取的逻辑单元，便于错误根因定位

  - 处理序列级规则匹配任务（如电商文案语法合规校验、用户query否定意图识别、优惠券使用规则匹配）时，可借鉴自遗忘量化器设计，给每个规则检测单元添加可学习遗忘率，自动适配规则的上下文有效窗口，精度优于固定窗口匹配

  - 多跳推理类任务（如长会话用户搜索意图理解）中，可参考NC-FFN的分层分配经验：浅层层配置更高比例的显式逻辑单元提升特征组合效率，深层保留GELU单元保证训练稳定性与泛化性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer FFN占模型大部分参数但运算过程黑盒，现有后验可解释方法仅能识别特征方向，无法还原特征组合逻辑；同时传统FFN对序列级规则、否定类意图的建模可解释性差，难以直接定位错误根源。
### 方法关键点
- 提出NC-FFN（支持否定的前馈层），将部分隐藏单元替换为sigmoid约束到[0,1]的显式模糊集合算子：交集`A·B`、差集`A·(1-B)`，后者实现显式正编码的否定逻辑，参数规模与原生GELU FFN完全一致
- 采用混合分区设计：保留75%的GELU单元作为梯度高速路避免训练发散，仅25%参数分配给显式逻辑算子，支持函数保留初始化，训练稳定性与基线对齐
- 新增自遗忘量化器模块：在序列维度新增软存在、软比例两类模糊量化算子，每个单元配备可学习的遗忘率，初始化为非遗忘状态，自动学习特征的有效记忆窗口
### 关键实验结果
- 推理能力探针：N位奇偶校验任务中，单层NC-FFN参数效率远超GELU，可解决8位奇偶校验，是同规模GELU的1.3倍
- 语言模型训练：125M参数规模下，NC-FFN在OpenWebText上的困惑度与GELU基线基本持平（18.36 vs 18.32）；加入自遗忘量化器后，BLiMP语法任务的差距在第一个epoch就缩小50%，LAMBADA精度小幅超过基线
- 可解释性：自遗忘量化器单元自动学习到约1.5个token的中位半衰期，无需字典学习即可直接识别为语法许可检测器，精准匹配比较级、被动分词等许可触发词的作用窗口
> 最值得记住的结论：模型中逻辑结构的保留程度完全由训练目标决定，任务需要的逻辑会被固化，不需要的会自动退化为普通激活单元
