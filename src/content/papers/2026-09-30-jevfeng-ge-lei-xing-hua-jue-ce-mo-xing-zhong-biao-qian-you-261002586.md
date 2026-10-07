---
title: Labels Override Definitions in Jev-Style Typed Decision Models
title_zh: Jev风格类型化决策模型中标签优先级高于定义
authors:
- Seyedarmin Azizi
- Erfan Baghaei Potraghloo
- Massoud Pedram
affiliations:
- University of Southern California
arxiv_id: '2610.02586'
url: https://arxiv.org/abs/2610.02586
pdf_url: https://arxiv.org/pdf/2610.02586
published: '2026-09-30'
collected: '2026-10-07'
category: LLM
direction: LLM分类 标签偏见检测与缓解
tags:
- Typed Decision Model
- Prompt Engineering
- Label Bias
- LLM Classification
- Mitigation Strategy
one_liner: 发现Jev类决策模型标签优先于定义的偏见源于prompt拼接 给出检测与缓解方案
practical_value: '- 用LLM做用户意图分类、售后工单路由、商品合规审核、广告素材打标等分类任务时，可将选项标签改为A/B等无意义标识符，规则全部写入定义字段，实测可提升15%左右分类准确率

  - 若业务要求必须保留有意义的选项标签，可先跑一次空输入的基准概率分布，对实际预测结果做上下文校准，可提升3%~7%的分类准确率

  - 不要依赖LLM自带的置信度阈值过滤分类错误，标签与定义冲突时置信度会反向排序（高置信对应错误结果），建议用双prompt渲染结果对比做错误过滤

  - 所有上线的LLM分类服务，先跑两次仅修改选项标签、定义不变的请求，若输出分布差异大说明存在标签偏见，需做对应缓解'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Jev类类型化决策模型因仅需单轮前向传播、推理成本比通用LLM低1~2个数量级，被广泛用于路由、内容审核、工单分流等场景。其设计假设是模型按选项的定义做决策，标签仅作为返回标识，但工业界观察到仅修改标签就会大幅改变决策结果，此前研究将该现象归因于受限决策头，机制未明确且缺乏可落地的缓解方案。
### 方法关键点
- 构造PolicyBench合成路由数据集，决策规则仅出现在选项定义中，标签分为对齐、任意、误导三类，完全排除标签本身的信息干扰
- 测试4个开源类型化决策模型、3种基于Qwen2.5的分类读出方式，覆盖11个公开分类任务
- 做双向干预实验：给LAYA系列模型的输入删除标签前缀、给VON模型的输入增加标签前缀，全程不修改权重、决策头，验证偏见来源
- 提出2-call无监督检测法：仅修改选项标签重跑同个请求，对比输出分布即可判断是否存在标签偏见，无需标注数据或模型权重权限
### 关键结果
- LAYA系列模型删除全部定义后准确率几乎不变（0.8559 vs 0.8487），将标签改为A/B等无意义标识符后准确率提升0.1511，标签与定义冲突时准确率从0.85降至0.1357
- 仅修改prompt拼接方式（删除/增加标签前缀）即可完全消除/引入标签偏见，对应准确率波动为0
- 通用LLM做分类器时也存在相同标签偏见，Qwen2.5-7B改用无意义标签后准确率提升0.1203
### 核心结论
LLM分类任务的标签偏见源于prompt中标签与定义的拼接方式，而非模型结构或决策头，优化prompt的收益远高于调整模型参数
