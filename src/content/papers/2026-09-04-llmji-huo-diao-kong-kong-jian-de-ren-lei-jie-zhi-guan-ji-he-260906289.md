---
title: 'Steering Geometry: Validating Human Value Geometry in LLM Steering Space'
title_zh: LLM激活调控空间的人类价值观几何结构有效性验证
authors:
- Mohammad Mahdi Abootorabi
- Armin Saghafian
- Ali Bazshoushtari
- Hamid Rezaei
- EunJeong Hwang
- Vered Shwartz
- Parvin Mousavi
- Purang Abolmaesumi
affiliations:
- University of British Columbia
- Vector Institute for AI
- Queen's University
arxiv_id: '2609.06289'
url: https://arxiv.org/abs/2609.06289
pdf_url: https://arxiv.org/pdf/2609.06289
published: '2026-09-04'
collected: '2026-09-09'
category: LLM
direction: LLM激活调控 · 价值观对齐优化
tags:
- Activation Steering
- Human Value Alignment
- LLM Interpretability
- Representation Geometry
- Alignment
one_liner: 对比两类LLM激活调控方法，证实分布驱动类可还原与人类价值观理论对齐的几何结构
practical_value: '- 做电商客服、Agent人设等需要价值观/行为调控的场景时，优先选择分布驱动类激活调控方法（如CAA、SAS），相比行为中心类方法，不会出现改了目标行为但连带破坏其他相关人设属性的问题，大幅降低意外副作用概率

  - 若业务需要多维度可控LLM输出（如电商导购要同时兼顾专业、礼貌、不夸大宣传），可参考本文的几何对齐验证思路，预先校验调控向量的语义关联性，提前规避多目标调控冲突

  - 定制化LLM行为调控优先选用基座模型而非指令微调模型，基座的激活空间保留了更完整的语义几何结构，调控的跨属性迁移性更符合预期，调试成本更低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM激活调控方法仅验证单目标行为的调控效果，无法确认调控向量是捕获了真实语义结构还是仅利用行为特定捷径，在需要多维度可控输出的场景（如电商客服、Agent人设调控）中容易出现不可预期的副作用，因此需要验证调控空间的几何结构是否与人类公认的价值观理论对齐。
### 方法关键点
- 以Schwartz人类基本价值观理论（20个价值观构成环形拓扑，兼容/冲突价值观的位置关系明确，跨文化通用）为基准，构建26K样本的对比问答数据集，覆盖20类人类价值观；
- 对比两类主流激活调控范式：分布驱动类（CAA、SAS、SphericalSteer、ODESteer，通过对比样本激活差异提取调控向量）、行为中心类（OPT、COLD-Steer、BiPO，通过梯度优化直接拟合行为目标），统一用激活偏移向量表征不同方法的调控效果；
- 设计几何对齐度、跨价值观迁移度两类评估指标，量化调控向量与理论拓扑的匹配程度。
### 关键结果
在Qwen3.5、Llama3.1等7个模型系列上测试：分布驱动类方法的理论秩相关系数Spearman ρ最高达0.51（p < 1e-13），而行为中心类方法相关度接近0，尽管二者单目标调控准确率相当；模型规模越大，分布驱动方法的几何对齐度越高，但指令微调后对齐度平均下降30%以上；几何对齐度越高的方法，跨价值观迁移越符合人类预期：调控某一价值观时会同步提升兼容价值观的表现、抑制冲突价值观。
### 核心结论
单目标调控效果好的方法不一定具备语义一致性，行为中心类调控方法容易学到捷径，仅改变目标行为但破坏底层语义结构，带来不可控的副作用
