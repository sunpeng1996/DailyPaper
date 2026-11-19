---
title: Attention at Absolute Zero
title_zh: 零温度注意力：可泛化超训练规模的高阶精确推理层
authors:
- Mostafa &#39;Neo&#39; Mohsenvand
affiliations:
- MIT Media Lab
arxiv_id: '2611.11937'
url: https://arxiv.org/abs/2611.11937
pdf_url: https://arxiv.org/pdf/2611.11937
published: '2026-11-16'
collected: '2026-11-19'
category: Reasoning
direction: 推理优化 · 零温度注意力设计
tags:
- Attention
- Zero Temperature
- Algorithmic Reasoning
- Long Context
- Generalization
one_liner: 提出零温度高阶注意力层，无需中间监督即可泛化至千倍训练规模，精度远超软注意力
practical_value: '- 长上下文关系推理场景（电商用户行为链分析、商品关联规则挖掘）可借鉴零温度注意力思路替换部分软注意力模块，解决长序列下注意力权重弥散、精度下跌问题

  - 需小样本训练后泛化到超大输入规模的任务（大促万级商品池排序规则校验、Agent超长工具调用链正确性验证），可复用「仅输出比较bit、每轮重建状态避免漂移」的设计，大幅提升泛化精度

  - LLM外挂推理模块场景（Agent多跳商品查询、客服会话长关系推理）可借鉴冻结LLM+冷注意力层的架构，仅训练轻量注意力层即可大幅提升长上下文推理准确率，远低于全量微调成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
软注意力在输入规模远超训练集时会出现三类失效：固定温度下注意力权重随候选数增加弥散；学习到的分数无法分辨大输入下缩小的score gap；循环网络中连续状态随迭代漂移，导致无法可靠执行算法推理、长上下文关系链计算等任务，且现有算法推理模型依赖中间状态hint监督，泛化性差。

### 方法关键点
- 设计冷注意力（cold attention）层，状态建立在item对上，以第三item为见证（witness）计算pair间的关系，适配多跳、关系类推理任务
- 零温度下读取注意力分数，仅保留最优见证的分数及平局数，完全消除温度参数影响，解决权重弥散问题
- 层内仅输出count比较的2个bit（更大/相等），不传递连续score，避免分辨率不足的误差；每轮循环从输入和计算得到的bit重建状态，无连续状态传递，解决漂移问题
- 用straight-through梯度训练硬选择逻辑，无需中间状态hint监督

### 关键结果
- 最大检索任务：训练集最大16个item，测试到16384个item（千倍规模）时准确率≥99.95%，同配置软注意力在4096个item时准确率仅42%
- CLRS-30算法推理基准：无hint训练下平均准确率97.20%，优于此前SOTA FloydNet（带hint训练时96.64%，无hint时94.81%）
- 长上下文关系推理：冻结7B LLM仅训练冷注意力层，16条语句训练后可在1000条语句的家族关系推理上100%正确，原生LLM准确率仅44%

**最值得记住的一句话**：软注意力的三类失效根源均来自连续分数的传递与计算，零温度下仅保留比较bit、每轮重建离散状态的设计，可在无额外监督的情况下实现跨规模的精确推理。
