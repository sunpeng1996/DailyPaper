---
title: 'A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model''s Thinking
  Loops and Complement a Frontier Model''s Weight Edit'
title_zh: 极小梯度编辑停止小模型思维循环并可与前沿模型权重编辑互补
authors:
- Hussamuddin Syed
affiliations:
- Independent Researcher
arxiv_id: '2611.33133'
url: https://arxiv.org/abs/2611.33133
pdf_url: https://arxiv.org/pdf/2611.33133
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM 权重编辑 · 推理循环优化
tags:
- weight editing
- sparse fine-tuning
- reasoning loop
- small language model
- gradient selection
one_liner: 用最少140权重的梯度编辑解决小模型思维循环，可与前沿模型权重编辑叠加提分
practical_value: '- 解决Agent思维死循环问题可借鉴梯度选Top-K权重稀疏微调的方案，仅需几十训练样本、单GPU几分钟即可完成，成本极低

  - 无偏置LLM的推理长度控制可直接在前几层恒定通道添加固定向量实现，比全量微调/LoRA效率高100倍以上

  - 不同来源的权重编辑可正交叠加，调优编辑强度可兼顾推理质量和推理速度，适合短上下文推理场景的Agent优化

  - 小模型性能优化优先做能力解锁（比如解决循环）而非新增能力，投入产出比远高于重新训练/大参数量微调'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小语言模型开启思维模式时普遍存在循环问题，会反复输出同类语句耗尽token预算无法输出有效结果；前沿模型生成的权重编辑方案虽能解决该问题，但缺少普通梯度方法的基线对比，也未知两类编辑方案能否互补叠加。

### 方法关键点
- 选择无偏置项的Qwen3.5-0.8B（873M参数）作为实验模型，训练数据为模型自身正确解答的MATH训练集样本，最少仅需50条即可生效
- 基于全参数的绝对梯度和排序选Top-K权重做稀疏微调，仅更新选中权重，其余参数完全冻结
- 发现无偏置模型的梯度编辑集中在前3层的恒定通道，效果等价于在残差流添加3个固定向量
- 对比随机位置编辑、GPT-6 Astra权重编辑方案，在4k到32k不同token预算下测试效果

### 关键结果
- 140个梯度选中的权重微调即可将4k token下思维模式MATH-500准确率从15.4%提升至39.0%，仅需单GPU 2分钟训练；139750权重微调最高可达45.5%
- 1398权重规模下随机位置编辑仅达16.3%，梯度选中权重可达42.9%，证明梯度选择的有效性
- 梯度编辑在16k token以内预算效果优于Astra编辑（4k下39.5% vs 6.7%），Astra编辑在32k预算下效果更好（52.1% vs 45.7%）
- 两者半强度叠加后32k下准确率达62.2%，比单独Astra编辑高10.1个点，平均token消耗减少近一半

**最值得记住的一句话**：小模型的很多性能问题不是能力不足，而是缺陷限制了能力释放，低成本的稀疏权重编辑即可解锁已有能力，远比重训高效。
