---
title: 'When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time
  Scaling'
title_zh: 《采样越多效果越差：测试时缩放的模态天花板与相关性天花板》
authors:
- Yong Yi Bay
- Kathleen A. Yearick
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2606.28661'
url: https://arxiv.org/abs/2606.28661
pdf_url: https://arxiv.org/pdf/2606.28661
published: '2026-06-26'
collected: '2026-07-03'
category: LLM
direction: LLM推理优化 · 测试时采样
tags:
- test-time scaling
- inference optimization
- effective sample size
- self-consistency
- pass@k
one_liner: 揭示测试时采样的两类性能天花板，给出有效样本量计算方法与场景化算力分配规则
practical_value: '- 做LLM驱动的推荐query生成/Agent推理时，无验证器的多数投票采样不用超过64次，超过后不仅不提升效果还可能反降，可大幅节省推理成本

  - 评估LLM/Agent业务场景准确率时，不要堆单问题采样数，按1/ρ_b（实测约2-3倍独立样本量）折算有效样本量，多余算力花在扩充测试问题集性价比更高

  - 做生成式推荐的候选生成+排序时，若有验证规则（如库存校验、合规校验）可多采样提升覆盖，否则优先调温度/prompt多样性降低答案集中度，比加采样数效果更好

  - 业务上报采样相关指标时，同时上报有效样本量n_eff而非仅名义采样数n，避免高估模型能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM推理普遍通过多采样（self-consistency、best-of-n、pass@k）提升效果，但实践中采样数增长到一定程度后效果停滞甚至下降，算力浪费严重，缺乏统一理论框架解释该现象并给出采样预算边界。

### 方法关键点
- 将测试时多采样重定义为集群抽样，引入调查统计的组内相关系数ρ量化样本相关性，推导有效样本量公式 $n_{eff} = n/(1+(n-1)ρ)$，其上限为 $1/ρ$（相关性天花板）
- 拆分测试时采样的三类核心目标：覆盖率（pass@k）、选择准确率（多数投票/self-consistency）、基准准确率估计，分别对应不同约束边界
- 提出选择准确率的模态天花板：采样数足够大时，多数投票收敛到模型的模态答案，准确率上限为模态答案正确率 $\pi_{mode}$，超过阈值的采样反而会提升错误答案置信度（反缩放）

### 关键结果
- GSM8K数据集上Llama-3-8B单问题采样1e4次时覆盖率达1.0，但self-consistency准确率仅停留在0.87，可识别差距达13%
- MATH-500数据集上256次采样覆盖率达0.88，但self-consistency准确率仅为0.45，超过64次采样后基本无提升
- 实测跨基准的问题难度相关系数$\rho_b$约为0.4-0.6，对应有效样本量上限仅为1.6-2.5，即单问题采样超过3次对基准估计几乎无增益

**最值得记住的一句话**：测试时缩放的瓶颈已经从生成正确答案转移到识别正确答案，多余的采样算力应该花在降低答案相关性与提升选择能力上，而非增加采样数。
